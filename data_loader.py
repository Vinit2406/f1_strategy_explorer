import json
import pandas as pd
import numpy as np

def load_data():
    with open('data/drivers.json', encoding='utf-8') as f:
        drivers = json.load(f)
    drivers_df = pd.DataFrame(drivers)

    with open('data/laps.json', encoding='utf-8') as f:
        laps = json.load(f)
    laps_df = pd.DataFrame(laps)

    with open('data/stints.json', encoding='utf-8') as f:
        stints = json.load(f)
    stints_df = pd.DataFrame(stints)

    with open('data/pit.json', encoding='utf-8') as f:
        pit = json.load(f)
    pit_df = pd.DataFrame(pit)

    with open('data/race_control.json', encoding='utf-8') as f:
        race_control = json.load(f)
    race_control_df = pd.DataFrame(race_control)

    with open('data/weather.json', encoding='utf-8') as f:
        weather = json.load(f)
    weather_df = pd.DataFrame(weather)

    with open('data/lap_positions.json', encoding='utf-8') as f:
        lap_positions = json.load(f)

    with open('data/telemetry.json', encoding='utf-8') as f:
        telemetry = json.load(f)

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
    print("Drivers:", len(d['drivers']))
    print("Laps:", len(d['laps']))
    print("Lap positions laps count:", len(d['lap_positions']))
    print("Telemetry keys:", list(d['telemetry'].keys()))
