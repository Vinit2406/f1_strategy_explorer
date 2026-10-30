def get_rb20_svg(active_system="tyres"):
    """
    Renders an ultra-realistic, high-fidelity side-profile illustration of the 
    Red Bull Racing RB20 on the wet Interlagos circuit with authentic livery, 
    Pirelli Intermediate wheels, rain reflections, and glowing interactive subsystems.
    """
    # Active system glows and highlights
    glow_tyre = "filter: url(#neon-glow-green);" if active_system == "tyres" else ""
    glow_engine = "filter: url(#neon-glow-red);" if active_system == "engine" else ""
    glow_cockpit = "filter: url(#neon-glow-cyan);" if active_system == "cockpit" else ""
    glow_aero = "filter: url(#neon-glow-amber);" if active_system == "aero" else ""
    glow_strat = "filter: url(#neon-glow-purple);" if active_system == "strategy" else ""

    # Stroke colors for subsystem highlights
    s_tyre = "#39B54A" if active_system == "tyres" else "#1F7A2D"
    s_engine = "#FF3B30" if active_system == "engine" else "#881313"
    s_cockpit = "#38BDF8" if active_system == "cockpit" else "#1E3A8A"
    s_aero = "#F59E0B" if active_system == "aero" else "#78350F"
    s_strat = "#C084FC" if active_system == "strategy" else "#581C87"

    svg = f"""
    <svg viewBox="0 0 1200 480" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background: radial-gradient(circle at 50% 30%, #0F172A 0%, #080D1A 60%, #03060B 100%); border: 1px solid #1E293B; border-radius: 14px; font-family: 'Segoe UI', system-ui, sans-serif;">
      <defs>
        <!-- Glowing Filters -->
        <filter id="neon-glow-green" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="6" result="blur" />
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
        <filter id="neon-glow-red" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="7" result="blur" />
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
        <filter id="neon-glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="7" result="blur" />
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
        <filter id="neon-glow-amber" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="7" result="blur" />
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
        <filter id="neon-glow-purple" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="7" result="blur" />
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>

        <!-- Red Bull Livery Gradients -->
        <linearGradient id="rb-matte-navy" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#1B2845"/>
          <stop offset="35%" stop-color="#0E182E"/>
          <stop offset="80%" stop-color="#070D1A"/>
          <stop offset="100%" stop-color="#040812"/>
        </linearGradient>

        <linearGradient id="rb-top-highlight" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.8"/>
          <stop offset="50%" stop-color="#3671C6" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0"/>
        </linearGradient>

        <linearGradient id="sun-yellow" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#FFE600"/>
          <stop offset="100%" stop-color="#FF9900"/>
        </linearGradient>

        <linearGradient id="bull-red" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#E10600"/>
          <stop offset="100%" stop-color="#B91C1C"/>
        </linearGradient>

        <linearGradient id="carbon-texture" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#18181B"/>
          <stop offset="100%" stop-color="#09090B"/>
        </linearGradient>

        <linearGradient id="asphalt-wet" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#0F172A"/>
          <stop offset="20%" stop-color="#0B1120"/>
          <stop offset="100%" stop-color="#020617"/>
        </linearGradient>

        <linearGradient id="track-reflection" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.25"/>
          <stop offset="40%" stop-color="#3671C6" stop-opacity="0.1"/>
          <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
        </linearGradient>

        <linearGradient id="spray-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
          <stop offset="50%" stop-color="#94A3B8" stop-opacity="0.2"/>
          <stop offset="100%" stop-color="#0F172A" stop-opacity="0"/>
        </linearGradient>
      </defs>

      <!-- ============================================== -->
      <!-- BACKGROUND: INTERLAGOS WET TRACK & LIGHTING -->
      <!-- ============================================== -->

      <!-- Circuit Stadium Floodlight Flares in Rain -->
      <circle cx="200" cy="50" r="140" fill="#38BDF8" opacity="0.06"/>
      <circle cx="950" cy="40" r="180" fill="#60A5FA" opacity="0.08"/>
      
      <!-- Telemetry Engineering Grid (Subtle) -->
      <g stroke="#1E293B" stroke-width="0.7" opacity="0.4" stroke-dasharray="4,8">
        <line x1="50" y1="90" x2="1150" y2="90" />
        <line x1="50" y1="180" x2="1150" y2="180" />
        <line x1="50" y1="270" x2="1150" y2="270" />
        <line x1="300" y1="40" x2="300" y2="350" />
        <line x1="600" y1="40" x2="600" y2="350" />
        <line x1="900" y1="40" x2="900" y2="350" />
      </g>

      <!-- Track Surface (Wet Asphalt with standing water line) -->
      <rect x="0" y="340" width="1200" height="140" fill="url(#asphalt-wet)" />
      
      <!-- Wet Track Reflection Zone directly under car -->
      <ellipse cx="620" cy="360" rx="450" ry="25" fill="url(#track-reflection)" />

      <!-- Interlagos Curbs (Red & White wet curbing at track edge) -->
      <g transform="skewX(-35)">
        <rect x="180" y="348" width="50" height="8" fill="#DC2626" opacity="0.7"/>
        <rect x="230" y="348" width="50" height="8" fill="#F8FAFC" opacity="0.8"/>
        <rect x="280" y="348" width="50" height="8" fill="#DC2626" opacity="0.7"/>
        <rect x="330" y="348" width="50" height="8" fill="#F8FAFC" opacity="0.8"/>
        <rect x="380" y="348" width="50" height="8" fill="#DC2626" opacity="0.7"/>
        <rect x="430" y="348" width="50" height="8" fill="#F8FAFC" opacity="0.8"/>
      </g>

      <!-- Water Spray Mist Kicking Up Behind the Car -->
      <path d="M 880 320 Q 980 260 1120 220 Q 1150 280 1000 340 Z" fill="url(#spray-gradient)" />
      <path d="M 330 325 Q 400 310 460 325 Q 420 338 340 338 Z" fill="url(#spray-gradient)" opacity="0.5"/>

      <!-- ============================================== -->
      <!-- REALISTIC RED BULL RB20 FORMULA 1 CAR PROFILE -->
      <!-- Nose at Left (x=160), Rear Wing at Right (x=980), Ground at y=335 -->
      <!-- ============================================== -->

      <!-- UNDERFLOOR & VENTURI TUNNEL DIFFUSER -->
      <path d="M 280 325 L 500 322 L 780 322 L 850 315 L 940 285 L 950 328 L 780 330 L 320 330 Z" 
            fill="#09090B" stroke="#27272A" stroke-width="1.5"/>
      <!-- Floor Edge Wing Strakes (Adrian Newey ground-effect floor) -->
      <path d="M 460 320 L 720 320 L 740 314 L 480 314 Z" fill="#E10600" opacity="0.8"/>

      <!-- REAR SUSPENSION & TRANSMISSION CASING -->
      <line x1="840" y1="285" x2="880" y2="295" stroke="#3F3F46" stroke-width="3"/>
      <line x1="835" y1="265" x2="880" y2="295" stroke="#3F3F46" stroke-width="3"/>
      <line x1="850" y1="298" x2="885" y2="305" stroke="#52525B" stroke-width="2"/>

      <!-- REAR WING ASSEMBLY (High-Downforce Wet Interlagos Spec) -->
      <g style="{glow_strat}">
        <!-- Endplate (Curved 2024 spec) -->
        <path d="M 880 180 L 960 175 Q 985 185 980 280 L 960 280 Q 960 210 930 205 L 880 205 Z" 
              fill="#0A1120" stroke="{s_strat}" stroke-width="2"/>
        <!-- Mobil 1 / Red Bull Red Accent on Endplate -->
        <rect x="965" y="195" width="8" height="65" rx="3" fill="#E10600"/>
        
        <!-- Mainplane & DRS Flap -->
        <path d="M 870 180 L 960 175 L 955 195 L 868 200 Z" fill="#0C1527" stroke="#38BDF8" stroke-width="1.2"/>
        <path d="M 875 195 L 955 192 L 952 208 L 872 210 Z" fill="#1E293B" stroke="#64748B" stroke-width="1"/>
        <!-- DRS Actuator Pod -->
        <rect x="910" y="170" width="16" height="12" rx="3" fill="#E10600"/>
        <!-- Beam Wing -->
        <path d="M 890 285 L 950 280 L 945 295 L 888 298 Z" fill="#18181B" stroke="#3F3F46"/>
        <!-- Rain Light (Flashing Red LED) -->
        <rect x="955" y="300" width="10" height="12" rx="2" fill="#EF4444"/>
        <circle cx="960" cy="306" r="3.5" fill="#FFFFFF"/>
      </g>

      <!-- MAIN MONOCOQUE, NOSE & SIDEPOD BODYWORK (The sculpted RB20) -->
      <g>
        <!-- Main Chassis Outline -->
        <path d="M 160 280 
                 Q 210 270 280 258 
                 Q 360 250 440 248 
                 L 460 205 
                 Q 510 185 560 182 
                 L 640 182 
                 Q 760 185 860 250 
                 L 860 295 
                 L 760 305 
                 Q 600 310 460 305 
                 L 360 300 
                 Q 260 298 180 290 
                 Z" 
              fill="url(#rb-matte-navy)" stroke="#1E293B" stroke-width="1.5"/>

        <!-- Top Body Highlights (Wet Reflection Sheen) -->
        <path d="M 190 278 Q 300 260 440 250 L 560 185 Q 700 185 820 235" 
              fill="none" stroke="url(#rb-top-highlight)" stroke-width="2.5"/>

        <!-- Nose Cone Tip (Yellow Chevron & Driver #1) -->
        <path d="M 160 280 L 195 274 L 195 288 L 160 285 Z" fill="url(#sun-yellow)"/>
        <text x="215" y="278" fill="#FFFFFF" font-size="14" font-weight="900" font-style="italic">1</text>

        <!-- Red Bull Yellow Sun on Engine Cover -->
        <circle cx="700" cy="225" r="32" fill="url(#sun-yellow)" opacity="0.95"/>

        <!-- Red Bull Charging Bull (Iconic Logo Silhouette) -->
        <path d="M 680 238 
                 C 670 230, 665 215, 680 210 
                 C 695 205, 715 210, 725 220 
                 C 740 215, 755 220, 750 232 
                 C 745 240, 730 242, 715 235 
                 C 700 245, 685 242, 680 238 Z" 
              fill="url(#bull-red)"/>
        <!-- Bull Horns (Yellow accent) -->
        <path d="M 720 210 Q 730 198 740 202 Q 735 210 725 215 Z" fill="#FFE600"/>

        <!-- "RED BULL" Decal Lettering on Sidepod -->
        <text x="610" y="258" fill="#FFFFFF" font-size="20" font-weight="900" font-style="italic" letter-spacing="2" opacity="0.9">RED BULL</text>
        <text x="610" y="275" fill="#38BDF8" font-size="11" font-weight="800" letter-spacing="3" opacity="0.8">ORACLE</text>

        <!-- RB20 Aggressive Overbite Sidepod Inlet (Newey's Masterpiece) -->
        <path d="M 480 252 L 530 248 L 535 275 L 485 285 Z" fill="#030712" stroke="#3671C6" stroke-width="1.8"/>
        <!-- Deep Undercut Air Channel -->
        <path d="M 535 275 Q 630 282 720 295 L 710 305 Q 610 295 510 290 Z" fill="#050B17"/>

        <!-- Engine Cover Cooling Cannon / Shoulder Gulleys -->
        <g style="{glow_engine}">
          <path d="M 570 190 Q 680 192 780 230 L 775 245 Q 670 208 565 205 Z" 
                fill="#0F172A" stroke="{s_engine}" stroke-width="1.5"/>
          <text x="735" y="215" fill="{s_engine}" font-size="9" font-weight="800">HONDA RBPT</text>
        </g>

        <!-- Shark Fin Dorsal Spine -->
        <path d="M 640 182 L 840 215 L 830 225 L 640 190 Z" fill="#0B132B" stroke="#1E293B"/>
      </g>

      <!-- COCKPIT, HALO & DRIVER HELMET (Max Verstappen) -->
      <g style="{glow_cockpit}">
        <!-- Cockpit Opening Rim -->
        <path d="M 440 248 Q 470 225 520 225 L 535 248 Z" fill="#070A0F" stroke="#334155" stroke-width="1.2"/>
        
        <!-- Max Verstappen Helmet (Orange Lion with dark visor) -->
        <ellipse cx="485" cy="226" rx="13" ry="11" fill="#FF6B00" stroke="#FFFFFF" stroke-width="1"/>
        <path d="M 474 227 Q 486 225 496 228 L 494 233 Q 484 230 475 232 Z" fill="#090D16"/>
        <!-- Helmet Aero Winglet -->
        <path d="M 472 222 L 480 220 L 478 225 Z" fill="#FF6B00"/>

        <!-- Titanium Halo Safety Structure -->
        <path d="M 445 245 Q 475 210 520 215 L 530 235" 
              fill="none" stroke="{s_cockpit}" stroke-width="4.5" stroke-linecap="round"/>
        <path d="M 475 213 L 478 245" stroke="{s_cockpit}" stroke-width="3.5"/>
        
        <!-- Rear View Mirror (Left) -->
        <rect x="430" y="235" width="16" height="8" rx="2" fill="#090D16" stroke="#38BDF8"/>
      </g>

      <!-- FRONT SUSPENSION (Push-rod Geometry & Steering Arm) -->
      <line x1="285" y1="262" x2="310" y2="295" stroke="#3F3F46" stroke-width="3"/>
      <line x1="260" y1="288" x2="310" y2="295" stroke="#3F3F46" stroke-width="3"/>
      <line x1="290" y1="285" x2="310" y2="300" stroke="#52525B" stroke-width="2"/>

      <!-- FRONT WING (Complex Multi-element 2024 spec) -->
      <g style="{glow_aero}">
        <!-- Endplate (Red outer face) -->
        <path d="M 110 270 L 160 268 L 155 315 L 115 318 Z" fill="#E10600" stroke="{s_aero}" stroke-width="1.5"/>
        <!-- Diveplane / Canard -->
        <path d="M 120 285 Q 140 280 150 275" fill="none" stroke="#FFFFFF" stroke-width="2"/>
        <!-- Multi-tier Cascade Flaps -->
        <path d="M 125 305 L 220 295 L 215 308 L 122 318 Z" fill="#0E1726" stroke="#38BDF8" stroke-width="1.2"/>
        <path d="M 130 295 L 215 288 L 212 298 L 128 305 Z" fill="#1E293B" stroke="#64748B"/>
        <path d="M 138 285 L 205 280 L 203 288 L 135 293 Z" fill="#090D16" stroke="#38BDF8"/>
      </g>

      <!-- ============================================== -->
      <!-- PIRELLI INTERMEDIATE 18-INCH WHEELS & TYRES -->
      <!-- Front Wheel Center: (310, 295) r=40 -->
      <!-- Rear Wheel Center: (880, 292) r=43 -->
      <!-- ============================================== -->

      <!-- FRONT WHEEL ASSEMBLY -->
      <g style="{glow_tyre}">
        <!-- Rubber Tyre Outer -->
        <circle cx="310" cy="295" r="41" fill="#121316" stroke="#27272A" stroke-width="1"/>
        <!-- Wet Tread Grooves on Top Edge -->
        <path d="M 275 275 Q 310 250 345 275" fill="none" stroke="#09090B" stroke-width="4" stroke-dasharray="3,3"/>
        <!-- Pirelli Intermediate Distinctive Green Sidewall Ring -->
        <circle cx="310" cy="295" r="35" fill="none" stroke="{s_tyre}" stroke-width="3.5"/>
        <text x="310" y="267" fill="{s_tyre}" font-size="7" font-weight="900" text-anchor="middle" letter-spacing="1">P ZERO</text>
        <text x="310" y="329" fill="{s_tyre}" font-size="6.5" font-weight="900" text-anchor="middle">INTERMEDIATE</text>
        <!-- 18-inch BBS Carbon Aerodynamic Wheel Cover -->
        <circle cx="310" cy="295" r="28" fill="#1C1917" stroke="#44403C" stroke-width="1.5"/>
        <circle cx="310" cy="295" r="14" fill="#0C0A09" stroke="#78716C" stroke-width="1"/>
        <!-- Wheel Center Nut (Red Bull Red) -->
        <circle cx="310" cy="295" r="5" fill="#DC2626"/>
        <!-- Front Wheel Wake Deflector (2024 FIA regulation aero eyebrow) -->
        <path d="M 290 250 Q 325 248 350 262 L 350 268 Q 325 255 292 256 Z" fill="#09090B" stroke="#38BDF8"/>
      </g>

      <!-- REAR WHEEL ASSEMBLY -->
      <g style="{glow_tyre}">
        <!-- Rubber Tyre Outer -->
        <circle cx="880" cy="292" r="43" fill="#121316" stroke="#27272A" stroke-width="1"/>
        <!-- Wet Tread Grooves on Top Edge -->
        <path d="M 843 270 Q 880 245 917 270" fill="none" stroke="#09090B" stroke-width="4" stroke-dasharray="3,3"/>
        <!-- Pirelli Intermediate Distinctive Green Sidewall Ring -->
        <circle cx="880" cy="292" r="37" fill="none" stroke="{s_tyre}" stroke-width="4"/>
        <text x="880" y="262" fill="{s_tyre}" font-size="7.5" font-weight="900" text-anchor="middle" letter-spacing="1">P ZERO</text>
        <text x="880" y="328" fill="{s_tyre}" font-size="7" font-weight="900" text-anchor="middle">INTERMEDIATE</text>
        <!-- 18-inch BBS Carbon Aerodynamic Wheel Cover -->
        <circle cx="880" cy="292" r="30" fill="#1C1917" stroke="#44403C" stroke-width="1.5"/>
        <circle cx="880" cy="292" r="15" fill="#0C0A09" stroke="#78716C" stroke-width="1"/>
        <!-- Wheel Center Nut (Red Bull Blue) -->
        <circle cx="880" cy="292" r="5" fill="#2563EB"/>
        <!-- Rear Wheel Wake Deflector Winglet -->
        <path d="M 855 245 Q 895 244 922 258 L 920 264 Q 895 250 858 252 Z" fill="#09090B" stroke="#38BDF8"/>
      </g>

      <!-- ============================================== -->
      <!-- CRISP HUD OVERLAY BADGES (NON-OVERLAPPING) -->
      <!-- Placed in clean corners without touching the car -->
      <!-- ============================================== -->

      <!-- Bottom-Left Status Pill -->
      <rect x="35" y="415" width="280" height="42" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.5"/>
      <circle cx="55" cy="436" r="5" fill="#39B54A"/>
      <text x="70" y="432" fill="#E2E8F0" font-size="12" font-weight="800">CIRCUIT: AUTÓDROMO DE INTERLAGOS</text>
      <text x="70" y="447" fill="#94A3B8" font-size="10.5">SÃO PAULO GP 2024 • WET WEATHER CONDITIONS</text>

      <!-- Bottom-Right Status Pill -->
      <rect x="865" y="415" width="300" height="42" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.5"/>
      <circle cx="885" cy="436" r="5" fill="#38BDF8"/>
      <text x="900" y="432" fill="#E2E8F0" font-size="12" font-weight="800">CHAMPIONSHIP VICTORY: P17 ➔ P1</text>
      <text x="900" y="447" fill="#94A3B8" font-size="10.5">FASTEST LAP: 1:20.472 • MARGIN: +19.477s</text>
    </svg>
    """
    return svg
