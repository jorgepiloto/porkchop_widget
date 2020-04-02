"""
File: porkchop_widget.py
Author: Jorge M.G.
Data: 2nd April, 2020
Description: The following file generates a GUI for solving porkchops making
             use of the poliastro software for the orbital mechanics
             computations and PySimpleGUI for the graphical user interface.
"""

# For building the GUI
import PySimpleGUI as sg

# Matplotlib utilities
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import our favourite library: poliastro
from poliastro.plotting.porkchop import porkchop
from poliastro.util import time_range

# Layouts are hosted in the design.py custom module
from design import main_layout, poliastro_bodies

# Generate main application window
window = sg.Window("Porkchop generator using poliastro", main_layout)


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Updates the canvas figure """

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def body_from_name(planet_name):
    """ Returns a poliastro body instance from name """

    for body in poliastro_bodies:
        if body.name.capitalize() == planet_name:
            return body
        else:
            continue

# Always show the window
while True:
    # Check for any signals
    event, values = window.Read()

    # If event is None or just Exit, close the application form
    if event in (None, "Exit"):
        break

    # For the Generate button, start solving the porkchop
    if event == "Generate":

        # Collect planets data
        body_dpt, body_arr = (
            body_from_name(values["dpt"]),
            body_from_name(values["arr"]),
        )

        # Collect dates data
        min_dpt, max_dpt = (
            values["min_dpt"].replace("/", "-"),
            values["max_dpt"].replace("/", "-", 2),
        )
        min_arr, max_arr = (
            values["min_arr"].replace("/", "-"),
            values["max_arr"].replace("/", "-", 2),
        )

        # Collect plotting options
        max_c3 = values["max_c3"]

        # Get CANVAS elements
        canvas = window["porkchop_canvas"].TKCanvas

        # Generate porkchop
        launch_span = time_range(min_dpt, end=max_dpt)
        arrival_span = time_range(min_arr, end=max_arr)
        dv_launch, dev_dpt, c3dpt, c3arr, tof = porkchop(
            body_dpt, body_arr, launch_span, arrival_span
        )

        # Draw the canvas figure
        fig = plt.gcf()
        fig.set_size_inches(5, 5)
        fig_porkchop = draw_figure(canvas, fig)
