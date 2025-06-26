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

# -------------------- 魚画像＆説明辞書 --------------------
fish_info = {
    "イワナ": {"img": "https://upload.wikimedia.org/wikipedia/commons/6/66/Iwana01.jpg", "desc": "冷たい清流に住むイワナ。美しい体色が特徴です。"},
    "ヤマメ": {"img": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Yamame_fish.jpg", "desc": "渓流釣りで人気のヤマメ。サケ科の淡水魚です。"},
    "ニジマス": {"img": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Rainbow_trout.png", "desc": "派手な虹色模様をもつ美しい魚。養殖も盛ん。"},
    "アマゴ": {"img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Amago_fish_2.jpg", "desc": "アマゴは関西地方に多い渓流魚。赤い斑点が特徴。"},
    "オイカワ": {"img": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Oikawa_male.jpg", "desc": "婚姻色が美しい小型淡水魚。群れで泳ぎます。"},
    "フナ": {"img": "https://upload.wikimedia.org/wikipedia/commons/7/75/Carassius_auratus_langsdorfii1.jpg", "desc": "日本全国の池や川にいるおなじみの魚。"},
    "ウグイ": {"img": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Tribolodon_hakonenis_by_OpenCage.jpg", "desc": "幅広い環境に適応できる淡水魚。婚姻色は赤くなる。"},
    "ナマズ": {"img": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Silurus_asotus.jpg", "desc": "夜行性で口ひげが特徴。雷魚と混同されがち。"},
    "ボラ": {"img": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Mugil_cephalus1.jpg", "desc": "汽水域に多く、群れで泳ぐ魚。成魚は大型になります。"},
    "スズキ": {"img": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Lateolabrax_japonicus.jpg", "desc": "釣りでも食でも人気の白身魚。成長と共に名前が変わる出世魚。"},
    "ハゼ": {"img": "https://upload.wikimedia.org/wikipedia/commons/3/33/Acanthogobius_flavimanus.jpg", "desc": "汽水域で釣れる小型魚。天ぷらが美味。"},
    "シーバス": {"img": "https://upload.wikimedia.org/wikipedia/commons/6/66/Lateolabrax_maculatus.jpg", "desc": "ルアー釣りのターゲット。別名スズキ。"},
    "クロダイ": {"img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Acanthopagrus_schlegelii.jpg", "desc": "磯釣りの代表格。力強い引きが魅力です。"},
    "キス": {"img": "https://upload.wikimedia.org/wikipedia/commons/d/de/Sillago_japonica.jpg", "desc": "砂浜で投げ釣りで狙う人気の魚。白身が上品な味わい。"},
    "アジ": {"img": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Trachurus_japonicus.jpg", "desc": "釣り初心者にも人気の青魚。脂がのった味わい。"},
    "カサゴ": {"img": "https://upload.wikimedia.org/wikipedia/commons/1/15/Sebastiscus_marmoratus.jpg", "desc": "岩礁に潜む小型の根魚。煮付けが美味しい。"},
    "メバル": {"img": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Sebastes_inermis.jpg", "desc": "夜釣りで人気の根魚。暗い所を好む。"},
    "カツオ": {"img": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Katsuwonus_pelamis.jpg", "desc": "回遊魚の代表格。刺身やたたきで人気。"},
    "シイラ": {"img": "https://upload.wikimedia.org/wikipedia/commons/6/60/MahiMahi.png", "desc": "鮮やかな体色が美しい大型魚。夏に多く釣れる。"},
    "ブリ": {"img": "https://upload.wikimedia.org/wikipedia/commons/4/47/Japanese_amberjack.jpg", "desc": "出世魚として有名。冬の寒ブリが特に美味。"},
    "ヒラメ": {"img": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Paralichthys_olivaceus_by_OpenCage.jpg", "desc": "平たい体と隠れる習性。刺身が絶品。"},
    "タチウオ": {"img": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Trichiurus_lepturus2.jpg", "desc": "刀のような見た目。夜釣りの人気者。"}
}

# -------------------- 魚情報表示関数 --------------------
def show_fish_info(fish_name):
    if fish_name in fish_info:
        st.image(fish_info[fish_name]["img"], width=200)
        st.caption(fish_info[fish_name]["desc"])
