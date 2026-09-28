import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Social Media Trend Analysis",
    page_icon="📱",
    layout="wide"
)

# Title
st.title("📱 Social Media Trend Analysis")
st.write("Analyze trending topics, sentiment and engagement behavior.")

st.divider()

# Sidebar
st.sidebar.title("🔍 Filters")

platform = st.sidebar.selectbox(
    "Select Platform",
    ["All Platforms", "Instagram", "Twitter", "Facebook"]
)

time_period = st.sidebar.selectbox(
    "Time Period",
    ["Today", "This Week", "This Month"]
)

# Sample social media data
data = {
    "Topic": [
        "Artificial Intelligence",
        "Cricket",
        "Movies",
        "Technology",
        "Fashion"
    ],
    "Posts": [850, 720, 650, 580, 450]
}

df = pd.DataFrame(data)

# Dashboard metrics
st.subheader("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Posts", "3,250")
col2.metric("🔥 Trending Topic", "AI")
col3.metric("😊 Positive", "52%")
col4.metric("💬 Engagement", "78%")

st.divider()

# Trending topics
st.subheader("🔥 Trending Topics")

fig = px.bar(
    df,
    x="Topic",
    y="Posts",
    title="Most Discussed Topics",
    labels={
        "Topic": "Topic",
        "Posts": "Number of Posts"
    }
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Two columns
left, right = st.columns(2)

# Sentiment analysis
with left:
    st.subheader("😊 Sentiment Analysis")

    sentiment = pd.DataFrame({
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Percentage": [52, 30, 18]
    })

    fig2 = px.pie(
        sentiment,
        names="Sentiment",
        values="Percentage",
        title="Overall Sentiment"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Engagement analysis
with right:
    st.subheader("📈 Engagement Analysis")

    engagement = pd.DataFrame({
        "Type": ["Likes", "Comments", "Shares"],
        "Count": [5200, 2100, 1350]
    })

    fig3 = px.bar(
        engagement,
        x="Type",
        y="Count",
        title="User Engagement"
    )

    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Dataset upload
st.subheader("📂 Upload Social Media Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    uploaded_data = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully! ✅")

    st.write("### Dataset Preview")
    st.dataframe(uploaded_data)

    st.write("### Dataset Information")

    col1, col2 = st.columns(2)

    col1.metric(
        "Number of Rows",
        uploaded_data.shape[0]
    )

    col2.metric(
        "Number of Columns",
        uploaded_data.shape[1]
    )

st.divider()

st.caption(
    "Social Media Trend Analysis | Data Science Project"
)
