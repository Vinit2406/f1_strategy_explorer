import json
import os
import pandas as pd
import numpy as np

def resolve_path(filename):
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
    for root, dirs, files in os.walk(script_dir):
        if filename in files:
            return os.path.join(root, filename)
    return filename

def load_json(filename):
    with open(resolve_path(filename), encoding='utf-8') as f:
        return json.load(f)

def load_data():
    drivers_df = pd.DataFrame(load_json('drivers.json'))
    laps_df = pd.DataFrame(load_json('laps.json'))
    stints_df = pd.DataFrame(load_json('stints.json'))
    pit_df = pd.DataFrame(load_json('pit.json'))
    race_control_df = pd.DataFrame(load_json('race_control.json'))
    weather_df = pd.DataFrame(load_json('weather.json'))
    lap_positions = load_json('lap_positions.json')
    telemetry = load_json('telemetry.json')

    return {
        'drivers': drivers_df,
        'laps': laps_df,
        'stints': stints_df,
        'pit': pit_df,
        'race_control': race_control_df,
        'weather': weather_df,
        'lap_positions': lap_positions,
        'telemetry': telemetry
    }

if __name__ == '__main__':
    d = load_data()
    print("Loaded data successfully. Drivers:", len(d['drivers']), "Laps:", len(d['laps']))
