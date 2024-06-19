import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Link lengths
l1 = 1.0
l2 = 1.0

t = np.arange(0, 10, 0.1)
theta_d = 0.8 - 0.8 * np.cos(t)

theta1_range = theta_d
theta2_range = theta_d

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

(line,) = ax.plot([], [], "o-", lw=2)


def init():
    line.set_data([], [])
    return (line,)


def update(frame):
    theta1 = theta1_range[frame]
    theta2 = theta2_range[frame]

    # Compute positions
    x0, y0 = 0, 0
    x1, y1 = l1 * np.cos(theta1), l1 * np.sin(theta1)
    x2, y2 = x1 + l2 * np.cos(theta1 + theta2), y1 + l2 * np.sin(theta1 + theta2)

    # Update line data
    line.set_data([x0, x1, x2], [y0, y1, y2])
    return (line,)


# Create animation
ani = FuncAnimation(
    fig, update, frames=range(len(theta1_range)), init_func=init, blit=True
)

# Add title
plt.title("Trajectory Animation (x2)")


# Save as GIF
ani.save("trajectory reference.gif", writer=PillowWriter(fps=20))

plt.show()
