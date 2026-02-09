import streamlit as st
import random

# Sayfa ayarları
st.set_page_config(
    page_title="Günün Sürprizi",
    page_icon="❤️"
)

st.title("🌸 Günaydın Güzelim 🌸")

# Soru havuzu
questions = [
    {
        "soru": "Acil serviste 'akut koroner sendrom' şüphesiyle gelen hastada çekilmesi gereken ilk tetkik nedir?",
        "secenekler": ["EKG", "Akciğer Grafisi", "Kan Gazı"],
        "dogru": "EKG",
        "mesaj": "Tıpkı bu EKG gibi, kalbim seninle her an ritim tutuyor ❤️"
    },
    {
        "soru": "Diş Zikzik ve Erkek Zikziğin en sevdiği meyve/sebze nedir?",
        "secenekler": ["Elma", "Havuç", "Maydanoz"],
        "dogru": "Maydanoz",
        "mesaj": "Kuşlarımızın cıvıltısı kadar neşeli bir günün olsun 🐦"
    },
    {
        "soru": "EKG'de 'testere dişi' görünümü hangi ritim bozukluğuna işaret eder?",
        "secenekler": ["Atrial Fibrilasyon", "Atrial Flutter", "Ventriküler Taşikardi"],
        "dogru": "Atrial Flutter",
        "mesaj": "Kalbin ritmi gibi günün de harika aksın 💓"
    },
    {
        "soru": "Yenidoğanlarda K vitamini eksikliğine bağlı kanamayı önlemek için hangi kas içine enjeksiyon yapılır?",
        "secenekler": ["M. Deltoideus", "M. Gluteus Maximus", "M. Vastus Lateralis"],
        "dogru": "M. Vastus Lateralis",
        "mesaj": "Bilgin taze, zihnin benimle dolsun ✨"
    }
]

# Session state
if "soru_no" not in st.session_state:
    st.session_state.soru_no = random.randint(0, len(questions) - 1)

soru = questions[st.session_state.soru_no]

st.subheader("📝 Günün Sorusu")
st.info(soru["soru"])

# Cevap girişi
cevap = st.text_input("Cevabını yaz:").strip().lower()

# Buton
if st.button("Sürprizi Aç 🎁"):
    if soru["dogru"].lower() in cevap:
        st.balloons()
        st.success(soru["mesaj"])
        st.image(
            "https://media.giphy.com/media/l41lTfuxV3VfW2WME/giphy.gif"
        )
    else:
        st.warning("Hımm, biraz daha düşünmen gerekebilir mi? 💭")
