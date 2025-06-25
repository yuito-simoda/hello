import streamlit as st
import datetime

st.title("飲み過ぎ防止アプリ")

# 上限量の入力
limit = st.number_input("1日の飲酒上限（ml）を入力", min_value=0, step=10, format="%d")

# 今日の日付
today = datetime.date.today()

# セッションステートに履歴を保存
if "logs" not in st.session_state:
    st.session_state["logs"] = []

# 飲酒量の入力
amount = st.text_input("今日の飲酒量（ml）を入力", "")

# 現在時刻取得
now = datetime.datetime.now()

# 締め切り時刻（今日の23:59:59）
deadline = datetime.datetime.combine(today, datetime.time(23, 59, 59))

# 記録ボタン
if st.button("記録する"):
    # 現在時刻が締め切りを過ぎている場合
    if now > deadline:
        st.info("健康に気を付ける気はありますかね？（23:59までに入力しましょう）")
    elif amount.strip() == "":
        st.warning("今日の飲酒量が未記入です")
    else:
        try:
            amount_val = int(amount)
            st.session_state["logs"].append({"date": today, "amount": amount_val})
            if limit and amount_val > limit:
                st.error("飲み過ぎです！")
            else:
                st.success("記録しました。")
        except ValueError:
            st.warning("数字で入力してください")

# 23:59までに入力しなかった場合の警告（ページが開かれたときにもメッセージ）
if now > deadline and not any(log["date"] == today for log in st.session_state["logs"]):
    st.info("健康に気を付ける気はありますかね？（本日の飲酒量が23:59までに入力されませんでした）")

# 履歴の表示
st.subheader("飲酒履歴")
if st.session_state["logs"]:
    for log in reversed(st.session_state["logs"]):
        st.write(f"{log['date']}: {log['amount']}ml")
else:
    st.write("まだ記録がありません。")