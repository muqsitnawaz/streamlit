import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("apple-sales.csv")
st.line_chart(df["Mac"])
