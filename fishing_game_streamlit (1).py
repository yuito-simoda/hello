import streamlit as st
import random

# -------------------- 場所リスト --------------------
locations = [
    "上流", "中流", "下流", "河口",
    "東京湾", "太平洋", "日本海", "瀬戸内海", "相模湾",
    "オホーツク海", "東シナ海", "玄界灘", "大間", "五島列島",
    "積丹半島", "女川港", "大洗港", "城ヶ島", "沼津港",
    "串本", "室戸岬", "枕崎", "糸満漁港"
]

seasons = ["春", "夏", "秋", "冬"]
weathers = ["晴れ", "雨", "曇り"]

# -------------------- 魚図鑑 --------------------
fish_catalog = {
    "カツオ": {"rare": "★★★", "weight_range": (2, 5)},
    "アジ": {"rare": "★", "weight_range": (0.2, 0.5)},
    "イカ": {"rare": "★★", "weight_range": (0.5, 1.2)},
    "メジナ": {"rare": "★", "weight_range": (0.5, 1.0)},
    "シイラ": {"rare": "★★★", "weight_range": (3, 6)},
    "ヒラマサ": {"rare": "★★★", "weight_range": (4, 8)},
    "ブリ": {"rare": "★★★", "weight_range": (5, 10)},
    "サワラ": {"rare": "★★", "weight_range": (2, 4)},
    "イサキ": {"rare": "★", "weight_range": (0.8, 1.5)},
    "シマアジ": {"rare": "★★★", "weight_range": (1.5, 3.0)},
    "カサゴ": {"rare": "★", "weight_range": (0.3, 0.7)},
    "ホッケ": {"rare": "★", "weight_range": (0.5, 1.2)},
    "サクラマス": {"rare": "★★★", "weight_range": (1.5, 3.0)},
    "カレイ": {"rare": "★", "weight_range": (0.4, 1.0)},
    "アキアジ": {"rare": "★★", "weight_range": (2.0, 4.0)},
    "ソイ": {"rare": "★", "weight_range": (0.5, 1.5)},
    "アイナメ": {"rare": "★", "weight_range": (0.7, 1.5)},
    "タチウオ": {"rare": "★★", "weight_range": (1.0, 2.0)},
    "シーバス": {"rare": "★★", "weight_range": (1.5, 5.0)},
    "ヒラメ": {"rare": "★★★", "weight_range": (2.0, 4.0)},
    "アオリイカ": {"rare": "★★", "weight_range": (0.8, 1.8)},
    "マグロ": {"rare": "★★★★★", "weight_range": (30, 200)},
    "ミーバイ": {"rare": "★★", "weight_range": (1.0, 3.0)},
    "タマン": {"rare": "★★★", "weight_range": (2.0, 5.0)},
    "ガーラ": {"rare": "★★★", "weight_range": (1.5, 6.0)}
}

# -------------------- 図鑑登録 --------------------
caught_fish_log = []

# -------------------- UI --------------------
st.title("🎣 全国釣り場シミュレーター")

location = st.selectbox("場所を選ぶ", locations)
season = st.selectbox("季節を選ぶ", seasons)
weather = st.selectbox("天気を選ぶ", weathers)

if st.button("釣る！"):
    if location in fish_data and season in fish_data[location] and weather in fish_data[location][season]:
        fish_list = fish_data[location][season][weather]
        caught = random.choice(fish_list)
        weight = round(random.uniform(*fish_catalog.get(caught, {}).get("weight_range", (0.5, 1.5))), 2)
        rarity = fish_catalog.get(caught, {}).get("rare", "？")
        st.success(f"🎉 {location}の{season}・{weather}で「{caught}」が釣れました！\n重さ: {weight}kg / レア度: {rarity}")
        caught_fish_log.append((caught, weight, rarity))
    else:
        st.warning("まだこの場所のデータが未設定です。魚を登録してね！")

# -------------------- 図鑑 --------------------
if st.button("🎏 図鑑を見る"):
    if caught_fish_log:
        st.subheader("🐟 あなたの釣った魚図鑑")
        for fish, weight, rarity in caught_fish_log:
            st.write(f"- {fish}（{weight}kg / {rarity}）")
    else:
        st.info("まだ魚を釣っていません。釣ってから図鑑を開こう！")
