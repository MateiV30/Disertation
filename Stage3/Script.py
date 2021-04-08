# Initial approach, just combine precompiled code. Because liniar execution,
# no interferance between features.
# 3d animation is a continuous loop which makes the feature integration a lot
# more complicated
#
# Build code in steps
# First header then functions
# Put functions inside text files.
# Some headers and functions will be the default code.
# Add bits of code as fucntions

# Write the bits of code from txt files to a new c file

# Important components, where the code is written and where the code is combined
# Need to identify the combination hotspots: the main function, the init function,
# the viewpoint function

drawStarfield = input("Do you want a starfield [yes/no] ")

print("Writing header")
with open('headers.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'w') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing variables")
with open('variables.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing randomisation function")
with open('myRand.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

if drawStarfield == "yes":
    print("Writing drawStarfield")
    with open('drawStarfield.c', 'r') as reader:
        code = reader.read()
    with open('final.c', 'a') as writer:
        writer.write(code)
    reader.close()
    writer.close()

print("Writing calculate_lookpoint function")
with open('calculate_lookpoint.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing set view function")
with open('setView.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing menu")
with open('menu.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawStarfield == "yes":
        print("**Adding drawStarfield toggle")
        writer.write("  case 9: draw_starfield= !draw_starfield; break;\n")
    writer.write("  case 10: exit(0);\n")
    writer.write("  }\n")
    writer.write("}\n")
reader.close()
writer.close()

print("Writing initialization function")
with open('init.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawStarfield == "yes":
        print("**Adding drawStarfield to menu")
        writer.write('  glutAddMenuEntry ("Toggle starfield", 9);\n')
    writer.write('  glutAddMenuEntry ("", 999);\n')
    writer.write('  glutAddMenuEntry ("Quit", 10);\n')
    writer.write('  glutAttachMenu (GLUT_RIGHT_BUTTON);\n')
    if drawStarfield == "yes":
        print("**Initialize starfield")
        writer.write('  draw_starfield= 1;\n')
    writer.write("}\n")
reader.close()
writer.close()

print("Writing drawOrbit function")
with open('drawOrbit.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing drawBody function")
with open('drawBody.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing drawAxes function")
with open('drawAxes.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing display function")
with open('display.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawStarfield == "yes":
        print("**Adding drawStarfield check")
        writer.write("  if (draw_starfield) drawStarfield();\n")
    writer.write("  glutSwapBuffers();\n")
    writer.write("}\n")
reader.close()
writer.close()

print("Writing readSystem function")
with open('readSystem.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

print("Writing rest of code")
with open('remaining.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()
