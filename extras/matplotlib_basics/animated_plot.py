from typing import Callable
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def euler_solver(
    f: Callable, t: float, y: np.ndarray, h: float = 0.05
) -> np.ndarray:
    return h * f(t, y)


def oscillator(
    t: float, r: np.ndarray, omega: float = 1, m: float = 1
) -> np.ndarray:
    """DiffEQ of a simple harmonic oscillator"""
    k = m * omega**2
    dx = r[1]
    dv = -k * r[0]
    return np.array([dx, dv], float)


def make_animation():
    f, ax = plt.subplots()
    x0 = 0
    v0 = 8
    N = 1000
    r_data = np.zeros((N, 2), float)
    sin_data = np.zeros(N, float)
    t_data = np.zeros(N, float)
    r_data[0, :] = [x0, v0]
    sin_data[0] = 0
    t_data[0] = 0
    (pt,) = plt.plot(0, r_data[0, 0], color="k", marker="o")
    (lin,) = plt.plot(
        0,
        r_data[0, 0],
        color="k",
        linestyle="--",
        label="Euler Solver Oscillator",
    )
    (pt_real,) = plt.plot(0, 0, color="r", marker="o")
    (lin_real,) = plt.plot(
        0, 0, color="r", linestyle="--", label="Real Harmonic Oscillator"
    )
    ax.set_ylim(-15, 15)
    ax.set_xlim(0, N)
    ax.legend()

    def step(frame):
        rnew = r_data[frame, :] + euler_solver(
            oscillator, frame, r_data[frame, :]
        )
        r_data[frame + 1, :] = rnew
        sin_data[frame + 1] = v0 * np.sin(0.05 * frame)
        t_data[frame + 1] = frame

        pt.set_data([frame], [r_data[frame, 0]])
        lin.set_data(t_data[:frame], r_data[:frame, 0])

        pt_real.set_data([frame], [v0 * np.sin(frame * 0.05)])
        lin_real.set_data(t_data[:frame], sin_data[:frame])
        return [pt]

    anim = FuncAnimation(  # noqa
        f,
        step,
        frames=N - 1,
        interval=5,
    )
    plt.show()
    # anim.save("./animation.gif")


if __name__ == "__main__":
    make_animation()

# def make_animation():
#     # Initializing plot
#     f, ax = plt.subplots()

#     omega =

#     def step(frame: int):
#         ax.scatter(frame, sine(frame))
