import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

KINDS = ["ビール", "ワイン", "日本酒", "焼酎", "ウイスキー", "チューハイ", "その他"]
DEFAULT_GOAL = 700

st.title("飲み過ぎ防止アプリ")

if "records" not in st.session_state:
    st.session_state.records = []

with st.form("record_form"):
    col1, col2 = st.columns(2)
    date = col1.date_input("日付", datetime.now().date())
    kind = col2.selectbox("種類", KINDS)
    amount = st.number_input("飲んだ量(ml)", min_value=0, step=50, value=0)
    goal = st.number_input("1日の目標(ml)", min_value=100, step=50, value=DEFAULT_GOAL, key="goal")
    submitted = st.form_submit_button("記録する")
    if submitted and amount > 0:
        st.session_state.records.append({"date": date, "kind": kind, "amount": amount})

df = pd.DataFrame(st.session_state.records)
if not df.empty:
    df["date"] = pd.to_datetime(df["date"])
    today = datetime.now().date()
    today_total = df[df["date"] == pd.to_datetime(today)]["amount"].sum()

    # 通知機能: 目標を超えたら警告
    if today_total > goal:
        st.warning(f"⚠️ 今日の飲酒量 {int(today_total)} ml は目標({goal} ml)を超えています！")
        st.toast("飲み過ぎ注意！今日はこのくらいにしませんか？", icon="⚠️")

    st.write(f"### 今日の合計: {int(today_total)} ml")
    st.write("#### 種類ごとの今日の合計")
    st.write(df[df["date"] == pd.to_datetime(today)].groupby("kind")["amount"].sum())

    date_range = [today - timedelta(days=i) for i in range(6, -1, -1)]
    chart_data = pd.DataFrame({"date": date_range}).set_index("date")
    for kind in KINDS:
        kind_series = df[df["kind"] == kind].groupby("date")["amount"].sum()
        chart_data[kind] = [kind_series.get(pd.Timestamp(d), 0) for d in date_range]

    st.write("### 直近7日間の飲酒量（種類別・折れ線グラフ）")
    fig, ax = plt.subplots()
    for kind in KINDS:
        ax.plot(chart_data.index, chart_data[kind], marker="o", label=kind)
    ax.set_ylabel("ml")
    ax.set_xlabel("日付")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write("### 飲酒記録一覧")
    st.dataframe(df.sort_values("date", ascending=False).reset_index(drop=True))
else:
    st.info("記録がありません。上のフォームから記録してください。")