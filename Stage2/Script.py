import os
from graphviz import Source

source = """
digraph G{
ConversationSystem -> Greeting [style=bold];
ConversationSystem -> Farewell [style=bold];
Greeting -> Hello [style=bold];
Greeting -> Attribute;
Greeting -> Object [style=bold];
Attribute -> {Beautiful; Nice};
Object -> {Planet; World; UserInput};
Planet -> Attribute [style=dotted, label="<requires>"];
Farewell -> Bye [style=bold];
Bye -> {ByeWithComma; ByeWithExclamation};
Farewell -> Object;
UserInput -> ByeWithComma [style=dotted, label="<requires>"];

Attribute [style=dotted];
Object [peripheries=2];
Bye [peripheries=2];
}
"""

model = Source(source, filename="feature_model.gv", format="png")
model.view()

objectFarewell = input("Are we telling farewell to the object? [yes/no] ")
object = input("Which object do you want? [Planet/World/PrintUserInput] ")

if object == "World":
  isAttribute = input("Do you want an attribute? [yes/no] " )
elif object == "Planet":
  isAttribute = "yes"
else:
  os.system("java GetUserInput")
  isAttribute = input("Do you want an attribute? [yes/no] " )
if isAttribute == "yes":
  attribute = input("Which attribute do you want? [Nice/Beautiful] ")
  if attribute != "Nice" and attribute != "Beautiful":
    print("Wrong attribute, display default version")

os.system("java Hello")
if isAttribute == "yes":
  os.system("java " + attribute)
os.system("java " + object)
if objectFarewell == "yes":
  os.system("java Bye")
  os.system("java " + object)
else:
  os.system("java ByeEnd")
