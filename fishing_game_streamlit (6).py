import streamlit as st
import random

# --- 場所リスト ---
locations = [
    "上流", "中流", "下流", "河口",
    "東京湾", "太平洋", "日本海", "瀬戸内海", "相模湾",
    "オホーツク海", "東シナ海", "玄界灘", "大間", "五島列島",
    "積丹半島", "女川港", "大洗港", "城ヶ島", "沼津港",
    "串本", "室戸岬", "枕崎", "糸満漁港"
]

seasons = ["春", "夏", "秋", "冬"]
weathers = ["晴れ", "雨", "曇り"]

# --- 魚データ（略） ---
# fish_data は省略（上記コード参照）

# --- 魚画像＆説明辞書（略） ---
# fish_info は省略（上記コード参照）

# --- 魚図鑑 ---
st.sidebar.title("🎏 魚図鑑")
if st.sidebar.button("図鑑を開く"):
    for name, info in sorted(fish_info.items()):
        st.subheader(name)
        st.image(info["img"], width=250)
        st.caption(info["desc"])

# --- Streamlit UI ---
st.title("🎣 日本の釣りゲーム 完全版")

location = st.selectbox("釣り場を選択してください", locations)
season = st.selectbox("季節を選択してください", seasons)
weather = st.selectbox("天気を選択してください", weathers)

if st.button("釣りをする！"):
    fish_list = fish_data.get(location, {}).get(season, {}).get(weather, [])
    if not fish_list:
        st.write("この条件では魚が釣れませんでした。")
    else:
        caught = random.choice(fish_list)
        weight = round(random.uniform(0.2, 10.0), 2)  # 重さ（kg）
        rarity_score = random.randint(1, 100)  # レア度スコア

        if rarity_score > 95:
            rarity = "🌈 超激レア！"
        elif rarity_score > 80:
            rarity = "🌟 激レア"
        elif rarity_score > 50:
            rarity = "⭐ レア"
        else:
            rarity = "★ ノーマル"

        st.success(f"おめでとう！{caught}（{weight}kg）が釣れました！")
        st.info(f"レア度: {rarity}")

        # 魚画像と説明表示
        info = fish_info.get(caught)
        if info:
            st.image(info["img"], width=300)
            st.write(info["desc"])
