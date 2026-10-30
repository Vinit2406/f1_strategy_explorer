import json
import requests
import datetime

with open('data/laps.json') as f:
    laps = json.load(f)

targets = {
    'VER_Lap67_Fastest': (1, 67, 'Max Verstappen - Lap 67 (Fastest Lap 1:20.472)'),
    'VER_Lap43_Restart': (1, 43, 'Max Verstappen - Lap 43 (Restart & Lead Overtake)'),
    'VER_Lap1_Charge': (1, 1, 'Max Verstappen - Lap 1 (P17 to P11 Charge)'),
    'NOR_Lap66_Fastest': (4, 66, 'Lando Norris - Lap 66 (Norris Fastest Lap 1:21.517)'),
    'RUS_Lap66_Fastest': (63, 66, 'George Russell - Lap 66 (Russell Fastest Lap 1:21.645)'),
    'OCO_Lap65_Fastest': (31, 65, 'Esteban Ocon - Lap 65 (Ocon Fastest Lap 1:21.771)'),
    'LEC_Lap67_Fastest': (16, 67, 'Charles Leclerc - Lap 67 (Leclerc Fastest Lap 1:21.631)'),
}

telemetry_data = {}

for key, (drv, lap_num, desc) in targets.items():
    match = [l for l in laps if l['driver_number'] == drv and l['lap_number'] == lap_num]
    if not match:
        print(f"Lap not found for {key}")
        continue
    lap_info = match[0]
    d_start_str = lap_info['date_start']
    # compute end time using lap_duration
    start_dt = datetime.datetime.fromisoformat(d_start_str.replace('Z', '+00:00'))
    dur = lap_info['lap_duration']
    if not dur:
        dur = 90.0
    end_dt = start_dt + datetime.timedelta(seconds=dur + 2.0)
    
    d_start_iso = start_dt.isoformat()
    d_end_iso = end_dt.isoformat()
    
    url = f"https://api.openf1.org/v1/car_data?session_key=9636&driver_number={drv}&date>={d_start_iso}&date<={d_end_iso}"
    print(f"Fetching telemetry for {key} (Driver {drv}, Lap {lap_num})...")
    resp = requests.get(url).json()
    print(f"  Got {len(resp)} points.")
    
    # Calculate relative elapsed time and estimated distance
    # Interlagos circuit is approx 4309 meters.
    # We can calculate cumulative distance from speed * delta_t
    points = []
    cum_dist = 0.0
    prev_time = None
    for pt in resp:
        pt_dt = datetime.datetime.fromisoformat(pt['date'].replace('Z', '+00:00'))
        elapsed = (pt_dt - start_dt).total_seconds()
        if elapsed < 0:
            continue
        if prev_time is not None:
            dt = (pt_dt - prev_time).total_seconds()
            if 0 < dt < 1.0:
                speed_mps = pt['speed'] / 3.6
                cum_dist += speed_mps * dt
        prev_time = pt_dt
        
        points.append({
            'elapsed_s': round(elapsed, 3),
            'distance_m': round(cum_dist, 1),
            'speed': pt['speed'],
            'throttle': pt['throttle'],
            'brake': pt['brake'],
            'n_gear': pt['n_gear'],
            'rpm': pt['rpm'],
            'drs': pt['drs']
        })
    
    telemetry_data[key] = {
        'driver_number': drv,
        'lap_number': lap_num,
        'label': desc,
        'lap_duration': dur,
        's1': lap_info.get('duration_sector_1'),
        's2': lap_info.get('duration_sector_2'),
        's3': lap_info.get('duration_sector_3'),
        'st_speed': lap_info.get('st_speed'),
        'i1_speed': lap_info.get('i1_speed'),
        'i2_speed': lap_info.get('i2_speed'),
        'telemetry': points
    }

with open('data/telemetry.json', 'w') as f:
    json.dump(telemetry_data, f)

print("Saved data/telemetry.json successfully!")
