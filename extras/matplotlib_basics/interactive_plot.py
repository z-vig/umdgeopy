from matplotlib.backend_bases import Event, MouseEvent
import matplotlib.pyplot as plt
import numpy as np


class InteractivePlot:
    def __init__(self, data: np.ndarray):
        _fig, self.main_ax = plt.subplots()
        self.canvas = _fig.canvas
        self.main_ax.set(xlim=(0, 10), ylim=(0, 10))

        self.stats = {"num_clicks": 0}

        self.canvas.mpl_connect("button_press_event", self.on_click)

    def on_click(self, event: Event):
        if not isinstance(event, MouseEvent):
            return
        if event.xdata is not None and event.ydata is not None:
            self.main_ax.scatter(event.xdata, event.ydata)
            self.stats["num_clicks"] += 1
            print(
                f"You have clicked the plot {self.stats["num_clicks"]} times."
            )

        self.canvas.draw_idle()

    def show(self):
        plt.show()


rng = np.random.default_rng()
data = rng.normal(0, 1, (100, 2))
my_interactive_plot = InteractivePlot(data)
my_interactive_plot.show()
