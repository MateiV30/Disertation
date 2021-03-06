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

# Because it is C, need to pay particular attention to the order of funcitons

# The drawOrbit case is interesting as I had to keep a piece of code which would
# be useless if we choose to not have orbits but needs to be present to be able
# to have orbits if the user wants them.
# Having inneficienties created by the need to write versatile code
# Introduced a variable in the code to check if we actually have orbits selected

# If there are no requirements we have 4096 variants
# Introducing the requirements we remain with 460

readStyle = input("How do you want to input the planet data? [file/cmd] ")
drawAnimation = input("Do you want the planets moving? [yes/no] ")
print("Axes, starfield, orbits, multiple camera views require the ability to interact with the system!")
interaction = input("Do you want to be able to interact with the system? [yes/no] ")
if interaction == "yes":
    print("The player controlled camera view requires keyboard input!")
    keyboardControl = input("Do you want to be able to interact by using the keyboard? [yes/no] ")
    print("Axes, starfield, orbits, camera views and the player controlled view require having a menu!")
    drawMenu = input("Do you want a menu? [yes/no] ")
    if drawMenu == "yes":
        drawOrbits = input("Do you want orbits? [yes/no] ")
        drawStarfield = input("Do you want a starfield? [yes/no] ")
        drawAxes = input("Do you want axes? [yes/no] ")
        multipleCamera = input("Do you want more than the default static top camera view? [yes/no] ")
        if multipleCamera == "yes":
            earthView = input("Do you want earthView? [yes/no] ")
            movieView = input("Do you want movieView? [yes/no] ")
        else:
            earthView = "no"
            movieView = "no"
    else:
        drawOrbits = "no"
        drawStarfield = "no"
        drawAxes = "no"
    if keyboardControl == "yes" and drawMenu == "yes" and multipleCamera == "yes":
        playerView = input("Do you want playerView? [yes/no] ")
    else:
        playerView = "no"
else:
    keyboardControl = "no"
    drawMenu = "no"
    drawOrbits = "no"
    drawStarfield = "no"
    drawAxes = "no"
    multipleCamera = "no"
    earthView = "no"
    movieView = "no"
    playerView = "no"

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
    if drawOrbits == "yes":
        print("**Adding drawOrbits variable")
        writer.write("GLboolean have_Orbit = GL_TRUE;\n")
    else:
        writer.write("GLboolean have_Orbit = GL_FALSE;\n")
    writer.write("\n/*****************************/\n")
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
    if drawMenu == "yes" and multipleCamera == "yes":
        if earthView == "yes":
            writer.write("  case EARTH_VIEW:\n")
            writer.write("      x_earth = bodies[3].orbital_radius * sin((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component\n")
            writer.write("      z_earth = bodies[3].orbital_radius * cos((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component\n")
            writer.write("      gluLookAt(x_earth*1.1, 10000000, z_earth*1.1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );\n")
            writer.write("      break;\n")
        if movieView == "yes":
            writer.write("  case MOVIE_VIEW:\n")
            writer.write("      x_movie = bodies[3].orbital_radius * sinf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component\n")
            writer.write("      z_movie = bodies[3].orbital_radius * cosf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component\n")
            writer.write("      gluLookAt(x_movie+bodies[3].orbital_radius, bodies[3].orbital_radius, z_movie+bodies[3].orbital_radius, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );\n")
            writer.write("      break;\n")
        if playerView == "yes":
            writer.write("  case FLY_VIEW:\n")
            writer.write("      calculate_lookpoint(); /* Compute the centre of interest   */\n")
            writer.write("      gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz);\n")
            writer.write("      break;\n")
    writer.write("  }\n")
    writer.write("  glutPostRedisplay();\n")
    writer.write("}\n")
reader.close()
writer.close()

if drawMenu == "yes":
    print("Writing menu") ##################HOTSPOT#################################
    with open('menu.c', 'r') as reader:
        code = reader.read()
    with open('final.c', 'a') as writer:
        writer.write(code)
        if earthView == "yes":
            writer.write("  case 4: current_view= EARTH_VIEW;\n")
            writer.write("          break;\n")
        if movieView == "yes":
            writer.write("  case 5: current_view= MOVIE_VIEW;\n")
            writer.write("          break;\n")
        if playerView == "yes":
            writer.write("  case 6: current_view= FLY_VIEW;\n")
            writer.write("          break;\n")
        if drawOrbits == "yes":
            print("**Adding drawOrbits toggle")
            writer.write("  case 7: draw_orbits= !draw_orbits; break;\n")
        if drawStarfield == "yes":
            print("**Adding drawStarfield toggle")
            writer.write("  case 8: draw_starfield= !draw_starfield; break;\n")
        if drawAxes == "yes":
            print("**Adding drawAxes toggle")
            writer.write("  case 9: draw_Axes= !draw_Axes; break;\n")
        writer.write("  case 10: exit(0);\n")
        writer.write("  }\n")
        writer.write("}\n")
    reader.close()
    writer.close()

print("Writing initialization function") ###########HOTSPOT#####################
with open('init.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawMenu == "yes":
        print("**Adding default menu entries")
        writer.write('  glutCreateMenu (menu);\n')
        if multipleCamera == "yes":
            writer.write('  glutAddMenuEntry ("Top view", 1);\n')
        if earthView == "yes":
            print("**Adding earthView to menu")
            writer.write('  glutAddMenuEntry ("Earth view", 4);\n')
        if movieView == "yes":
            print("**Adding movieView to menu")
            writer.write('  glutAddMenuEntry ("Movie view", 5);\n')
        if playerView == "yes":
            print("**Adding playerView to menu")
            writer.write('  glutAddMenuEntry ("Fly view", 6);\n')
        writer.write('  glutAddMenuEntry ("", 999);\n')
        if drawOrbits == "yes":
            print("**Adding drawOrbits to menu")
            writer.write('  glutAddMenuEntry ("Toggle orbits", 7);\n')
        if drawStarfield == "yes":
            print("**Adding drawStarfield to menu")
            writer.write('  glutAddMenuEntry ("Toggle starfield", 8);\n')
        if drawAxes == "yes":
            print("**Adding drawAxes to menu")
            writer.write('  glutAddMenuEntry ("Toggle axes", 9);\n')
        writer.write('  glutAddMenuEntry ("", 999);\n')
        writer.write('  glutAddMenuEntry ("Quit", 10);\n')
        writer.write('  glutAttachMenu (GLUT_RIGHT_BUTTON);\n')
    if drawStarfield == "yes":
        print("**Initialize starfield")
        writer.write('  draw_starfield= 1;\n')
    writer.write("}\n")
reader.close()
writer.close()

if drawOrbits == "yes":
    print("Writing drawOrbit function")
    with open('drawOrbit.c', 'r') as reader:
        code = reader.read()
else:
    code = "\nvoid drawOrbit (int n) {}\n"
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

if drawAxes == "yes":
    print("Writing drawAxes function")
    with open('drawAxes.c', 'r') as reader:
        code = reader.read()
    with open('final.c', 'a') as writer:
        writer.write(code)
    reader.close()
    writer.close()

print("Writing display function") ##################HOTSPOT####################
with open('display.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawStarfield == "yes":
        print("**Adding drawStarfield check")
        writer.write("  if (draw_starfield) drawStarfield();\n")
    if drawAxes == "yes":
        print("**Adding drawAxes check")
        writer.write("  if (draw_Axes) drawAxes();\n")
    writer.write("  glutSwapBuffers();\n")
    writer.write("}\n")
reader.close()
writer.close()

print("Writing readSystem function")
if readStyle == "file":
  with open('readSystemFile.c', 'r') as reader:
      code = reader.read()
else:
  with open('readSystemCmd.c', 'r') as reader:
      code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
reader.close()
writer.close()

if drawAnimation == "yes":
    print("Writing animation function")
    with open('animate.c', 'r') as reader:
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

if keyboardControl == "yes":
    print("Writing keyboardControl functions")
    with open('keyboardControl.c', 'r') as reader:
        code = reader.read()
    with open('final.c', 'a') as writer:
        writer.write(code)
    reader.close()
    writer.close()

print("Writing the main function")
with open('main.c', 'r') as reader:
    code = reader.read()
with open('final.c', 'a') as writer:
    writer.write(code)
    if drawAnimation == "yes":
        print("**Adding animation")
        writer.write("  glutIdleFunc (animate);\n")
    if keyboardControl == "yes":
        print("**Adding keyboard control")
        writer.write("  glutKeyboardFunc (keyboard);\n")
        writer.write("  glutSpecialFunc (cursor_keys);\n")
    writer.write("  glutMainLoop();\n")
    writer.write("  return 0;\n")
    writer.write("}")
reader.close()
writer.close()
