import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

F1_TEMPLATE = {
    'layout': {
        'paper_bgcolor': '#0E1117',
        'plot_bgcolor': '#161A23',
        'font': {'color': '#E0E0E0', 'family': 'sans-serif'},
        'xaxis': {
            'gridcolor': '#2A2E39',
            'linecolor': '#3A3F4D',
            'zerolinecolor': '#3A3F4D'
        },
        'yaxis': {
            'gridcolor': '#2A2E39',
            'linecolor': '#3A3F4D',
            'zerolinecolor': '#3A3F4D'
        },
        'hovermode': 'x unified',
        'margin': {'t': 40, 'r': 20, 'b': 40, 'l': 50}
    }
}

def create_position_chart(positions_df, selected_drivers, driver_info_by_num):
    fig = go.Figure()

    # Add incident background bands
    # Lap 27-28 VSC
    fig.add_vrect(
        x0=27, x1=28.5,
        fillcolor="rgba(255, 230, 0, 0.15)",
        layer="below", line_width=1, line_color="rgba(255, 230, 0, 0.4)",
        annotation_text="VSC (Hulk spin)", annotation_position="top left",
        annotation_font=dict(color="#FFE600", size=10)
    )
    # Lap 30-32 Safety Car
    fig.add_vrect(
        x0=29.5, x1=32,
        fillcolor="rgba(255, 165, 0, 0.18)",
        layer="below", line_width=1, line_color="rgba(255, 165, 0, 0.5)",
        annotation_text="Safety Car (Rain)", annotation_position="top left",
        annotation_font=dict(color="#FFA500", size=10)
    )
    # Lap 32-33 Red Flag
    fig.add_vrect(
        x0=32, x1=33,
        fillcolor="rgba(255, 30, 30, 0.25)",
        layer="below", line_width=2, line_color="#FF1E1E",
        annotation_text="RED FLAG (Colapinto Crash)", annotation_position="top left",
        annotation_font=dict(color="#FF4D4D", size=11, family="sans-serif")
    )
    # Lap 39-42 Safety Car 2
    fig.add_vrect(
        x0=39, x1=42.5,
        fillcolor="rgba(255, 165, 0, 0.18)",
        layer="below", line_width=1, line_color="rgba(255, 165, 0, 0.5)",
        annotation_text="SC 2 (Sainz)", annotation_position="top left",
        annotation_font=dict(color="#FFA500", size=10)
    )

    # Plot driver lines
    for drv_num in selected_drivers:
        sub = positions_df[positions_df['driver_number'] == drv_num].sort_values('lap')
        if sub.empty:
            continue
        info = driver_info_by_num.get(drv_num, {})
        color = info.get('color', '#FFFFFF')
        name = info.get('code', str(drv_num))
        is_max = (drv_num == 1)
        
        fig.add_trace(go.Scatter(
            x=sub['lap'],
            y=sub['position'],
            mode='lines+markers' if is_max else 'lines',
            name=f"{name} ({info.get('team', '')})",
            line=dict(
                color=color,
                width=4 if is_max else 2,
                dash='solid'
            ),
            marker=dict(
                size=6 if is_max else 3,
                color=color,
                symbol='circle'
            ),
            hovertemplate=f"<b>{name}</b><br>Lap: %{{x}}<br>Position: P%{{y}}<extra></extra>"
        ))

    # Add key milestone annotations for Max Verstappen
    fig.add_annotation(
        x=1, y=17, text="Grid: P17", showarrow=True,
        arrowhead=2, arrowcolor="#3671C6", arrowsize=1,
        font=dict(color="#3671C6", size=11), ax=-25, ay=-20
    )
    fig.add_annotation(
        x=1, y=11, text="Lap 1: P11 (+6)", showarrow=True,
        arrowhead=2, arrowcolor="#3671C6",
        font=dict(color="#3671C6", size=10), ax=30, ay=25
    )
    fig.add_annotation(
        x=29, y=2, text="P2 (Russell/Norris Pit)", showarrow=True,
        arrowhead=2, arrowcolor="#FFE600",
        font=dict(color="#FFE600", size=10), ax=-20, ay=-30
    )
    fig.add_annotation(
        x=43, y=1, text="Lap 43: P1 (Lead Overtake)", showarrow=True,
        arrowhead=2, arrowcolor="#39B54A",
        font=dict(color="#39B54A", size=11), ax=20, ay=-35
    )

    fig.update_layout(
        template=F1_TEMPLATE,
        title="<b>Position Progression (Laps 1 - 69)</b> • Note: Y-axis is inverted (P1 at top)",
        xaxis_title="Lap Number",
        yaxis_title="Track Position",
        yaxis=dict(
            autorange='reversed',
            tickmode='linear',
            tick0=1,
            dtick=2,
            range=[20.5, 0.5]
        ),
        xaxis=dict(range=[0, 70], dtick=5),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=520
    )
    return fig


def create_lap_time_chart(laps_clean, selected_drivers, driver_info_by_num, remove_outliers=True, show_rolling=True):
    fig = go.Figure()

    # Incidents bands
    fig.add_vrect(x0=27, x1=28.5, fillcolor="rgba(255, 230, 0, 0.12)", layer="below", line_width=0)
    fig.add_vrect(x0=29.5, x1=32, fillcolor="rgba(255, 165, 0, 0.12)", layer="below", line_width=0)
    fig.add_vrect(x0=32, x1=33, fillcolor="rgba(255, 30, 30, 0.15)", layer="below", line_width=0)
    fig.add_vrect(x0=39, x1=42.5, fillcolor="rgba(255, 165, 0, 0.12)", layer="below", line_width=0)

    for drv_num in selected_drivers:
        sub = laps_clean[laps_clean['driver_number'] == drv_num].sort_values('lap_number').copy()
        if sub.empty:
            continue
        
        # Outlier filter (e.g. SC / pit laps)
        if remove_outliers:
            sub = sub[sub['lap_duration'] < 100]

        info = driver_info_by_num.get(drv_num, {})
        color = info.get('color', '#FFFFFF')
        name = info.get('code', str(drv_num))
        is_max = (drv_num == 1)

        # Raw scatter / subtle line
        fig.add_trace(go.Scatter(
            x=sub['lap_number'],
            y=sub['lap_duration'],
            mode='markers+lines' if not show_rolling else 'markers',
            name=f"{name} Lap Time",
            marker=dict(
                size=5 if is_max else 3,
                color=color,
                opacity=0.7 if is_max else 0.4
            ),
            line=dict(color=color, width=1, dash='dot'),
            hovertemplate=f"<b>{name}</b><br>Lap: %{{x}}<br>Time: %{{y:.3f}}s<extra></extra>"
        ))

        # Rolling average curve
        if show_rolling and len(sub) > 3:
            sub['rolling_avg'] = sub['lap_duration'].rolling(window=3, min_periods=1).mean()
            fig.add_trace(go.Scatter(
                x=sub['lap_number'],
                y=sub['rolling_avg'],
                mode='lines',
                name=f"{name} 3-Lap Trend",
                line=dict(color=color, width=3.5 if is_max else 1.8),
                hovertemplate=f"<b>{name} Trend</b><br>Lap: %{{x}}<br>Avg: %{{y:.3f}}s<extra></extra>"
            ))

    # Mark Max's fastest lap
    max_laps = laps_clean[laps_clean['driver_number'] == 1]
    if not max_laps.empty:
        fastest = max_laps.loc[max_laps['lap_duration'].idxmin()]
        fig.add_annotation(
            x=fastest['lap_number'], y=fastest['lap_duration'],
            text=f"Max Fastest: {fastest['lap_duration']:.3f}s (L{int(fastest['lap_number'])})",
            showarrow=True, arrowhead=2, arrowcolor="#A855F7",
            font=dict(color="#C084FC", size=11, family="sans-serif"),
            ax=0, ay=-35
        )

    fig.update_layout(
        template=F1_TEMPLATE,
        title="<b>Pace Dynamics & Lap Times (Seconds)</b> • Note Max's purple surge Laps 43-69",
        xaxis_title="Lap Number",
        yaxis_title="Lap Time (Seconds)",
        xaxis=dict(range=[0, 70], dtick=5),
        yaxis=dict(dtick=2),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=500
    )
    return fig


def create_stint_timeline_chart(stints_df, driver_info_by_num, selected_drivers):
    fig = go.Figure()

    compound_colors = {
        'INTERMEDIATE': '#39B54A',  # Pirelli green
        'WET': '#0090D0',           # Pirelli blue
        'SOFT': '#E10600',
        'MEDIUM': '#FFD100',
        'HARD': '#FFFFFF'
    }

    # Filter to selected drivers
    plot_drivers = [d for d in selected_drivers if d in stints_df['driver_number'].values]
    # Keep reverse order so top driver is at top of y-axis
    plot_drivers.reverse()

    for idx, drv in enumerate(plot_drivers):
        sub = stints_df[stints_df['driver_number'] == drv].sort_values('stint_number')
        info = driver_info_by_num.get(drv, {})
        code = info.get('code', str(drv))

        for _, row in sub.iterrows():
            compound = row.get('compound', 'INTERMEDIATE')
            color = compound_colors.get(compound, '#39B54A')
            lap_start = row['lap_start']
            lap_end = row['lap_end']
            stint_len = lap_end - lap_start + 1

            fig.add_trace(go.Bar(
                y=[f"{code} (#{drv})"],
                x=[stint_len],
                base=[lap_start],
                orientation='h',
                name=compound,
                marker=dict(
                    color=color,
                    line=dict(color='#1A1D24', width=2)
                ),
                text=f"{compound[:3]} (L{lap_start}-{lap_end})",
                textposition='inside',
                insidetextfont=dict(color='#000000', size=11, family='sans-serif'),
                hovertemplate=f"<b>{code}</b><br>Stint {row['stint_number']}: {compound}<br>Laps {lap_start} to {lap_end} ({stint_len} laps)<extra></extra>",
                showlegend=(idx == 0 and row['stint_number'] == 1)
            ))

    # Add Red Flag line
    fig.add_vline(
        x=32, line_width=2, line_dash="dash", line_color="#FF1E1E",
        annotation_text="Red Flag Stoppage (Free Tyre Change)",
        annotation_position="top left",
        annotation_font=dict(color="#FF4D4D", size=10)
    )

    fig.update_layout(
        template=F1_TEMPLATE,
        barmode='stack',
        title="<b>Tyre Stint Comparison & Strategy Split</b> • Green = Intermediate Compound",
        xaxis_title="Race Lap",
        xaxis=dict(range=[0, 70], dtick=5),
        height=380,
        margin={'l': 100, 'r': 20, 't': 40, 'b': 40}
    )
    return fig


def create_telemetry_chart(telemetry_data, target_lap_keys):
    fig = make_subplots(
        rows=4, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,
        subplot_titles=("Speed (km/h)", "Throttle (%)", "Brake", "Gear"),
        row_heights=[0.42, 0.22, 0.16, 0.20]
    )

    line_styles = ['solid', 'dash', 'dot', 'dashdot']
    colors = ['#3671C6', '#FF8000', '#27F4D2', '#0093CC', '#E8002D', '#A855F7']

    for i, key in enumerate(target_lap_keys):
        if key not in telemetry_data:
            continue
        lap_obj = telemetry_data[key]
        points = lap_obj['telemetry']
        if not points:
            continue
        
        df_pts = pd.DataFrame(points)
        label = lap_obj.get('label', key)
        color = colors[i % len(colors)]
        dash = line_styles[i % len(line_styles)]
        is_hero = (i == 0)

        # 1. Speed trace
        fig.add_trace(
            go.Scatter(
                x=df_pts['distance_m'],
                y=df_pts['speed'],
                mode='lines',
                name=label,
                line=dict(color=color, width=3 if is_hero else 1.8, dash=dash),
                hovertemplate=f"<b>{label}</b><br>Dist: %{{x:.0f}}m<br>Speed: %{{y}} km/h<extra></extra>"
            ),
            row=1, col=1
        )

        # 2. Throttle trace
        fig.add_trace(
            go.Scatter(
                x=df_pts['distance_m'],
                y=df_pts['throttle'],
                mode='lines',
                name=label,
                line=dict(color=color, width=2 if is_hero else 1.5, dash=dash),
                showlegend=False,
                hovertemplate=f"Throttle: %{{y}}%<extra></extra>"
            ),
            row=2, col=1
        )

        # 3. Brake trace
        fig.add_trace(
            go.Scatter(
                x=df_pts['distance_m'],
                y=df_pts['brake'],
                mode='lines',
                name=label,
                line=dict(color=color, width=2 if is_hero else 1.5, dash=dash),
                showlegend=False,
                hovertemplate=f"Brake: %{{y}}<extra></extra>"
            ),
            row=3, col=1
        )

        # 4. Gear trace
        fig.add_trace(
            go.Scatter(
                x=df_pts['distance_m'],
                y=df_pts['n_gear'],
                mode='lines',
                name=label,
                line=dict(color=color, width=2 if is_hero else 1.5, dash=dash),
                showlegend=False,
                hovertemplate=f"Gear: %{{y}}<extra></extra>"
            ),
            row=4, col=1
        )

    # Annotate key corners on Interlagos circuit (approx distance in meters)
    corner_annotations = [
        (400, "Turn 1-2 (Senna S)"),
        (1100, "Turn 4 (Descida do Lago)"),
        (1850, "Turn 6-7 (Ferradura)"),
        (2500, "Turn 8-9 (Infield)"),
        (3100, "Turn 10 (Bico de Pato)"),
        (3700, "Turn 12 (Junção)")
    ]
    for dist, cname in corner_annotations:
        fig.add_vline(
            x=dist, line_width=1, line_dash="dot", line_color="#4A5568",
            row="all", col=1
        )
        fig.add_annotation(
            x=dist, y=325, text=cname, showarrow=False,
            font=dict(color="#A0AEC0", size=9),
            row=1, col=1
        )

    fig.update_layout(
        template=F1_TEMPLATE,
        title="<b>High-Resolution Telemetry Comparison across 4,309m Interlagos Circuit</b>",
        xaxis4_title="Lap Distance (Meters)",
        yaxis_title="km/h",
        yaxis2_title="Throttle %",
        yaxis3_title="Brake",
        yaxis4_title="Gear",
        yaxis=dict(range=[60, 340]),
        yaxis2=dict(range=[-5, 105]),
        yaxis3=dict(range=[-0.1, 1.2], tickvals=[0, 1]),
        yaxis4=dict(range=[1, 8.5], tickvals=[1, 2, 3, 4, 5, 6, 7, 8]),
        height=720,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="right",
            x=1
        )
    )
    return fig


def create_weather_chart(weather_df):
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=("Track & Air Temperature (°C)", "Rainfall Status (Wet Conditions)"),
        row_heights=[0.65, 0.35]
    )

    if not weather_df.empty:
        # Convert date to datetime
        weather_df = weather_df.copy()
        weather_df['dt'] = pd.to_datetime(weather_df['date'], format='ISO8601')

        # 1. Track & Air Temp
        fig.add_trace(
            go.Scatter(
                x=weather_df['dt'],
                y=weather_df['track_temperature'],
                mode='lines',
                name='Track Temp (°C)',
                line=dict(color='#FF5722', width=2.5),
                hovertemplate="Track: %{y:.1f}°C<extra></extra>"
            ),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=weather_df['dt'],
                y=weather_df['air_temperature'],
                mode='lines',
                name='Air Temp (°C)',
                line=dict(color='#00BCD4', width=2),
                hovertemplate="Air: %{y:.1f}°C<extra></extra>"
            ),
            row=1, col=1
        )

        # 2. Rainfall binary / intensity
        fig.add_trace(
            go.Scatter(
                x=weather_df['dt'],
                y=weather_df['rainfall'],
                mode='lines',
                fill='tozeroy',
                name='Rainfall Active',
                line=dict(color='#2196F3', width=2),
                fillcolor='rgba(33, 150, 243, 0.3)',
                hovertemplate="Rain: %{y}<extra></extra>"
            ),
            row=2, col=1
        )

    fig.update_layout(
        template=F1_TEMPLATE,
        title="<b>Micro-Climate & Rainfall Evolution During São Paulo GP</b>",
        xaxis2_title="Race Time (UTC)",
        yaxis_title="Temperature (°C)",
        yaxis2_title="Rainfall (1=Yes)",
        yaxis2=dict(tickvals=[0, 1], range=[-0.1, 1.2]),
        height=450,
        legend=dict(orientation="h", yanchor="bottom", y=1.03, xanchor="right", x=1)
    )
    return fig


def create_sector_pace_chart(laps_clean, driver_info_by_num, target_drivers=[1, 4, 63, 31, 16]):
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=("Sector 1 (Power & Senna S)", "Sector 2 (Infield Mechanical Grip)", "Sector 3 (Uphill Junção Drag)")
    )

    colors = ['#3671C6', '#FF8000', '#27F4D2', '#0093CC', '#E8002D']

    # Filter to green flag clean laps (e.g. lap > 43 clean air phase)
    clean_phase = laps_clean[(laps_clean['lap_number'] >= 44) & (laps_clean['lap_number'] <= 69)]

    for idx, drv in enumerate(target_drivers):
        sub = clean_phase[clean_phase['driver_number'] == drv]
        if sub.empty:
            continue
        info = driver_info_by_num.get(drv, {})
        code = info.get('code', str(drv))
        color = info.get('color', colors[idx % len(colors)])

        fig.add_trace(
            go.Box(
                y=sub['duration_sector_1'],
                name=code,
                marker_color=color,
                boxmean=True,
                showlegend=False
            ),
            row=1, col=1
        )
        fig.add_trace(
            go.Box(
                y=sub['duration_sector_2'],
                name=code,
                marker_color=color,
                boxmean=True,
                showlegend=False
            ),
            row=1, col=2
        )
        fig.add_trace(
            go.Box(
                y=sub['duration_sector_3'],
                name=code,
                marker_color=color,
                boxmean=True,
                showlegend=(idx == 0)
            ),
            row=1, col=3
        )

    fig.update_layout(
        template=F1_TEMPLATE,
        title="<b>Clean Air Sector Pace Distribution (Laps 44 - 69)</b> • Note Max's dominance in Sector 2",
        yaxis_title="Seconds",
        height=380
    )
    return fig
