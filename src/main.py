import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# Load data
data = pd.read_csv("data/poll_data.csv")

# Convert date
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Cleaning
data = data.drop_duplicates()
data = data.dropna()

# Feature
data['Date'] = data['Timestamp'].dt.date

print(data.head())

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# =========================
# BAR CHART
# =========================
plt.figure()
sns.countplot(x='Preferred Tool', data=data)
plt.title("Tool Preference")
plt.savefig("outputs/bar_chart.png")
plt.close()

# =========================
# HISTOGRAM
# =========================
plt.figure()
plt.hist(data['Satisfaction (1-5)'])
plt.title("Satisfaction Distribution")
plt.savefig("outputs/histogram.png")
plt.close()

# =========================
# LINE CHART
# =========================
daily = data.groupby('Date').size()

plt.figure()
daily.plot()
plt.title("Daily Responses")
plt.savefig("outputs/line_chart.png")
plt.close()

# =========================
# WORD CLOUD
# =========================
text = " ".join(data['Feedback'])

wc = WordCloud().generate(text)

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.savefig("outputs/wordcloud.png")
plt.close()

print("✅ Project Completed Successfully!")