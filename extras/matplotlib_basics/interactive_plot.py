from matplotlib.backend_bases import Event, MouseEvent
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


class InteractivePlot:
    def __init__(self, amplitude: float, freq: float):
        self.amp = amplitude
        self.freq = freq
        self.xdata = np.linspace(0, 10, 1000)

        # Setting up figure
        fig, self.main_ax = plt.subplots()
        self.canvas = fig.canvas

        fig.subplots_adjust(left=0.25, bottom=0.25)

        # Make a horizontal slider to control the frequency.
        self.axfreq = fig.add_axes((0.25, 0.1, 0.65, 0.03))
        self.axamp = fig.add_axes((0.1, 0.25, 0.0225, 0.63))

        self.freq_slider = Slider(
            self.axfreq, "Frequency", 1, 10, valinit=freq
        )
        self.amp_slider = Slider(
            self.axamp,
            "Amplitude",
            0,
            10,
            valinit=amplitude,
            orientation="vertical",
        )

        (self.sine_plot,) = self.main_ax.plot(
            self.xdata,
            self.amp * np.sin(self.freq * self.xdata),
            linestyle="-",
            color="red",
        )

        # Setting limits
        self.main_ax.set(xlim=(0, 10), ylim=(-10, 10))

        # Setting stats attribute
        self.stats = {"num_clicks": 0}

        self.canvas.mpl_connect("button_press_event", self.on_click)
        self.amp_slider.on_changed(self.on_changed)
        self.freq_slider.on_changed(self.on_changed)

    def on_click(self, event: Event):
        # Filters bad events
        if not isinstance(event, MouseEvent):
            return

        if event.inaxes != self.main_ax:
            return

        # Filtes clicks that are off the figure
        if event.xdata is not None and event.ydata is not None:
            self.main_ax.scatter(event.xdata, event.ydata, color="red")
            self.stats["num_clicks"] += 1
            print(
                f"You have clicked the plot {self.stats["num_clicks"]} times."
            )

        self.canvas.draw_idle()

    def on_changed(self, val: float):
        new_data = self.amp_slider.val * np.sin(
            self.freq_slider.val * self.xdata
        )
        self.sine_plot.set_data(self.xdata, new_data)
        self.canvas.draw_idle()

    def show(self):
        plt.show()


rng = np.random.default_rng()
data = rng.normal(0, 1, (100, 2))
my_interactive_plot = InteractivePlot(amplitude=4, freq=4)
my_interactive_plot.show()
