# 🏎️ F1 Strategy Explorer — 2024 São Paulo Grand Prix (Interlagos)
### *Max Verstappen's Masterclass: P17 to P1 in Torrential Rain*

An interactive, high-precision Formula 1 analytics and telemetry dashboard built with Python and Streamlit, recreating and analyzing one of the greatest wet-weather drives in motorsport history.

---

## 🌟 Key Highlights & Analytical Focus

At the **2024 São Paulo Grand Prix**, Max Verstappen qualified P12 (compromised by a red flag in Q2) and took a **5-place engine grid penalty**, starting **P17** on the grid. In treacherous, changing wet conditions, he carved through the field to win by **+19.477 seconds**, setting **17 fastest laps** and clocking the fastest lap of the race (**1:20.472** on Lap 67 — over **1.045 seconds** quicker than any other driver).

### Core Analytical Questions Addressed:
1. **Tyre Management (Push vs Conserve):**
   - **Phase 1 Attack (Laps 1–11):** Aggressive energy input into intermediate tyres to pass 6 cars on Lap 1 and reach P6 by Lap 11.
   - **Phase 2 Conservation (Laps 12–24):** Tucked behind Charles Leclerc's Ferrari; rather than destroying front tyre rubber in blinding aerosol spray, Max managed tyre temps, found off-line wet patches down straights to cool treads, and forced Leclerc into severe thermal degradation.
   - **Phase 3 Strategic Patience (Laps 25–32):** Staying out on worn inters under intensifying rain while rivals pitted; intermediate tyres in standing water do not thermally degrade.
   - **Phase 5 Clean Air Domination (Laps 44–69):** Unleashing alternative wet racing lines, braking 15m later into Turn 1, and pulling a +19.5s gap in 26 laps.
2. **Red Bull's Strategic Call vs McLaren & Mercedes:**
   - Under the Lap 27 Virtual Safety Car (VSC), Mercedes pitted race leader George Russell and McLaren pitted Lando Norris.
   - Red Bull (Gianpiero Lambiase & Hannah Schmitz) kept Verstappen out on track. Track position is king in spray, and weather radar showed an imminent severe downpour.
   - When Franco Colapinto crashed heavily under Safety Car on Lap 32, a **Red Flag** was deployed. Under FIA Sporting Code regulations, Verstappen was granted a **FREE tyre change** in the pit lane (zero time lost), wiping out the 26+ seconds Norris and Russell sacrificed.
3. **Flags & Incident Timeline:**
   - Complete breakdown of all 111 Race Control messages: VSC (Lap 27–28), Safety Car 1 (Lap 30–32), Red Flag (Lap 32), Safety Car 2 (Lap 39–42), and the decisive Lap 43 Restart.
4. **Telemetry Deep Dive (Lap 67 vs Rivals):**
   - Subplot telemetry traces (Speed, Throttle, Brake, Gear, DRS) comparing Max's fastest lap (1:20.472) against Lando Norris (1:21.517), Esteban Ocon (1:21.771), George Russell, and Charles Leclerc.

---

## 🚀 How to Run the Dashboard

The dashboard is served locally via Streamlit:

```bash
# Run using Python 3.13
python3.13 -m streamlit run app.py --server.port 8501
```

Once running, open your browser at:
`http://localhost:8501`

---

## 📊 Dashboard Modules & Features

1. **🏆 The P17 Masterclass:**
   - 6 KPI Hero Cards (Grid P17 ➔ P1, Winning Margin +19.477s, 1:20.472 Fastest Lap, 17 Fastest Laps Broken, ~24.5s Red Flag Time Saved, +18 Pt Championship Swing).
   - The 5 Strategic Phases expandable analysis.
   - Interactive Overtake Timeline for all 10 on-track passes.
2. **🏁 Lap-by-Lap Progression:**
   - Inverted track position progression chart across all 69 laps with VSC, SC, and Red Flag shading.
   - Interactive Lap Inspector slider showing exact field standings, team, and lap times on any lap.
3. **🛞 Tyre Management & Pace Dynamics:**
   - Scatter & 3-lap rolling average pace plot with outlier filtering.
   - Deep-dive cards on wet tyre physics, thermal balance, and spray dirty air.
   - Stint comparison timeline with Pirelli Intermediate green bands.
   - Sector 1, Sector 2, and Sector 3 boxplot pace distributions.
4. **🚩 Flags, Incidents & Weather:**
   - Dual-axis micro-climate evolution chart (Track Temp, Air Temp, Rainfall binary).
   - Case studies on Hulkenberg's VSC & Black Flag, Colapinto's Red Flag crash, and Sainz's SC.
   - Searchable, filterable 111-message FIA Race Control log.
5. **🧠 Red Bull Strategy & "What-If" Simulator:**
   - Comparative decision matrix (Red Bull vs Mercedes vs McLaren).
   - Authentic pit wall radio transcripts (GP Lambiase, Max Verstappen, Christian Horner).
   - Interactive Strategy Simulator: toggle VSC pit stop, Red Flag deployment, and wet pace delta to view simulated finish position and championship impact.
6. **⚡ Telemetry Deep Dive:**
   - Synchronized 4-row subplots across 4,309m Interlagos track distance.
   - Speed trace, throttle modulation, brake pressure, and gear selection.
   - Corner-by-corner tactical analysis: Turn 1-2 Senna S, Turn 4 Descida do Lago, and Turn 10-12 Junção.

---

## 📁 Repository Structure

```text
├── app.py                   # Main Streamlit dashboard application
├── charts.py                # Plotly figure builders with dark F1 telemetry template
├── data_processor.py        # Data pipeline, overtakes data & radio transcripts
├── data_loader.py           # Core JSON loader and validation utilities
├── download_telemetry.py    # OpenF1 telemetry extractor
├── data/
│   ├── drivers.json         # All 20 driver profiles, codes, numbers, and colors
│   ├── laps.json            # All 1,137 laps with sector times and speeds
│   ├── lap_positions.json   # Lap-by-lap positions for all 69 laps
│   ├── stints.json          # Tyre compounds and stint lengths
│   ├── pit.json             # Pit stop durations and timestamps
│   ├── race_control.json    # 111 FIA race control messages
│   ├── weather.json         # High-resolution weather and temperature logs
│   └── telemetry.json       # High-frequency telemetry for key laps
└── README.md
```
