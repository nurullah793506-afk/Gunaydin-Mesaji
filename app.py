import streamlit as st
import json
import os
from datetime import datetime, time

# =========================
# AYARLAR
# =========================
ACILIS_SAATI = time(1, 19)
KAPANIS_SAATI = time(11, 0)

QUESTIONS_FILE = "questions.json"
MESSAGES_FILE = "messages.json"
USED_QUESTIONS_FILE = "used_questions.json"
USED_MESSAGES_FILE = "used_messages.json"


# =========================
# YARDIMCI FONKSİYONLAR
# =========================
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=False, indent=2)
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def saat_uygun_mu():
    simdi = datetime.now().time()
    return ACILIS_SAATI <= simdi <= KAPANIS_SAATI


# =========================
# VERİLERİ YÜKLE
# =========================
questions = load_json(QUESTIONS_FILE, [])
messages = load_json(MESSAGES_FILE, [])

used_questions = load_json(USED_QUESTIONS_FILE, [])
used_messages = load_json(USED_MESSAGES_FILE, [])


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Günaydın ☀️", page_icon="☀️")
st.title("☀️ Günaydın Oyunu")

if not saat_uygun_mu():
    st.warning("⏰ Bu uygulama sadece sabah saatlerinde aktif.")
    st.stop()


# =========================
# KALAN SORULAR
# =========================
kalan_sorular = [q for q in questions if q["id"] not in used_questions]

if not kalan_sorular:
    st.success("🎉 Bugünün tüm sorularını tamamladın!")
    st.stop()


# =========================
# SESSION STATE
# =========================
if "question_id" not in st.session_state:
    st.session_state.question_id = kalan_sorular[0]["id"]

q = next(q for q in questions if q["id"] == st.session_state.question_id)

st.subheader("💬 Soru")
st.write(q["question"])

answer = st.text_input("Cevabın", key="answer_input")


# =========================
# CEVAP KONTROL
# =========================
if st.button("Cevabı Gönder"):
    if answer.strip().lower() == q["answer"].strip().lower():

        # soru kullanıldı
        used_questions.append(q["id"])
        save_json(USED_QUESTIONS_FILE, used_questions)

        # mesaj seç
        kalan_mesajlar = [m for m in messages if m["id"] not in used_messages]

        st.success("✅ Doğru cevap!")

        if kalan_mesajlar:
            mesaj = kalan_mesajlar[0]
            used_messages.append(mesaj["id"])
            save_json(USED_MESSAGES_FILE, used_messages)

            st.markdown(f"💖 **{mesaj['text']}**")
        else:
            st.info("💌 Tüm romantik mesajlar kullanıldı.")

        # yeni soru hazırla
        yeni_kalanlar = [q for q in questions if q["id"] not in used_questions]
        if yeni_kalanlar:
            st.session_state.question_id = yeni_kalanlar[0]["id"]
            st.session_state.answer_input = ""
        else:
            del st.session_state.question_id

    else:
        st.error("❌ Yanlış cevap, bir daha dene.")
