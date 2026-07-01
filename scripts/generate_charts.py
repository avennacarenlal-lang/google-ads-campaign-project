import pandas as pd
import matplotlib.pyplot as plt

# Load metrics
df = pd.read_csv("assets/metrics.csv")

# CTR Trend (Line Chart)
plt.figure(figsize=(6,4))
plt.plot(df["Week"], df["CTR (%)"], marker="o", color="blue")
plt.title("CTR Trend")
plt.xlabel("Week")
plt.ylabel("CTR (%)")
plt.grid(True)
plt.savefig("assets/ctr_trend.png")
plt.close()

# Conversions (Bar Chart)
plt.figure(figsize=(6,4))
plt.bar(df["Week"], df["Conversions"], color="green")
plt.title("Conversions per Week")
plt.xlabel("Week")
plt.ylabel("Conversions")
plt.savefig("assets/conversions_bar.png")
plt.close()

# Avg CPC Trend (Line Chart)
plt.figure(figsize=(6,4))
plt.plot(df["Week"], df["Avg CPC (₹)"], marker="o", color="red")
plt.title("Average CPC Trend")
plt.xlabel("Week")
plt.ylabel("Avg CPC (₹)")
plt.grid(True)
plt.savefig("assets/cpc_trend.png")
plt.close()

print("Charts saved in assets/ folder!")
