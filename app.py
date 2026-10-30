import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import data_processor
import charts
import rb20_blueprint

# Page setup
st.set_page_config(
    page_title="F1 Strategy Explorer • RB20 Telemetry HUD • São Paulo 2024",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for F1 Dark Aesthetics & HUD Styling
st.markdown("""
<style>
    /* Dark Slate / Carbon Background */
    .stApp {
        background-color: #070A0F;
        color: #F0F2F6;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Hero Title Card */
    .f1-header {
        background: linear-gradient(135deg, #111726 0%, #162035 50%, #0B111E 100%);
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    }
    .f1-title {
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .f1-subtitle {
        font-size: 14px;
        color: #94A3B8;
        margin-top: 4px;
        margin-bottom: 0px;
    }
    .tag-rb {
        background-color: #3671C6;
        color: white;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
    }
    .tag-wet {
        background-color: #39B54A;
        color: black;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
    }
    .tag-redflag {
        background-color: #E10600;
        color: white;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
    }

    /* Interactive HUD Container */
    .hud-card {
        background: #0B0F19;
        border: 1px solid #1F293D;
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .hud-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    .hud-header-title {
        font-size: 16px;
        font-weight: 800;
        letter-spacing: 1px;
        color: #E2E8F0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* KPI Metrics Cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 14px;
        margin-bottom: 22px;
    }
    .metric-card {
        background: #111622;
        border: 1px solid #1E283D;
        border-radius: 10px;
        padding: 14px 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .metric-label {
        font-size: 11px;
        text-transform: uppercase;
        color: #8C9BB4;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 800;
        color: #FFFFFF;
        margin: 4px 0;
    }
    .metric-delta {
        font-size: 11px;
        font-weight: 600;
    }
    .delta-green { color: #10B981; }
    .delta-red { color: #EF4444; }
    .delta-purple { color: #C084FC; }
    .delta-amber { color: #F59E0B; }

    /* Overtake card */
    .overtake-card {
        background: #111622;
        border-left: 4px solid #3671C6;
        border-top: 1px solid #1E283D;
        border-right: 1px solid #1E283D;
        border-bottom: 1px solid #1E283D;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .overtake-title {
        font-size: 14px;
        font-weight: 700;
        color: #FFFFFF;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .overtake-desc {
        font-size: 12.5px;
        color: #94A3B8;
        margin-top: 4px;
    }

    /* Strategy box */
    .strategy-card {
        background: #111622;
        border: 1px solid #1E283D;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 14px;
    }

    /* Radio message box */
    .radio-card {
        background: #0D111A;
        border-left: 3px solid #10B981;
        border-radius: 6px;
        padding: 12px 16px;
        margin-bottom: 10px;
        font-family: monospace;
        font-size: 13px;
    }

    /* Component Active Badge */
    .active-badge {
        background: #1E283D;
        border: 1px solid #3B82F6;
        color: #60A5FA;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

# Load data via cache
@st.cache_data
def load_all_data():
    return data_processor.get_processed_data()

data = load_all_data()

drivers_df = data['drivers']
driver_info_by_num = data['driver_info_by_num']
laps_clean = data['laps_clean']
positions_df = data['positions_df']
stints_df = data['stints']
pit_df = data['pit']
race_control_df = data['race_control']
weather_df = data['weather']
telemetry_data = data['telemetry']
overtakes = data['overtakes']
radio_transcripts = data['radio_transcripts']

# Initialize active system session state
if 'active_system' not in st.session_state:
    st.session_state['active_system'] = 'tyres'

# ----------------- SIDEBAR CONTROLS -----------------
with st.sidebar:
    st.image("https://media.formula1.com/content/dam/fom-website/2018-redesign-assets/circuit-assets/circuits/interlagos.png", width=280)
    st.markdown("### 🏎️ Race Selector")
    st.selectbox("Select Grand Prix", ["2024 São Paulo GP (Interlagos)"], index=0)
    
    st.markdown("---")
    st.markdown("### 👥 Contenders Selection")
    
    all_driver_nums = sorted(list(driver_info_by_num.keys()))
    default_selected = [1, 4, 63, 31, 10, 16]
    
    selected_drivers = st.multiselect(
        "Choose Drivers to Compare:",
        options=all_driver_nums,
        default=default_selected,
        format_func=lambda x: f"{driver_info_by_num[x]['code']} (#{x}) - {driver_info_by_num[x]['short_name']} ({driver_info_by_num[x]['team']})"
    )
    if not selected_drivers:
        selected_drivers = [1, 4, 63]

    st.markdown("---")
    st.markdown("### ⚙️ Telemetry Settings")
    filter_outliers = st.checkbox("Filter Safety Car / Outlier Laps (>100s)", value=True)
    show_rolling = st.checkbox("Show 3-Lap Rolling Trend", value=True)

    st.markdown("---")
    st.markdown("""
    **Event Summary:**
    - **Date:** Nov 3, 2024
    - **Circuit:** Autódromo José Carlos Pace
    - **Distance:** 69 Laps (Wet)
    - **Winner:** Max Verstappen (P17 -> P1)
    - **Fastest Lap:** 1:20.472 (VER, L67)
    - **Winning Margin:** +19.477s
    """)

# ----------------- HEADER & HERO SECTION -----------------
st.markdown("""
<div class="f1-header">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
        <div>
            <div class="f1-title">
                <span>ORACLE RED BULL RACING • RB20 STRATEGY EXPLORER</span>
            </div>
            <div class="f1-subtitle">
                São Paulo 2024 Grand Prix • Interactive Vehicle Schematic & Deep Telemetry Analytics
            </div>
        </div>
        <div style="display: flex; gap: 8px; align-items: center; margin-top: 4px;">
            <span class="tag-rb">CHASSIS: RB20 #1</span>
            <span class="tag-wet">INTERMEDIATE TYRES</span>
            <span class="tag-redflag">RED FLAG LAP 32</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- HERO KPI METRICS -----------------
st.markdown("""
<div class="metric-grid">
    <div class="metric-card">
        <div class="metric-label">Grid to Victory</div>
        <div class="metric-value">P17 ➔ P1</div>
        <div class="metric-delta delta-green">▲ +16 Positions Gained</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Winning Margin</div>
        <div class="metric-value">+19.477s</div>
        <div class="metric-delta delta-green">Over Esteban Ocon (P2)</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Fastest Lap of Race</div>
        <div class="metric-value">1:20.472</div>
        <div class="metric-delta delta-purple">⚡ Lap 67 (1.045s faster than NOR)</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Fastest Laps Broken</div>
        <div class="metric-value">17 Times</div>
        <div class="metric-delta delta-purple">Uncontested in Clean Air</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Strategic Time Saved</div>
        <div class="metric-value">~24.5s</div>
        <div class="metric-delta delta-amber">Free tyre change under Red Flag</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Championship Swing</div>
        <div class="metric-value">+18 Points</div>
        <div class="metric-delta delta-green">62 pt lead over Norris</div>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================================
# INTERACTIVE RB20 CAR HUD & SYSTEM SWITCHER
# =========================================================================
st.markdown("""
<div class="hud-header">
    <div class="hud-header-title">
        <span>🏎️ INTERACTIVE RB20 TELEMETRY BLUEPRINT</span>
    </div>
    <div>
        <span class="active-badge">CLICK ANY SYSTEM TO INSPECT SENSORS & STRATEGY</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 6 System Selector Buttons
col_b1, col_b2, col_b3, col_b4, col_b5, col_b6 = st.columns(6)

with col_b1:
    if st.button("🛞 Tyres & Stints", use_container_width=True, type="primary" if st.session_state['active_system'] == 'tyres' else "secondary"):
        st.session_state['active_system'] = 'tyres'
        st.rerun()

with col_b2:
    if st.button("🧠 Pit Wall & Strategy", use_container_width=True, type="primary" if st.session_state['active_system'] == 'strategy' else "secondary"):
        st.session_state['active_system'] = 'strategy'
        st.rerun()

with col_b3:
    if st.button("⚡ Power Unit & Overtakes", use_container_width=True, type="primary" if st.session_state['active_system'] == 'engine' else "secondary"):
        st.session_state['active_system'] = 'engine'
        st.rerun()

with col_b4:
    if st.button("🏎️ Cockpit & Telemetry", use_container_width=True, type="primary" if st.session_state['active_system'] == 'cockpit' else "secondary"):
        st.session_state['active_system'] = 'cockpit'
        st.rerun()

with col_b5:
    if st.button("🌧️ Aero, Rain & Flags", use_container_width=True, type="primary" if st.session_state['active_system'] == 'aero' else "secondary"):
        st.session_state['active_system'] = 'aero'
        st.rerun()

with col_b6:
    if st.button("📊 Full Race Progression", use_container_width=True, type="primary" if st.session_state['active_system'] == 'progression' else "secondary"):
        st.session_state['active_system'] = 'progression'
        st.rerun()

# Render RB20 SVG Blueprint
svg_code = rb20_blueprint.get_rb20_svg(st.session_state['active_system'])
components.html(svg_code, height=455)


# =========================================================================
# DYNAMIC SUBSYSTEM DEEP-DIVES BASED ON SELECTION
# =========================================================================

active = st.session_state['active_system']

if active == 'tyres':
    st.markdown("---")
    st.markdown("### 🛞 Subsystem Focus: Pirelli Intermediate Tyres & Thermal Dynamics")
    
    col_t_a, col_t_b = st.columns([3, 2])
    with col_t_a:
        st.markdown("""
        **Pirelli Intermediate Compound (Green Rim):**
        - **Groove Density:** 35 litres of water evacuated per second at 300 km/h.
        - **Optimal Working Window:** 80°C – 100°C.
        - **The Wet Paradox:** In wet conditions, tyres do not degrade from friction. They degrade from **thermal overheating** if driven aggressively on dry asphalt patches, causing the tall tread blocks to squirm, tear, and blister.
        """)
        # Lap time chart
        fig_laps = charts.create_lap_time_chart(
            laps_clean, selected_drivers, driver_info_by_num,
            remove_outliers=filter_outliers, show_rolling=show_rolling
        )
        st.plotly_chart(fig_laps, use_container_width=True)

    with col_t_b:
        st.markdown("#### 🔬 Max's Tyre Management Masterclass")
        st.markdown("""
        <div class="strategy-card">
            <h5 style="color:#39B54A; margin-top:0;">1. Thermal Discipline behind Leclerc (L12-24)</h5>
            <p style="font-size:13px; color:#CBD5E1;">
            Trailing within 1.5s in the wet traps boiling aerosol onto radiators and front tyres. Rather than forcing a high-risk dive on Leclerc, Verstappen sat back at 1.4s, continually finding wet patches off-line down the straight to cool the rubber. When Leclerc's tyres overheated, Charles pitted, freeing Max.
            </p>
        </div>
        <div class="strategy-card">
            <h5 style="color:#FFE600; margin-top:0;">2. The VSC Patience on Worn Inters (L27-28)</h5>
            <p style="font-size:13px; color:#CBD5E1;">
            When rain intensified on Lap 27, Russell and Norris pitted for new inters. But new wet tyres offer little advantage in standing water where aquaplaning is the limiter. Old inters with worn tread blocks suffer <i>less</i> squirm and heat buildup. Max preserved track position.
            </p>
        </div>
        <div class="strategy-card">
            <h5 style="color:#C084FC; margin-top:0;">3. Clean Air Alternative Wet Lines (L44-69)</h5>
            <p style="font-size:13px; color:#CBD5E1;">
            In wet conditions, the rubbered-in dry racing line becomes slick as ice. Max drove classic karting wet lines: squaring off Turn 1, driving around the outside of Curva do Sol where fresh tarmac offered higher friction, and getting on full throttle 20m earlier than Norris.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Stint comparison
    st.markdown("#### 📊 Stint Lengths & Tyre Strategies Across the Field")
    fig_stints = charts.create_stint_timeline_chart(stints_df, driver_info_by_num, selected_drivers)
    st.plotly_chart(fig_stints, use_container_width=True)

    # Sector pace
    st.markdown("#### ⏱️ Clean Air Sector Pace Distribution (Laps 44 - 69)")
    fig_sectors = charts.create_sector_pace_chart(laps_clean, driver_info_by_num, target_drivers=[1, 4, 63, 31, 16])
    st.plotly_chart(fig_sectors, use_container_width=True)


elif active == 'strategy':
    st.markdown("---")
    st.markdown("### 🧠 Subsystem Focus: Pit Wall Masterstroke & 'What-If' Strategy Simulator")

    col_s1, col_s2 = st.columns([3, 2])
    with col_s1:
        st.markdown("""
        #### ⚖️ The Critical Decision on Lap 28
        When the Virtual Safety Car was called for Hulkenberg's off, Formula 1 pit walls faced an existential choice:
        
        - **Mercedes & McLaren Philosophy:** *"We have track position, but fresh intermediate tyres will give us 1.5 seconds per lap. Let's box under VSC while the pit lane delta is reduced to ~16 seconds."*
        - **Red Bull Philosophy:** *"Track position in the wet is everything because spray destroys following cars. Furthermore, our radar shows the mother of all rainstorms arriving in 3 minutes. In heavy rain, they will either deploy a full Safety Car or throw a Red Flag. **Stay out.**"*
        """)

        st.markdown("""
        | Team | Driver | Decision Lap 28 | Pit Delta Lost | Track Position After Red Flag | Outcome |
        |---|---|---|---|---|---|
        | **Red Bull** | Max Verstappen | **STAY OUT** | **0.0s (Free Stop)** | **P2 (Lead battle)** | **Won Race (P1)** |
        | **Alpine** | Esteban Ocon | **STAY OUT** | **0.0s (Free Stop)** | **P1 (Leader)** | **P2 Podium** |
        | **Alpine** | Pierre Gasly | **STAY OUT** | **0.0s (Free Stop)** | **P3** | **P3 Podium** |
        | **Mercedes** | George Russell | Pitted for Intermediates | -26.4s lost | P5 | P4 Finish |
        | **McLaren** | Lando Norris | Pitted for Intermediates | -27.1s lost | P4 | P6 Finish |
        """)

        st.markdown("#### 📻 Authentic Pit Wall Radio Communications")
        for rad in radio_transcripts:
            st.markdown(f"""
            <div class="radio-card">
                <span style="color:#38BDF8; font-weight:700;">[{rad['lap']}]</span> 
                <span style="color:#F59E0B; font-weight:700;">{rad['speaker']} ({rad['role']}):</span> 
                <span style="color:#FFFFFF;">"{rad['message']}"</span>
                <div style="font-size:11px; color:#64748B; margin-top:3px; font-style:italic;">Context: {rad['context']}</div>
            </div>
            """, unsafe_allow_html=True)

    with col_s2:
        st.markdown("#### 🎮 'What-If' Strategy Simulator")
        sim_max_pits_vsc = st.checkbox("Simulate: Max Verstappen pits under VSC on Lap 28", value=False)
        sim_red_flag_called = st.checkbox("Was the Red Flag deployed on Lap 32?", value=True)
        sim_wet_pace_delta = st.slider("Max Verstappen Wet Pace Advantage (sec/lap):", 0.0, 2.5, 1.2, step=0.1)

        st.markdown("---")
        st.markdown("##### 🔮 Simulated Strategic Outcome:")

        net_delta = 0.0
        projected_finish = "P1 (Victory)"
        championship_impact = "+18 pts over Norris (62 pt lead)"

        if sim_max_pits_vsc:
            net_delta += 18.5
            if not sim_red_flag_called:
                projected_finish = "P2 or P3 (Podium)"
                championship_impact = "+7 pts over Norris"
            else:
                projected_finish = "P4 or P5"
                championship_impact = "-2 pts to Norris"
        else:
            if not sim_red_flag_called:
                net_delta += 8.0
                projected_finish = "P2 (Battle with Russell/Norris)"
                championship_impact = "+10 pts over Norris"
            else:
                projected_finish = "P1 (Historical Domination • +19.477s margin)"
                championship_impact = "+18 pts over Norris (Title sealed)"

        st.metric("Projected Finish Position", projected_finish, f"Net Time Delta: {net_delta:+.1f}s")
        st.metric("Simulated Championship Impact", championship_impact)

        if sim_max_pits_vsc:
            st.error("⚠️ **Strategic Blunder Verdict:** Boxing under VSC would have dropped Verstappen into dirty spray behind Lawson and Piastri, wiping out the Red Flag free tyre change.")
        else:
            st.success("✅ **Strategic Masterclass Verdict:** Staying out preserved track position and capitalized 100% on the Red Flag free pit stop regulations (saving ~24.5s).")


elif active == 'engine':
    st.markdown("---")
    st.markdown("### ⚡ Subsystem Focus: Honda RBPT Power Unit & The P17 Charge")

    col_e1, col_e2 = st.columns([3, 2])
    with col_e1:
        st.markdown("""
        #### ⚙️ The Engine Penalty Backstory
        Heading into the São Paulo weekend, Red Bull discovered internal combustion engine (ICE) wear on Max's power unit pool following the Mexico GP.
        Red Bull opted to fit **Internal Combustion Engine #6**, exceeding the season allocation and incurring an automatic **5-place grid penalty**.
        
        Compounding this, in Sunday morning's delayed wet Qualifying, Lance Stroll crashed in Q2 bringing out a Red Flag right as Verstappen was completing his flying lap. Verstappen was eliminated in **P12**, which became **P17** after applying the penalty.
        """)
        
        st.markdown("#### 🚀 Power Unit Telemetry Specs in the Wet")
        st.markdown("""
        - **Engine:** Honda RBPTH002 1.6L 90° V6 Turbocharged Hybrid
        - **Electrical Boost (MGU-K):** 120 kW (161 hp) instant torque deployed through the uphill drag of Junção
        - **Top Speed on Reta Oposta:** 324.5 km/h in wet slipstream
        - **Throttle Mapping:** Progressive wet-weather torque curve calibrated to prevent snap oversteer on exit of Turn 2 and Turn 12.
        """)

    with col_e2:
        st.markdown("#### ⚔️ The 10 Overtakes Breakdown (P17 to P1)")
        for ot in overtakes:
            st.markdown(f"""
            <div class="overtake-card">
                <div class="overtake-title">
                    <span>Lap {ot['lap']} • {ot['position_before']} ➔ {ot['position_after']}</span>
                    <span class="tag-rb" style="font-size:11px;">{ot['badge']}</span>
                </div>
                <div style="font-weight:600; color:#E2E8F0; margin-top:3px; font-size:13px;">
                    Passed: {ot['car_passed']}
                </div>
                <div style="font-size:12px; color:#38BDF8; margin-top:2px;">
                    📍 {ot['location']}
                </div>
                <div class="overtake-desc">{ot['details']}</div>
            </div>
            """, unsafe_allow_html=True)


elif active == 'cockpit':
    st.markdown("---")
    st.markdown("### 🏎️ Subsystem Focus: Cockpit Telemetry & Fastest Lap (1:20.472)")

    st.markdown("""
    On Lap 67, Max Verstappen clocked a **1:20.472** — over **1.045 seconds faster** than Lando Norris, and 1.2+ seconds faster than Russell, Leclerc, and Ocon. 
    Compare the telemetry traces across speed, throttle, braking, and gear selection across all 4,309 meters of Interlagos.
    """)

    available_keys = list(telemetry_data.keys())
    selected_telemetry_keys = st.multiselect(
        "Select Laps to Overlay on Telemetry Traces:",
        options=available_keys,
        default=['VER_Lap67_Fastest', 'NOR_Lap66_Fastest', 'OCO_Lap65_Fastest'],
        format_func=lambda x: telemetry_data[x]['label']
    )

    if selected_telemetry_keys:
        fig_telem = charts.create_telemetry_chart(telemetry_data, selected_telemetry_keys)
        st.plotly_chart(fig_telem, use_container_width=True)

    st.markdown("#### 🏁 Micro-Sector & Corner Breakdown: Where Did Max Find 1.045s?")
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        st.markdown("""
        <div class="strategy-card">
            <h5 style="color:#38BDF8; margin-top:0;">Turn 1-2 (Senna S)</h5>
            <p style="font-size:12px; color:#CBD5E1;">
            <b>Braking Point:</b> Max braked 15 meters later from 309 km/h into Turn 1, trusting front axle mechanical grip without locking the inside tyre.
            <br><b>Apex Speed:</b> 114 km/h vs Norris 108 km/h (+6 km/h delta).
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        st.markdown("""
        <div class="strategy-card">
            <h5 style="color:#10B981; margin-top:0;">Turn 4 (Descida do Lago)</h5>
            <p style="font-size:12px; color:#CBD5E1;">
            <b>The Wet Line:</b> Rather than hugging the rubbered-in curb, Max placed his car half a car-width wider on fresher, grittier tarmac, allowing 100% throttle application 25m earlier onto the Reta Oposta.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col_c3:
        st.markdown("""
        <div class="strategy-card">
            <h5 style="color:#C084FC; margin-top:0;">Turn 10-12 (Bico de Pato & Junção)</h5>
            <p style="font-size:12px; color:#CBD5E1;">
            <b>Traction Traction Traction:</b> While Norris and Russell had to feather throttle to catch snaps of oversteer, Verstappen achieved smooth linear throttle progression in 3rd gear, launching up the steep uphill drag.
            </p>
        </div>
        """, unsafe_allow_html=True)


elif active == 'aero':
    st.markdown("---")
    st.markdown("### 🌧️ Subsystem Focus: Aero Balance, Micro-Climate & Race Incidents")

    col_a1, col_a2 = st.columns([3, 2])
    with col_a1:
        fig_weather = charts.create_weather_chart(weather_df)
        st.plotly_chart(fig_weather, use_container_width=True)

    with col_a2:
        st.markdown("#### 🚨 Key Incident Deep-Dives")
        st.markdown("""
        <div class="strategy-card">
            <div style="display:flex; justify-content:space-between;">
                <b>Nico Hulkenberg Turn 1 Beaching</b>
                <span class="incident-pill-vsc">VSC Lap 27</span>
            </div>
            <p style="font-size:12px; color:#94A3B8; margin-top:6px;">
            Hulkenberg spun at Turn 1 and beached his Haas on the curb. Marshals pushed him back onto the track, triggering a Virtual Safety Car and ultimately a rare <b>Black Flag</b> disqualification.
            </p>
        </div>

        <div class="strategy-card">
            <div style="display:flex; justify-content:space-between;">
                <b>Franco Colapinto Heavy Crash</b>
                <span class="incident-pill-red">RED FLAG Lap 32</span>
            </div>
            <p style="font-size:12px; color:#94A3B8; margin-top:6px;">
            Under the Safety Car in torrential downpour, Colapinto aquaplaned exiting Junção and smashed violently into the outer wall on the main straight. The session was suspended, triggering the free tyre change.
            </p>
        </div>

        <div class="strategy-card">
            <div style="display:flex; justify-content:space-between;">
                <b>Carlos Sainz Barrier Impact</b>
                <span class="incident-pill-sc">Safety Car Lap 39</span>
            </div>
            <p style="font-size:12px; color:#94A3B8; margin-top:6px;">
            Sainz lost the rear of his Ferrari in the twisty infield at Turn 8, causing front-wing damage and retirement, leading to Safety Car 2 and setting up the Lap 43 restart.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Race Control Log Table
    st.markdown("#### 📋 Official FIA Race Control Messages Log")
    filter_flag = st.selectbox("Filter Messages By Category:", ["All Messages", "Flags & Safety Cars Only", "Red Flag & SC Only"])
    
    rc_filtered = race_control_df.copy()
    if filter_flag == "Flags & Safety Cars Only":
        rc_filtered = rc_filtered[rc_filtered['category'].isin(['Flag', 'SafetyCar']) | rc_filtered['message'].str.contains('FLAG|SAFETY|VIRTUAL', case=False, na=False)]
    elif filter_flag == "Red Flag & SC Only":
        rc_filtered = rc_filtered[rc_filtered['message'].str.contains('RED FLAG|SAFETY CAR|VIRTUAL', case=False, na=False)]
    
    display_rc = rc_filtered[['lap_number', 'category', 'flag', 'message', 'date']].rename(columns={
        'lap_number': 'Lap',
        'category': 'Category',
        'flag': 'Flag',
        'message': 'Race Control Message',
        'date': 'Timestamp (UTC)'
    })
    st.dataframe(display_rc, use_container_width=True, hide_index=True)


elif active == 'progression':
    st.markdown("---")
    st.markdown("### 📊 Subsystem Focus: 69-Lap Position Progression & Field Standings")

    fig_pos = charts.create_position_chart(positions_df, selected_drivers, driver_info_by_num)
    st.plotly_chart(fig_pos, use_container_width=True)

    st.markdown("#### 🔍 Real-Time Lap Inspector")
    lap_inspect = st.slider("Select Lap Number to Inspect Full Field Standings:", min_value=1, max_value=69, value=43, step=1)
    
    lap_data = positions_df[positions_df['lap'] == lap_inspect].sort_values('position')
    
    if not lap_data.empty:
        col_l1, col_l2, col_l3 = st.columns([1, 1, 2])
        leader_row = lap_data.iloc[0]
        max_row = lap_data[lap_data['driver_number'] == 1]
        max_pos_str = f"P{max_row.iloc[0]['position']}" if not max_row.empty else "N/A"
        
        with col_l1:
            st.metric("Race Leader", f"{leader_row['driver_name']} ({leader_row['team']})", f"Lap {lap_inspect}")
        with col_l2:
            st.metric("Max Verstappen Position", max_pos_str, "Started P17")
        with col_l3:
            incident_text = "🟢 Green Flag Racing"
            if lap_inspect in [27, 28]:
                incident_text = "🟡 VSC (Hulkenberg Spin at Turn 1)"
            elif 29 <= lap_inspect <= 32:
                incident_text = "🟠 Full Safety Car Deployed (Heavy Rain)"
            elif lap_inspect == 32:
                incident_text = "🔴 RED FLAG (Franco Colapinto Crash)"
            elif 39 <= lap_inspect <= 42:
                incident_text = "🟠 Full Safety Car 2 (Carlos Sainz Crash)"
            elif lap_inspect == 43:
                incident_text = "🟢 Restart 2: Verstappen overtakes Ocon for P1!"
            st.info(f"**Track Condition at Lap {lap_inspect}:** {incident_text}")

        display_cols = ['position', 'driver_code', 'driver_name', 'team', 'lap_time_str']
        st.dataframe(
            lap_data[display_cols].rename(columns={
                'position': 'Position',
                'driver_code': 'Code',
                'driver_name': 'Driver',
                'team': 'Team',
                'lap_time_str': 'Lap Time'
            }),
            use_container_width=True,
            hide_index=True
        )
