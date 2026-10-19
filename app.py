import streamlit as st
import pandas as pd
from copilot_logic import answer_question

st.set_page_config(page_title="Seller Support Copilot", page_icon=":package:")
st.title("AI Seller Support Copilot")
st.caption("Prototype for e-commerce shipping support. Answers are grounded in a hypothetical knowledge base and may escalate to a human agent.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if m.get("sources"):
            st.caption("Sources: " + ", ".join(m["sources"]))

if prompt := st.chat_input("Ask a shipping, pickup, return, billing, or account question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    result = answer_question(prompt)
    response = result["answer"]
    sources = result["sources"]

    with st.chat_message("assistant"):
        st.markdown(response)
        if sources:
            st.caption("Sources: " + ", ".join(sources))
        if result["action"] == "escalate":
            st.warning("This query has been flagged for human support review.")

    st.session_state.messages.append({
        "role": "assistant", "content": response,
        "sources": sources, "action": result["action"]
    })
