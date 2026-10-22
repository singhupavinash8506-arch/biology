#!/usr/bin/env python3
"""
Telegram progress notifier for the notes build.

Credentials are read from the environment (never hard-coded, never committed):
    TELEGRAM_BOT_TOKEN   the bot token from @BotFather
    TELEGRAM_CHAT_ID     your numeric chat id (get it from @userinfobot)

Usage
-----
    # 1. one-off connectivity test
    export TELEGRAM_BOT_TOKEN=...   TELEGRAM_CHAT_ID=...
    python tools/notify_telegram.py --test

    # 2. build all 13 sheets and ping Telegram after each chapter,
    #    attaching that chapter's PNG
    python tools/notify_telegram.py --build

If the two variables are not set, the script explains what is missing and exits
without touching the network.
"""
import argparse
import json
import mimetypes
import os
import pathlib
import sys
import urllib.error
import urllib.request
import uuid

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://api.telegram.org/bot{token}/{method}"


def _first_env(*names):
    """First non-empty value among the given variable names."""
    for n in names:
        v = os.environ.get(n, "").strip()
        if v:
            return v, n
    return "", None


def creds():
    token, tname = _first_env("TELEGRAM_BOT_TOKEN", "BOT_TOKEN")
    chat, cname = _first_env("TELEGRAM_CHAT_ID", "CHAT_ID", "ID")
    if not token or not chat:
        print("Telegram credentials not found in the environment.")
        print("\nAccepted variable names (first match wins):")
        print("    token : TELEGRAM_BOT_TOKEN, BOT_TOKEN")
        print("    chat  : TELEGRAM_CHAT_ID, CHAT_ID, ID")
        print("\nSet them and re-run, for example:")
        print("    export BOT_TOKEN='123456:ABC-DEF...'")
        print("    export ID='987654321'")
        print("\nBot token comes from @BotFather; chat id from @userinfobot.")
        print("Send /start to your bot once, otherwise Telegram blocks the first message.")
        sys.exit(2)
    print(f"  [telegram] using token from ${tname}, chat id from ${cname}")
    return token, chat


def _post(token, method, fields, files=None, timeout=60):
    """multipart/form-data POST with no third-party dependencies."""
    boundary = uuid.uuid4().hex
    body = bytearray()
    for k, v in fields.items():
        body += f"--{boundary}\r\n".encode()
        body += f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode()
        body += f"{v}\r\n".encode()
    for k, path in (files or {}).items():
        p = pathlib.Path(path)
        ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
        body += f"--{boundary}\r\n".encode()
        body += (f'Content-Disposition: form-data; name="{k}"; '
                 f'filename="{p.name}"\r\n').encode()
        body += f"Content-Type: {ctype}\r\n\r\n".encode()
        body += p.read_bytes() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        API.format(token=token, method=method), data=bytes(body),
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        return {"ok": False, "error": f"HTTP {e.code}", "detail": detail}
    except Exception as e:                                    # noqa: BLE001
        return {"ok": False, "error": repr(e)}


def send_message(token, chat, text):
    return _post(token, "sendMessage",
                 {"chat_id": chat, "text": text, "parse_mode": "HTML",
                  "disable_web_page_preview": "true"})


def send_photo(token, chat, caption, image):
    return _post(token, "sendPhoto",
                 {"chat_id": chat, "caption": caption[:1024], "parse_mode": "HTML"},
                 {"photo": image})


def send_document(token, chat, caption, path):
    return _post(token, "sendDocument",
                 {"chat_id": chat, "caption": caption[:1024], "parse_mode": "HTML"},
                 {"document": path})


def _report(label, res):
    if res.get("ok"):
        print(f"  [telegram] {label}: sent")
    else:
        print(f"  [telegram] {label}: FAILED -> "
              f"{res.get('error') or res.get('description')} {res.get('detail','')}")
    return bool(res.get("ok"))


def cmd_test(token, chat):
    res = send_message(token, chat,
        "<b>UP Board Class 12 Biology — notes builder</b>\n"
        "Test message. Connection is working.\n\n"
        "You will get one update per chapter as the one-page notes are built.")
    ok = _report("test message", res)
    if not ok:
        print("\nCommon causes: wrong chat id, or you have not sent /start to the bot yet.")
    sys.exit(0 if ok else 1)


def cmd_build(token, chat):
    sys.path.insert(0, str(ROOT / "tools"))
    import render
    from content import CHAPTERS

    _report("build start", send_message(token, chat,
        "<b>Build started</b> — UP Board Class 12 Biology (348), सत्र 2026-27\n"
        f"13 chapters, one coloured A4 sheet each (PNG + PDF)."))

    done = {"n": 0}

    def notify(ch, png, pdf):
        done["n"] += 1
        cap = (f"<b>[{done['n']}/13] अध्याय {ch['num']}: {ch['hi']}</b>\n"
               f"{ch['en']}\n"
               f"{ch['unit']} — {ch['unit_name']} ({ch['unit_marks']} अंक)\n"
               f"चित्र: {', '.join(d['t'] for d in ch['diagrams'])}\n"
               f"PNG {png.stat().st_size // 1024} KB  ·  PDF {pdf.stat().st_size // 1024} KB")
        _report(f"ch{ch['num']:02d} photo", send_photo(token, chat, cap, png))

    made = render.render(CHAPTERS, notify=notify)
    merged = render.merge(made)

    _report("merged pdf", send_document(token, chat,
        "<b>सभी 13 अध्याय पूर्ण</b> — संयुक्त एक-पृष्ठीय नोट्स (हिंदी माध्यम)\n"
        "स्रोत: UPMSP आधिकारिक पाठ्यक्रम 2026-27 + प्रतिदर्श प्रश्नपत्र + बोर्ड प्रश्नपत्र 2020-2026",
        merged))
    _report("build done", send_message(token, chat, "<b>Build complete.</b> All 13 chapters done."))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--test", action="store_true", help="send a single test message and exit")
    g.add_argument("--build", action="store_true",
                   help="render all 13 chapters, notifying after each one")
    a = ap.parse_args()
    t, c = creds()
    cmd_test(t, c) if a.test else cmd_build(t, c)
