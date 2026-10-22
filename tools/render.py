"""
Renders one-page coloured revision notes (Hindi medium) for UP Board Class 12 Biology.

Output per chapter:  PNG (notes/images/) + PDF (notes/pdf/)
Plus a merged all-chapter PDF.

Guarantees "1 chapter = 1 page": the page is a fixed A4 portrait box and an
auto-fit loop searches for the largest font scale at which the content still
fits, so each sheet is both single-page and well filled.

Neither Noto Sans nor Noto Sans Devanagari ships arrow/star glyphs, so those
are drawn in CSS/SVG instead of typed as characters.
"""
import os
import re
import sys
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "_work" / "fonts"
OUT_IMG = ROOT / "notes" / "images"
OUT_PDF = ROOT / "notes" / "pdf"
BUILD = ROOT / "_work" / "build"

THEMES = {
    "u6":  dict(main="#1b7f4d", dark="#0f5c36", light="#e7f6ee", accent="#ffa000", band="#d3f0e0"),
    "u7":  dict(main="#1152a3", dark="#0b3a76", light="#e8f1fb", accent="#f4511e", band="#d2e4f8"),
    "u8":  dict(main="#b3261e", dark="#8a1a14", light="#fdecea", accent="#2e7d32", band="#f9d9d6"),
    "u9":  dict(main="#6a1b9a", dark="#4a148c", light="#f4eafa", accent="#00897b", band="#e8d5f3"),
    "u10": dict(main="#00695c", dark="#004d40", light="#e4f4f1", accent="#ef6c00", band="#cfe9e4"),
}

ARROW_SVG = (
    "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2026%2012'"
    "%3E%3Cpath%20d='M1%206h19M16%201.5l5%204.5-5%204.5'%20fill='none'%20stroke='%231c2b3a'"
    "%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'/%3E%3C/svg%3E"
)


def font_face_css() -> str:
    css = []
    for fam, fname in [("NotoDeva", "NotoSansDevanagari.ttf")]:
        p = FONT_DIR / fname
        if not p.exists():
            raise SystemExit(f"missing font: {p}")
        b64 = base64.b64encode(p.read_bytes()).decode()
        css.append(
            "@font-face{font-family:'%s';src:url(data:font/truetype;base64,%s) "
            "format('truetype');font-weight:100 900;font-display:block;}" % (fam, b64)
        )
    return "".join(css)


BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4 portrait;margin:0}
:root{--fs:1}
html{font-size:calc(var(--fs) * 1px)}
body{width:210mm;font-family:'NotoDeva','Noto Sans',sans-serif;-webkit-font-smoothing:antialiased}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;
      display:flex;flex-direction:column}
/* ---------- arrow + diamond (font has no glyph for these) ---------- */
.ar{display:inline-block;width:3.1mm;height:1.8mm;vertical-align:-0.1mm;margin:0 .25mm;
    background:no-repeat center/contain url("ARROWURL")}
/* ---------- header ---------- */
.hdr{background:linear-gradient(100deg,var(--dark),var(--main) 58%,var(--accent) 170%);
     color:#fff;padding:3.1mm 4mm 2.8mm;display:flex;align-items:center;gap:3.2mm}
.chno{flex:0 0 auto;width:12.4mm;height:12.4mm;border-radius:50%;background:#fff;
      color:var(--dark);display:flex;align-items:center;justify-content:center;
      font-size:20rem;font-weight:800;box-shadow:0 0 0 1.1mm rgba(255,255,255,.28)}
.htxt{flex:1 1 auto;min-width:0}
.htxt h1{font-size:25rem;line-height:1.1;font-weight:800}
.htxt .en{font-size:12rem;opacity:.93;font-weight:600;margin-top:.6mm;
          font-family:'Noto Sans',sans-serif}
.hmk{flex:0 0 auto;text-align:center;background:rgba(255,255,255,.17);
     border:.35mm solid rgba(255,255,255,.5);border-radius:1.6mm;padding:1.4mm 2.6mm}
.hmk b{display:block;font-size:21rem;line-height:1}
.hmk span{font-size:9rem;opacity:.95}
/* ---------- unit strip ---------- */
.strip{background:var(--band);color:var(--dark);padding:1.5mm 4mm;display:flex;
       align-items:center;gap:2.4mm;font-size:9.4rem;font-weight:700;white-space:nowrap;
       border-bottom:.4mm solid var(--main)}
.strip .tag{background:var(--main);color:#fff;border-radius:1mm;padding:.45mm 1.6mm;font-size:9rem}
.strip .sp{margin-left:auto;font-weight:600;opacity:.85;font-size:8.6rem}
/* ---------- body ---------- */
.body{flex:1 1 auto;display:flex;gap:2.4mm;padding:2.4mm 3.2mm 0;min-height:0}
.colA{flex:0 0 57%;display:flex;flex-direction:column;gap:1.8mm;min-height:0;
      justify-content:space-between}
.colB{flex:1 1 auto;display:flex;flex-direction:column;gap:1.8mm;min-height:0;
      justify-content:space-between}
/* keep natural height so a too-full page really overflows and autofit can see it */
.box,.must,.pyq,.dia{flex-shrink:0}
/* ---------- concept box ---------- */
.box{border:.32mm solid var(--main);border-radius:1.5mm;overflow:hidden;background:#fff}
.box>h3{background:var(--light);color:var(--dark);font-size:12rem;font-weight:800;
        padding:1.05mm 2mm;border-bottom:.3mm dashed var(--main);
        display:flex;align-items:baseline;gap:1.5mm}
.box>h3 em{font-style:normal;font-size:9rem;font-weight:600;opacity:.72;
           font-family:'Noto Sans',sans-serif}
.box ul{list-style:none;padding:1.2mm 2mm 1.4mm}
.box li{font-size:11.2rem;line-height:1.42;padding-left:2.9mm;position:relative;
        margin-bottom:.5mm}
.box li:before{content:"";position:absolute;left:.55mm;top:1.5mm;width:1.3mm;height:1.3mm;
               border-radius:50%;background:var(--accent)}
.box li b{color:var(--dark);font-weight:800}
.box li .k{font-family:'Noto Sans',sans-serif;font-size:9.6rem;opacity:.72;font-weight:600}
/* ---------- diagram card ---------- */
.dia{border:.42mm solid var(--dark);border-radius:1.5mm;background:#fff;
     display:flex;flex-direction:column}
.dia>h3{background:var(--dark);color:#fff;font-size:11.4rem;font-weight:800;padding:1.1mm 2mm;
        display:flex;align-items:center;gap:1.5mm}
.dia>h3 .pill{background:var(--accent);color:#17120a;border-radius:4mm;padding:.3mm 1.6mm;
              font-size:9rem;font-weight:800;margin-left:auto;white-space:nowrap}
.dia .svgwrap{padding:1.2mm;display:flex;align-items:center;justify-content:center;flex:1 1 auto}
.dia svg{width:100%;height:auto;display:block}
.dia .cap{font-size:9.4rem;text-align:center;padding:0 1.6mm 1.2mm;color:#333;line-height:1.32}
/* ---------- must-know ---------- */
.must{border:.32mm solid var(--accent);border-left:1.4mm solid var(--accent);
      border-radius:1.2mm;background:#fffdf5;padding:1.3mm 2mm}
.must h4{font-size:11.2rem;color:#8a5a00;font-weight:800;margin-bottom:.6mm}
.must ul{list-style:none}
.must li{font-size:10.8rem;line-height:1.4;padding-left:2.8mm;position:relative;margin-bottom:.35mm}
.must li:before{content:"";position:absolute;left:.3mm;top:1.5mm;width:1.4mm;height:1.4mm;
                background:var(--accent);transform:rotate(45deg)}
.must li b{color:#7a4f00;font-weight:800}
.must li .k{font-family:'Noto Sans',sans-serif;font-size:9.4rem;opacity:.72;font-weight:600}
/* ---------- pyq box ---------- */
.pyq{border:.32mm solid var(--main);border-radius:1.2mm;background:var(--light);padding:1.3mm 2mm}
.pyq h4{font-size:11.2rem;color:var(--dark);font-weight:800;margin-bottom:.6mm}
.pyq ul{list-style:none}
.pyq li{font-size:10.4rem;line-height:1.38;padding-left:3mm;position:relative;margin-bottom:.3mm}
.pyq li:before{content:"\\203A";position:absolute;left:.4mm;top:-.1mm;
               color:var(--main);font-weight:800}
.pyq li i{font-style:normal;background:var(--main);color:#fff;border-radius:.8mm;
          padding:0 1mm;font-size:9rem;font-weight:700;margin-right:.8mm;
          font-family:'Noto Sans',sans-serif}
.pyq li b{color:var(--dark);font-weight:800}
/* ---------- footer ---------- */
.ftr{flex:0 0 auto;background:var(--dark);color:#fff;font-size:8.6rem;
     padding:1.35mm 4mm;display:flex;align-items:center;gap:2.5mm}
.ftr .r{margin-left:auto;opacity:.9;font-size:8rem}
/* ---------- svg helpers ---------- */
svg text{font-family:'NotoDeva','Noto Sans',sans-serif}
svg .lb{font-size:8.4px;font-weight:700;fill:#14202e}
svg .lbs{font-size:7.2px;font-weight:600;fill:#2b3a4d}
svg .lbt{font-size:8.6px;font-weight:800}
svg .lbw{font-size:8px;font-weight:800;fill:#fff}
svg .ld{stroke:#3c4a5a;stroke-width:.65;fill:none}
svg .ldd{stroke:#3c4a5a;stroke-width:.6;fill:none;stroke-dasharray:1.8 1.2}
svg .dot{fill:#3c4a5a}
""".replace("ARROWURL", ARROW_SVG)


def li(items):
    out = []
    for it in items:
        it = re.sub(r"\{\{(.+?)\}\}", r'<span class="k">\1</span>', it)
        it = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", it)
        it = it.replace("->", '<span class="ar"></span>')
        out.append(f"<li>{it}</li>")
    return "".join(out)


def build_html(ch, fs=1.0) -> str:
    th = THEMES[ch["theme"]]
    varcss = ";".join(f"--{k}:{v}" for k, v in th.items())

    boxes = "".join(
        '<div class="box"><h3>{t}{en}</h3><ul>{items}</ul></div>'.format(
            t=b["t"], en=f"<em>{b['en']}</em>" if b.get("en") else "", items=li(b["items"])
        ) for b in ch["boxes"]
    )
    dias = "".join(
        '<div class="dia"><h3>{t}<span class="pill">{pill}</span></h3>'
        '<div class="svgwrap">{svg}</div><div class="cap">{cap}</div></div>'.format(
            t=d["t"], pill=d.get("pill", "अति महत्वपूर्ण"), svg=d["svg"], cap=d["cap"]
        ) for d in ch["diagrams"]
    )
    must = ('<div class="must"><h4>%s</h4><ul>%s</ul></div>'
            % (ch.get("must_title", "रटने योग्य तथ्य (Must-remember)"), li(ch["must"]))
            if ch.get("must") else "")
    pyq = ('<div class="pyq"><h4>बोर्ड परीक्षा में पूछे गए (PYQ 2020&ndash;2026 + प्रतिदर्श पत्र)</h4><ul>%s</ul></div>'
           % li(ch["pyq"]) if ch.get("pyq") else "")

    return f"""<!doctype html><html lang="hi"><head><meta charset="utf-8">
<style>{font_face_css()}{BASE_CSS}</style><style>:root{{--fs:{fs}}}</style></head><body>
<div class="page" style="{varcss}">
  <div class="hdr">
    <div class="chno">{ch['num']}</div>
    <div class="htxt"><h1>{ch['hi']}</h1><div class="en">{ch['en']}</div></div>
    <div class="hmk"><b>{ch['unit_marks']}</b><span>अंक / इकाई</span></div>
  </div>
  <div class="strip">
    <span class="tag">{ch['unit']}</span><span>{ch['unit_name']}</span>
    <span class="sp">UP Board (UPMSP) &middot; कक्षा 12 &middot; जीव विज्ञान (348) &middot; सत्र 2026&ndash;27 &middot; लिखित 70 + प्रायोगिक 30</span>
  </div>
  <div class="body">
    <div class="colA">{boxes}</div>
    <div class="colB">{dias}{must}{pyq}</div>
  </div>
  <div class="ftr">
    <span>अध्याय {ch['num']} / 13 &nbsp;&middot;&nbsp; {ch['hi']}</span>
    <span class="r">स्रोत: UPMSP आधिकारिक पाठ्यक्रम 2026&ndash;27 + प्रतिदर्श प्रश्नपत्र + बोर्ड प्रश्नपत्र 2020&ndash;2026</span>
  </div>
</div></body></html>"""


def _overflow(page):
    return page.evaluate(
        """()=>{const b=document.querySelector('.body');
        let m=b.scrollHeight-b.clientHeight;
        for(const c of document.querySelectorAll('.colA,.colB'))
            m=Math.max(m,c.scrollHeight-c.clientHeight);
        return m;}"""
    )


def autofit(page, ch, lo=0.80, hi=1.34, tol=0.008):
    """Largest font scale whose content still fits one A4 page."""
    best = lo
    for _ in range(9):
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
    for d in (OUT_IMG, OUT_PDF, BUILD):
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
            page.wait_for_timeout(300)
            over = _overflow(page)

            png, pdf = OUT_IMG / f"{slug}.png", OUT_PDF / f"{slug}.pdf"
            page.locator(".page").screenshot(path=str(png))
            page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
            page.close()

            flag = "  <-- OVERFLOW" if over > 1 else ""
            print(f"  ch{ch['num']:02d}  fs={fs:.3f}  over={over}px  "
                  f"{ch['hi'][:30]:<32}{png.stat().st_size//1024:>5}KB png{flag}")
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
        "title": "UP Board Class 12 Biology (348) - One Page Chapter Notes, Hindi Medium, 2026-27",
        "author": "Built from UPMSP official syllabus 2026-27, model paper and board papers 2020-2026",
        "subject": "One-page coloured revision notes with exam-priority labelled diagrams",
        "keywords": "UP Board, UPMSP, Class 12, Biology, 348, 2026-27, Hindi medium, notes, diagrams, PYQ",
    })
    out = ROOT / "notes" / "UP_Board_Class12_Biology_OnePage_Notes_AllChapters.pdf"
    doc.save(out, deflate=True)
    print(f"\n  merged -> {out.relative_to(ROOT)}  "
          f"({out.stat().st_size//1024} KB, {doc.page_count} pages)")
    return out


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    from content import CHAPTERS
    only = set(sys.argv[1:])
    chs = [c for c in CHAPTERS if not only or str(c["num"]) in only]
    print(f"rendering {len(chs)} chapter(s) of {len(CHAPTERS)}...")
    made = render(chs)
    if len(chs) == len(CHAPTERS):
        merge(made)
    else:
        print("\n  (subset render: merged all-chapter PDF left untouched)")
