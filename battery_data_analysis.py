import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv('battery_test_data.csv')

# 2. Quick look at the data
print("First few rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())

# 3. Plot Voltage vs Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time_s'], df['Voltage_V'], label='Voltage (V)', color='blue', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Battery Voltage During Discharge')
plt.grid(True)
plt.legend()
plt.savefig('voltage_vs_time.png')  # Saves the picture
plt.show()

# 4. Plot Temperature vs Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time_s'], df['Temperature_C'], label='Temperature (°C)', color='red', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.title('Battery Temperature During Discharge')
plt.grid(True)
plt.legend()
plt.savefig('temperature_vs_time.png')
plt.show()

# 5. (Optional) Calculate average temperature per cycle
avg_temp_per_cycle = df.groupby('Cycle')['Temperature_C'].mean()
print("\nAverage temperature per cycle:")
print(avg_temp_per_cycle)
