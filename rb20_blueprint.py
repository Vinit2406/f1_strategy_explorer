def get_rb20_svg(active_system="tyres"):
    """
    Generates a high-tech F1 telemetry HUD blueprint of the Red Bull Racing RB20.
    Highlights components based on the active_system ('tyres', 'strategy', 'engine', 'cockpit', 'aero', 'progression').
    """
    # Color accents based on active system
    c_tyre = "#39B54A" if active_system == "tyres" else "#1F7A2D"
    c_tyre_glow = "filter: drop-shadow(0 0 10px #39B54A);" if active_system == "tyres" else ""
    
    c_engine = "#FF3B30" if active_system == "engine" else "#A31616"
    c_engine_glow = "filter: drop-shadow(0 0 12px #FF3B30);" if active_system == "engine" else ""

    c_cockpit = "#38BDF8" if active_system == "cockpit" else "#1E40AF"
    c_cockpit_glow = "filter: drop-shadow(0 0 12px #38BDF8);" if active_system == "cockpit" else ""

    c_aero = "#F59E0B" if active_system == "aero" else "#B45309"
    c_aero_glow = "filter: drop-shadow(0 0 12px #F59E0B);" if active_system == "aero" else ""

    c_strategy = "#C084FC" if active_system == "strategy" else "#6B21A8"
    c_strat_glow = "filter: drop-shadow(0 0 12px #C084FC);" if active_system == "strategy" else ""

    svg = f"""
    <svg viewBox="0 0 1100 440" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:#090C12; border:1px solid #1E2536; border-radius:12px; font-family:'Segoe UI', sans-serif;">
      <defs>
        <!-- Gradients -->
        <linearGradient id="rb-dark" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#080F1E"/>
          <stop offset="50%" stop-color="#14213D"/>
          <stop offset="100%" stop-color="#0B132B"/>
        </linearGradient>
        <linearGradient id="rb-blue" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#1E3A8A"/>
          <stop offset="50%" stop-color="#3671C6"/>
          <stop offset="100%" stop-color="#1D4ED8"/>
        </linearGradient>
        <linearGradient id="redbull-yellow" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#FFDD00"/>
          <stop offset="100%" stop-color="#FF9900"/>
        </linearGradient>
        <radialGradient id="tyre-glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#39B54A" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#39B54A" stop-opacity="0"/>
        </radialGradient>
        <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
          <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#161C2C" stroke-width="0.8"/>
        </pattern>
      </defs>

      <!-- Background Grid & Telemetry Crosshairs -->
      <rect width="100%" height="100%" fill="url(#grid)" />
      <circle cx="550" cy="220" r="180" fill="none" stroke="#1E283D" stroke-dasharray="4,4" stroke-width="1.2"/>
      <circle cx="550" cy="220" r="120" fill="none" stroke="#1A2234" stroke-width="1"/>
      <line x1="550" y1="20" x2="550" y2="420" stroke="#1A2234" stroke-dasharray="3,3" stroke-width="1"/>
      <line x1="50" y1="220" x2="1050" y2="220" stroke="#1A2234" stroke-dasharray="3,3" stroke-width="1"/>

      <!-- HUD Header Banner -->
      <text x="35" y="42" fill="#E2E8F0" font-size="14" font-weight="800" letter-spacing="1.5">ORACLE RED BULL RACING • RB20 TELEMETRY HUD</text>
      <text x="35" y="60" fill="#64748B" font-size="11">AUTÓDROMO JOSÉ CARLOS PACE • SÃO PAULO 2024 • MAX VERSTAPPEN #1</text>
      
      <!-- Status Badges Top Right -->
      <rect x="880" y="26" width="180" height="26" rx="5" fill="#131B2A" stroke="#253248"/>
      <circle cx="896" cy="39" r="4.5" fill="#10B981"/>
      <text x="908" y="43" fill="#E2E8F0" font-size="11" font-weight="700">WET SESSION • INTERS</text>

      <!-- ============================================== -->
      <!-- TOP-DOWN SCHEMATIC OF RED BULL RB20 CHASSIS -->
      <!-- Center: (550, 220). Nose points to Left (x=240), Rear at Right (x=830) -->
      <!-- ============================================== -->

      <!-- Main Chassis Floor & Diffuser (Carbon underbody) -->
      <path d="M 320 185 L 430 155 L 680 155 L 750 170 L 800 175 L 800 265 L 750 270 L 680 285 L 430 285 L 320 255 Z" 
            fill="#0C1322" stroke="#222F46" stroke-width="1.8"/>

      <!-- Front Wing Assembly (Nose at ~240, wing spans 110 to 330 Y) -->
      <g style="{c_aero_glow}">
        <!-- Main planes -->
        <path d="M 225 110 L 255 125 L 265 210 L 265 230 L 255 315 L 225 330 L 215 325 L 245 220 L 215 115 Z" 
              fill="#0F172A" stroke="{c_aero}" stroke-width="2"/>
        <!-- Flap elements -->
        <path d="M 235 118 L 260 130 L 268 210 L 268 230 L 260 310 L 235 322" 
              fill="none" stroke="#3671C6" stroke-width="1.5"/>
        <!-- Endplates -->
        <rect x="210" y="105" width="25" height="12" rx="3" fill="#E10600"/>
        <rect x="210" y="323" width="25" height="12" rx="3" fill="#E10600"/>
      </g>

      <!-- Front Suspension Wishbones -->
      <line x1="320" y1="205" x2="350" y2="135" stroke="#475569" stroke-width="2"/>
      <line x1="345" y1="205" x2="360" y2="135" stroke="#475569" stroke-width="2"/>
      <line x1="320" y1="235" x2="350" y2="305" stroke="#475569" stroke-width="2"/>
      <line x1="345" y1="235" x2="360" y2="305" stroke="#475569" stroke-width="2"/>

      <!-- Front Tyres (Pirelli Intermediate Green) -->
      <g style="{c_tyre_glow}">
        <!-- Front Left Tyre -->
        <rect x="325" y="90" width="68" height="42" rx="6" fill="#15171C" stroke="{c_tyre}" stroke-width="2.5"/>
        <rect x="333" y="97" width="52" height="6" rx="2" fill="{c_tyre}"/>
        <circle cx="359" cy="111" r="9" fill="#0D0F14" stroke="#475569" stroke-width="1.5"/>
        
        <!-- Front Right Tyre -->
        <rect x="325" y="308" width="68" height="42" rx="6" fill="#15171C" stroke="{c_tyre}" stroke-width="2.5"/>
        <rect x="333" y="337" width="52" height="6" rx="2" fill="{c_tyre}"/>
        <circle cx="359" cy="329" r="9" fill="#0D0F14" stroke="#475569" stroke-width="1.5"/>
      </g>

      <!-- Nose Cone & Cockpit Entry -->
      <path d="M 255 220 L 320 205 L 440 198 L 440 242 L 320 235 Z" 
            fill="url(#rb-blue)" stroke="#3B82F6" stroke-width="1.5"/>
      <!-- Yellow nose tip -->
      <path d="M 255 220 L 275 212 L 275 228 Z" fill="url(#redbull-yellow)"/>
      <text x="290" y="224" fill="#FFFFFF" font-size="11" font-weight="800" text-anchor="middle">1</text>

      <!-- Sidepods & Engine Cover Bodywork (Signature RB20 profile) -->
      <path d="M 440 198 L 460 162 L 530 160 L 640 175 L 740 198 L 740 242 L 640 265 L 530 280 L 460 278 L 440 242 Z" 
            fill="url(#rb-dark)" stroke="#3671C6" stroke-width="2"/>
      
      <!-- Red Bull Red Bull Livery Streaks -->
      <path d="M 520 185 Q 580 180 630 190 Q 640 205 600 205 Z" fill="#E10600" opacity="0.9"/>
      <path d="M 520 255 Q 580 260 630 250 Q 640 235 600 235 Z" fill="#E10600" opacity="0.9"/>

      <!-- Cockpit & Halo Assembly -->
      <g style="{c_cockpit_glow}">
        <!-- Cockpit opening -->
        <ellipse cx="465" cy="220" rx="30" ry="16" fill="#070A10" stroke="#334155" stroke-width="1.5"/>
        <!-- Max Verstappen Helmet (Orange / Lion) -->
        <circle cx="465" cy="220" r="10" fill="#FF8000" stroke="#FFFFFF" stroke-width="1"/>
        <path d="M 462 216 L 472 220 L 462 224 Z" fill="#000000"/>
        <!-- Halo Titanium Structure -->
        <path d="M 445 220 L 478 206 L 495 208 L 495 232 L 478 234 Z" 
              fill="none" stroke="{c_cockpit}" stroke-width="2.5" stroke-linejoin="round"/>
        <line x1="445" y1="220" x2="495" y2="220" stroke="{c_cockpit}" stroke-width="3"/>
      </g>

      <!-- Engine Bay & Honda Turbo Hybrid (L600-L740) -->
      <g style="{c_engine_glow}">
        <!-- Airbox inlet -->
        <ellipse cx="510" cy="220" rx="9" ry="6" fill="#FFDD00" stroke="#E10600" stroke-width="1.5"/>
        <!-- Power Unit core -->
        <rect x="580" y="208" width="85" height="24" rx="4" fill="#111827" stroke="{c_engine}" stroke-width="1.8"/>
        <text x="622" y="224" fill="{c_engine}" font-size="9" font-weight="700" text-anchor="middle">HONDA RBPT</text>
      </g>

      <!-- Rear Suspension Wishbones -->
      <line x1="710" y1="210" x2="740" y2="140" stroke="#475569" stroke-width="2"/>
      <line x1="735" y1="210" x2="755" y2="140" stroke="#475569" stroke-width="2"/>
      <line x1="710" y1="230" x2="740" y2="300" stroke="#475569" stroke-width="2"/>
      <line x1="735" y1="230" x2="755" y2="300" stroke="#475569" stroke-width="2"/>

      <!-- Rear Tyres (Wider Pirelli Intermediates) -->
      <g style="{c_tyre_glow}">
        <!-- Rear Left Tyre -->
        <rect x="715" y="85" width="75" height="50" rx="7" fill="#15171C" stroke="{c_tyre}" stroke-width="2.5"/>
        <rect x="725" y="93" width="55" height="7" rx="2" fill="{c_tyre}"/>
        <circle cx="752" cy="110" r="10" fill="#0D0F14" stroke="#475569" stroke-width="1.5"/>
        
        <!-- Rear Right Tyre -->
        <rect x="715" y="305" width="75" height="50" rx="7" fill="#15171C" stroke="{c_tyre}" stroke-width="2.5"/>
        <rect x="725" y="340" width="55" height="7" rx="2" fill="{c_tyre}"/>
        <circle cx="752" cy="330" r="10" fill="#0D0F14" stroke="#475569" stroke-width="1.5"/>
      </g>

      <!-- Rear Wing Assembly & Beam Wing -->
      <g style="{c_strat_glow}">
        <!-- Beam wing -->
        <rect x="765" y="180" width="20" height="80" rx="3" fill="#1E293B" stroke="#475569"/>
        <!-- Rear Wing Mainplane -->
        <rect x="800" y="130" width="30" height="180" rx="4" fill="#0F172A" stroke="{c_strategy}" stroke-width="2"/>
        <!-- Endplates -->
        <rect x="790" y="125" width="45" height="8" rx="2" fill="#E10600"/>
        <rect x="790" y="307" width="45" height="8" rx="2" fill="#E10600"/>
        <!-- Rain Light (Flashing Red in wet) -->
        <rect x="832" y="215" width="8" height="10" rx="2" fill="#FF1E1E"/>
        <circle cx="836" cy="220" r="3" fill="#FFFFFF"/>
      </g>

      <!-- ============================================== -->
      <!-- HUD CALLOUT BOXES & REAL-TIME SENSOR STATS -->
      <!-- ============================================== -->

      <!-- Callout 1: Front Tyres & Wet Thermal Management (Top Left) -->
      <g>
        <line x1="360" y1="90" x2="360" y2="40" stroke="{c_tyre}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <line x1="360" y1="40" x2="290" y2="40" stroke="{c_tyre}" stroke-width="1.2"/>
        <circle cx="360" cy="90" r="3" fill="{c_tyre}"/>
        <rect x="110" y="15" width="180" height="52" rx="6" fill="#111622" stroke="{c_tyre}" stroke-width="1.4"/>
        <text x="120" y="33" fill="{c_tyre}" font-size="11" font-weight="800">🛞 PIRELLI INTERMEDIATE</text>
        <text x="120" y="48" fill="#E2E8F0" font-size="11">FL: 82°C • FR: 86°C (Managed)</text>
        <text x="120" y="61" fill="#94A3B8" font-size="10">Cooling via off-line spray</text>
      </g>

      <!-- Callout 2: Front Wing & Braking Apex (Bottom Left) -->
      <g>
        <line x1="240" y1="330" x2="240" y2="390" stroke="{c_aero}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <line x1="240" y1="390" x2="290" y2="390" stroke="{c_aero}" stroke-width="1.2"/>
        <circle cx="240" cy="330" r="3" fill="{c_aero}"/>
        <rect x="110" y="365" width="180" height="54" rx="6" fill="#111622" stroke="{c_aero}" stroke-width="1.4"/>
        <text x="120" y="383" fill="{c_aero}" font-size="11" font-weight="800">💨 AERO & BRAKING</text>
        <text x="120" y="398" fill="#E2E8F0" font-size="11">Turn 1: Braked 15m Later</text>
        <text x="120" y="411" fill="#94A3B8" font-size="10">Apex: 114 km/h (+6 vs NOR)</text>
      </g>

      <!-- Callout 3: Cockpit & GP Radio (Top Center) -->
      <g>
        <line x1="475" y1="205" x2="475" y2="50" stroke="{c_cockpit}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <circle cx="475" cy="205" r="3" fill="{c_cockpit}"/>
        <rect x="400" y="15" width="185" height="52" rx="6" fill="#111622" stroke="{c_cockpit}" stroke-width="1.4"/>
        <text x="410" y="33" fill="{c_cockpit}" font-size="11" font-weight="800">🏎️ COCKPIT & GP RADIO</text>
        <text x="410" y="48" fill="#E2E8F0" font-size="11">GP: "Stay out, track pos is king"</text>
        <text x="410" y="61" fill="#94A3B8" font-size="10">Max: "Rain really coming down!"</text>
      </g>

      <!-- Callout 4: Honda Power Unit (Top Right) -->
      <g>
        <line x1="630" y1="208" x2="630" y2="40" stroke="{c_engine}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <line x1="630" y1="40" x2="690" y2="40" stroke="{c_engine}" stroke-width="1.2"/>
        <circle cx="630" cy="208" r="3" fill="{c_engine}"/>
        <rect x="690" y="15" width="180" height="52" rx="6" fill="#111622" stroke="{c_engine}" stroke-width="1.4"/>
        <text x="700" y="33" fill="{c_engine}" font-size="11" font-weight="800">⚡ HONDA RBPT (ICE #6)</text>
        <text x="700" y="48" fill="#E2E8F0" font-size="11">Penalty: +5 Grid ➔ P17</text>
        <text x="700" y="61" fill="#94A3B8" font-size="10">Max Speed: 324.5 km/h</text>
      </g>

      <!-- Callout 5: Rear Tyre & Traction (Bottom Center) -->
      <g>
        <line x1="750" y1="355" x2="750" y2="395" stroke="{c_tyre}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <line x1="750" y1="395" x2="690" y2="395" stroke="{c_tyre}" stroke-width="1.2"/>
        <circle cx="750" cy="355" r="3" fill="{c_tyre}"/>
        <rect x="500" y="365" width="190" height="54" rx="6" fill="#111622" stroke="{c_tyre}" stroke-width="1.4"/>
        <text x="510" y="383" fill="{c_tyre}" font-size="11" font-weight="800">🛞 REAR TRACTION / WET LINE</text>
        <text x="510" y="398" fill="#E2E8F0" font-size="11">32 Laps on Stint 1 without deg</text>
        <text x="510" y="411" fill="#94A3B8" font-size="10">Water evacuation: 35 L/s</text>
      </g>

      <!-- Callout 6: Pit Wall Strategy & Margin (Bottom Right) -->
      <g>
        <line x1="820" y1="280" x2="820" y2="380" stroke="{c_strategy}" stroke-width="1.2" stroke-dasharray="2,2"/>
        <line x1="820" y1="380" x2="790" y2="380" stroke="{c_strategy}" stroke-width="1.2"/>
        <circle cx="820" cy="280" r="3" fill="{c_strategy}"/>
        <rect x="710" y="365" width="220" height="54" rx="6" fill="#111622" stroke="{c_strategy}" stroke-width="1.4"/>
        <text x="720" y="383" fill="{c_strategy}" font-size="11" font-weight="800">🧠 RED FLAG MASTERSTROKE</text>
        <text x="720" y="398" fill="#E2E8F0" font-size="11">Time Saved: ~24.5s vs NOR</text>
        <text x="720" y="411" fill="#94A3B8" font-size="10">Winning Margin: +19.477s (P1)</text>
      </g>
    </svg>
    """
    return svg
