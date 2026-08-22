import streamlit as st
import random

st.title("星座占い✨")
st.write("まずは星座を選んでね！")

st.selectbox("みたい星座を選択してね",["牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座","山羊座","水瓶座","魚座"])