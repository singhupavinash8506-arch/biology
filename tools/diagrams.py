# -*- coding: utf-8 -*-
"""
Minimal, exam-priority labelled diagrams (Hindi labels + English gloss) as inline SVG.

Each figure here was selected because it is among the most frequently demanded
figures in the UPMSP model paper + UP Board Biology papers 2020-2026.
See docs/DIAGRAM_PRIORITY.md for the frequency table that drove the choice.
Deliberately minimal: no decorative anatomy, only parts that carry marks.
"""

# ------------------------------------------------- Ch 1: ovule + embryo sac
OVULE = r"""
<svg viewBox="0 0 330 196" role="img">
  <defs>
    <radialGradient id="o_nuc" cx="45%" cy="40%">
      <stop offset="0%" stop-color="#fff6d9"/><stop offset="100%" stop-color="#f1dd9f"/></radialGradient>
    <linearGradient id="o_int" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8bc34a"/><stop offset="100%" stop-color="#558b2f"/></linearGradient>
    <radialGradient id="o_sac" cx="40%" cy="38%">
      <stop offset="0%" stop-color="#e8f5ff"/><stop offset="100%" stop-color="#b3d8f2"/></radialGradient>
  </defs>
  <ellipse cx="163" cy="98" rx="80" ry="58" fill="url(#o_int)"/>
  <ellipse cx="163" cy="98" rx="71" ry="50" fill="#c5e1a5"/>
  <ellipse cx="165" cy="98" rx="63" ry="43" fill="url(#o_nuc)" stroke="#c9a227" stroke-width=".7"/>
  <ellipse cx="169" cy="98" rx="51" ry="30" fill="url(#o_sac)" stroke="#1565c0" stroke-width=".9"/>
  <path d="M84,98 l-17,-8 v16 z" fill="#fff" stroke="#558b2f" stroke-width=".7"/>
  <path d="M84,90 a10,8 0 0 0 0,16" fill="#fff" stroke="#558b2f" stroke-width=".7"/>
  <path d="M243,98 q23,2 31,16" stroke="#6d4c41" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="243" cy="98" r="3.4" fill="#4e342e"/>
  <ellipse cx="138" cy="98" rx="12" ry="9" fill="#ff8a80" stroke="#c62828" stroke-width=".8"/>
  <circle cx="138" cy="98" r="3.6" fill="#b71c1c"/>
  <ellipse cx="132" cy="84"  rx="9" ry="6.5" fill="#ffe0b2" stroke="#ef6c00" stroke-width=".7"/>
  <ellipse cx="132" cy="112" rx="9" ry="6.5" fill="#ffe0b2" stroke="#ef6c00" stroke-width=".7"/>
  <circle cx="171" cy="93" r="5.2" fill="#ce93d8" stroke="#6a1b9a" stroke-width=".8"/>
  <circle cx="181" cy="103" r="5.2" fill="#ce93d8" stroke="#6a1b9a" stroke-width=".8"/>
  <circle cx="206" cy="88"  r="5" fill="#a5d6a7" stroke="#2e7d32" stroke-width=".7"/>
  <circle cx="212" cy="98" r="5" fill="#a5d6a7" stroke="#2e7d32" stroke-width=".7"/>
  <circle cx="206" cy="108" r="5" fill="#a5d6a7" stroke="#2e7d32" stroke-width=".7"/>
  <path class="ld" d="M64,106 L42,126"/><circle class="dot" cx="64" cy="106" r="1.2"/>
  <text class="lb" x="2" y="136">बीजाण्डद्वार</text><text class="lbs" x="2" y="145">(Micropyle)</text>
  <path class="ld" d="M132,82 L106,52"/><circle class="dot" cx="132" cy="82" r="1.2"/>
  <text class="lb" x="40" y="45">सहाय कोशिकाएँ</text><text class="lbs" x="40" y="54">(2 Synergids)</text>
  <path class="ld" d="M138,106 L124,164"/><circle class="dot" cx="138" cy="106" r="1.2"/>
  <text class="lb" x="82" y="176">अण्ड कोशिका</text><text class="lbs" x="82" y="185">(Egg, n)</text>
  <path class="ld" d="M176,91 L182,50"/><circle class="dot" cx="176" cy="91" r="1.2"/>
  <text class="lb" x="152" y="36">2 ध्रुवीय केन्द्रक</text><text class="lbs" x="152" y="45">(Polar nuclei, 2n)</text>
  <path class="ld" d="M212,108 L218,164"/><circle class="dot" cx="212" cy="108" r="1.2"/>
  <text class="lb" x="192" y="176">3 प्रतिव्यासांत</text><text class="lbs" x="192" y="185">(Antipodals)</text>
  <path class="ld" d="M219,70 L256,48"/><circle class="dot" cx="219" cy="70" r="1.2"/>
  <text class="lb" x="252" y="36">भ्रूणकोष</text><text class="lbs" x="252" y="45">(Embryo sac)</text>
  <path class="ld" d="M226,128 L262,146"/><circle class="dot" cx="226" cy="128" r="1.2"/>
  <text class="lb" x="250" y="157">अध्यावरण</text><text class="lbs" x="250" y="166">(Integument)</text>
  <path class="ld" d="M272,114 L292,130"/><circle class="dot" cx="272" cy="114" r="1.2"/>
  <text class="lb" x="274" y="141">बीजाण्डवृन्त</text><text class="lbs" x="274" y="150">(Funicle)</text>
  <text class="lbt" x="96" y="16" fill="#1565c0">7 कोशिका + 8 केन्द्रक (मोनोस्पोरिक, पॉलीगोनम प्रकार)</text>
</svg>
"""

# ------------------------------------------------- Ch 2: human sperm
SPERM = r"""
<svg viewBox="0 0 330 150" role="img">
  <defs>
    <linearGradient id="s_ac" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4fc3f7"/><stop offset="100%" stop-color="#0288d1"/></linearGradient>
    <linearGradient id="s_mp" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffb74d"/><stop offset="100%" stop-color="#ef6c00"/></linearGradient>
  </defs>
  <!-- head: acrosome (front half) + nucleus -->
  <path d="M30,74 a30,22 0 0 1 30,-22 l0,44 a30,22 0 0 1 -30,-22 z" fill="url(#s_ac)" stroke="#01579b" stroke-width=".8"/>
  <path d="M60,52 a30,22 0 0 1 0,44 z" fill="#b39ddb" stroke="#4527a0" stroke-width=".8"/>
  <ellipse cx="56" cy="74" rx="13" ry="14" fill="#7e57c2" stroke="#311b92" stroke-width=".8"/>
  <!-- neck -->
  <rect x="88" y="66" width="11" height="16" rx="2.4" fill="#ef9a9a" stroke="#b71c1c" stroke-width=".8"/>
  <!-- middle piece with mitochondrial spiral -->
  <rect x="99" y="68" width="48" height="12" rx="5" fill="url(#s_mp)" stroke="#bf360c" stroke-width=".8"/>
  <path d="M103,68 q4,12 8,0 q4,12 8,0 q4,12 8,0 q4,12 8,0 q4,12 8,0"
        fill="none" stroke="#7f2704" stroke-width=".85"/>
  <!-- tail -->
  <path d="M147,74 q24,-14 44,0 q20,14 42,0 q20,-14 42,0 q14,10 28,2"
        fill="none" stroke="#546e7a" stroke-width="4.2" stroke-linecap="round"/>
  <!-- plasma membrane hint -->
  <path class="ldd" d="M28,74 a32,24 0 0 1 32,-24" />
  <!-- brackets for regions -->
  <path class="ld" d="M30,104 h60 M30,101 v6 M90,101 v6"/>
  <text class="lb" x="38" y="116">शीर्ष</text><text class="lbs" x="38" y="125">(Head)</text>
  <path class="ld" d="M99,104 h48 M99,101 v6 M147,101 v6"/>
  <text class="lb" x="100" y="116">मध्य भाग</text><text class="lbs" x="100" y="125">(Middle piece)</text>
  <path class="ld" d="M150,104 h150 M150,101 v6 M300,101 v6"/>
  <text class="lb" x="204" y="116">पुच्छ</text><text class="lbs" x="204" y="125">(Tail)</text>
  <!-- leaders -->
  <path class="ld" d="M40,56 L28,30"/><circle class="dot" cx="40" cy="56" r="1.2"/>
  <text class="lb" x="2" y="22">अग्रपिधान</text><text class="lbs" x="2" y="31">(Acrosome)</text>
  <path class="ld" d="M56,62 L80,26"/><circle class="dot" cx="56" cy="62" r="1.2"/>
  <text class="lb" x="76" y="18">केन्द्रक</text><text class="lbs" x="76" y="27">(Nucleus, n)</text>
  <path class="ld" d="M93,66 L112,36"/><circle class="dot" cx="93" cy="66" r="1.2"/>
  <text class="lb" x="128" y="18">ग्रीवा</text><text class="lbs" x="128" y="27">(Neck, सेन्ट्रिओल)</text>
  <path class="ld" d="M126,68 L176,40"/><circle class="dot" cx="126" cy="68" r="1.2"/>
  <text class="lb" x="182" y="34">माइटोकॉन्ड्रिया</text><text class="lbs" x="182" y="43">(ऊर्जा / Mitochondria)</text>
  <path class="ld" d="M238,80 L262,96"/><circle class="dot" cx="238" cy="80" r="1.2"/>
  <text class="lb" x="246" y="140">अक्षीय तंतु (9+2)</text>
  <path class="ld" d="M262,96 L272,132"/>
</svg>
"""

# ------------------------------------------------- Ch 2b: female reproductive system
FEMALE_RS = r"""
<svg viewBox="0 0 330 168" role="img">
  <defs><linearGradient id="f_ut" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#f8bbd0"/><stop offset="100%" stop-color="#e91e63"/></linearGradient></defs>
  <!-- uterus body -->
  <path d="M135,48 q30,-10 60,0 q12,30 6,52 q-8,26 -36,26 q-28,0 -36,-26 q-6,-22 6,-52 z"
        fill="url(#f_ut)" stroke="#880e4f" stroke-width="1"/>
  <!-- uterine cavity -->
  <path d="M148,58 q17,-6 34,0 q7,24 3,42 q-5,15 -20,15 q-15,0 -20,-15 q-4,-18 3,-42 z"
        fill="#fff3f6" stroke="#ad1457" stroke-width=".7"/>
  <!-- cervix + vagina -->
  <rect x="155" y="120" width="20" height="14" rx="3" fill="#ce93d8" stroke="#6a1b9a" stroke-width=".8"/>
  <path d="M152,134 q13,20 26,0 l0,22 q-13,8 -26,0 z" fill="#f3e5f5" stroke="#6a1b9a" stroke-width=".8"/>
  <!-- fallopian tubes -->
  <path d="M137,50 q-34,-6 -46,16" fill="none" stroke="#ad1457" stroke-width="3.6" stroke-linecap="round"/>
  <path d="M193,50 q34,-6 46,16" fill="none" stroke="#ad1457" stroke-width="3.6" stroke-linecap="round"/>
  <!-- fimbriae -->
  <path d="M91,66 l-9,-5 M91,66 l-10,2 M91,66 l-6,8" stroke="#ad1457" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M239,66 l9,-5 M239,66 l10,2 M239,66 l6,8" stroke="#ad1457" stroke-width="1.5" stroke-linecap="round"/>
  <!-- ovaries -->
  <ellipse cx="84" cy="84" rx="16" ry="10.5" fill="#fff59d" stroke="#f57f17" stroke-width=".9"/>
  <ellipse cx="246" cy="84" rx="16" ry="10.5" fill="#fff59d" stroke="#f57f17" stroke-width=".9"/>
  <circle cx="80" cy="84" r="3" fill="#f9a825"/><circle cx="250" cy="84" r="3" fill="#f9a825"/>
  <!-- labels -->
  <path class="ld" d="M100,58 L72,34"/><circle class="dot" cx="100" cy="58" r="1.2"/>
  <text class="lb" x="6" y="26">अंडवाहिनी (फैलोपियन)</text><text class="lbs" x="6" y="35">(Fallopian tube)</text>
  <path class="ld" d="M84,94 L68,122"/><circle class="dot" cx="84" cy="94" r="1.2"/>
  <text class="lb" x="6" y="134">अंडाशय</text><text class="lbs" x="6" y="143">(Ovary)</text>
  <path class="ld" d="M86,62 L62,52"/><circle class="dot" cx="86" cy="62" r="1.2"/>
  <text class="lb" x="2" y="50">तंतुमय</text>
  <path class="ld" d="M165,70 L212,26"/><circle class="dot" cx="165" cy="70" r="1.2"/>
  <text class="lb" x="214" y="20">गर्भाशय</text><text class="lbs" x="214" y="29">(Uterus)</text>
  <path class="ld" d="M182,92 L262,52"/><circle class="dot" cx="182" cy="92" r="1.2"/>
  <text class="lb" x="256" y="44">एंडोमेट्रियम</text>
  <path class="ld" d="M176,126 L240,112"/><circle class="dot" cx="176" cy="126" r="1.2"/>
  <text class="lb" x="238" y="108">गर्भाशय ग्रीवा</text><text class="lbs" x="238" y="117">(Cervix)</text>
  <path class="ld" d="M178,148 L240,150"/><circle class="dot" cx="178" cy="148" r="1.2"/>
  <text class="lb" x="242" y="147">योनि</text><text class="lbs" x="242" y="156">(Vagina)</text>
</svg>
"""

# ------------------------------------------------- Ch 3: contraception / ART chart
CONTRA = r"""
<svg viewBox="0 0 330 184" role="img">
  <defs><marker id="c_a" markerWidth="7" markerHeight="7" refX="5.6" refY="2.6" orient="auto">
    <path d="M0,0 L5.6,2.6 L0,5.2 z" fill="#37474f"/></marker></defs>
  <rect x="96" y="4" width="138" height="20" rx="4" fill="#4a148c"/>
  <text class="lbw" x="113" y="17">गर्भनिरोधक विधियाँ (Contraception)</text>
  <path class="ld" d="M165,24 v10 M34,34 h262 M34,34 v8 M100,34 v8 M165,34 v8 M231,34 v8 M296,34 v8"
        marker-end=""/>
  <g font-weight="700">
    <rect x="4"   y="42" width="60" height="30" rx="3.5" fill="#ede7f6" stroke="#4a148c" stroke-width=".8"/>
    <text class="lb" x="12" y="54">प्राकृतिक</text><text class="lbs" x="8" y="64">आवर्तकाल, स्तनपान</text>
    <rect x="70"  y="42" width="60" height="30" rx="3.5" fill="#ede7f6" stroke="#4a148c" stroke-width=".8"/>
    <text class="lb" x="80" y="54">अवरोधक</text><text class="lbs" x="73" y="64">कंडोम, डायफ्राम</text>
    <rect x="136" y="42" width="60" height="30" rx="3.5" fill="#ede7f6" stroke="#4a148c" stroke-width=".8"/>
    <text class="lb" x="146" y="54">IUDs</text><text class="lbs" x="139" y="64">CuT, LNG-20</text>
    <rect x="202" y="42" width="60" height="30" rx="3.5" fill="#ede7f6" stroke="#4a148c" stroke-width=".8"/>
    <text class="lb" x="208" y="54">हार्मोनल</text><text class="lbs" x="205" y="64">गोली, इंजेक्शन</text>
    <rect x="268" y="42" width="58" height="30" rx="3.5" fill="#ede7f6" stroke="#4a148c" stroke-width=".8"/>
    <text class="lb" x="274" y="54">शल्य (स्थायी)</text><text class="lbs" x="272" y="64">नसबंदी, ट्यूबेक्टमी</text>
  </g>
  <rect x="96" y="86" width="138" height="20" rx="4" fill="#00695c"/>
  <text class="lbw" x="100" y="99">सहायक जनन प्रौद्योगिकी (ART)</text>
  <path class="ld" d="M165,106 v10 M46,116 h238 M46,116 v8 M125,116 v8 M205,116 v8 M284,116 v8"/>
  <g>
    <rect x="8"   y="124" width="76" height="30" rx="3.5" fill="#e0f2f1" stroke="#00695c" stroke-width=".8"/>
    <text class="lb" x="28" y="136">IVF + ET</text><text class="lbs" x="11" y="146">परखनली शिशु</text>
    <rect x="90"  y="124" width="70" height="30" rx="3.5" fill="#e0f2f1" stroke="#00695c" stroke-width=".8"/>
    <text class="lb" x="108" y="136">ZIFT</text><text class="lbs" x="93" y="146">युग्मनज -&gt; अंडवाहिनी</text>
    <rect x="166" y="124" width="70" height="30" rx="3.5" fill="#e0f2f1" stroke="#00695c" stroke-width=".8"/>
    <text class="lb" x="186" y="136">GIFT</text><text class="lbs" x="169" y="146">युग्मक -&gt; अंडवाहिनी</text>
    <rect x="242" y="124" width="84" height="30" rx="3.5" fill="#e0f2f1" stroke="#00695c" stroke-width=".8"/>
    <text class="lb" x="262" y="136">ICSI / AI</text><text class="lbs" x="245" y="146">शुक्राणु सीधे अंड में</text>
  </g>
  <rect x="4" y="162" width="322" height="18" rx="3" fill="#fff8e1" stroke="#ff8f00" stroke-width=".8"/>
  <text class="lb" x="10" y="174" fill="#6d4c00">MTP: 12 सप्ताह तक सुरक्षित  &#183;  एमीनोसेंटेसिस = भ्रूण लिंग-परीक्षण पर रोक  &#183;  RCH कार्यक्रम</text>
</svg>
"""

# ------------------------------------------------- Ch 4: dihybrid Punnett square
PUNNETT = r"""
<svg viewBox="0 0 330 196" role="img">
  <defs>
    <linearGradient id="p_h" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1152a3"/><stop offset="100%" stop-color="#0b3a76"/></linearGradient>
  </defs>
  <text class="lbt" x="4" y="12" fill="#0b3a76">द्विसंकर संकरण (Dihybrid cross): RrYy  &#215;  RrYy</text>
  <!-- grid 4x4 at x0=56,y0=20, cell 32 -->
  <g>
    <!-- column gamete headers -->
    <g>
      <rect x="56" y="20" width="32" height="16" fill="url(#p_h)"/><text class="lbw" x="64" y="32">RY</text>
      <rect x="88" y="20" width="32" height="16" fill="url(#p_h)"/><text class="lbw" x="96" y="32">Ry</text>
      <rect x="120" y="20" width="32" height="16" fill="url(#p_h)"/><text class="lbw" x="128" y="32">rY</text>
      <rect x="152" y="20" width="32" height="16" fill="url(#p_h)"/><text class="lbw" x="160" y="32">ry</text>
    </g>
    <!-- row gamete headers -->
    <g>
      <rect x="24" y="36" width="32" height="32" fill="url(#p_h)"/><text class="lbw" x="32" y="56">RY</text>
      <rect x="24" y="68" width="32" height="32" fill="url(#p_h)"/><text class="lbw" x="32" y="88">Ry</text>
      <rect x="24" y="100" width="32" height="32" fill="url(#p_h)"/><text class="lbw" x="32" y="120">rY</text>
      <rect x="24" y="132" width="32" height="32" fill="url(#p_h)"/><text class="lbw" x="32" y="152">ry</text>
    </g>
  </g>
  <!-- cells: colour by phenotype class -->
  <g stroke="#0b3a76" stroke-width=".55" font-weight="700">
    <!-- row RY -->
    <rect x="56"  y="36"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="60" y="56">RRYY</text>
    <rect x="88"  y="36"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="92" y="56">RRYy</text>
    <rect x="120" y="36"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="124" y="56">RrYY</text>
    <rect x="152" y="36"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="156" y="56">RrYy</text>
    <!-- row Ry -->
    <rect x="56"  y="68"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="60" y="88">RRYy</text>
    <rect x="88"  y="68"  width="32" height="32" fill="#a5d6a7"/><text class="lbs" x="92" y="88">RRyy</text>
    <rect x="120" y="68"  width="32" height="32" fill="#ffe082"/><text class="lbs" x="124" y="88">RrYy</text>
    <rect x="152" y="68"  width="32" height="32" fill="#a5d6a7"/><text class="lbs" x="156" y="88">Rryy</text>
    <!-- row rY -->
    <rect x="56"  y="100" width="32" height="32" fill="#ffe082"/><text class="lbs" x="60" y="120">RrYY</text>
    <rect x="88"  y="100" width="32" height="32" fill="#ffe082"/><text class="lbs" x="92" y="120">RrYy</text>
    <rect x="120" y="100" width="32" height="32" fill="#90caf9"/><text class="lbs" x="124" y="120">rrYY</text>
    <rect x="152" y="100" width="32" height="32" fill="#90caf9"/><text class="lbs" x="156" y="120">rrYy</text>
    <!-- row ry -->
    <rect x="56"  y="132" width="32" height="32" fill="#ffe082"/><text class="lbs" x="60" y="152">RrYy</text>
    <rect x="88"  y="132" width="32" height="32" fill="#a5d6a7"/><text class="lbs" x="92" y="152">Rryy</text>
    <rect x="120" y="132" width="32" height="32" fill="#90caf9"/><text class="lbs" x="124" y="152">rrYy</text>
    <rect x="152" y="132" width="32" height="32" fill="#ef9a9a"/><text class="lbs" x="156" y="152">rryy</text>
  </g>
  <!-- phenotype legend -->
  <g>
    <rect x="196" y="38" width="10" height="10" fill="#ffe082" stroke="#0b3a76" stroke-width=".5"/>
    <text class="lb" x="210" y="47">9 गोल-पीला</text>
    <rect x="196" y="56" width="10" height="10" fill="#a5d6a7" stroke="#0b3a76" stroke-width=".5"/>
    <text class="lb" x="210" y="65">3 गोल-हरा</text>
    <rect x="196" y="74" width="10" height="10" fill="#90caf9" stroke="#0b3a76" stroke-width=".5"/>
    <text class="lb" x="210" y="83">3 झुर्रीदार-पीला</text>
    <rect x="196" y="92" width="10" height="10" fill="#ef9a9a" stroke="#0b3a76" stroke-width=".5"/>
    <text class="lb" x="210" y="101">1 झुर्रीदार-हरा</text>
  </g>
  <rect x="194" y="112" width="132" height="24" rx="3" fill="#0b3a76"/>
  <text class="lbw" x="202" y="122">लक्षणप्रारूप अनुपात</text>
  <text class="lbw" x="216" y="132" style="font-size:9.6px">9 : 3 : 3 : 1</text>
  <rect x="194" y="140" width="132" height="24" rx="3" fill="#f4511e"/>
  <text class="lbw" x="200" y="150">जीनप्रारूप अनुपात</text>
  <text class="lbw" x="198" y="160" style="font-size:8.6px">1:2:1:2:4:2:1:2:1</text>
  <text class="lb" x="4" y="178" fill="#0b3a76">स्वतंत्र अपव्यूहन का नियम (मेंडल का तृतीय नियम) &#183; परीक्षार्थ संकरण Rryy &#215; rryy -&gt; 1:1:1:1</text>
  <text class="lbs" x="4" y="190">मेंडल ने मटर (Pisum sativum) के 7 विपर्यासी लक्षण चुने; एकसंकर 3:1, द्विसंकर 9:3:3:1</text>
</svg>
"""

# ------------------------------------------------- Ch 5: DNA double helix
DNA = r"""
<svg viewBox="0 0 330 206" role="img">
  <defs>
    <linearGradient id="d_b1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1565c0"/><stop offset="100%" stop-color="#42a5f5"/></linearGradient>
    <linearGradient id="d_b2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ad1457"/><stop offset="100%" stop-color="#ec407a"/></linearGradient>
  </defs>
  <!-- two antiparallel sugar-phosphate backbones as sine curves -->
  <path d="M70,18 C110,34 110,58 70,74 C30,90 30,114 70,130 C110,146 110,170 70,186"
        fill="none" stroke="url(#d_b1)" stroke-width="5.5" stroke-linecap="round"/>
  <path d="M70,18 C30,34 30,58 70,74 C110,90 110,114 70,130 C30,146 30,170 70,186"
        fill="none" stroke="url(#d_b2)" stroke-width="5.5" stroke-linecap="round"/>
  <!-- base pairs (rungs) -->
  <g stroke-width="2.2">
    <line x1="56" y1="30"  x2="84" y2="30"  stroke="#2e7d32"/>
    <line x1="44" y1="46"  x2="96" y2="46"  stroke="#ef6c00"/>
    <line x1="42" y1="62"  x2="98" y2="62"  stroke="#2e7d32"/>
    <line x1="56" y1="78"  x2="84" y2="78"  stroke="#ef6c00"/>
    <line x1="56" y1="94"  x2="84" y2="94"  stroke="#2e7d32"/>
    <line x1="44" y1="110" x2="96" y2="110" stroke="#ef6c00"/>
    <line x1="42" y1="126" x2="98" y2="126" stroke="#2e7d32"/>
    <line x1="56" y1="142" x2="84" y2="142" stroke="#ef6c00"/>
    <line x1="56" y1="158" x2="84" y2="158" stroke="#2e7d32"/>
    <line x1="44" y1="174" x2="96" y2="174" stroke="#ef6c00"/>
  </g>
  <!-- polarity labels -->
  <text class="lb" x="52" y="12" fill="#1565c0">5&#8242;</text>
  <text class="lb" x="80" y="12" fill="#ad1457">3&#8242;</text>
  <text class="lb" x="52" y="200" fill="#1565c0">3&#8242;</text>
  <text class="lb" x="80" y="200" fill="#ad1457">5&#8242;</text>
  <!-- leaders -->
  <path class="ld" d="M100,46 L142,38"/><circle class="dot" cx="100" cy="46" r="1.2"/>
  <text class="lb" x="144" y="34">शर्करा-फॉस्फेट रीढ़</text><text class="lbs" x="144" y="43">(फॉस्फोडाइएस्टर बंध)</text>
  <path class="ld" d="M98,62 L142,66"/><circle class="dot" cx="98" cy="62" r="1.2"/>
  <text class="lb" x="144" y="62">क्षार युग्म</text>
  <text class="lbs" x="144" y="76">A = T (2 हाइड्रोजन बंध)</text>
  <text class="lbs" x="144" y="86">G &#8801; C (3 हाइड्रोजन बंध)</text>
  <path class="ld" d="M98,126 L142,120"/><circle class="dot" cx="98" cy="126" r="1.2"/>
  <text class="lb" x="144" y="104">प्रतिसमानांतर रचना</text><text class="lbs" x="144" y="113">(Antiparallel)</text>
  <!-- dimension marks -->
  <path class="ld" d="M110,18 v56 M106,18 h8 M106,74 h8"/>
  <text class="lb" x="116" y="136">एक कुंडल = 3.4 nm</text>
  <text class="lbs" x="116" y="146">= 10 क्षार युग्म</text>
  <text class="lbs" x="116" y="156">दो क्षारों की दूरी = 0.34 nm</text>
  <path class="ld" d="M42,190 h56 M42,186 v8 M98,186 v8"/>
  <text class="lb" x="116" y="170">व्यास = 2 nm</text>
  <text class="lbs" x="116" y="180">दक्षिणावर्त (Right-handed)</text>
  <rect x="112" y="186" width="214" height="16" rx="3" fill="#0b3a76"/>
  <text class="lbw" x="118" y="197">वाटसन-क्रिक (1953) &#183; चारगॉफ: A/T = G/C = 1</text>
</svg>
"""

# ------------------------------------------------- Ch 6: adaptive radiation (Darwin's finches)
FINCHES = r"""
<svg viewBox="0 0 330 182" role="img">
  <text class="lbt" x="4" y="12" fill="#0b3a76">अनुकूली विकिरण — डार्विन के फिंच (गैलापैगोस द्वीप)</text>
  <!-- four finch heads with different beaks -->
  <g stroke="#3e2723" stroke-width=".9">
    <!-- 1 seed eater: thick conical -->
    <g transform="translate(14,26)">
      <circle cx="26" cy="26" r="19" fill="#8d6e63"/>
      <circle cx="33" cy="19" r="2.6" fill="#fff"/><circle cx="33" cy="19" r="1.3" fill="#000"/>
      <path d="M44,24 l16,5 l-16,7 z" fill="#ffb300"/>
      <text class="lb" x="2" y="62">मोटी-शंक्वाकार</text><text class="lbs" x="6" y="71">बीज खाने वाला</text>
    </g>
    <!-- 2 insect eater: slender pointed -->
    <g transform="translate(94,26)">
      <circle cx="26" cy="26" r="19" fill="#6d4c41"/>
      <circle cx="33" cy="19" r="2.6" fill="#fff"/><circle cx="33" cy="19" r="1.3" fill="#000"/>
      <path d="M44,25 l22,3 l-22,4 z" fill="#ffca28"/>
      <text class="lb" x="6" y="62">पतली-नुकीली</text><text class="lbs" x="8" y="71">कीट खाने वाला</text>
    </g>
    <!-- 3 cactus / nectar: long curved -->
    <g transform="translate(174,26)">
      <circle cx="26" cy="26" r="19" fill="#795548"/>
      <circle cx="33" cy="19" r="2.6" fill="#fff"/><circle cx="33" cy="19" r="1.3" fill="#000"/>
      <path d="M44,24 q16,2 20,12 q-6,-2 -20,-6 z" fill="#ffa726"/>
      <text class="lb" x="2" y="62">लंबी-मुड़ी</text><text class="lbs" x="0" y="71">कैक्टस/मकरंद</text>
    </g>
    <!-- 4 warbler: very fine -->
    <g transform="translate(252,26)">
      <circle cx="26" cy="26" r="19" fill="#5d4037"/>
      <circle cx="33" cy="19" r="2.6" fill="#fff"/><circle cx="33" cy="19" r="1.3" fill="#000"/>
      <path d="M44,25.5 l24,1.5 l-24,2 z" fill="#ffd54f"/>
      <text class="lb" x="4" y="62">अत्यंत पतली</text><text class="lbs" x="4" y="71">वार्बलर फिंच</text>
    </g>
  </g>
  <!-- common ancestor arrow fan -->
  <rect x="104" y="106" width="122" height="18" rx="4" fill="#0b3a76"/>
  <text class="lbw" x="110" y="118">एक सामान्य पूर्वज (बीज खाने वाला)</text>
  <g class="ld">
    <path d="M140,106 L52,80"/><path d="M155,106 L132,80"/>
    <path d="M175,106 L208,80"/><path d="M190,106 L288,80"/>
  </g>
  <text class="lb" x="4" y="140" fill="#0b3a76">एक पूर्वज से विभिन्न आवासों में अनुकूलन -&gt; <tspan font-weight="800">अनुकूली विकिरण</tspan> (अपसारी विकास)</text>
  <text class="lbs" x="4" y="152">आस्ट्रेलियाई मार्सूपियल भी उदाहरण &#183; प्लेसेन्टल + मार्सूपियल साथ = <tspan font-weight="700">अभिसारी विकास</tspan></text>
  <rect x="4" y="158" width="322" height="20" rx="3" fill="#fff3e0" stroke="#ef6c00" stroke-width=".8"/>
  <text class="lb" x="10" y="166" fill="#8a4500">हार्डी-वेनबर्ग: p&#178; + 2pq + q&#178; = 1  (p + q = 1)</text>
  <text class="lbs" x="10" y="175" fill="#8a4500">साम्य भंग के 5 कारक: जीन प्रवाह, आनुवंशिक अपवाह, उत्परिवर्तन, पुनर्योजन, प्राकृतिक चयन</text>
</svg>
"""

# ------------------------------------------------- Ch 7a: antibody molecule
ANTIBODY = r"""
<svg viewBox="0 0 330 168" role="img">
  <defs>
    <linearGradient id="a_h" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1565c0"/><stop offset="100%" stop-color="#64b5f6"/></linearGradient>
  </defs>
  <!-- heavy chains: Y shape -->
  <path d="M165,148 L165,92 L112,34" fill="none" stroke="url(#a_h)" stroke-width="13" stroke-linecap="round"/>
  <path d="M165,148 L165,92 L218,34" fill="none" stroke="url(#a_h)" stroke-width="13" stroke-linecap="round"/>
  <!-- light chains -->
  <path d="M136,62 L94,20" fill="none" stroke="#ef6c00" stroke-width="9" stroke-linecap="round"/>
  <path d="M194,62 L236,20" fill="none" stroke="#ef6c00" stroke-width="9" stroke-linecap="round"/>
  <!-- variable region shading -->
  <path d="M124,46 L112,34" stroke="#c62828" stroke-width="13" stroke-linecap="round"/>
  <path d="M206,46 L218,34" stroke="#c62828" stroke-width="13" stroke-linecap="round"/>
  <path d="M106,32 L94,20" stroke="#ad1457" stroke-width="9" stroke-linecap="round"/>
  <path d="M224,32 L236,20" stroke="#ad1457" stroke-width="9" stroke-linecap="round"/>
  <!-- disulphide bonds -->
  <g stroke="#ffd600" stroke-width="2.1">
    <line x1="158" y1="100" x2="172" y2="100"/>
    <line x1="158" y1="110" x2="172" y2="110"/>
    <line x1="133" y1="58" x2="142" y2="66"/>
    <line x1="197" y1="58" x2="188" y2="66"/>
  </g>
  <!-- antigen binding sites -->
  <circle cx="103" cy="25" r="7" fill="none" stroke="#c62828" stroke-width="1.6" stroke-dasharray="2.4 1.6"/>
  <circle cx="227" cy="25" r="7" fill="none" stroke="#c62828" stroke-width="1.6" stroke-dasharray="2.4 1.6"/>
  <!-- labels -->
  <path class="ld" d="M112,40 L62,46"/><circle class="dot" cx="112" cy="40" r="1.2"/>
  <text class="lb" x="4" y="42">भारी श्रृंखला (H)</text><text class="lbs" x="4" y="51">2 Heavy chains</text>
  <path class="ld" d="M100,30 L58,22"/><circle class="dot" cx="100" cy="30" r="1.2"/>
  <text class="lb" x="4" y="16">हल्की श्रृंखला (L)</text><text class="lbs" x="4" y="25">2 Light chains</text>
  <path class="ld" d="M227,25 L286,20"/><circle class="dot" cx="227" cy="25" r="1.2"/>
  <text class="lb" x="256" y="16">प्रतिजन-बंधन स्थल</text><text class="lbs" x="256" y="25">(Antigen binding)</text>
  <path class="ld" d="M218,42 L276,48"/><circle class="dot" cx="218" cy="42" r="1.2"/>
  <text class="lb" x="252" y="44">परिवर्ती क्षेत्र</text><text class="lbs" x="252" y="53">(Variable, V)</text>
  <path class="ld" d="M172,105 L252,90"/><circle class="dot" cx="172" cy="105" r="1.2"/>
  <text class="lb" x="238" y="80">डाइसल्फाइड बंध</text><text class="lbs" x="238" y="89">(&#8211;S&#8211;S&#8211;)</text>
  <path class="ld" d="M165,140 L240,128"/><circle class="dot" cx="165" cy="140" r="1.2"/>
  <text class="lb" x="236" y="118">स्थिर क्षेत्र</text><text class="lbs" x="236" y="127">(Constant, C)</text>
  <rect x="4" y="128" width="150" height="36" rx="3" fill="#fdecea" stroke="#b3261e" stroke-width=".8"/>
  <text class="lb" x="10" y="140" fill="#8a1a14">संरचना = <tspan font-weight="800">H&#8322;L&#8322;</tspan></text>
  <text class="lbs" x="10" y="150" fill="#8a1a14">5 प्रकार: IgG, IgA, IgM, IgE, IgD</text>
  <text class="lbs" x="10" y="160" fill="#8a1a14">IgA = दूध/कोलोस्ट्रम, IgE = एलर्जी</text>
</svg>
"""

# ------------------------------------------------- Ch 7b: malaria life cycle
MALARIA = r"""
<svg viewBox="0 0 330 150" role="img">
  <defs><marker id="m_a" markerWidth="7" markerHeight="7" refX="5.4" refY="2.6" orient="auto">
    <path d="M0,0 L5.4,2.6 L0,5.2 z" fill="#8a1a14"/></marker></defs>
  <!-- mosquito side -->
  <rect x="4" y="6" width="152" height="14" rx="3" fill="#8a1a14"/>
  <text class="lbw" x="10" y="17">मादा एनोफिलीज मच्छर (वाहक)</text>
  <rect x="174" y="6" width="152" height="14" rx="3" fill="#1152a3"/>
  <text class="lbw" x="212" y="17">मानव (द्वितीयक परपोषी)</text>
  <!-- boxes human side -->
  <g font-weight="700">
    <rect x="174" y="26" width="152" height="18" rx="3" fill="#e8f1fb" stroke="#1152a3" stroke-width=".8"/>
    <text class="lb" x="178" y="38">1. स्पोरोज़ोइट -&gt; यकृत कोशिका</text>
    <rect x="174" y="48" width="152" height="18" rx="3" fill="#e8f1fb" stroke="#1152a3" stroke-width=".8"/>
    <text class="lb" x="178" y="60">2. यकृत में गुणन -&gt; RBC में प्रवेश</text>
    <rect x="174" y="70" width="152" height="18" rx="3" fill="#e8f1fb" stroke="#1152a3" stroke-width=".8"/>
    <text class="lb" x="178" y="82">3. RBC फटना -&gt; हीमोज़ोइन निकले</text>
    <rect x="174" y="92" width="152" height="18" rx="3" fill="#fdecea" stroke="#b3261e" stroke-width=".8"/>
    <text class="lb" x="178" y="104">4. ठंड लगकर तेज़ ज्वर (हीमोज़ोइन)</text>
    <rect x="174" y="114" width="152" height="18" rx="3" fill="#e8f1fb" stroke="#1152a3" stroke-width=".8"/>
    <text class="lb" x="178" y="126">5. गैमीटोसाइट बनना</text>
  </g>
  <!-- boxes mosquito side -->
  <g font-weight="700">
    <rect x="4" y="38" width="152" height="18" rx="3" fill="#fdecea" stroke="#8a1a14" stroke-width=".8"/>
    <text class="lb" x="8" y="50">6. मच्छर रक्त चूसे -&gt; गैमीटोसाइट</text>
    <rect x="4" y="60" width="152" height="18" rx="3" fill="#fdecea" stroke="#8a1a14" stroke-width=".8"/>
    <text class="lb" x="8" y="72">7. आमाशय में निषेचन -&gt; युग्मनज</text>
    <rect x="4" y="82" width="152" height="18" rx="3" fill="#fdecea" stroke="#8a1a14" stroke-width=".8"/>
    <text class="lb" x="8" y="94">8. उओसिस्ट -&gt; स्पोरोज़ोइट</text>
    <rect x="4" y="104" width="152" height="18" rx="3" fill="#fdecea" stroke="#8a1a14" stroke-width=".8"/>
    <text class="lb" x="8" y="116">9. लार ग्रंथि में संचय</text>
  </g>
  <!-- cycle arrows -->
  <g class="ld" stroke="#8a1a14" stroke-width="1.1" marker-end="url(#m_a)">
    <path d="M160,113 L172,100"/>
    <path d="M172,123 L160,112"/>
  </g>
  <text class="lbs" x="4" y="134" fill="#8a1a14">रोगजनक: <tspan font-weight="800">प्लाज्मोडियम</tspan> (वाइवैक्स, फाल्सीपेरम सर्वाधिक घातक, मैलेरिआई, ओवेल)</text>
  <text class="lbs" x="4" y="146" fill="#8a1a14">परपोषी बदलना = <tspan font-weight="800">द्विपरपोषी जीवनचक्र</tspan> &#183; मच्छर = प्राथमिक/अंतिम परपोषी</text>
</svg>
"""

# ------------------------------------------------- Ch 8: biogas plant
BIOGAS = r"""
<svg viewBox="0 0 330 178" role="img">
  <defs>
    <linearGradient id="b_sl" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8d6e63"/><stop offset="100%" stop-color="#4e342e"/></linearGradient>
    <linearGradient id="b_gas" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#b3e5fc"/><stop offset="100%" stop-color="#4fc3f7"/></linearGradient>
  </defs>
  <!-- ground -->
  <rect x="0" y="86" width="330" height="70" fill="#d7ccc8"/>
  <line x1="0" y1="86" x2="330" y2="86" stroke="#6d4c41" stroke-width="1.2"/>
  <!-- digester tank -->
  <rect x="86" y="86" width="150" height="66" rx="4" fill="url(#b_sl)" stroke="#3e2723" stroke-width="1.2"/>
  <!-- floating gas holder -->
  <path d="M94,86 q67,-44 134,0 z" fill="url(#b_gas)" stroke="#01579b" stroke-width="1.2"/>
  <line x1="94" y1="86" x2="228" y2="86" stroke="#01579b" stroke-width="1"/>
  <!-- gas outlet pipe -->
  <path d="M161,42 v-26 h58" fill="none" stroke="#37474f" stroke-width="3.4"/>
  <circle cx="161" cy="42" r="3" fill="#37474f"/>
  <!-- inlet (slurry in) -->
  <path d="M34,62 l0,24 q0,8 8,8 l44,0" fill="none" stroke="#5d4037" stroke-width="7"/>
  <rect x="18" y="48" width="34" height="16" rx="3" fill="#8d6e63" stroke="#3e2723" stroke-width=".9"/>
  <!-- outlet (spent slurry) -->
  <path d="M236,118 l34,0 q8,0 8,8 l0,20" fill="none" stroke="#5d4037" stroke-width="7"/>
  <rect x="262" y="150" width="34" height="14" rx="3" fill="#a1887f" stroke="#3e2723" stroke-width=".9"/>
  <!-- bubbles -->
  <g fill="#b3e5fc" opacity=".85">
    <circle cx="120" cy="104" r="2.6"/><circle cx="140" cy="116" r="2"/><circle cx="168" cy="106" r="2.8"/>
    <circle cx="192" cy="120" r="2.2"/><circle cx="208" cy="100" r="2.4"/><circle cx="152" cy="130" r="2"/>
  </g>
  <!-- labels -->
  <path class="ld" d="M219,16 L262,16"/><circle class="dot" cx="219" cy="16" r="1.2"/>
  <text class="lb" x="246" y="12">गैस निर्गम</text><text class="lbs" x="246" y="26">(CH&#8324; 50-70%)</text>
  <path class="ld" d="M161,62 L112,46"/><circle class="dot" cx="161" cy="62" r="1.2"/>
  <text class="lb" x="60" y="40">तैरता गैस धारक</text><text class="lbs" x="60" y="30">(Gas holder)</text>
  <path class="ld" d="M35,56 L10,42"/><circle class="dot" cx="35" cy="56" r="1.2"/>
  <text class="lb" x="2" y="38">गोबर-जल घोल</text><text class="lbs" x="2" y="28">(Slurry inlet)</text>
  <path class="ld" d="M160,140 L108,166"/><circle class="dot" cx="160" cy="140" r="1.2"/>
  <text class="lb" x="60" y="172">पाचन कुंड (अवायवीय)</text>
  <path class="ld" d="M278,140 L306,124"/><circle class="dot" cx="278" cy="140" r="1.2"/>
  <text class="lb" x="256" y="120">शेष घोल</text><text class="lbs" x="256" y="110">(खाद के रूप में)</text>
  <text class="lbt" x="4" y="98" fill="#8a1a14" transform="rotate(-90 14 110)">मेथैनोजन</text>
  <rect x="86" y="158" width="170" height="18" rx="3" fill="#fdecea" stroke="#b3261e" stroke-width=".8"/>
  <text class="lb" x="92" y="170" fill="#8a1a14">मेथैनोजन: <tspan font-weight="800">मेथैनोबैक्टीरियम</tspan> (गोबर + रूमेन)</text>
</svg>
"""

# ------------------------------------------------- Ch 9: pBR322 + EcoRI sticky ends
PBR322 = r"""
<svg viewBox="0 0 330 200" role="img">
  <!-- ============ left: plasmid map ============ -->
  <circle cx="74" cy="84" r="50" fill="none" stroke="#4a148c" stroke-width="3.6"/>
  <path d="M74,34 A50,50 0 0 1 119,65" fill="none" stroke="#00897b" stroke-width="7.5"/>
  <path d="M119,103 A50,50 0 0 1 74,134" fill="none" stroke="#f4511e" stroke-width="7.5"/>
  <path d="M29,103 A50,50 0 0 1 29,65" fill="none" stroke="#1565c0" stroke-width="7.5"/>
  <g>
    <circle cx="74" cy="34" r="3.4" fill="#c62828"/><text class="lbs" x="62" y="27">EcoRI</text>
    <circle cx="109" cy="49" r="2.9" fill="#6a1b9a"/><text class="lbs" x="113" y="51">ClaI</text>
    <circle cx="121" cy="72" r="2.9" fill="#6a1b9a"/><text class="lbs" x="125" y="74">HindIII</text>
    <circle cx="118" cy="108" r="2.9" fill="#6a1b9a"/><text class="lbs" x="122" y="111">BamHI</text>
    <circle cx="96" cy="128" r="2.9" fill="#6a1b9a"/><text class="lbs" x="92" y="142">SalI</text>
    <circle cx="36" cy="114" r="2.9" fill="#6a1b9a"/><text class="lbs" x="10" y="126">PvuII</text>
  </g>
  <text class="lb" x="84" y="44" fill="#00695c">amp<tspan font-size="6.2px" dy="-3.2">R</tspan></text>
  <text class="lb" x="86" y="126" fill="#bf360c">tet<tspan font-size="6.2px" dy="-3.2">R</tspan></text>
  <text class="lb" x="16" y="88" fill="#0d47a1">ori</text>
  <text class="lbt" x="50" y="84" fill="#4a148c">pBR322</text>
  <text class="lbs" x="52" y="94" fill="#4a148c">4361 bp</text>
  <text class="lbs" x="4" y="156" fill="#4a148c">चयनयोग्य चिह्नक = amp<tspan font-size="5.2px" dy="-2.6">R</tspan><tspan dy="2.6">, tet</tspan><tspan font-size="5.2px" dy="-2.6">R</tspan></text>
  <text class="lbs" x="4" y="166" fill="#4a148c">ori = प्रतिकृतियन का उद्गम</text>
  <text class="lbs" x="4" y="176" fill="#4a148c">(कॉपी संख्या तय करता है)</text>
  <!-- ============ right: EcoRI staggered cut ============ -->
  <rect x="152" y="8" width="174" height="106" rx="4" fill="#f4eafa" stroke="#4a148c" stroke-width="1"/>
  <text class="lbt" x="158" y="21" fill="#4a148c">EcoRI — पैलिंड्रोमिक स्थल व विषम कटाव</text>
  <!-- bases laid out on a fixed pitch so the cut marks line up exactly -->
  <g font-family="'Noto Sans',sans-serif" font-weight="800" font-size="9px" fill="#1a1a1a"
     text-anchor="middle">
    <text x="166" y="42">5&#8242;</text>
    <text x="184" y="42">G</text><text x="197" y="42">A</text><text x="210" y="42">A</text>
    <text x="223" y="42">T</text><text x="236" y="42">T</text><text x="249" y="42">C</text>
    <text x="266" y="42">3&#8242;</text>
    <text x="166" y="60">3&#8242;</text>
    <text x="184" y="60">C</text><text x="197" y="60">T</text><text x="210" y="60">T</text>
    <text x="223" y="60">A</text><text x="236" y="60">A</text><text x="249" y="60">G</text>
    <text x="266" y="60">5&#8242;</text>
  </g>
  <!-- staggered cut: top between G|A (x=190.5), bottom between A|G (x=242.5) -->
  <path d="M190.5,33 V51 H242.5 V69" fill="none" stroke="#c62828" stroke-width="1.5"/>
  <text class="lbs" x="272" y="46" fill="#c62828">कटाव</text>
  <text class="lbs" x="272" y="58" fill="#c62828">रेखा</text>
  <!-- resulting sticky ends -->
  <text class="lbs" x="158" y="76" fill="#4a148c">कटने के बाद दोनों खंडों पर एक-सा चिपचिपा सिरा:</text>
  <g font-family="'Noto Sans',sans-serif" font-weight="800" font-size="8.6px" fill="#1a1a1a">
    <text x="160" y="90">5&#8242;-G           </text>
    <text x="212" y="90">A A T T C-3&#8242;</text>
    <text x="160" y="102">3&#8242;-C T T A A</text>
    <text x="254" y="102">G-5&#8242;</text>
  </g>
  <text class="lbs" x="158" y="112" fill="#00695c">चिपचिपे सिरों को <tspan font-weight="800">DNA लाइगेज</tspan> जोड़ता है।</text>
  <!-- rDNA steps -->
  <rect x="152" y="120" width="174" height="76" rx="4" fill="#fff" stroke="#00897b" stroke-width="1"/>
  <text class="lbt" x="158" y="133" fill="#00695c">पुनर्योगज DNA तकनीक के 5 चरण</text>
  <text class="lbs" x="158" y="146">1. इच्छित DNA तथा वाहक का पृथक्करण</text>
  <text class="lbs" x="158" y="157">2. प्रतिबंधन एंजाइम से कटाव (चिपचिपे सिरे)</text>
  <text class="lbs" x="158" y="168">3. लाइगेज से वाहक में जोड़ना (पुनर्योगज DNA)</text>
  <text class="lbs" x="158" y="179">4. परपोषी कोशिका में स्थानांतरण + चयन</text>
  <text class="lbs" x="158" y="190">5. बायोरिएक्टर में संवर्धन + अनुप्रवाह संसाधन</text>
  <text class="lbs" x="4" y="186" fill="#4a148c">नाम: <tspan font-weight="800">Eco</tspan> (E. coli) + <tspan font-weight="800">R</tspan> (RY13) + <tspan font-weight="800">I</tspan> (क्रम)</text>
</svg>
"""

# ------------------------------------------------- Ch 10: Bt cotton + RNAi + gene therapy
BT_APPS = r"""
<svg viewBox="0 0 330 200" role="img">
  <!-- Panel 1: Bt toxin -->
  <rect x="4" y="4" width="322" height="64" rx="4" fill="#f4eafa" stroke="#4a148c" stroke-width="1"/>
  <text class="lbt" x="10" y="17" fill="#4a148c">1. Bt कपास — cry जीन की क्रियाविधि</text>
  <g font-weight="700">
    <rect x="10" y="24" width="62" height="18" rx="3" fill="#fff" stroke="#00897b" stroke-width=".8"/>
    <text class="lbs" x="13" y="36">बैसिलस थुरिंजिएंसिस</text>
    <rect x="82" y="24" width="56" height="18" rx="3" fill="#fff" stroke="#00897b" stroke-width=".8"/>
    <text class="lbs" x="88" y="36">cry जीन अलग</text>
    <rect x="148" y="24" width="56" height="18" rx="3" fill="#fff" stroke="#00897b" stroke-width=".8"/>
    <text class="lbs" x="152" y="36">कपास में प्रवेश</text>
    <rect x="214" y="24" width="52" height="18" rx="3" fill="#fff" stroke="#00897b" stroke-width=".8"/>
    <text class="lbs" x="218" y="36">निष्क्रिय प्रोटोक्सिन</text>
    <rect x="276" y="24" width="50" height="18" rx="3" fill="#ffe0b2" stroke="#ef6c00" stroke-width=".8"/>
    <text class="lbs" x="280" y="36">कीट खाता है</text>
  </g>
  <g class="ld" stroke-width="1"><path d="M72,33 h10"/><path d="M138,33 h10"/>
     <path d="M204,33 h10"/><path d="M266,33 h10"/></g>
  <text class="lbs" x="10" y="54" fill="#4a148c">कीट की <tspan font-weight="800">क्षारीय आंत</tspan> में प्रोटोक्सिन -&gt; सक्रिय विष -&gt; आंत की उपकला कोशिकाओं में छिद्र -&gt; कोशिका फूलकर फटे -&gt; कीट मरे।</text>
  <text class="lbs" x="10" y="64" fill="#4a148c">cry IAc व cry IIAb = <tspan font-weight="800">मुकुट कृमि (बॉलवर्म)</tspan>  &#183;  cry IAb = मक्का छेदक  &#183;  Bt बैंगन, Bt मक्का</text>
  <!-- Panel 2: RNAi -->
  <rect x="4" y="72" width="322" height="58" rx="4" fill="#e0f2f1" stroke="#00695c" stroke-width="1"/>
  <text class="lbt" x="10" y="85" fill="#00695c">2. RNA अंतरक्षेप (RNAi) — मेलॉइडोगाइनी इनकॉग्निटा प्रतिरोध</text>
  <g>
    <!-- dsRNA depiction -->
    <path d="M14,98 h74" stroke="#1565c0" stroke-width="3.4" stroke-linecap="round"/>
    <path d="M14,106 h74" stroke="#ad1457" stroke-width="3.4" stroke-linecap="round"/>
    <g stroke="#546e7a" stroke-width=".9">
      <line x1="22" y1="98" x2="22" y2="106"/><line x1="34" y1="98" x2="34" y2="106"/>
      <line x1="46" y1="98" x2="46" y2="106"/><line x1="58" y1="98" x2="58" y2="106"/>
      <line x1="70" y1="98" x2="70" y2="106"/><line x1="82" y1="98" x2="82" y2="106"/>
    </g>
    <text class="lbs" x="14" y="120" fill="#00695c">द्विरज्जुकी RNA (dsRNA)</text>
    <path class="ld" d="M92,102 h16" stroke-width="1.1"/>
    <rect x="110" y="92" width="76" height="22" rx="3" fill="#fff" stroke="#00695c" stroke-width=".8"/>
    <text class="lbs" x="114" y="101">परजीवी के mRNA से</text><text class="lbs" x="114" y="110">पूरक बंधन</text>
    <path class="ld" d="M190,102 h16" stroke-width="1.1"/>
    <rect x="208" y="92" width="112" height="22" rx="3" fill="#ffcdd2" stroke="#b3261e" stroke-width=".8"/>
    <text class="lbs" x="212" y="101">mRNA निःशब्द (silencing)</text>
    <text class="lbs" x="212" y="110">-&gt; परजीवी जीवित नहीं रह पाता</text>
  </g>
  <text class="lbs" x="14" y="127" fill="#00695c">कोशिकीय सुरक्षा विधि; <tspan font-weight="800">एग्रोबैक्टीरियम</tspan> वाहक से तंबाकू में dsRNA जीन डाला गया।</text>
  <!-- Panel 3: insulin + gene therapy -->
  <rect x="4" y="134" width="158" height="62" rx="4" fill="#e8f1fb" stroke="#1152a3" stroke-width="1"/>
  <text class="lbt" x="10" y="147" fill="#0b3a76">3. मानव इंसुलिन (ह्यूमुलिन)</text>
  <text class="lbs" x="10" y="158">इंसुलिन = A श्रृंखला (21) + B श्रृंखला (30),</text>
  <text class="lbs" x="10" y="168">जुड़ी <tspan font-weight="800">डाइसल्फाइड बंध</tspan> से।</text>
  <text class="lbs" x="10" y="178">प्राक्-हार्मोन में अतिरिक्त <tspan font-weight="800">C-पेप्टाइड</tspan>।</text>
  <text class="lbs" x="10" y="190">एली लिली ने A व B अलग-अलग <tspan font-weight="800">E. coli</tspan> में बनाए।</text>
  <rect x="168" y="134" width="158" height="62" rx="4" fill="#fdecea" stroke="#b3261e" stroke-width="1"/>
  <text class="lbt" x="174" y="147" fill="#8a1a14">4. जीन चिकित्सा + GEAC</text>
  <text class="lbs" x="174" y="158">प्रथम (1990): <tspan font-weight="800">ADA की कमी</tspan> वाली बालिका।</text>
  <text class="lbs" x="174" y="168">रोगी के लसीकाणु में सामान्य ADA cDNA</text>
  <text class="lbs" x="174" y="178">रेट्रोवायरस वाहक से डाला -&gt; पुनः आरोपण।</text>
  <text class="lbs" x="174" y="190">बायोपायरेसी उदा. <tspan font-weight="800">बासमती, हल्दी, नीम</tspan>।</text>
</svg>
"""

# ------------------------------------------------- Ch 11: population growth curves
GROWTH = r"""
<svg viewBox="0 0 330 186" role="img">
  <!-- axes -->
  <line x1="40" y1="150" x2="300" y2="150" stroke="#263238" stroke-width="1.4"/>
  <line x1="40" y1="150" x2="40" y2="18" stroke="#263238" stroke-width="1.4"/>
  <text class="lb" x="112" y="164">समय (Time)</text>
  <text class="lb" x="6" y="88" transform="rotate(-90 16 92)">समष्टि घनत्व (N)</text>
  <!-- carrying capacity line -->
  <line x1="40" y1="48" x2="300" y2="48" stroke="#ef6c00" stroke-width="1.1" stroke-dasharray="3.4 2.2"/>
  <text class="lb" x="276" y="44" fill="#bf360c">K</text>
  <text class="lbs" x="236" y="36" fill="#bf360c">पोषण क्षमता</text>
  <!-- J curve (exponential) -->
  <path d="M40,150 C106,150 150,140 176,96 C192,66 198,36 202,20"
        fill="none" stroke="#c62828" stroke-width="2.6"/>
  <text class="lb" x="206" y="26" fill="#b71c1c">J आकार</text>
  <text class="lbs" x="206" y="36" fill="#b71c1c">चरघातांकी वृद्धि</text>
  <!-- S curve (logistic) -->
  <path d="M40,150 C96,150 118,146 142,116 C164,88 182,58 232,50 C258,48 278,48 300,48"
        fill="none" stroke="#1b5e20" stroke-width="2.6"/>
  <text class="lb" x="236" y="66" fill="#1b5e20">S आकार</text>
  <text class="lbs" x="236" y="76" fill="#1b5e20">संभार तंत्र वृद्धि</text>
  <!-- phase markers on S -->
  <g stroke="#78909c" stroke-width=".8" stroke-dasharray="2 1.6">
    <line x1="104" y1="150" x2="104" y2="140"/><line x1="176" y1="150" x2="176" y2="80"/>
  </g>
  <text class="lbs" x="52" y="146">लैग</text><text class="lbs" x="116" y="132">लॉग</text>
  <text class="lbs" x="196" y="146">स्थिर</text>
  <!-- equations -->
  <rect x="4" y="168" width="158" height="16" rx="3" fill="#fdecea" stroke="#b3261e" stroke-width=".8"/>
  <text class="lbs" x="9" y="179" fill="#8a1a14">चरघातांकी: dN/dt = rN  &#183;  N&#7511; = N&#8320;e^(rt)</text>
  <rect x="168" y="168" width="158" height="16" rx="3" fill="#e8f5e9" stroke="#1b5e20" stroke-width=".8"/>
  <text class="lbs" x="173" y="179" fill="#1b5e20">संभार तंत्र: dN/dt = rN[(K &#8211; N)/K]</text>
  <!-- age pyramid insert -->
  <g transform="translate(246,96)">
    <text class="lbs" x="-4" y="-2" fill="#263238">आयु पिरामिड</text>
    <g fill="#90caf9" stroke="#1565c0" stroke-width=".5">
      <rect x="4"  y="2"  width="40" height="7"/>
      <rect x="9"  y="11" width="30" height="7"/>
      <rect x="14" y="20" width="20" height="7"/>
      <rect x="18" y="29" width="12" height="7"/>
    </g>
    <text class="lbs" x="0" y="46">विस्तारी (वृद्धिशील)</text>
  </g>
  <text class="lbs" x="44" y="26" fill="#37474f">r = जननिक क्षमता (बाह्य वृद्धि दर)</text>
  <text class="lbs" x="44" y="36" fill="#37474f">प्रकृति में कोई भी समष्टि अनंत काल तक J वृद्धि नहीं कर सकती</text>
</svg>
"""

# ------------------------------------------------- Ch 12: energy flow + ecological pyramid
ECOSYS = r"""
<svg viewBox="0 0 330 200" role="img">
  <!-- trophic pyramid -->
  <g stroke="#004d40" stroke-width=".8">
    <polygon points="22,150 196,150 178,126 40,126" fill="#a5d6a7"/>
    <polygon points="40,126 178,126 160,102 58,102" fill="#80cbc4"/>
    <polygon points="58,102 160,102 142,78 76,78" fill="#4db6ac"/>
    <polygon points="76,78 142,78 124,54 94,54" fill="#26a69a"/>
  </g>
  <g font-weight="700">
    <text class="lbs" x="56" y="143">उत्पादक (T&#8321;)</text>
    <text class="lbs" x="62" y="119">प्रथम उपभोक्ता (T&#8322;)</text>
    <text class="lbs" x="68" y="95">द्वितीय उपभोक्ता (T&#8323;)</text>
    <text class="lbs" x="80" y="70">तृतीय (T&#8324;)</text>
  </g>
  <!-- energy numbers -->
  <g>
    <text class="lb" x="204" y="144" fill="#1b5e20">10,000 J</text>
    <text class="lb" x="204" y="120" fill="#1b5e20">1,000 J</text>
    <text class="lb" x="204" y="96" fill="#1b5e20">100 J</text>
    <text class="lb" x="204" y="72" fill="#1b5e20">10 J</text>
  </g>
  <!-- heat loss arrows -->
  <g stroke="#ef6c00" stroke-width="1.3">
    <path d="M258,138 l14,-7"/><path d="M258,114 l14,-7"/><path d="M258,90 l14,-7"/>
  </g>
  <text class="lbs" x="276" y="112" fill="#bf360c">प्रत्येक स्तर पर</text>
  <text class="lbs" x="276" y="122" fill="#bf360c">ऊष्मा रूप में</text>
  <text class="lbs" x="276" y="132" fill="#bf360c">90% हानि</text>
  <!-- sun -->
  <circle cx="24" cy="24" r="11" fill="#ffd54f" stroke="#f57f17" stroke-width="1"/>
  <text class="lbs" x="40" y="21" fill="#c76f00">सौर ऊर्जा — PAR का</text>
  <text class="lbs" x="40" y="31" fill="#c76f00">केवल 1&#8211;5% स्थिरीकृत</text>
  <path class="ld" d="M30,34 L58,54" stroke="#f57f17" stroke-width="1.2"/>
  <text class="lbt" x="150" y="24" fill="#004d40">10% नियम (लिंडेमान)</text>
  <!-- facts strip -->
  <rect x="4" y="158" width="158" height="38" rx="3" fill="#e4f4f1" stroke="#00695c" stroke-width=".8"/>
  <text class="lbs" x="9" y="169" fill="#004d40"><tspan font-weight="800">संख्या व भार</tspan> का पिरामिड उल्टा भी हो सकता है</text>
  <text class="lbs" x="9" y="179" fill="#004d40">(सागरीय पारितंत्र, एक वृक्ष पर कीट)।</text>
  <text class="lbs" x="9" y="190" fill="#004d40"><tspan font-weight="800">ऊर्जा का पिरामिड सदैव सीधा</tspan> होता है।</text>
  <rect x="168" y="158" width="158" height="38" rx="3" fill="#fff3e0" stroke="#ef6c00" stroke-width=".8"/>
  <text class="lbs" x="173" y="169" fill="#8a4500">GPP &#8211; श्वसन = <tspan font-weight="800">NPP</tspan></text>
  <text class="lbs" x="173" y="179" fill="#8a4500">अपघटन के चरण: खंडन, निक्षालन, अपचयन,</text>
  <text class="lbs" x="173" y="190" fill="#8a4500">ह्यूमसीकरण, खनिजीकरण।</text>
</svg>
"""

# ------------------------------------------------- Ch 13: biodiversity patterns
BIODIV = r"""
<svg viewBox="0 0 330 200" role="img">
  <text class="lbt" x="4" y="12" fill="#004d40">जैव विविधता के प्रतिरूप एवं संरक्षण</text>
  <!-- latitudinal gradient -->
  <g>
    <rect x="10" y="22" width="26" height="92" rx="3" fill="#b2dfdb" stroke="#00695c" stroke-width=".7"/>
    <rect x="10" y="22" width="26" height="30" fill="#00695c"/>
    <text class="lbw" x="14" y="40">उच्च</text>
    <text class="lbs" x="8" y="124">भूमध्य रेखा</text>
    <rect x="46" y="52" width="26" height="62" rx="3" fill="#b2dfdb" stroke="#00695c" stroke-width=".7"/>
    <rect x="46" y="52" width="26" height="20" fill="#26a69a"/>
    <text class="lbs" x="44" y="124">शीतोष्ण</text>
    <rect x="82" y="86" width="26" height="28" rx="3" fill="#b2dfdb" stroke="#00695c" stroke-width=".7"/>
    <rect x="82" y="86" width="26" height="9" fill="#80cbc4"/>
    <text class="lbs" x="82" y="124">ध्रुवीय</text>
    <text class="lbs" x="8" y="136" fill="#004d40">अक्षांश बढ़ने पर विविधता घटती है</text>
  </g>
  <!-- species-area curve -->
  <g transform="translate(130,18)">
    <line x1="4" y1="96" x2="86" y2="96" stroke="#263238" stroke-width="1.1"/>
    <line x1="4" y1="96" x2="4" y2="14" stroke="#263238" stroke-width="1.1"/>
    <path d="M4,96 C26,58 48,36 86,26" fill="none" stroke="#ef6c00" stroke-width="2.4"/>
    <text class="lbs" x="22" y="108">क्षेत्र (log A)</text>
    <text class="lbs" x="-6" y="10">जाति समृद्धि</text>
    <text class="lbs" x="30" y="40" fill="#bf360c">log S = log C</text>
    <text class="lbs" x="30" y="50" fill="#bf360c">+ Z log A</text>
    <text class="lbs" x="4" y="120" fill="#bf360c">Z = 0.1&#8211;0.2 (छोटा क्षेत्र)</text>
    <text class="lbs" x="4" y="130" fill="#bf360c">Z = 0.6&#8211;1.2 (बड़ा क्षेत्र)</text>
  </g>
  <!-- global share -->
  <g transform="translate(232,18)">
    <text class="lbs" x="0" y="8" fill="#004d40" font-weight="800">वैश्विक अनुपात</text>
    <g stroke="#004d40" stroke-width=".5">
      <rect x="0" y="14" width="84" height="11" fill="#ffb300"/>
      <text class="lbs" x="3" y="23">कीट ~70% (सर्वाधिक)</text>
      <rect x="0" y="28" width="52" height="11" fill="#4db6ac"/>
      <text class="lbs" x="3" y="37">अन्य प्राणी</text>
      <rect x="0" y="42" width="38" height="11" fill="#81c784"/>
      <text class="lbs" x="3" y="51">पादप ~22%</text>
      <rect x="0" y="56" width="26" height="11" fill="#90caf9"/>
      <text class="lbs" x="3" y="65">कवक</text>
    </g>
    <text class="lbs" x="0" y="82" fill="#004d40">भारत = विश्व का 8.1%</text>
    <text class="lbs" x="0" y="92" fill="#004d40">जातियाँ (क्षेत्र केवल 2.4%)</text>
    <text class="lbs" x="0" y="104" fill="#004d40">विश्व में 34 हॉट स्पॉट;</text>
    <text class="lbs" x="0" y="114" fill="#004d40">भारत में 3 &#8212; पश्चिमी घाट-</text>
    <text class="lbs" x="0" y="124" fill="#004d40">श्रीलंका, हिमालय, इंडो-बर्मा</text>
  </g>
  <!-- the evil quartet -->
  <rect x="4" y="144" width="322" height="24" rx="3" fill="#fdecea" stroke="#b3261e" stroke-width=".8"/>
  <text class="lbs" x="10" y="155" fill="#8a1a14" font-weight="800">विलुप्ति के 4 कारण (The Evil Quartet):</text>
  <text class="lbs" x="10" y="165" fill="#8a1a14">1. आवास की क्षति व विखंडन (सर्वाधिक)  2. अतिदोहन  3. विदेशी जातियों का आक्रमण (नील पर्च, जलकुंभी, पार्थेनियम)  4. सहविलुप्ति</text>
  <rect x="4" y="172" width="322" height="24" rx="3" fill="#e4f4f1" stroke="#00695c" stroke-width=".8"/>
  <text class="lbs" x="10" y="183" fill="#004d40" font-weight="800">संरक्षण:</text>
  <text class="lbs" x="56" y="183" fill="#004d40"><tspan font-weight="700">स्वस्थाने</tspan> — राष्ट्रीय उद्यान, वन्यजीव अभयारण्य, बायोस्फीयर रिजर्व, पवित्र उपवन</text>
  <text class="lbs" x="10" y="193" fill="#004d40"><tspan font-weight="700">बहिस्थाने</tspan> — चिड़ियाघर, वानस्पतिक उद्यान, बीज बैंक, क्रायोप्रिजर्वेशन (&#8211;196&#176;C) &#183; रेड डाटा बुक = IUCN सूची</text>
</svg>
"""
