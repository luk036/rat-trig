import numpy as np
import matplotlib.pyplot as plt


def draw_rational_chart():
    fig, ax = plt.subplots(figsize=(8, 8))

    # 1. Draw the Boundary (The Unit Disk where Quadrance Q = 1)
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=2, label="Boundary (Q=1)")

    # 2. Draw Constant Quadrance "Circles" (Algebraic Distance)
    # Q = r^2. We pick rational steps for Q.
    quadrance_steps = [0.1, 0.3, 0.5, 0.7, 0.9]
    for q in quadrance_steps:
        r = np.sqrt(q)  # In RT, we plot the sqrt for the visual disk representation
        circle = plt.Circle(
            (0, 0), r, color="blue", fill=False, linestyle="--", alpha=0.5
        )
        ax.add_artist(circle)

    # 3. Draw Constant Spread "Lines" (Algebraic Phase)
    # In RT, spread is related to the 'opening' of the angle.
    # We plot rational directions: s = 0, 1/4, 1/2, 3/4, 1
    num_spread_lines = 12
    for i in range(num_spread_lines):
        angle = (i / num_spread_lines) * 2 * np.pi
        # These are the geodesics of the hyperbolic space
        x_vals = [0, np.cos(angle)]
        y_vals = [0, np.sin(angle)]
        ax.plot(x_vals, y_vals, color="red", alpha=0.3)

    # 4. Projective Point Plotting
    # Example: A mismatched load point
    z_load = 2 + 1j
    gamma = (z_load - 1) / (z_load + 1)
    ax.plot(gamma.real, gamma.imag, "go", markersize=10, label="Load Impedance")

    # Formatting
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.set_title("The Rational 'Smith' Chart (Universal Hyperbolic Grid)")
    ax.grid(True, which="both", linestyle=":", alpha=0.2)
    ax.legend()

    plt.show()


if __name__ == "__main__":
    draw_rational_chart()
