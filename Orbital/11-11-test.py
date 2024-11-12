import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# Replace 'your_file.csv' with the actual path to your CSV file
data = pd.read_csv('.//11-11-test/PID_boiled_4.csv')

# Extract the relevant columns (Time and Vel Y)
time = data['Time']
velocity = data['Vel Y']

# Plot Time vs. Velocity
plt.figure(figsize=(10, 6))
plt.plot(time, velocity, marker='o', color='b', linestyle='-')
plt.title('Time vs Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (Vel Y)')
plt.grid(True)

# Show the plot
plt.show()
