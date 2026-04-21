import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Page Config ----
st.set_page_config(page_title="Instagram Reach Dashboard", layout="wide")

st.title("📊 Instagram Reach Analysis Dashboard")

# ---- File Upload ----
uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

# ---- Load Data ----
try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='latin1')
        st.success("Dataset loaded successfully")
    else:
        df = pd.read_csv("insta.csv", encoding='latin1')
        st.warning("Using default dataset")

    st.write("Dataset Shape:", df.shape)
    st.dataframe(df.head())

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ---- Drop Hashtags ----
if "Hashtags" in df.columns:
    df = df.drop(columns=["Hashtags"])

# ---- Handle Zero Values ----
df['Impressions'] = df['Impressions'].replace(0, 1)
df['Profile Visits'] = df['Profile Visits'].replace(0, 1)

# ---- Feature Engineering ----
try:
    df['total_engagement'] = df['Likes'] + df['Comments'] + df['Shares'] + df['Saves']
    df['engagement_rate'] = df['total_engagement'] / df['Impressions']

    df['home_ratio'] = df['From Home'] / df['Impressions']
    df['explore_ratio'] = df['From Explore'] / df['Impressions']
    df['hashtag_ratio'] = df['From Hashtags'] / df['Impressions']
    df['other_ratio'] = df['From Other'] / df['Impressions']

    df['follow_rate'] = df['Follows'] / df['Profile Visits']
    df['visit_rate'] = df['Profile Visits'] / df['Impressions']

    df['caption_length'] = df['Caption'].astype(str).apply(len)

except Exception as e:
    st.error(f"Feature Engineering Error: {e}")
    st.stop()

# ---- Outlier Detection ----
st.subheader("🚨 Outlier Detection (Impressions)")

Q1 = df['Impressions'].quantile(0.25)
Q3 = df['Impressions'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Impressions'] < lower_bound) | (df['Impressions'] > upper_bound)]

st.write(f"Lower Bound: {lower_bound:.2f}")
st.write(f"Upper Bound: {upper_bound:.2f}")
st.write(f"Total Outliers: {outliers.shape[0]}")

st.dataframe(outliers[['Impressions','Likes','Comments','Shares','Saves']])

# Boxplot
fig, ax = plt.subplots()
plt.title("Outliers Detection")
sns.boxplot(x=df['Impressions'], ax=ax)
st.pyplot(fig)

# ---- Remove Outliers (Toggle) ----
use_clean = st.checkbox("Remove Outliers", value=True)

df_clean = df[(df['Impressions'] >= lower_bound) & (df['Impressions'] <= upper_bound)]

data = df_clean if use_clean else df

st.subheader("📊 Dataset Info")
st.write("Original Shape:", df.shape)
st.write("Current Shape:", data.shape)

# ---- KPIs ----
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Engagement Rate", f"{data['engagement_rate'].mean()*100:.2f}%")
col2.metric("Avg Follow Rate", f"{data['follow_rate'].mean()*100:.2f}%")
col3.metric("Avg Visit Rate", f"{data['visit_rate'].mean()*100:.2f}%")

# ---- Correlation Heatmap ----
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10,6))
plt.title("Correlation Heatmap")
sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", ax=ax)
st.pyplot(fig)

# ---- Engagement vs Impressions ----
st.subheader("📈 Engagement vs Impressions")

fig, ax = plt.subplots()
plt.title(" Engagement vs Impressions")
sns.scatterplot(x='Impressions', y='engagement_rate', data=data, ax=ax)
st.pyplot(fig)

# ---- Traffic Sources (Bar) ----
st.subheader("🚦 Traffic Source Contribution")

fig, ax = plt.subplots()
plt.title(" Traffic Source Contribution")
data[['home_ratio','explore_ratio','hashtag_ratio','other_ratio']].mean().plot(kind='bar', ax=ax)
st.pyplot(fig)

# ---- Pie Chart: Impression Sources ----
st.subheader("🥧 Impression Source Distribution")

impression_data = [
    data['From Home'].sum(),
    data['From Hashtags'].sum(),
    data['From Explore'].sum(),
    data['From Other'].sum()
]

labels = ['From Home', 'From Hashtags', 'From Explore', 'From Other']

fig1, ax1 = plt.subplots(figsize=(6,6))
plt.title("Impression Source Distribution")
wedges, texts, autotexts = ax1.pie(
    impression_data,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    labeldistance=1.05
)

# Reduce label size
for text in texts:
    text.set_fontsize(9)

# 🔥 Reduce percentage size (main fix)
for autotext in autotexts:
    autotext.set_fontsize(10)   # smaller %
    autotext.set_alpha(0.9)    # optional: lighter look

ax1.axis('equal')
st.pyplot(fig1)

# ---- Conversion Funnel ----
st.subheader("🔄 Conversion Funnel")

fig, ax = plt.subplots()
plt.title("Conversion Funnel")
sns.scatterplot(x='Profile Visits', y='Follows', data=data, ax=ax)
st.pyplot(fig)

# ---- Pie Chart: Engagement + Conversion ----
st.subheader("🥧 Engagement & Conversion Distribution")

engagement_data = [
    data['Likes'].sum(),
    data['Comments'].sum(),
    data['Saves'].sum(),
    data['Follows'].sum(),
    data['Profile Visits'].sum()
]

labels2 = ['Likes', 'Comments', 'Saves', 'Follows', 'Profile Visits']

fig2, ax2 = plt.subplots(figsize=(6,6))
plt.title(" Engagement & Conversion Distribution")
wedges, texts, autotexts = ax2.pie(
    engagement_data,
    labels=labels2,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    labeldistance=1.05
)

for text in texts:
    text.set_fontsize(9)

for autotext in autotexts:
    autotext.set_fontsize(8)

ax2.axis('equal')
st.pyplot(fig2)

# ---- Caption Analysis ----
st.subheader("✍️ Caption Length Impact")

fig, ax = plt.subplots()
plt.title("Caption Length Impact")
sns.scatterplot(x='caption_length', y='engagement_rate', data=data, ax=ax)
st.pyplot(fig)

# ---- Top Posts ----
st.subheader("🏆 Top Performing Posts")

top_posts = data.sort_values(by='engagement_rate', ascending=False).head(10)

# Create a readable percentage column
top_posts['Engagement Rate (%)'] = (top_posts['engagement_rate'] * 100).round(2)

# Select important columns to display
columns_to_show = [
    'Impressions', 'Likes', 'Comments', 'Shares', 'Saves',
    'Profile Visits', 'Follows', 'Engagement Rate (%)'
]

st.dataframe(top_posts[columns_to_show])

# ---- Download Clean Data ----
st.subheader("⬇️ Download Dataset")

csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="instagram_data_processed.csv",
    mime='text/csv'
)