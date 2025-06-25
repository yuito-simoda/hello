import streamlit as st
import random
import time

st.title("目覚まし記憶パズル")

# ステート初期化
if "puzzle_started" not in st.session_state:
    st.session_state.puzzle_started = False
if "sequence" not in st.session_state:
    st.session_state.sequence = []
if "user_input" not in st.session_state:
    st.session_state.user_input = []
if "show_sequence" not in st.session_state:
    st.session_state.show_sequence = False
if "result" not in st.session_state:
    st.session_state.result = ""

colors = ["red", "green", "blue", "yellow"]

def start_puzzle():
    st.session_state.puzzle_started = True
    st.session_state.sequence = [random.choice(colors) for _ in range(4)]
    st.session_state.user_input = []
    st.session_state.show_sequence = True
    st.session_state.result = ""

def check_answer():
    if st.session_state.user_input == st.session_state.sequence:
        st.session_state.result = "正解！目が覚めましたか？"
    else:
        st.session_state.result = "不正解！もう一度挑戦しましょう。"
    st.session_state.puzzle_started = False

if not st.session_state.puzzle_started:
    st.button("パズル開始", on_click=start_puzzle)

if st.session_state.puzzle_started and st.session_state.show_sequence:
    st.write("色の順番を覚えてください：")
    st.write(" → ".join(st.session_state.sequence))
    time.sleep(2)
    st.session_state.show_sequence = False
    st.experimental_rerun()

if st.session_state.puzzle_started and not st.session_state.show_sequence:
    st.write("さあ、順番通りに色を選んでください。")
    for i in range(len(st.session_state.sequence)):
        c = st.selectbox(f"{i+1}番目の色", options=["選択してください"] + colors, key=f"input_{i}")
        if c != "選択してください":
            if len(st.session_state.user_input) < i + 1:
                st.session_state.user_input.append(c)
            else:
                st.session_state.user_input[i] = c

    if len(st.session_state.user_input) == len(st.session_state.sequence):
        st.button("答え合わせ", on_click=check_answer)

if st.session_state.result:
    st.write(st.session_state.result)