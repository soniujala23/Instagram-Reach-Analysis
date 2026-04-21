# 📊 Instagram Reach Analysis Dashboard

> An interactive data analytics dashboard built with **Streamlit** to analyze Instagram post reach, engagement, and audience conversion metrics.

---

## 🖼️ Dashboard Preview


[Dashboard]<img width="1335" height="470" alt="Screenshot 2026-04-08 181220" src="https://github.com/user-attachments/assets/99ae2bd2-c016-4125-ad25-bbce967885cc" />


[Outliers]<img width="1041" height="908" alt="9ef5cfd70d003bb915cd9df27c418e86fe9f7a9ec6c84e95e15d8f80" src="https://github.com/user-attachments/assets/211cedcb-ba5f-4296-9bed-e4027f4fa591" />
 


 [Heatmap]<img width="1460" height="1048" alt="73965992b6234818f2de4b52d7baa9b0d41a8ad4c56e63a3e682d13c" src="https://github.com/user-attachments/assets/bae07acf-57f3-4dd5-97ff-22fe686bbac9" />
 
 
 [Traffic]<img width="1095" height="1031" alt="d742762485b2575c08213dcf7c309cd115b65ba5476133cd57058601" src="https://github.com/user-attachments/assets/35afc29a-48d6-4040-904b-ef5828312375" />
 


## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [License](#license)

---

## 📖 About the Project

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on Instagram post data to uncover patterns in content reach, audience engagement, and follower conversion. 

The interactive **Streamlit dashboard** allows users to:
- Upload their own Instagram analytics CSV
- Detect and remove outliers using IQR method
- View key performance metrics (KPIs)
- Explore visual insights through charts and graphs
- Download the processed dataset

---

## ✨ Features

- 📁 **Custom Dataset Upload** — Upload your own Instagram CSV or use the default dataset
- 🚨 **Outlier Detection** — IQR-based outlier detection on Impressions with toggle to remove
- 📌 **KPI Metrics** — Avg Engagement Rate, Avg Follow Rate, Avg Visit Rate
- 🔥 **Correlation Heatmap** — Visualize relationships between all features
- 📈 **Engagement vs Impressions** — Scatter plot analysis
- 🚦 **Traffic Source Analysis** — Bar chart and pie chart for Home, Hashtags, Explore, Other
- 🔄 **Conversion Funnel** — Profile Visits vs Follows scatter plot
- ✍️ **Caption Length Analysis** — Impact of caption length on engagement rate
- 🏆 **Top Performing Posts** — Top 10 posts ranked by engagement rate
- ⬇️ **Download Processed Data** — Export clean dataset as CSV

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Interactive web dashboard |
| **Pandas** | Data loading and manipulation |
| **Matplotlib** | Plot generation |
| **Seaborn** | Statistical visualizations |
| **NumPy** | Numerical computations |

---

## 📂 Dataset

The dataset is an Instagram Analytics export in CSV format containing **119 posts** with the following features:

| Feature | Description |
|---|---|
| `Impressions` | Total times the post was displayed |
| `From Home` | Impressions from Home feed |
| `From Hashtags` | Impressions via Hashtags |
| `From Explore` | Impressions from Explore page |
| `From Other` | Impressions from other sources |
| `Likes` | Number of likes |
| `Comments` | Number of comments |
| `Shares` | Number of shares |
| `Saves` | Number of saves |
| `Profile Visits` | Profile visits from the post |
| `Follows` | New followers gained |
| `Caption` | Post caption text |

**Derived Features (after Feature Engineering):**

| Feature | Formula |
|---|---|
| `total_engagement` | Likes + Comments + Shares + Saves |
| `engagement_rate` | total_engagement / Impressions |
| `home_ratio` | From Home / Impressions |
| `explore_ratio` | From Explore / Impressions |
| `hashtag_ratio` | From Hashtags / Impressions |
| `other_ratio` | From Other / Impressions |
| `follow_rate` | Follows / Profile Visits |
| `visit_rate` | Profile Visits / Impressions |
| `caption_length` | len(Caption) |


## 📁 Project Structure

```
instagram-reach-analysis/
│
├── insta_fds_code.py        # Main Streamlit application
├── insta.csv                # Default Instagram dataset
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
│
├── screenshots/             # Dashboard screenshots
│   ├── dashboard.png
│   ├── outliers.png
│   ├── heatmap.png
│   ├── traffic.png
│   ├── engagement.png
│   └── top_posts.png
│
└── report/                  # Project report (optional)
    └── Instagram_Reach_Analysis_Report.docx
```

---

## 📊 Key Insights

Based on the analysis of **119 Instagram posts**:

- 🏠 **Home feed is the #1 traffic source** contributing **51.3%** of all impressions
- #️⃣ **Hashtags contribute 34.8%** — making them the second most important reach channel
- 💾 **Saves account for 37.1%** of all engagement actions — highest value signal for the algorithm
- 📉 **Higher impressions ≠ higher engagement** — posts with 3,000–6,000 impressions achieved the best engagement rates
- 👤 **Average Follow Rate: 33.85%** — 1 in 3 profile visitors converts to a follower
- ✍️ **Short captions (50–250 characters)** perform best with highest engagement rates
- 🏆 **Top post achieved 13.03% engagement rate** with 393 saves out of 5,409 impressions

---
 Top Performing Posts
 [Top Posts]<img width="1262" height="521" alt="Screenshot 2026-04-08 183309" src="https://github.com/user-attachments/assets/8c6598d3-6ef0-435e-b2f8-391f78612215" />





Ujala Soni
