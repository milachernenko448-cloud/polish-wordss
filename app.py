import streamlit as st
import random

words = [
    {"word": "kot", "translation": "кіт", "example": "To jest mój kot."},
    {"word": "pies", "translation": "собака", "example": "Mój pies lubi spać."},
    {"word": "szkoła", "translation": "школа", "example": "Idę do szkoły."},
    {"word": "dom", "translation": "дім", "example": "Mój dom jest duży."}
]

st.title("📚 Polish Word of the Day")
word = random.choice(words)
st.subheader(word["word"])
st.write(f"**Переклад:** {word['translation']}")
st.write(f"**Приклад:** {word['example']}")
if st.button("🔁 Наступне слово"):
    st.experimental_rerun()
