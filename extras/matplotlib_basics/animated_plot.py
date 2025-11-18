from typing import Callable
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def euler_solver(
    f: Callable, t: float, y: np.ndarray, h: float = 0.05, *args, **kwargs
) -> np.ndarray:
    """
    Euler method for numerically solving coupled ODEs.

    Parameters
    ----------
    f: Callable
        Function for the coupled ODEs you are trying to solve.
    t: float
        Independent variable, usually time.
    y: np.ndarray
        Array of current coupled ODE values.
    h: float, optional
        Step size for Euler Method (default is 0.05)

    Returns
    -------
    y_n+1: np.ndarray
        Next estimation step for estimating y(t)
    """
    return h * f(t, y, *args, **kwargs)


def oscillator(
    t: float, r: np.ndarray, omega: float = 1, m: float = 1, c: float = 0
) -> np.ndarray:
    """Coupled ODEs of a damped simple harmonic oscillator"""
    k = m * omega**2
    dx = r[1]
    dv = -c * dx - k * r[0]
    return np.array([dx, dv], float)


def make_animation():
    # Initializing plot
    f, ax = plt.subplots()

    # Number of time steps to run
    N = 1000

    # Creating empty arrays to store ODE info
    r_data = np.zeros((N, 2), float)
    sin_data = np.zeros(N, float)
    t_data = np.zeros(N, float)

    # Initial position and velocity of oscillator
    x0 = 0
    v0 = 8

    # Harmonic Oscillator Specs
    m = 1
    omega = 1
    c = 0 * np.sqrt(m * m * omega**2)

    # Putting initial values into info arrays
    r_data[0, :] = [x0, v0]  # position and velocity
    sin_data[0] = 0  # analytical solution of the harmonic oscillator
    t_data[0] = 0  # time values

    # Making plot objects
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
    ax.legend(loc="upper left")

    def step(frame):
        rnew = r_data[frame, :] + euler_solver(
            oscillator, frame, r_data[frame, :], m=m, omega=omega, c=c
        )
        r_data[frame + 1, :] = rnew
        sin_data[frame + 1] = (
            np.exp(-c * frame * 0.05) * v0 * np.sin(0.05 * frame)
        )
        t_data[frame + 1] = frame

        pt.set_data([frame], [r_data[frame, 0]])
        lin.set_data(t_data[:frame], r_data[:frame, 0])

        pt_real.set_data([frame], [sin_data[frame]])
        lin_real.set_data(t_data[:frame], sin_data[:frame])

        _ymin = np.min(r_data[: frame + 1])
        _ymax = np.max(r_data[: frame + 1])

        if _ymin < -15 or _ymax > 15:
            ax.set_ylim(_ymin - 0.05 * _ymin, _ymax + 0.05 * _ymax)

        return [pt]

    anim = FuncAnimation(  # noqa
        f,
        step,
        frames=N - 1,
        interval=1,
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
