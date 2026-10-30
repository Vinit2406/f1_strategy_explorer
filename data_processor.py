import json
import os
import pandas as pd
import numpy as np

def resolve_path(filename):
    """
    Finds file whether it is located in 'data/<filename>' or in the root directory './<filename>',
    or relative to the script directory. This prevents FileNotFoundError on Streamlit Cloud.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, 'data', filename),
        os.path.join(script_dir, filename),
        os.path.join(os.getcwd(), 'data', filename),
        os.path.join(os.getcwd(), filename),
        os.path.join('data', filename),
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    # If not found yet, try searching current dir for the filename
    for root, dirs, files in os.walk(script_dir):
        if filename in files:
            return os.path.join(root, filename)
    return filename

def load_json_file(filename):
    path = resolve_path(filename)
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def get_processed_data():
    drivers = load_json_file('drivers.json')
    drivers_df = pd.DataFrame(drivers)
    
    # Map driver number to info
    driver_info_by_num = {}
    driver_info_by_id = {}
    
    # Official team colors for 2024 Sao Paulo GP
    driver_colors = {
        1: '#3671C6',   # Max Verstappen
        4: '#FF8000',   # Lando Norris
        63: '#27F4D2',  # George Russell
        31: '#0093CC',  # Esteban Ocon
        10: '#FF69B4',  # Pierre Gasly
        16: '#E8002D',  # Charles Leclerc
        44: '#00A19B',  # Lewis Hamilton
        81: '#FFB800',  # Oscar Piastri
        14: '#229971',  # Fernando Alonso
        55: '#FF4D4D',  # Carlos Sainz
        22: '#6692FF',  # Yuki Tsunoda
        30: '#99B8FF',  # Liam Lawson
        50: '#B6BABD',  # Oliver Bearman
        27: '#E0E0E0',  # Nico Hulkenberg
        11: '#1E41B0',  # Sergio Perez
        23: '#64C4FF',  # Alex Albon
        43: '#005AFF',  # Franco Colapinto
        77: '#52E252',  # Valtteri Bottas
        24: '#88FF88',  # Zhou Guanyu
        18: '#006F62'   # Lance Stroll
    }

    for d in drivers:
        num = d['driver_number']
        last = d['last_name'].lower().replace(' ', '_')
        team = d['team_name']
        d_color = driver_colors.get(num, f"#{d.get('team_colour', 'FFFFFF')}")
        info = {
            'number': num,
            'code': d['name_acronym'],
            'full_name': d['full_name'],
            'short_name': f"{d['first_name'][0]}. {d['last_name']}",
            'team': team,
            'color': d_color,
            'headshot': d.get('headshot_url', '')
        }
        driver_info_by_num[num] = info
        if num == 1:
            driver_info_by_id['max_verstappen'] = info
        else:
            driver_info_by_id[last] = info

    laps = load_json_file('laps.json')
    laps_df = pd.DataFrame(laps)

    stints = load_json_file('stints.json')
    stints_df = pd.DataFrame(stints)

    pit = load_json_file('pit.json')
    pit_df = pd.DataFrame(pit)

    race_control = load_json_file('race_control.json')
    race_control_df = pd.DataFrame(race_control)

    weather = load_json_file('weather.json')
    weather_df = pd.DataFrame(weather)

    lap_positions = load_json_file('lap_positions.json')
    telemetry = load_json_file('telemetry.json')

    # Build comprehensive lap positions dataframe
    pos_records = []
    for lap_str, timings in lap_positions.items():
        lap_num = int(lap_str)
        for t in timings:
            drv_id = t['driverId']
            info = driver_info_by_id.get(drv_id, None)
            if not info:
                continue
            pos_records.append({
                'lap': lap_num,
                'driver_id': drv_id,
                'driver_number': info['number'],
                'driver_code': info['code'],
                'driver_name': info['short_name'],
                'team': info['team'],
                'color': info['color'],
                'position': int(t['position']),
                'lap_time_str': t['time']
            })
    positions_df = pd.DataFrame(pos_records)

    # Clean lap times & calculate rolling averages
    laps_clean = laps_df[laps_df['lap_duration'].notnull() & (laps_df['lap_duration'] > 60) & (laps_df['lap_duration'] < 130)].copy()
    
    # Max Verstappen overtakes data
    overtakes = [
        {
            'lap': 1,
            'car_passed': 'Hamilton, Perez, Zhou, Bearman, Bottas, Colapinto',
            'position_before': 'P17',
            'position_after': 'P11',
            'location': 'Turns 1-4 & Throughout Lap 1',
            'details': 'Aggressive launch on intermediate tyres, threading through the spray into the Senna S, gaining 6 places on the opening lap.',
            'badge': '+6 Places'
        },
        {
            'lap': 2,
            'car_passed': 'Lewis Hamilton (Mercedes #44)',
            'position_before': 'P11',
            'position_after': 'P10',
            'location': 'Turn 1 (Senna S)',
            'details': 'Late braking down the inside into Turn 1, passing the 7-time World Champion on wet asphalt into the points.',
            'badge': 'Into Points'
        },
        {
            'lap': 6,
            'car_passed': 'Pierre Gasly (Alpine #10)',
            'position_before': 'P10',
            'position_after': 'P9',
            'location': 'Turn 1 (Senna S)',
            'details': 'Sucked into the tow down the main straight, clinical dive into Turn 1 with zero wheel-locking.',
            'badge': 'Overtake'
        },
        {
            'lap': 7,
            'car_passed': 'Fernando Alonso (Aston Martin #14)',
            'position_before': 'P9',
            'position_after': 'P8',
            'location': 'Turn 1 (Senna S)',
            'details': 'Bold late-braking move on wet racing line into Turn 1 against the veteran Spaniard.',
            'badge': 'Overtake'
        },
        {
            'lap': 10,
            'car_passed': 'Oscar Piastri (McLaren #81)',
            'position_before': 'P8',
            'position_after': 'P7',
            'location': 'Turn 1 (Senna S)',
            'details': 'Sliced past Piastri into Turn 1. Setting fastest laps while navigating traffic.',
            'badge': 'Fastest Lap'
        },
        {
            'lap': 11,
            'car_passed': 'Liam Lawson (RB #30)',
            'position_before': 'P7',
            'position_after': 'P6',
            'location': 'Turn 1 (Senna S)',
            'details': 'Made it 5 passes into Turn 1 in 10 laps, latching onto the tail of Charles Leclerc in P5.',
            'badge': 'Overtake'
        },
        {
            'lap': 25,
            'car_passed': 'Charles Leclerc (Ferrari #16)',
            'position_before': 'P6',
            'position_after': 'P5',
            'location': 'Pit Strategy / Tyre Conservation',
            'details': 'Max tucked behind Leclerc from Lap 12-24, saving front tyre life in wet spray until Leclerc suffered severe thermal deg and was forced to box.',
            'badge': 'Tyre Mastery'
        },
        {
            'lap': 29,
            'car_passed': 'George Russell & Lando Norris (P1 & P2)',
            'position_before': 'P4',
            'position_after': 'P2',
            'location': 'VSC Pit Strategy Gamble',
            'details': 'Under VSC, Russell and Norris pitted for new inters. Red Bull kept Max out on track, knowing torrential rain was imminent.',
            'badge': 'Strategic Call'
        },
        {
            'lap': 32,
            'car_passed': 'Pit Wall Masterstroke (Red Flag)',
            'position_before': 'P2',
            'position_after': 'P2 (Free Pit Stop)',
            'location': 'Pit Lane under Red Flag',
            'details': 'Colapinto crashed heavily under SC. Red Flag thrown. Max granted a FREE tyre change under regulations, wiping out the 24s advantage Norris and Russell sought!',
            'badge': 'Game Changer'
        },
        {
            'lap': 43,
            'car_passed': 'Esteban Ocon (Alpine #31)',
            'position_before': 'P2',
            'position_after': 'P1 (Race Lead)',
            'location': 'Turn 1 (Senna S)',
            'details': 'At the Safety Car restart, Verstappen sold Ocon a dummy and braked astonishingly deep into Turn 1 on cold wet tarmac to snatch the lead.',
            'badge': 'Lead Overtake'
        }
    ]

    # Red Bull Radio transcripts
    radio_transcripts = [
        {
            'lap': 'Lap 27',
            'speaker': 'Gianpiero Lambiase (GP)',
            'role': 'Race Engineer',
            'message': 'Max, VSC deployed. Hulkenberg off at Turn 1. Stay out, stay out.',
            'context': 'Russell and Norris were debating boxing. Red Bull radar showed severe downpour coming in 3 minutes.'
        },
        {
            'lap': 'Lap 28',
            'speaker': 'Max Verstappen',
            'role': 'Driver',
            'message': 'The rain is really coming down now! There is so much standing water in the final sector, you cannot see anything.',
            'context': 'Russell & Norris pit right as VSC ends. Verstappen moves into P2 behind Ocon.'
        },
        {
            'lap': 'Lap 29',
            'speaker': 'Gianpiero Lambiase (GP)',
            'role': 'Race Engineer',
            'message': 'Understood Max. Both Mercedes and Norris have boxed. You are P2 behind Ocon. Keep it on the island, this will get neutralized.',
            'context': 'Mercedes and McLaren gambled away track position; Red Bull held nerve.'
        },
        {
            'lap': 'Lap 30',
            'speaker': 'Race Control',
            'role': 'FIA',
            'message': 'SAFETY CAR DEPLOYED due to extreme weather conditions.',
            'context': 'Track conditions become undriveable. The decision to stay out is instantly vindicated.'
        },
        {
            'lap': 'Lap 32',
            'speaker': 'Gianpiero Lambiase (GP)',
            'role': 'Race Engineer',
            'message': 'Red Flag, Red Flag! Colapinto has crashed on the main straight. Bring it into the pit lane.',
            'context': 'The jackpot: under FIA Sporting Code Art 57, teams can change tyres during a red flag without serving a pit stop!'
        },
        {
            'lap': 'Lap 32',
            'speaker': 'Christian Horner',
            'role': 'Team Principal',
            'message': 'Brilliant patience Max. Free tyre change for us. We are starting on equal rubber from P2 with fresh inters.',
            'context': 'Norris and Russell have effectively thrown away 25 seconds for zero tyre advantage.'
        },
        {
            'lap': 'Lap 43',
            'speaker': 'Max Verstappen',
            'role': 'Driver',
            'message': '(After passing Ocon into Turn 1) Car feels very hooked up, let\'s go.',
            'context': 'Verstappen takes the lead and immediately begins unleashing purple sector after purple sector.'
        },
        {
            'lap': 'Lap 60',
            'speaker': 'Gianpiero Lambiase (GP)',
            'role': 'Race Engineer',
            'message': 'Max, you have a 14-second gap to Ocon. No need to push the limits on the curbs.',
            'context': 'Max ignores the call to slow down and continues setting consecutive fastest laps of the race.'
        },
        {
            'lap': 'Lap 69 (Checkered Flag)',
            'speaker': 'Gianpiero Lambiase (GP)',
            'role': 'Race Engineer',
            'message': 'Max Verstappen, you win the São Paulo Grand Prix from P17 on the grid! That was an absolute wet weather masterclass!',
            'context': 'Verstappen wins by +19.477s and sets the fastest lap (1:20.472).'
        },
        {
            'lap': 'Lap 69',
            'speaker': 'Christian Horner',
            'role': 'Team Principal',
            'message': 'Unbelievable Max. You were in a completely different league today. That is the drive of a champion.',
            'context': 'Extends championship lead to 62 points, all but sealing his 4th World Drivers\' Championship.'
        }
    ]

    return {
        'drivers': drivers_df,
        'driver_info_by_num': driver_info_by_num,
        'driver_info_by_id': driver_info_by_id,
        'laps': laps_df,
        'laps_clean': laps_clean,
        'stints': stints_df,
        'pit': pit_df,
        'race_control': race_control_df,
        'weather': weather_df,
        'positions_df': positions_df,
        'telemetry': telemetry,
        'overtakes': overtakes,
        'radio_transcripts': radio_transcripts
    }
