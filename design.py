"""
Holds all the different layouts
"""

import PySimpleGUI as sg
from poliastro.bodies import (
    Earth,
    Jupiter,
    Mars,
    Mercury,
    Neptune,
    Saturn,
    Uranus,
    Venus,
)

poliastro_bodies = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
planet_colletion = tuple([planet.name for planet in poliastro_bodies])

# Colorscheme
sg.theme("LightGrey1")

# Enables user to select departure planet and arrival one from a list
bodies_layout = [
    [sg.Text("Departure"), sg.Text("Arrival")],
    [
        sg.InputCombo(planet_colletion, default_value="Earth", key="dpt"),
        sg.InputCombo((planet_colletion), default_value="Mars", key="arr"),
    ],
]

# Enables user to select launching span conditions
launch_layout = [
    [
        sg.Text("Min. launch date", size=(16, 1)),
        sg.InputText("2005/04/30", size=(10, 1), key="min_dpt"),
    ],
    [
        sg.Text("Max. launch date", size=(16, 1)),
        sg.InputText("2005/10/07", size=(10, 1), key="max_dpt"),
    ],
]

# Enables user to select arrival span conditions
arrival_layout = [
    [
        sg.Text("Min. arrival date", size=(16, 1)),
        sg.InputText("2005/11/16", size=(10, 1), key="min_arr"),
    ],
    [
        sg.Text("Max. arrival date", size=(16, 1)),
        sg.InputText("2006/12/21", size=(10, 1), key="max_arr"),
    ],
]

# Enables user to select plotting configurations
plotting_layout = [
    [
        sg.Text("Max. C3 energy in km2/s2", size=(22, 1)),
        sg.InputText("45.00", size=(10, 1), key="max_c3"),
    ],
]

# Arrange all previous options into one single frame named 'Options'
options_layout = [
    [
        sg.Frame(
            layout=bodies_layout,
            title="Bodies",
            title_color="black",
            font=("Courier", 12, "bold"),
        )
    ],
    [
        sg.Frame(
            layout=launch_layout,
            title="Launch       YYYY/MM/DD",
            title_color="black",
            font=("Courier", 12, "bold"),
        )
    ],
    [
        sg.Frame(
            layout=arrival_layout,
            title="Arrival      YYYY/MM/DD",
            title_color="black",
            font=("Courier", 12, "bold"),
        )
    ],
    [
        sg.Frame(
            layout=plotting_layout,
            title="Plotting options",
            title_color="black",
            font=("Courier", 12, "bold"),
        )
    ],
    [sg.Button("Generate"), sg.Button("Clear"), sg.Button("Exit")],
]

# Main layout for the application
main_layout = [
    [
        sg.Canvas(size=(600, 500), background_color="black", key="porkchop_canvas"),
        sg.Frame(layout=options_layout, title="Options", font=("Courier", 12, "bold")),
    ]
]
