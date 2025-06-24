import streamlit as st
import random
import time

st.set_page_config(page_title="釣りゲーム", page_icon="🎣")

st.title("🎣 釣りゲーム")
st.write("川で魚を釣ってハイスコアを目指そう！")

if "score" not in st.session_state:
    st.session_state.score = 0
if "fish_count" not in st.session_state:
    st.session_state.fish_count = 0
if "log" not in st.session_state:
    st.session_state.log = []
if "fishing" not in st.session_state:
    st.session_state.fishing = False

fish_types = [
    ("ブラックバス", 10),
    ("ブルーギル", 5),
    ("ニジマス", 8),
    ("コイ", 12),
    ("ザリガニ", 1),
    ("カメ", 0),
    ("伝説の巨大魚", 50)
]
weights = [25, 30, 20, 15, 5, 4, 1]

def fishing_action():
    st.session_state.fishing = True
    with st.spinner("…釣り糸を垂らしています…"):
        time.sleep(random.uniform(1, 2.5))
    if random.random() < 0.2:
        st.session_state.log.append("何も釣れませんでした…")
    else:
        caught_fish, points = random.choices(fish_types, weights=weights)[0]
        st.session_state.log.append(f"やった！{caught_fish} を釣りました！（{points} ポイント）")
        st.session_state.score += points
        st.session_state.fish_count += 1
    st.session_state.fishing = False

def reset_game():
    st.session_state.score = 0
    st.session_state.fish_count = 0
    st.session_state.log = []

col1, col2 = st.columns(2)
with col1:
    if st.button("釣り糸を垂らす！", disabled=st.session_state.fishing):
        fishing_action()
with col2:
    if st.button("リセット"):
        reset_game()

st.subheader("釣果ログ")
for l in reversed(st.session_state.log):
    st.write(l)

st.write(f"🎯 合計釣果：{st.session_state.fish_count} 匹, 合計得点：{st.session_state.score} ポイント")