import streamlit as st
from utils import generate_story

st.header("🎭 Tell stories by different characters")

with st.sidebar:
    openai_api_key = st.text_input("Please enter your OpenAI API key", type="password")
    st.markdown("[How to get OpenAI API key](https://platform.openai.com/account/api-keys)")

identity = st.text_input("Please enter the identity of the storyteller (e.g. actor, chef, samurai, scientist, etc.)")
theme = st.text_input("background for the story")
submit = st.button("Start creating")

if submit and not openai_api_key:
    st.info("Please enter your OpenAI API key")
    st.stop()
if submit and not theme:
    st.info("Please enter one sentence for the story background")
    st.stop()
if submit and not identity:
    st.info("Please enter storyteller identity")
    st.stop()

if submit:
    with st.spinner("AI is working hard to create, please wait..."):
        result = generate_story(theme, identity, openai_api_key)
    st.divider()
    st.markdown(f"<h2 style='text-align: center'>{result.title}</h2>", unsafe_allow_html=True)
    st.write(result.content)

