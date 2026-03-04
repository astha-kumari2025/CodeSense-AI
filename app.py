import streamlit as st
from utils.ai_explainer import explain_code

st.set_page_config(page_title="CodeSense AI", page_icon="🤖")

st.title(" CodeSense AI")
st.subheader("AI That Makes Code Make Sense")

code = st.text_area("Paste your code here", height=200)

if st.button("Explain Code"):

    if code.strip() != "":
        explanation = explain_code(code)

        st.subheader("Explanation")
        st.write(explanation)

    else:
        st.warning("Please paste some code first.")
