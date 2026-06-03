# =========================================
# IPL Analytics Project
# analysis.py
# =========================================

# Import Libraries
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------------------
# Create visuals folder if not exists
# -----------------------------------------

os.makedirs("../visuals", exist_ok=True)

# -----------------------------------------
# Extract ZIP File
# -----------------------------------------

zip_path = "../archive.zip"

extract_path = "../data"

# Create data folder if not exists
os.makedirs(extract_path, exist_ok=True)

# Unzip archive.zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("\n========== ZIP FILE EXTRACTED ==========\n")

# -----------------------------------------
# Load Dataset
# -----------------------------------------

matches_path = os.path.join(extract_path, "matches.csv")
deliveries_path = os.path.join(extract_path, "deliveries.csv")

matches = pd.read_csv(matches_path)
deliveries = pd.read_csv(deliveries_path)

print("\n========== DATASET LOADED ==========\n")

print("Matches Dataset Shape:", matches.shape)
print("Deliveries Dataset Shape:", deliveries.shape)

# -----------------------------------------
# View Dataset
# -----------------------------------------

print("\n========== MATCHES DATASET ==========\n")
print(matches.head())

print("\n========== DELIVERIES DATASET ==========\n")
print(deliveries.head())

# -----------------------------------------
# Dataset Information
# -----------------------------------------

print("\n========== DATASET INFO ==========\n")
print(matches.info())

# -----------------------------------------
# Missing Values
# -----------------------------------------

print("\n========== MISSING VALUES ==========\n")
print(matches.isnull().sum())

# Fill Missing Winner Values
matches['winner'] = matches['winner'].fillna("No Result")

# -----------------------------------------
# Total IPL Matches
# -----------------------------------------

total_matches = matches.shape[0]

print("\n========== TOTAL MATCHES ==========\n")
print("Total IPL Matches:", total_matches)

# -----------------------------------------
# Total Teams
# -----------------------------------------

teams = matches['team1'].unique()

print("\n========== TOTAL TEAMS ==========\n")
print("Total Teams:", len(teams))

print("\nTeams List:\n")
print(teams)

# -----------------------------------------
# Team Wins Analysis
# -----------------------------------------

team_wins = matches['winner'].value_counts()

print("\n========== TEAM WINS ==========\n")
print(team_wins)

# -----------------------------------------
# Team Wins Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

team_wins.plot(kind='bar')

plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../visuals/team_wins.png")

plt.show()

# -----------------------------------------
# Toss Decision Analysis
# -----------------------------------------

toss_decision = matches['toss_decision'].value_counts()

print("\n========== TOSS DECISION ==========\n")
print(toss_decision)

# -----------------------------------------
# Toss Decision Pie Chart
# -----------------------------------------

plt.figure(figsize=(6, 6))

plt.pie(
    toss_decision,
    labels=toss_decision.index,
    autopct='%1.1f%%'
)

plt.title("Toss Decision Analysis")

plt.savefig("../visuals/toss_decision.png")

plt.show()

# -----------------------------------------
# Top Run Scorers
# -----------------------------------------

top_batsmen = deliveries.groupby(
    'batter'
)['batsman_runs'].sum().sort_values(
    ascending=False
).head(10)

print("\n========== TOP BATSMEN ==========\n")
print(top_batsmen)

# -----------------------------------------
# Top Batsmen Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

top_batsmen.plot(kind='bar')

plt.title("Top 10 Run Scorers")
plt.xlabel("Batsman")
plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../visuals/top_batsmen.png")

plt.show()

# -----------------------------------------
# Strike Rate Analysis
# -----------------------------------------

runs = deliveries.groupby(
    'batter'
)['batsman_runs'].sum()

balls = deliveries.groupby(
    'batter'
)['ball'].count()

strike_rate = (runs / balls) * 100

strike_rate = strike_rate.sort_values(
    ascending=False
)

print("\n========== STRIKE RATE ==========\n")
print(strike_rate.head(10))

# -----------------------------------------
# Strike Rate Visualization
# -----------------------------------------

top_sr = strike_rate.head(10)

plt.figure(figsize=(12, 6))

top_sr.plot(kind='bar', color='orange')

plt.title("Top Strike Rate Players")
plt.xlabel("Player")
plt.ylabel("Strike Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../visuals/strike_rate.png")

plt.show()

# -----------------------------------------
# Wicket Analysis
# -----------------------------------------

wickets = deliveries[
    deliveries['is_wicket'] == 1
]

top_bowlers = wickets['bowler'].value_counts().head(10)

print("\n========== TOP BOWLERS ==========\n")
print(top_bowlers)

# -----------------------------------------
# Top Bowlers Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

top_bowlers.plot(kind='bar')

plt.title("Top Wicket Takers")
plt.xlabel("Bowler")
plt.ylabel("Wickets")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../visuals/top_bowlers.png")

plt.show()

# -----------------------------------------
# Match Scores
# -----------------------------------------

match_scores = deliveries.groupby(
    'match_id'
)['total_runs'].sum()

print("\n========== MATCH SCORES ==========\n")
print(match_scores.head())

# -----------------------------------------
# NumPy Statistics
# -----------------------------------------

scores_array = np.array(match_scores)

print("\n========== NUMPY STATISTICS ==========\n")

print("Average Score:", np.mean(scores_array))
print("Maximum Score:", np.max(scores_array))
print("Minimum Score:", np.min(scores_array))
print("Standard Deviation:", np.std(scores_array))

# -----------------------------------------
# Score Distribution
# -----------------------------------------

plt.figure(figsize=(12, 6))

plt.hist(scores_array, bins=20)

plt.title("Match Score Distribution")
plt.xlabel("Runs")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("../visuals/score_distribution.png")

plt.show()

# -----------------------------------------
# Venue Analysis
# -----------------------------------------

venues = matches['venue'].value_counts().head(10)

print("\n========== TOP VENUES ==========\n")
print(venues)

# -----------------------------------------
# Venue Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

venues.plot(kind='bar')

plt.title("Top IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Matches")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("../visuals/top_venues.png")

plt.show()

# -----------------------------------------
# Season-wise Matches
# -----------------------------------------

season_matches = matches['season'].value_counts().sort_index()

print("\n========== SEASON MATCHES ==========\n")
print(season_matches)

# -----------------------------------------
# Season-wise Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

season_matches.plot(marker='o')

plt.title("Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")

plt.grid()

plt.tight_layout()

plt.savefig("../visuals/season_matches.png")

plt.show()

# -----------------------------------------
# Correlation Heatmap
# -----------------------------------------

numeric_cols = deliveries.select_dtypes(
    include=np.number
)

correlation = numeric_cols.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("../visuals/correlation_heatmap.png")

plt.show()

# -----------------------------------------
# Conclusion
# -----------------------------------------

print("\n====================================")
print(" IPL ANALYTICS COMPLETED SUCCESSFULLY ")
print("====================================")
