import os
from graphviz import Source

source = """
digraph G{
CameraView [style=dotted];
A [label="Reading planet data"];
B [label="Ability to toggle features"];
C [label="Single camera view"];
D [label="Multiple camera views", style=dotted];
E [label="Camera moving in a pattern"];
F [label="Camera moving from user input"];
SolarSystem -> KeyboardControl;
SolarSystem -> A [style=bold];
SolarSystem -> PlanetAnimation [style=bold];
SolarSystem -> CameraView [style=bold];
SolarSystem -> Menu;
SolarSystem -> B;
SolarSystem -> Axes;
SolarSystem -> StarField;
B -> Menu [style=dotted, label="<requires>"];
CameraView -> C;
CameraView -> D;
D -> B [style=dotted, label="<requires>"];
D -> StaticCamera;
D -> E;
D -> F;
F -> KeyboardControl [style=dotted, label="<requires>"];
Axes -> B [style=dotted, label="<requires>"];
StarField -> B [style=dotted, label="<requires>"];
}
"""
#
model = Source(source, filename="feature_model.gv", format="png")
model.view()

# Greeting -> Hello [style=bold];
# Greeting -> Attribute;
# Greeting -> Object [style=bold];
# Attribute -> {Beautiful; Nice};
# Object -> {Planet; World; UserInput};
# Planet -> Attribute [style=dotted, label="<requires>"];
# Farewell -> Bye [style=bold];
# Bye -> {ByeWithComma; ByeWithExclamation};
# Farewell -> Object;
# UserInput -> ByeWithComma [style=dotted, label="<requires>"];
#
# Attribute [style=dotted];
# Object [peripheries=2];
# Bye [peripheries=2];
