import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 

# Connect to SQLite database
conn = sqlite3.connect('barca2024')

# Read data from database into pandas dataframe
df = pd.read_sql_query("SELECT * FROM barca2024", conn)

# Close database connection
conn.close()

# Display dataframe
print(df)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['Player_Name'], df['Minutes_Played'], color = 'olive')
plt.xlabel('Player_Name')
plt.ylabel('Minutes Played')
plt.title('La Liga Minutes Played by FC Barcelona Players in 2023/2024 Season')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
