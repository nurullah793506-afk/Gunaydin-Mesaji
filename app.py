import streamlit as st
import random

# Uygulama Teması ve Başlığı
st.set_page_config(page_title="Günün Sürprizi", page_icon="❤️ 🩺")

st.title("🌸 Günaydın Güzelim 🌸")


# Soru Havuzu (Tıp + Romantizm + Kişisel)
if 'soru_no' not in st.session_state:
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
        "mesaj": "Kuşlarımızın cıvıltısı kadar neşeli bir gün 🐦"
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
        "mesaj": "Bilgin taze, zihnin ışıl ışıl ✨"
    }
]


},
    ]
    st.session_state.soru_no = random.randint(0, len(questions) - 1)
    st.session_state.questions = questions

soru = st.session_state.questions[st.session_state.soru_no]

st.write(f"### 📝 Günün Sorusu:")
st.info(soru["soru"])

cevap = st.text_input("Buraya yazabilirsin:").strip().lower()

if st.button("Sürprizi Aç 🎁"):
    if soru["cevap"].lower() in cevap:
        st.balloons()
        st.success(soru["odul"])
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1ZjR4N3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3VfW2WME/giphy.gif")
    else:
        st.st.warning("Hımm, biraz daha düşünmen gerekebilir mi? 💭")


