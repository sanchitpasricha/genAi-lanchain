import streamlit as st
import random

# Sample vocabulary list
vocab_list = [
    {
        "word": "Ephemeral",
        "definition": "Lasting for a very short time.",
        "example": "Fame in the world of pop music can be ephemeral."
    },
    {
        "word": "Serendipity",
        "definition": "The occurrence of events by chance in a happy or beneficial way.",
        "example": "Meeting her was pure serendipity."
    },
    {
        "word": "Ineffable",
        "definition": "Too great or extreme to be expressed in words.",
        "example": "The ineffable beauty of the canyon left them speechless."
    },
    {
        "word": "Eloquent",
        "definition": "Fluent or persuasive in speaking or writing.",
        "example": "She gave an eloquent speech on environmental policy."
    },
    {
        "word": "Petrichor",
        "definition": "A pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather.",
        "example": "The petrichor made him nostalgic for his childhood."
    },
]

st.set_page_config(page_title="📖 Word of the Day", layout="centered")
st.title("📖 Word of the Day")

if st.button("🔄 Get New Word"):
    word = random.choice(vocab_list)
    st.subheader(f"**{word['word']}**")
    st.write(f"**Definition:** {word['definition']}")
    st.write(f"**Example:** _{word['example']}_")
else:
    st.info("Click the button to discover a new word!")

st.caption("Improve your vocabulary, one word at a time.")
