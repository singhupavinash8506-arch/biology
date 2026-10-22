# -*- coding: utf-8 -*-
"""
Figures for the handwritten-style sheets.

The anatomical figures are redrawn here in the pink line-art look of a
hand-made study sheet: light rose fills, deep-pink outlines, thin grey leader
lines, Hindi label with the English term underneath.

Styling comes from CSS classes defined in render_hw.py (.organ, .organ2,
.lumen, .duct, .hl, .ld, .lb, .lbs ...), so every figure shares one palette.

The non-anatomical figures (charts, pyramids, plasmid maps) are reused from
diagrams.py -- they already use the same label classes, so they pick up the
handwriting font automatically.
"""

from diagrams import (                                    # noqa: F401
    CONTRA, PUNNETT, DNA, FINCHES, ANTIBODY, MALARIA,
    BIOGAS, PBR322, BT_APPS, GROWTH, ECOSYS, BIODIV,
)

# --------------------------------------------- Ch 1: ovule + embryo sac
OVULE_HW = r"""
<svg viewBox="0 0 300 184" role="img">
  <ellipse class="organ2" cx="150" cy="92" rx="76" ry="56"/>
  <ellipse class="organ" cx="150" cy="92" rx="68" ry="48"/>
  <ellipse class="organ3" cx="152" cy="92" rx="60" ry="41"/>
  <ellipse class="lumen" cx="156" cy="92" rx="48" ry="29"/>
  <path d="M74,92 l-16,-8 v16 z" fill="#fff" stroke="#ad1457" stroke-width=".8"/>
  <path d="M74,84 a9,8 0 0 0 0,16" fill="#fff" stroke="#ad1457" stroke-width=".8"/>
  <path class="duct" d="M226,92 q22,2 29,15"/>
  <circle cx="226" cy="92" r="3.2" fill="#880e4f"/>
  <ellipse cx="127" cy="92" rx="11.5" ry="8.5" fill="#ef9a9a" stroke="#c62828" stroke-width=".85"/>
  <circle cx="127" cy="92" r="3.4" fill="#b71c1c"/>
  <ellipse class="hl2" cx="121" cy="79"  rx="8.5" ry="6"/>
  <ellipse class="hl2" cx="121" cy="105" rx="8.5" ry="6"/>
  <circle class="pu" cx="159" cy="87" r="5"/>
  <circle class="pu" cx="169" cy="97" r="5"/>
  <circle class="gr" cx="193" cy="82"  r="4.8"/>
  <circle class="gr" cx="199" cy="92" r="4.8"/>
  <circle class="gr" cx="193" cy="102" r="4.8"/>
  <path class="ld" d="M56,98 L36,120"/><circle class="dot" cx="56" cy="98" r="1.2"/>
  <text class="lb" x="0" y="130">बीजाण्डद्वार</text><text class="lbs" x="0" y="139">(Micropyle)</text>
  <path class="ld" d="M121,77 L98,48"/><circle class="dot" cx="121" cy="77" r="1.2"/>
  <text class="lb" x="32" y="36">सहाय कोशिकाएँ</text><text class="lbs" x="32" y="45">(2 Synergids)</text>
  <path class="ld" d="M127,100 L112,154"/><circle class="dot" cx="127" cy="100" r="1.2"/>
  <text class="lb" x="70" y="166">अण्ड कोशिका</text><text class="lbs" x="70" y="175">(Egg, n)</text>
  <path class="ld" d="M164,85 L172,44"/><circle class="dot" cx="164" cy="85" r="1.2"/>
  <text class="lb" x="142" y="32">2 ध्रुवीय केन्द्रक</text><text class="lbs" x="142" y="41">(Polar nuclei, 2n)</text>
  <path class="ld" d="M199,102 L206,154"/><circle class="dot" cx="199" cy="102" r="1.2"/>
  <text class="lb" x="178" y="166">3 प्रतिव्यासांत</text><text class="lbs" x="178" y="175">(Antipodals)</text>
  <path class="ld" d="M204,68 L240,44"/><circle class="dot" cx="204" cy="68" r="1.2"/>
  <text class="lb" x="236" y="32">भ्रूणकोष</text><text class="lbs" x="236" y="41">(Embryo sac)</text>
  <path class="ld" d="M212,122 L246,138"/><circle class="dot" cx="212" cy="122" r="1.2"/>
  <text class="lb" x="234" y="149">अध्यावरण</text><text class="lbs" x="234" y="158">(Integument)</text>
  <path class="ld" d="M253,108 L272,122"/><circle class="dot" cx="253" cy="108" r="1.2"/>
  <text class="lb" x="252" y="133">बीजाण्डवृन्त</text>
  <text class="lbt" x="84" y="14">7 कोशिका + 8 केन्द्रक (पॉलीगोनम प्रकार)</text>
</svg>
"""

# --------------------------------------------- Ch 2a: male reproductive system
MALE_HW = r"""
<svg viewBox="0 0 250 206" role="img">
  <!-- seminal vesicles -->
  <path class="organ" d="M92,22 q-16,6 -14,22 q2,14 16,16 q10,-14 10,-38 z"/>
  <path class="organ" d="M158,22 q16,6 14,22 q-2,14 -16,16 q-10,-14 -10,-38 z"/>
  <!-- prostate -->
  <ellipse class="organ2" cx="125" cy="76" rx="26" ry="17"/>
  <!-- bulbourethral (Cowper) glands -->
  <circle class="hl" cx="100" cy="98" r="6"/>
  <circle class="hl" cx="150" cy="98" r="6"/>
  <!-- urethra through penis -->
  <rect class="organ3" x="112" y="90" width="26" height="78" rx="12"/>
  <path d="M125,92 V164" stroke="#c2185b" stroke-width="2.1" fill="none"/>
  <ellipse class="organ" cx="125" cy="170" rx="15" ry="11"/>
  <!-- scrotum -->
  <path class="organ3" d="M48,150 q-14,34 12,44 q18,6 30,-8 M202,150 q14,34 -12,44 q-18,6 -30,-8"/>
  <!-- testes -->
  <ellipse class="organ2" cx="60" cy="158" rx="22" ry="15"/>
  <ellipse class="organ2" cx="190" cy="158" rx="22" ry="15"/>
  <!-- epididymis crescents -->
  <path d="M40,150 q-8,10 2,18" stroke="#880e4f" stroke-width="2.6" fill="none" stroke-linecap="round"/>
  <path d="M210,150 q8,10 -2,18" stroke="#880e4f" stroke-width="2.6" fill="none" stroke-linecap="round"/>
  <!-- vas deferens -->
  <path class="duct" d="M44,146 q-8,-44 30,-56 q28,-7 44,-16"/>
  <path class="duct" d="M206,146 q8,-44 -30,-56 q-28,-7 -44,-16"/>
  <!-- labels (right and left like a hand-made sheet) -->
  <path class="ld" d="M170,34 L206,22"/><circle class="dot" cx="170" cy="34" r="1.2"/>
  <text class="lb" x="196" y="16">शुक्राशय</text><text class="lbs" x="196" y="25">(Seminal vesicle)</text>
  <path class="ld" d="M100,52 L58,34"/><circle class="dot" cx="100" cy="52" r="1.2"/>
  <text class="lb" x="2" y="28">शुक्रवाहक</text><text class="lbs" x="2" y="37">(Vas deferens)</text>
  <path class="ld" d="M149,76 L206,60"/><circle class="dot" cx="149" cy="76" r="1.2"/>
  <text class="lb" x="196" y="54">पुरस्थ ग्रंथि</text><text class="lbs" x="196" y="63">(Prostate)</text>
  <path class="ld" d="M156,98 L208,96"/><circle class="dot" cx="156" cy="98" r="1.2"/>
  <text class="lb" x="208" y="92">काउपर ग्रंथि</text><text class="lbs" x="208" y="101">(Bulbourethral)</text>
  <path class="ld" d="M138,124 L188,126"/><circle class="dot" cx="138" cy="124" r="1.2"/>
  <text class="lb" x="188" y="122">मूत्रमार्ग</text><text class="lbs" x="188" y="131">(Urethra)</text>
  <path class="ld" d="M112,150 L74,146"/>
  <path class="ld" d="M60,146 L34,120"/><circle class="dot" cx="60" cy="146" r="1.2"/>
  <text class="lb" x="2" y="112">वृषण</text><text class="lbs" x="2" y="121">(Testis)</text>
  <path class="ld" d="M34,172 L10,186"/><circle class="dot" cx="34" cy="172" r="1.2"/>
  <text class="lb" x="2" y="198">वृषणकोष</text><text class="lbs" x="48" y="198">(Scrotum)</text>
  <path class="ld" d="M125,182 L166,192"/><circle class="dot" cx="125" cy="182" r="1.2"/>
  <text class="lb" x="164" y="190">लिंग</text><text class="lbs" x="164" y="199">(Penis)</text>
</svg>
"""

# --------------------------------------------- Ch 2b: female reproductive system
FEMALE_HW = r"""
<svg viewBox="0 0 250 188" role="img">
  <!-- uterus -->
  <path class="organ2" d="M96,46 q29,-11 58,0 q12,30 6,52 q-8,26 -35,26 q-27,0 -35,-26 q-6,-22 6,-52 z"/>
  <path class="lumen" d="M109,56 q16,-6 32,0 q7,24 3,42 q-5,15 -19,15 q-14,0 -19,-15 q-4,-18 3,-42 z"/>
  <!-- cervix + vagina -->
  <rect class="pu" x="115" y="118" width="20" height="14" rx="3"/>
  <path class="organ3" d="M112,132 q13,19 26,0 l0,22 q-13,8 -26,0 z"/>
  <!-- fallopian tubes -->
  <path class="duct" d="M98,48 q-32,-6 -44,16"/>
  <path class="duct" d="M152,48 q32,-6 44,16"/>
  <!-- fimbriae -->
  <path d="M54,64 l-9,-5 M54,64 l-10,2 M54,64 l-6,8" stroke="#ad1457" stroke-width="1.5"
        stroke-linecap="round" fill="none"/>
  <path d="M196,64 l9,-5 M196,64 l10,2 M196,64 l6,8" stroke="#ad1457" stroke-width="1.5"
        stroke-linecap="round" fill="none"/>
  <!-- ovaries with follicles -->
  <ellipse class="hl" cx="46" cy="82" rx="16" ry="10.5"/>
  <ellipse class="hl" cx="204" cy="82" rx="16" ry="10.5"/>
  <circle cx="42" cy="82" r="3" fill="#f9a825"/><circle cx="208" cy="82" r="3" fill="#f9a825"/>
  <circle cx="51" cy="79" r="1.8" fill="#fbc02d"/><circle cx="199" cy="79" r="1.8" fill="#fbc02d"/>
  <!-- labels -->
  <path class="ld" d="M64,56 L36,32"/><circle class="dot" cx="64" cy="56" r="1.2"/>
  <text class="lb" x="0" y="24">अंडवाहिनी</text><text class="lbs" x="0" y="33">(Fallopian tube)</text>
  <path class="ld" d="M46,92 L30,118"/><circle class="dot" cx="46" cy="92" r="1.2"/>
  <text class="lb" x="0" y="130">अंडाशय</text><text class="lbs" x="0" y="139">(Ovary)</text>
  <path class="ld" d="M48,70 L22,58"/><circle class="dot" cx="48" cy="70" r="1.2"/>
  <text class="lb" x="0" y="52">तंतुमय</text>
  <path class="ld" d="M126,68 L178,26"/><circle class="dot" cx="126" cy="68" r="1.2"/>
  <text class="lb" x="176" y="20">गर्भाशय</text><text class="lbs" x="176" y="29">(Uterus)</text>
  <path class="ld" d="M142,90 L212,54"/><circle class="dot" cx="142" cy="90" r="1.2"/>
  <text class="lb" x="204" y="46">एंडोमेट्रियम</text>
  <path class="ld" d="M136,124 L196,110"/><circle class="dot" cx="136" cy="124" r="1.2"/>
  <text class="lb" x="192" y="106">गर्भाशय ग्रीवा</text><text class="lbs" x="192" y="115">(Cervix)</text>
  <path class="ld" d="M138,146 L192,148"/><circle class="dot" cx="138" cy="146" r="1.2"/>
  <text class="lb" x="194" y="145">योनि</text><text class="lbs" x="194" y="154">(Vagina)</text>
  <text class="lbt" x="30" y="176">निषेचन-स्थल = अंडवाहिनी की तुंबिका-संकीर्ण संधि</text>
</svg>
"""

# --------------------------------------------- Ch 2c: human sperm
SPERM_HW = r"""
<svg viewBox="0 0 300 136" role="img">
  <!-- head: acrosome + nucleus -->
  <path class="bl" d="M26,68 a28,21 0 0 1 28,-21 l0,42 a28,21 0 0 1 -28,-21 z"/>
  <path class="pu" d="M54,47 a28,21 0 0 1 0,42 z"/>
  <ellipse cx="50" cy="68" rx="12" ry="13" fill="#9575cd" stroke="#4527a0" stroke-width=".85"/>
  <!-- neck -->
  <rect class="organ2" x="81" y="60" width="10" height="16" rx="2.4"/>
  <!-- middle piece + mitochondrial spiral -->
  <rect class="hl2" x="91" y="62" width="44" height="12" rx="5"/>
  <path d="M95,62 q4,12 7.5,0 q4,12 7.5,0 q4,12 7.5,0 q4,12 7.5,0 q4,12 7,0"
        fill="none" stroke="#bf360c" stroke-width=".85"/>
  <!-- tail -->
  <path d="M135,68 q22,-13 40,0 q19,13 39,0 q19,-13 39,0 q13,9 26,2"
        fill="none" stroke="#880e4f" stroke-width="3.8" stroke-linecap="round"/>
  <path class="ldd" d="M24,68 a30,23 0 0 1 30,-23"/>
  <!-- region brackets -->
  <path class="ld" d="M26,96 h56 M26,93 v6 M82,93 v6"/>
  <text class="lb" x="36" y="108">शीर्ष</text><text class="lbs" x="32" y="117">(Head)</text>
  <path class="ld" d="M91,96 h44 M91,93 v6 M135,93 v6"/>
  <text class="lb" x="94" y="108">मध्य भाग</text><text class="lbs" x="92" y="117">(Middle piece)</text>
  <path class="ld" d="M138,96 h142 M138,93 v6 M280,93 v6"/>
  <text class="lb" x="194" y="108">पुच्छ</text><text class="lbs" x="190" y="117">(Tail, 9+2)</text>
  <!-- leaders -->
  <path class="ld" d="M34,50 L22,26"/><circle class="dot" cx="34" cy="50" r="1.2"/>
  <text class="lb" x="0" y="18">अग्रपिधान</text><text class="lbs" x="0" y="27">(Acrosome)</text>
  <path class="ld" d="M50,56 L74,22"/><circle class="dot" cx="50" cy="56" r="1.2"/>
  <text class="lb" x="70" y="14">केन्द्रक</text><text class="lbs" x="70" y="23">(Nucleus, n)</text>
  <path class="ld" d="M86,60 L106,32"/><circle class="dot" cx="86" cy="60" r="1.2"/>
  <text class="lb" x="120" y="14">ग्रीवा</text><text class="lbs" x="120" y="23">(Neck)</text>
  <path class="ld" d="M116,62 L168,36"/><circle class="dot" cx="116" cy="62" r="1.2"/>
  <text class="lb" x="172" y="30">माइटोकॉन्ड्रिया</text><text class="lbs" x="172" y="39">(ऊर्जा देता है)</text>
  <text class="lbt" x="2" y="132">एक स्खलन में 20&#8211;30 करोड़ शुक्राणु &#183; 60% से अधिक सक्रिय होना आवश्यक</text>
</svg>
"""

# --------------------------------------------- Ch 2d: gametogenesis ladder
GAMETO_HW = r"""
<svg viewBox="0 0 300 180" role="img">
  <text class="lbt" x="6" y="12">(A) शुक्राणुजनन</text>
  <text class="lbt" x="166" y="12">(B) अंडजनन</text>
  <g font-family="'Kalam'" >
    <!-- left ladder -->
    <rect class="bl" x="6" y="20" width="128" height="16" rx="3"/>
    <text class="lb" x="22" y="31">स्पर्मेटोगोनिया (2n)</text>
    <rect class="bl" x="6" y="46" width="128" height="16" rx="3"/>
    <text class="lb" x="14" y="57">प्राथमिक शुक्रकोशिका (2n)</text>
    <rect class="bl" x="6" y="72" width="128" height="16" rx="3"/>
    <text class="lb" x="12" y="83">द्वितीयक शुक्रकोशिका (n) &#215;2</text>
    <rect class="bl" x="6" y="98" width="128" height="16" rx="3"/>
    <text class="lb" x="30" y="109">शुक्राणुजन (n) &#215;4</text>
    <rect class="gr" x="6" y="124" width="128" height="16" rx="3"/>
    <text class="lb" x="38" y="135">4 शुक्राणु (n)</text>
    <!-- right ladder -->
    <rect class="hl" x="166" y="20" width="128" height="16" rx="3"/>
    <text class="lb" x="188" y="31">ओोगोनिया (2n)</text>
    <rect class="hl" x="166" y="46" width="128" height="16" rx="3"/>
    <text class="lb" x="178" y="57">प्राथमिक अंडक (2n)</text>
    <rect class="hl" x="166" y="72" width="128" height="16" rx="3"/>
    <text class="lb" x="170" y="83">द्वितीयक अंडक (n) + 1 ध्रुवीय</text>
    <rect class="hl" x="166" y="98" width="128" height="16" rx="3"/>
    <text class="lb" x="186" y="109">ऊटिड + ध्रुवीय कायिका</text>
    <rect class="gr" x="166" y="124" width="128" height="16" rx="3"/>
    <text class="lb" x="174" y="135">1 अंडाणु + 3 ध्रुवीय कायिका</text>
  </g>
  <g class="ld" stroke-width=".9">
    <path d="M70,36 v10"/><path d="M70,62 v10"/><path d="M70,88 v10"/><path d="M70,114 v10"/>
    <path d="M230,36 v10"/><path d="M230,62 v10"/><path d="M230,88 v10"/><path d="M230,114 v10"/>
  </g>
  <text class="lbs" x="74" y="45">गुणन (समसूत्री)</text>
  <text class="lbs" x="74" y="71">अर्धसूत्री I</text>
  <text class="lbs" x="74" y="97">अर्धसूत्री II</text>
  <text class="lbs" x="74" y="123">रूपांतरण</text>
  <text class="lbs" x="234" y="71">अर्धसूत्री I</text>
  <text class="lbs" x="234" y="97">अर्धसूत्री II</text>
  <text class="lbt" x="6" y="155">शुक्राणुजनन से 4 क्रियाशील युग्मक, अंडजनन से केवल 1 क्रियाशील अंडाणु बनता है।</text>
  <text class="lbs" x="6" y="168">अंडजनन भ्रूणीय अवस्था में प्रारंभ होकर अर्धसूत्री-I में रुक जाता है; अंडोत्सर्ग पर ही पूर्ण होता है।</text>
</svg>
"""
