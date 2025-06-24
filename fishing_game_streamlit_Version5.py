import streamlit as st
import random
import time

st.set_page_config(page_title="釣りゲーム", page_icon="🎣")

st.title("🎣 釣りゲーム")
st.write("川で魚を釣ってハイスコアを目指そう！")
st.write("20回釣るとゲーム終了です。")

MAX_TRIES = 20

# セッションステートの初期化
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
    ("伝説の巨大魚", 50),
    ("空き缶", -10),
    ("長靴", -5),
    ("ワニ", -20)
]
weights = [20, 22, 16, 12, 5, 4, 1, 7, 6, 7]  # 合計100

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
    fishing_disabled = (
        st.session_state.fishing or st.session_state.fish_count >= MAX_TRIES
    )
    if st.button("釣り糸を垂らす！", disabled=fishing_disabled):
        if st.session_state.fish_count < MAX_TRIES:
            fishing_action()
with col2:
    if st.button("リセット"):
        reset_game()

st.subheader("釣果ログ")
for l in reversed(st.session_state.log):
    st.write(l)

st.write(f"🎯 合計釣果：{st.session_state.fish_count} 回, 合計得点：{st.session_state.score} ポイント")

if st.session_state.fish_count >= MAX_TRIES:
    st.success("ゲーム終了！20回釣りました。お疲れさまでした！")
    # 評価メッセージ表示
    if st.session_state.score > 10:
        st.markdown("### 👍 いいね！")
    elif st.session_state.score > 0:
        st.markdown("### 🙂 まぁまぁかな")
    else:
        st.markdown("### 😅 腕が足りない")