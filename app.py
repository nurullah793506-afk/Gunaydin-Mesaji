import streamlit as st
import json
import random
from datetime import datetime
import pytz
import os

# =====================
# AYARLAR
# =====================
START_HOUR = 00
START_MINUTE = 46
QUESTIONS_PER_DAY = 3
TIMEZONE = "Europe/Istanbul"

QUESTIONS_FILE = "questions.json"
MESSAGES_FILE = "messages.json"
STATE_FILE = "state.json"

# =====================
# YARDIMCI FONKSİYONLAR
# =====================
def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# =====================
# ZAMAN KONTROLÜ
# =====================
tz = pytz.timezone(TIMEZONE)
now = datetime.now(tz)

start_time = now.replace(
    hour=START_HOUR,
    minute=START_MINUTE,
    second=0,
    microsecond=0
)

if now < start_time:
    st.title("🌸 Günaydın Güzelim 🌸")
    st.info(f"⏰ Günün sürprizi saat {START_HOUR:02d}:{START_MINUTE:02d}'da açılacak 💖")
    st.stop()

# =====================
# VERİLERİ YÜKLE
# =====================
questions = load_json(QUESTIONS_FILE, [])
messages = load_json(MESSAGES_FILE, [])

state = load_json(STATE_FILE, {
    "asked_questions": [],
    "used_messages": [],
    "today": now.date().isoformat(),
    "today_questions": [],
    "current_index": 0
})

# =====================
# GÜN DEĞİŞTİYSE RESET
# =====================
if state["today"] != now.date().isoformat():
    available = [q for q in questions if q["id"] not in state["asked_questions"]]
    daily = random.sample(available, min(QUESTIONS_PER_DAY, len(available)))

    state["today"] = now.date().isoformat()
    state["today_questions"] = [q["id"] for q in daily]
    state["current_index"] = 0
    save_json(STATE_FILE, state)

# =====================
# SORU BİTTİ Mİ?
# =====================
if state["current_index"] >= len(state["today_questions"]):
    st.success("🎉 Bugünün tüm sorularını tamamladın!")
    st.stop()

# =====================
# AKTİF SORU
# =====================
q_id = state["today_questions"][state["current_index"]]
question = next(q for q in questions if q["id"] == q_id)

st.title("🌸 Günaydın Güzelim 🌸")
st.subheader(f"🧠 Soru {state['current_index'] + 1} / {len(state['today_questions'])}")
st.write(question["soru"])

choice = st.radio(
    "Cevabını seç:",
    question["secenekler"],
    key=f"q_{q_id}"
)

# =====================
# CEVAP KONTROL
# =====================
if st.button("Cevabı Gönder 💌"):
    if choice == question["dogru"]:
        st.balloons()

        unused_messages = [
            m for m in messages if m["id"] not in state["used_messages"]
        ]

        if unused_messages:
            msg = random.choice(unused_messages)
            st.success(msg["text"])
            state["used_messages"].append(msg["id"])

        state["asked_questions"].append(q_id)
        state["current_index"] += 1
        save_json(STATE_FILE, state)
        st.experimental_rerun()
    else:
        st.warning("💭 Olmadı… bir daha dene, biliyorsun 💖")
