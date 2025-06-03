import numpy as np
import matplotlib.pyplot as plt


def plot_random(N: int) -> float:
    """
    Makes a scatter plot of some random numbers.

    Parameters
    ----------
    N: int
        Number of points to plot.

    Returns
    -------
    mu: float
        Mean X coordinate of random numbers.
    """
    rng = np.random.default_rng()
    x = rng.normal(3, 3, N)
    y = rng.normal(0, 2, N)
    plt.scatter(x, y, marker='x', color='red')
    print("TEST")

    return np.mean(x)


if __name__ == "__main__":
    mu = plot_random(500)
    print(f"Mean X of Data: {mu:.3f}")
    plt.show()
