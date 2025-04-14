import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="military_db",
    user="postgres",
    password="postgres123",  # 🔑 твій новий пароль
    host="localhost",
    port="5432",
    options="-c client_encoding=UTF8"
)

# Читання з таблиці
df = pd.read_sql("SELECT * FROM battle_reports", conn)

# Переконайся, що колонка 'date' у форматі datetime
df["date"] = pd.to_datetime(df["date"])

# Налаштування сторінки
st.set_page_config(page_title="Військовий аналітичний дашборд", layout="wide")
st.title("📊 Військовий аналітичний дашборд")

# 🔍 Фільтри
col1, col2 = st.columns(2)
with col1:
    locations = st.multiselect("Локація", df["location"].unique(), default=df["location"].unique())
with col2:
    date_range = st.date_input("Період", [df["date"].min().date(), df["date"].max().date()])

# 🔄 Фільтрація даних
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

filtered_df = df[
    (df["location"].isin(locations)) &
    (df["date"] >= start_date) &
    (df["date"] <= end_date)
]

# 📈 Графік 1: Втрати особового складу
fig1 = px.line(filtered_df, x="date", y="enemy_losses_personnel", color="location",
               title="Втрати особового складу за датами")
st.plotly_chart(fig1, use_container_width=True)

# 📊 Графік 2: Використання боєприпасів
fig2 = px.bar(filtered_df, x="date", y="ammo_used", color="location",
              title="Використані боєприпаси")
st.plotly_chart(fig2, use_container_width=True)

