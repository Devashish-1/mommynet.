import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Generate initial data
x_data = []
y_data = []
z_data = []
line, = ax.plot([], [], [], lw=2, color='blue')

# Set axis limits
ax.set_xlim(0, 100)
ax.set_ylim(-5, 5)
ax.set_zlim(-1.5, 1.5)
ax.set_title("Dynamic 3D Line Graph", fontsize=16)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Update function for animation
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1))
    z_data.append(np.cos(frame * 0.1))

    line.set_data(x_data, y_data)
    line.set_3d_properties(z_data)

    return line,

# Additional functions to enhance graph dynamics
def generate_random_color():
    """Generates a random color for the line graph."""
    return np.random.rand(3,)

def randomize_limits():
    """Randomly adjusts the axis limits during the animation."""
    ax.set_xlim(0, 100)
    ax.set_ylim(-5 + np.random.uniform(-1, 1), 5 + np.random.uniform(-1, 1))
    ax.set_zlim(-1.5 + np.random.uniform(-0.5, 0.5), 1.5 + np.random.uniform(-0.5, 0.5))

# Custom styles for the graph
def style_graph():
    """Applies custom styles to the graph axes and title."""
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_facecolor('#f0f0f0')
    ax.tick_params(axis='both', which='major', labelsize=10, color='black')

# Style and randomize initial setup
style_graph()
randomize_limits()

# Function for noise addition
def add_noise(data, intensity=0.1):
    """Adds random noise to a dataset."""
    return data + np.random.normal(0, intensity, len(data))

# Modified update function
def enhanced_update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1))
    z_data.append(np.cos(frame * 0.1))

    # Add noise for dynamic effect
    y_noisy = add_noise(np.array(y_data))
    z_noisy = add_noise(np.array(z_data))

    line.set_data(x_data, y_noisy)
    line.set_3d_properties(z_noisy)
    line.set_color(generate_random_color())

    # Randomize limits occasionally
    if frame % 20 == 0:
        randomize_limits()

    return line,

# Create the enhanced animation
ani = FuncAnimation(fig, enhanced_update, frames=range(200), interval=50, blit=True)

# Additional graph annotations
def add_annotations():
    """Adds annotations or markers to the graph."""
    ax.text(50, 0, 0, "Center Point", color='red', fontsize=12)
    ax.scatter([50], [0], [0], color='red', s=50)

# Call annotations
add_annotations()

# Display the animation
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Generate static data
x_data = np.linspace(0, 100, 500)
y_data = np.sin(x_data * 0.1)
z_data = np.cos(x_data * 0.1)

# Plot the static 3D line graph
ax.plot(x_data, y_data, z_data, lw=2, color='blue')

# Set axis limits
ax.set_xlim(0, 100)
ax.set_ylim(-5, 5)
ax.set_zlim(-1.5, 1.5)
ax.set_title("Static 3D Line Graph", fontsize=16)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Custom styles for the graph
def style_graph():
    """Applies custom styles to the graph axes and title."""
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_facecolor('#f0f0f0')
    ax.tick_params(axis='both', which='major', labelsize=10, color='black')

# Style the graph
style_graph()

# Add annotations
ax.text(50, 0, 0, "Center Point", color='red', fontsize=12)
ax.scatter([50], [0], [0], color='red', s=50)

# Display the static graph
plt.show()
