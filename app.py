import streamlit as st
import json
import random
from datetime import datetime, time, timedelta, timezone
from pathlib import Path

# ------------------ SABİT AYARLAR ------------------
ACILIS_SAATI = time(1, 23)    # 01:00
KAPANIS_SAATI = time(12, 0)  # 12:00
GUNLUK_SORU_LIMITI = 3

QUESTIONS_FILE = "questions.json"
MESSAGES_FILE = "messages.json"
ASKED_FILE = "asked_questions.json"
USED_MSG_FILE = "used_messages.json"

# ------------------ YARDIMCI FONKSİYONLAR ------------------
def load_json(path, default):
    if not Path(path).exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=False, indent=2)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def turkiye_saati():
    tr_tz = timezone(timedelta(hours=3))
    return datetime.now(tr_tz)

def saat_uygun_mu():
    simdi = turkiye_saati().time()
    return ACILIS_SAATI <= simdi <= KAPANIS_SAATI

# ------------------ VERİLER ------------------
questions = load_json(QUESTIONS_FILE, [])
messages = load_json(MESSAGES_FILE, [])
asked_questions = load_json(ASKED_FILE, [])
used_messages = load_json(USED_MSG_FILE, [])

# ------------------ SAAT KONTROL ------------------
if not saat_uygun_mu():
    st.warning("⏰ Bu uygulama sadece sabah saatlerinde aktif.")
    st.stop()

# ------------------ GÜNLÜK OTURUM ------------------
today = turkiye_saati().date().isoformat()

if "today" not in st.session_state:
    st.session_state.today = today
    st.session_state.asked_today = 0
    st.session_state.current_question = None

if st.session_state.today != today:
    st.session_state.today = today
    st.session_state.asked_today = 0
    st.session_state.current_question = None

if st.session_state.asked_today >= GUNLUK_SORU_LIMITI:
    st.success("🎉 Bugünün tüm sorularını tamamladın!")
    st.stop()

# ------------------ SORU SEÇ ------------------
if st.session_state.current_question is None:
    kalan_sorular = [q for q in questions if q["id"] not in asked_questions]
    if not kalan_sorular:
        st.success("🎉 Tüm sorular bitti!")
        st.stop()
    st.session_state.current_question = random.choice(kalan_sorular)

q = st.session_state.current_question

# ------------------ UI ------------------
st.title("💖 Günaydın Aşkım")
st.subheader(q["question"])

cevap = st.radio("Seç:", q["options"], key="answer")

if st.button("Cevapla"):
    if cevap == q["answer"]:
        asked_questions.append(q["id"])
        save_json(ASKED_FILE, asked_questions)

        kalan_mesajlar = [m for m in messages if m not in used_messages]
        if kalan_mesajlar:
            mesaj = random.choice(kalan_mesajlar)
            used_messages.append(mesaj)
            save_json(USED_MSG_FILE, used_messages)
            st.success(mesaj)

        st.session_state.asked_today += 1
        st.session_state.current_question = None
        st.rerun()
    else:
        st.error("❌ Yanlış ama vazgeçmek yok, tekrar dene 💪")
