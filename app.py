import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Feedback Analyzer", page_icon="🗣️", layout="wide")

# --- Custom Dark Theme via CSS ---
st.markdown("""
    <style>
        .block-container {background-color: #0f1116;}
        h1, h2, h3, p, label, .stMarkdown, .stTextInput label {
            color: #f8f9fa !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🗣️ Customer Feedback Analyzer")
st.markdown("**Ein Tool zur Analyse und Visualisierung von Kundenmeinungen.**")

# --- Daten laden ---
@st.cache_data
def load_data():
    return pd.read_csv("feedback_data.csv")

df = load_data()

# --- Filter ---
sentiments = df["Sentiment"].unique()
selected_sentiment = st.sidebar.multiselect("Sentiment auswählen:", sentiments)

if selected_sentiment:
    df = df[df["Sentiment"].isin(selected_sentiment)]

# --- Visualisierung 1: Sentiment-Verteilung ---
fig = px.pie(df, names="Sentiment", title="📊 Sentiment-Verteilung")
st.plotly_chart(fig, use_container_width=True)

# --- Visualisierung 2: WordCloud ---
st.subheader("💬 Häufigste Wörter im Feedback")
text = " ".join(df["Feedback"].astype(str))
wordcloud = WordCloud(width=1000, height=500, background_color="black", colormap="plasma").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# --- Datenanzeige ---
st.subheader("📋 Feedback-Tabelle")
st.dataframe(df)
