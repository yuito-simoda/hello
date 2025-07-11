# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oMBdRBHj5Gnna-pJdJ56d4V-nm-uohpi
"""

import streamlit as st
import random

# 魚データ
fish_data = {
    "湖": {
        "春": {
            "晴れ": [
                {"name": "ワカサギ", "image": "images/wakasagi.jpg", "rare": False},
                {"name": "フナ", "image": "images/funa.jpg", "rare": False}
            ],
            "雨": [
                {"name": "ナマズ", "image": "images/namazu.jpg", "rare": False},
                {"name": "ドジョウ", "image": "images/dojo.jpg", "rare": False}
            ]
        }
    }
}

# レア魚リスト
rare_fish = [
    {"name": "リュウグウノツカイ", "image": "images/ryugu.jpg", "rare": True},
    {"name": "シーラカンス", "image": "images/coelacanth.jpg", "rare": True}
]

# 初期化（図鑑の状態をセッションに保存）
if "zukan" not in st.session_state:
    st.session_state.zukan = {}

# ユーザー入力
st.title("🎣 魚釣りゲーム")
location = st.selectbox("場所", list(fish_data.keys()))
season = st.selectbox("季節", list(fish_data[location].keys()))
weather = st.selectbox("天気", list(fish_data[location][season].keys()))

if st.button("釣る！"):
    # レア判定
    if random.random() < 0.05:
        fish = random.choice(rare_fish)
        st.balloons()
        st.success(f"🌟 超レア！『{fish['name']}』が釣れた！")
    else:
        candidates = fish_data[location][season][weather]
        fish = random.choice(candidates)
        st.info(f"{fish['name']} を釣りました！")

    st.image(fish["image"], width=300)

    # 図鑑登録
    if fish["name"] not in st.session_state.zukan:
        st.session_state.zukan[fish["name"]] = fish["image"]
        st.write(f"📘 『{fish['name']}』を図鑑に登録！")

# 図鑑表示
with st.expander("🐟 図鑑を見る"):
    for name, image in st.session_state.zukan.items():
        st.write(f"📖 {name}")
        st.image(image, width=200)