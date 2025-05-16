import streamlit as st
from src.match import results

st.title("AI Candidate Matcher")
st.write("Upload a job description and view matching candidates.")

st.header("Top Matches:")
for name, score in results:
    st.write(f"**{name}** — Match Score: `{score:.3f}`")
