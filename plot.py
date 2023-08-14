import numpy as np
import matplotlib.pyplot as plt

# Load the .npy file
data = np.load('framework/data.npy')

# Assuming data is a list of segments where each segment contains an array of trajectories
# Let's extract the first segment for demonstration purposes
segment = data[0]


# Create a new figure and axis
fig, ax = plt.subplots()



x_values = segment[2]  # Extract latitude (x) values
y_values = segment[3]  # Extract longitude (y) values
ax.plot(x_values, y_values, marker='o', label=f'Trajectory')

# Set labels and title
ax.set_xlabel('Latitude (x)')
ax.set_ylabel('Longitude (y)')
ax.set_title('Trajectories')

plt.legend()
plt.grid(True)
plt.savefig('plot1.png')
plt.close()
