"""
Handwritten-notebook style one-page sheets for UP Board Class 12 Biology.

Visual target: the classic hand-made Hindi study sheet -- centred underlined
title, "परिचय" opener, numbered sections with (i)(ii)(iii) items, thin
pastel-bordered boxes, pink line-art figures, a "महत्वपूर्ण तथ्य" star box and
a flow chart along the bottom.

Typeface is Kalam (Devanagari handwriting, OFL) embedded as base64 so the page
renders identically anywhere. Kalam has no star or arrow glyph, so those are
drawn in CSS.

Output: notes-handwritten/images/*.png, notes-handwritten/pdf/*.pdf, merged PDF.
"""
import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "_work" / "fonts"
OUT = ROOT / "notes-handwritten"
BUILD = ROOT / "_work" / "build_hw"

# thin-bordered pastel box palette, cycled across the numbered sections
PALETTE = [
    dict(c="#c2185b", bg="#fdf1f5"),   # rose
    dict(c="#6a1b9a", bg="#f7f1fb"),   # purple
    dict(c="#2e7d32", bg="#f0f8f1"),   # green
    dict(c="#1565c0", bg="#eef5fd"),   # blue
    dict(c="#e65100", bg="#fff5ec"),   # orange
    dict(c="#00695c", bg="#eef7f5"),   # teal
    dict(c="#ad1457", bg="#fdf0f4"),   # deep pink
    dict(c="#4527a0", bg="#f3f0fb"),   # indigo
]
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]

ARROW = (
    "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2026%2012'"
    "%3E%3Cpath%20d='M1%206h19M16%201.5l5%204.5-5%204.5'%20fill='none'%20stroke='%23b0003a'"
    "%20stroke-width='2.1'%20stroke-linecap='round'%20stroke-linejoin='round'/%3E%3C/svg%3E"
)


def fonts_css() -> str:
    out = []
    for name, weight in [("Kalam-Light", 300), ("Kalam-Regular", 400), ("Kalam-Bold", 700)]:
        p = FONT_DIR / f"{name}.ttf"
        if not p.exists():
            raise SystemExit(f"missing font {p}")
        b64 = base64.b64encode(p.read_bytes()).decode()
        out.append("@font-face{font-family:'Kalam';font-style:normal;font-weight:%d;"
                   "src:url(data:font/truetype;base64,%s) format('truetype');"
                   "font-display:block}" % (weight, b64))
    return "".join(out)


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4 portrait;margin:0}
:root{--fs:1}
html{font-size:calc(var(--fs) * 1px)}
body{font-family:'Kalam',sans-serif;-webkit-font-smoothing:antialiased}
.sheet{width:210mm;height:297mm;background:#fff;padding:5.2mm 5.6mm 4mm;
       display:flex;flex-direction:column;overflow:hidden;position:relative}
/* ---------------- title ---------------- */
.ttl{text-align:center;flex:0 0 auto;margin-bottom:1.6mm}
.ttl h1{font-size:25rem;font-weight:700;color:#a4123f;line-height:1.16;
        display:inline-block;border-bottom:.45mm solid #d81b60;padding:0 3mm .7mm}
.ttl h1 span{color:#6a1b9a;font-size:.68em}
.ttl .sub{font-size:9.4rem;color:#555;margin-top:.9mm;font-weight:400}
/* ---------------- intro ---------------- */
.intro{flex:0 0 auto;border:.3mm solid #d81b60;border-left:1.1mm solid #d81b60;
       border-radius:1.4mm;background:#fdf1f5;padding:1.2mm 2mm;margin-bottom:1.8mm;
       font-size:11.4rem;line-height:1.46}
.intro b{color:#a4123f;font-weight:700}
.st{display:inline-block;width:2.5mm;height:2.5mm;background:#f9a825;margin-right:.9mm;
    vertical-align:-.25mm;
    clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
/* ---------------- grid ---------------- */
.grid{flex:1 1 auto;display:grid;grid-template-columns:repeat(12,1fr);
      gap:1.9mm;align-content:start;min-height:0}
.blk{border:.3mm solid var(--c);border-radius:1.6mm;background:var(--bg);
     padding:1.1mm 1.7mm 1.3mm;min-width:0;overflow:hidden}
.blk>h3{font-size:11.6rem;font-weight:700;color:var(--c);line-height:1.2;
        margin-bottom:.9mm;padding-bottom:.5mm;border-bottom:.22mm dashed var(--c)}
.blk>h3 em{font-style:normal;font-weight:400;font-size:9.4rem;opacity:.8}
/* ---------------- numbered items ---------------- */
.blk ol{list-style:none}
.blk ol li{font-size:11rem;line-height:1.44;padding-left:5.4mm;position:relative;
           margin-bottom:.5mm;text-align:left}
.blk ol li>i{position:absolute;left:0;top:0;font-style:normal;color:var(--c);
             font-weight:700;font-size:10.2rem}
.blk li b{color:var(--c);font-weight:700}
.blk li .k{font-size:9.4rem;opacity:.78}
.ar{display:inline-block;width:3.2mm;height:1.8mm;vertical-align:-.1mm;margin:0 .3mm;
    background:no-repeat center/contain url("ARROWURL")}
/* ---------------- side list box ---------------- */
.side ul{list-style:none}
.side ul li{font-size:10.4rem;line-height:1.4;padding-left:2.8mm;position:relative;
            margin-bottom:.45mm}
.side ul li:before{content:"";position:absolute;left:.3mm;top:1.5mm;width:1.3mm;height:1.3mm;
                   border-radius:50%;background:var(--c)}
.side ul li b{color:var(--c);font-weight:700}
/* ---------------- figure card ---------------- */
.fig{border:.34mm solid var(--c);border-radius:1.6mm;background:#fff;padding:0;
     display:flex;flex-direction:column;overflow:hidden;min-width:0}
.fig>h4{font-size:10.4rem;font-weight:700;color:var(--c);text-align:center;
        background:var(--bg);padding:.75mm 1.4mm;border-bottom:.22mm dashed var(--c)}
.fig .wrap{flex:1 1 auto;display:flex;align-items:center;justify-content:center;padding:.9mm}
.fig svg{width:100%;height:auto;display:block}
.fig .cap{font-size:8.8rem;text-align:center;color:#444;padding:0 1.2mm .9mm;line-height:1.3}
/* ---------------- important facts ---------------- */
.facts{border:.34mm solid #ef6c00;border-radius:1.6mm;background:#fffaf0;
       padding:1.1mm 1.7mm 1.3mm;overflow:hidden}
.facts>h3{font-size:11.6rem;font-weight:700;color:#bf4a00;text-align:center;
          margin-bottom:.8mm;padding-bottom:.5mm;border-bottom:.22mm dashed #ef6c00}
.facts ul{list-style:none}
.facts ul li{font-size:10.6rem;line-height:1.4;padding-left:3.4mm;position:relative;
             margin-bottom:.45mm}
.facts ul li .st{position:absolute;left:0;top:1.1mm;width:2.2mm;height:2.2mm;margin:0}
.facts li b{color:#a33c00;font-weight:700}
.facts li .k{font-size:9.2rem;opacity:.78}
/* ---------------- PYQ ---------------- */
.pyq{border:.3mm solid #4527a0;border-radius:1.6mm;background:#f4f1fc;
     padding:1.1mm 1.7mm 1.3mm;overflow:hidden}
.pyq>h3{font-size:11rem;font-weight:700;color:#4527a0;margin-bottom:.7mm;
        padding-bottom:.45mm;border-bottom:.22mm dashed #4527a0}
.pyq ul{list-style:none}
.pyq ul li{font-size:10rem;line-height:1.38;padding-left:3mm;position:relative;margin-bottom:.4mm}
.pyq ul li:before{content:"\\2022";position:absolute;left:.5mm;top:-.3mm;color:#4527a0;font-weight:700}
.pyq li i{font-style:normal;background:#4527a0;color:#fff;border-radius:.8mm;
          padding:0 1mm;font-size:8.8rem;font-weight:700;margin-right:.7mm}
.pyq li b{color:#4527a0;font-weight:700}
/* ---------------- flow chart ---------------- */
.flow{flex:0 0 auto;border:.34mm solid #d81b60;border-radius:1.6mm;background:#fdf1f5;
      padding:1.1mm 2mm 1.3mm;margin-top:1.8mm}
.flow>h3{font-size:10.6rem;font-weight:700;color:#a4123f;margin-bottom:.7mm}
.flow .chain{display:flex;flex-wrap:wrap;align-items:center;gap:.5mm 0;
             font-size:10.4rem;line-height:1.3}
.flow .pill{background:#fff;border:.26mm solid #d81b60;border-radius:3mm;
            padding:.3mm 1.6mm;font-weight:700;color:#8e1038;white-space:nowrap}
.flow .pill.alt{border-color:#2e7d32;color:#1b5e20}
.flow .pill.alt2{border-color:#1565c0;color:#0d47a1}
/* ---------------- footer ---------------- */
.ftr{flex:0 0 auto;display:flex;align-items:center;gap:2.5mm;margin-top:1.4mm;
     font-size:8rem;color:#777;border-top:.22mm solid #ccc;padding-top:.9mm}
.ftr .r{margin-left:auto}
/* ---------------- svg figure styling (pink line art) ---------------- */
svg text{font-family:'Kalam',sans-serif}
svg .lb{font-size:7.6px;font-weight:700;fill:#20242c}
svg .lbs{font-size:6.8px;font-weight:400;fill:#3c4450}
svg .lbt{font-size:8.2px;font-weight:700;fill:#a4123f}
svg .lbw{font-size:7.4px;font-weight:700;fill:#fff}
svg .ld{stroke:#555;stroke-width:.55;fill:none}
svg .ldd{stroke:#555;stroke-width:.5;fill:none;stroke-dasharray:1.7 1.2}
svg .dot{fill:#555}
svg .organ{fill:#f8bbd0;stroke:#ad1457;stroke-width:.85}
svg .organ2{fill:#f48fb1;stroke:#880e4f;stroke-width:.85}
svg .organ3{fill:#fce4ec;stroke:#ad1457;stroke-width:.8}
svg .lumen{fill:#fffafc;stroke:#c2185b;stroke-width:.7}
svg .hl{fill:#fff59d;stroke:#f9a825;stroke-width:.8}
svg .hl2{fill:#ffcc80;stroke:#ef6c00;stroke-width:.8}
svg .gr{fill:#c8e6c9;stroke:#2e7d32;stroke-width:.8}
svg .bl{fill:#bbdefb;stroke:#1565c0;stroke-width:.8}
svg .pu{fill:#e1bee7;stroke:#6a1b9a;stroke-width:.8}
svg .duct{stroke:#ad1457;stroke-width:2.6;fill:none;stroke-linecap:round}
""".replace("ARROWURL", ARROW)


def _inline(s: str, cls="") -> str:
    s = re.sub(r"\{\{(.+?)\}\}", r'<span class="k">(\1)</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s.replace("->", '<span class="ar"></span>')


def _items_ol(items):
    out = []
    for n, it in enumerate(items):
        out.append(f'<li><i>({ROMAN[n] if n < len(ROMAN) else n + 1})</i>{_inline(it)}</li>')
    return "<ol>" + "".join(out) + "</ol>"


def _items_ul(items, star=False):
    lead = '<span class="st"></span>' if star else ""
    return "<ul>" + "".join(f"<li>{lead}{_inline(it)}</li>" for it in items) + "</ul>"


def _block(b, idx):
    """Render one grid block. Palette cycles by section order."""
    pal = PALETTE[idx % len(PALETTE)]
    style = f"--c:{pal['c']};--bg:{pal['bg']};grid-column:span {b.get('span', 12)}"
    t = b["type"]

    if t == "sec":
        head = (f'<h3>{b["n"]}. {b["t"]}'
                + (f' <em>({b["en"]})</em>' if b.get("en") else "") + "</h3>")
        return f'<div class="blk" style="{style}">{head}{_items_ol(b["items"])}</div>'

    if t == "side":
        head = f'<h3>{b["t"]}' + (f' <em>({b["en"]})</em>' if b.get("en") else "") + "</h3>"
        return f'<div class="blk side" style="{style}">{head}{_items_ul(b["items"])}</div>'

    if t == "fig":
        return ('<div class="fig" style="{s}"><h4>{t}</h4><div class="wrap">{svg}</div>'
                '{cap}</div>').format(
            s=style, t=b["t"], svg=b["svg"],
            cap=f'<div class="cap">{b["cap"]}</div>' if b.get("cap") else "")

    if t == "facts":
        return ('<div class="facts" style="grid-column:span {sp}"><h3>{t}</h3>{ul}</div>').format(
            sp=b.get("span", 12), t=b.get("t", "महत्वपूर्ण तथ्य"),
            ul=_items_ul(b["items"], star=True))

    if t == "pyq":
        return ('<div class="pyq" style="grid-column:span {sp}"><h3>{t}</h3>{ul}</div>').format(
            sp=b.get("span", 12), t=b.get("t", "बोर्ड परीक्षा में पूछे गए प्रश्न"),
            ul="<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in b["items"]) + "</ul>")

    raise ValueError(f"unknown block type {t!r}")


def build_html(ch, fs=1.0) -> str:
    blocks = "".join(_block(b, i) for i, b in enumerate(ch["blocks"]))

    flow = ""
    if ch.get("flow"):
        chain = []
        for i, step in enumerate(ch["flow"]):
            alt = "" if i % 3 == 0 else (" alt" if i % 3 == 1 else " alt2")
            chain.append(f'<span class="pill{alt}">{step}</span>')
            if i != len(ch["flow"]) - 1:
                chain.append('<span class="ar"></span>')
        flow = ('<div class="flow"><h3>{t}</h3><div class="chain">{c}</div></div>').format(
            t=ch.get("flow_title") or "क्रमिक प्रक्रिया (Flow Chart)", c="".join(chain))

    return f"""<!doctype html><html lang="hi"><head><meta charset="utf-8">
<style>{fonts_css()}{CSS}</style><style>:root{{--fs:{fs}}}</style></head><body>
<div class="sheet">
  <div class="ttl">
    <h1>{ch['hi']} <span>({ch['en']})</span></h1>
    <div class="sub">UP Board (UPMSP) &middot; कक्षा 12 &middot; जीव विज्ञान 348 &middot; सत्र 2026&ndash;27
      &middot; इकाई {ch['unit_no']} &mdash; {ch['unit_name']} ({ch['unit_marks']} अंक)
      &middot; अध्याय {ch['num']}/13</div>
  </div>
  <div class="intro"><span class="st"></span><b>परिचय :&ndash;</b> {_inline(ch['intro'])}</div>
  <div class="grid">{blocks}</div>
  {flow}
  <div class="ftr"><span>अध्याय {ch['num']} &middot; {ch['hi']}</span>
    <span class="r">स्रोत: UPMSP आधिकारिक पाठ्यक्रम 2026&ndash;27 + प्रतिदर्श प्रश्नपत्र + बोर्ड प्रश्नपत्र 2020&ndash;2026</span></div>
</div></body></html>"""


def _overflow(page):
    return page.evaluate(
        """()=>{const s=document.querySelector('.sheet');
        let m=s.scrollHeight-s.clientHeight;
        const g=document.querySelector('.grid');
        m=Math.max(m,g.scrollHeight-g.clientHeight);
        for(const e of document.querySelectorAll('.blk,.fig,.facts,.pyq'))
            m=Math.max(m,e.scrollHeight-e.clientHeight);
        return m;}"""
    )


def autofit(page, ch, lo=0.60, hi=1.30, tol=0.007):
    best = lo
    for _ in range(10):
        mid = (lo + hi) / 2
        page.set_content(build_html(ch, mid))
        page.wait_for_timeout(110)
        if _overflow(page) <= 1:
            best, lo = mid, mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return best


def render(chapters, notify=None):
    for d in (OUT / "images", OUT / "pdf", BUILD):
        d.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright

    made = []
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        for ch in chapters:
            slug = "ch%02d_%s" % (ch["num"], ch["slug"])
            page = br.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=3)
            fs = autofit(page, ch)
            html = build_html(ch, fs)
            (BUILD / f"{slug}.html").write_text(html, encoding="utf-8")
            page.set_content(html)
            page.wait_for_timeout(320)
            over = _overflow(page)
            png, pdf = OUT / "images" / f"{slug}.png", OUT / "pdf" / f"{slug}.pdf"
            page.locator(".sheet").screenshot(path=str(png))
            page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
            page.close()
            flag = "  <-- OVERFLOW" if over > 1 else ""
            print(f"  ch{ch['num']:02d}  fs={fs:.3f}  over={over}px  {ch['hi'][:28]:<30}"
                  f"{png.stat().st_size // 1024:>5}KB{flag}")
            made.append((ch, png, pdf))
            if notify:
                notify(ch, png, pdf)
        br.close()
    return made


def merge(made):
    import pymupdf
    doc = pymupdf.open()
    for _, _, pdf in made:
        doc.insert_pdf(pymupdf.open(pdf))
    doc.set_metadata({
        "title": "UP Board Class 12 Biology (348) - Handwritten-style One Page Notes, 2026-27",
        "author": "Built from UPMSP official syllabus 2026-27, model paper and board papers 2020-2026",
        "subject": "Hindi medium handwritten-style revision sheets with labelled figures",
        "keywords": "UP Board, UPMSP, Class 12, Biology, 348, 2026-27, Hindi, notes, diagrams",
    })
    out = OUT / "UP_Board_Class12_Biology_Handwritten_Notes_AllChapters.pdf"
    doc.save(out, deflate=True)
    print(f"\n  merged -> {out.relative_to(ROOT)} "
          f"({out.stat().st_size // 1024} KB, {doc.page_count} pages)")
    return out


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    from content_hw import CHAPTERS_HW
    only = set(sys.argv[1:])
    chs = [c for c in CHAPTERS_HW if not only or str(c["num"]) in only]
    print(f"rendering {len(chs)} handwritten sheet(s) of {len(CHAPTERS_HW)}...")
    made = render(chs)
    if len(chs) == len(CHAPTERS_HW):
        merge(made)
    else:
        print("\n  (subset render: merged PDF left untouched)")
