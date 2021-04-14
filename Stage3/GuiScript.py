from tkinter import messagebox
from tkinter import *

def create_code():
    # print("{} {}".format("drawAnimation =", drawAnimation.get()))
    # print("{} {}".format("interaction =", interaction.get()))
    # print("{} {}".format("keyboardControl =", keyboardControl.get()))
    # print("{} {}".format("readStyle =", readStyle.get()))

    if readStyle.get() == 0:
        readStyleLabel.config(fg="red")
        messagebox.showerror("Error", "Selecting input method is required!")
    else:
        readStyleLabel.config(fg="black")
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
            if drawOrbits == 1:
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

        if drawStarfield.get() == 1:
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
            if multipleCamera.get() == 1:
                if earthView.get() == 1:
                    writer.write("  case EARTH_VIEW:\n")
                    writer.write("      x_earth = bodies[3].orbital_radius * sin((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component\n")
                    writer.write("      z_earth = bodies[3].orbital_radius * cos((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component\n")
                    writer.write("      gluLookAt(x_earth*1.1, 10000000, z_earth*1.1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );\n")
                    writer.write("      break;\n")
                if movieView.get() == 1:
                    writer.write("  case MOVIE_VIEW:\n")
                    writer.write("      x_movie = bodies[3].orbital_radius * sinf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component\n")
                    writer.write("      z_movie = bodies[3].orbital_radius * cosf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component\n")
                    writer.write("      gluLookAt(x_movie+bodies[3].orbital_radius, bodies[3].orbital_radius, z_movie+bodies[3].orbital_radius, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );\n")
                    writer.write("      break;\n")
                if playerView.get() == 1:
                    writer.write("  case FLY_VIEW:\n")
                    writer.write("      calculate_lookpoint(); /* Compute the centre of interest   */\n")
                    writer.write("      gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz);\n")
                    writer.write("      break;\n")
            writer.write("  }\n")
            writer.write("  glutPostRedisplay();\n")
            writer.write("}\n")
        reader.close()
        writer.close()

        if drawMenu.get() == 1:
            print("Writing menu") ##################HOTSPOT#################################
            with open('menu.c', 'r') as reader:
                code = reader.read()
            with open('final.c', 'a') as writer:
                writer.write(code)
                if earthView.get() == 1:
                    writer.write("  case 4: current_view= EARTH_VIEW;\n")
                    writer.write("          break;\n")
                if movieView.get() == 1:
                    writer.write("  case 5: current_view= MOVIE_VIEW;\n")
                    writer.write("          break;\n")
                if playerView.get() == 1:
                    writer.write("  case 6: current_view= FLY_VIEW;\n")
                    writer.write("          break;\n")
                if drawOrbits.get() == 1:
                    print("**Adding drawOrbits toggle")
                    writer.write("  case 7: draw_orbits= !draw_orbits; break;\n")
                if drawStarfield.get() == 1:
                    print("**Adding drawStarfield toggle")
                    writer.write("  case 8: draw_starfield= !draw_starfield; break;\n")
                if drawAxes.get() == 1:
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
            if drawMenu.get() == 1:
                print("**Adding default menu entries")
                writer.write('  glutCreateMenu (menu);\n')
                if multipleCamera.get() == 1:
                    writer.write('  glutAddMenuEntry ("Top view", 1);\n')
                if earthView.get() == 1:
                    print("**Adding earthView to menu")
                    writer.write('  glutAddMenuEntry ("Earth view", 4);\n')
                if movieView.get() == 1:
                    print("**Adding movieView to menu")
                    writer.write('  glutAddMenuEntry ("Movie view", 5);\n')
                if playerView.get() == 1:
                    print("**Adding playerView to menu")
                    writer.write('  glutAddMenuEntry ("Fly view", 6);\n')
                writer.write('  glutAddMenuEntry ("", 999);\n')
                if drawOrbits.get() == 1:
                    print("**Adding drawOrbits to menu")
                    writer.write('  glutAddMenuEntry ("Toggle orbits", 7);\n')
                if drawStarfield.get() == 1:
                    print("**Adding drawStarfield to menu")
                    writer.write('  glutAddMenuEntry ("Toggle starfield", 8);\n')
                if drawAxes.get() == 1:
                    print("**Adding drawAxes to menu")
                    writer.write('  glutAddMenuEntry ("Toggle axes", 9);\n')
                writer.write('  glutAddMenuEntry ("", 999);\n')
                writer.write('  glutAddMenuEntry ("Quit", 10);\n')
                writer.write('  glutAttachMenu (GLUT_RIGHT_BUTTON);\n')
            if drawStarfield.get() == 1:
                print("**Initialize starfield")
                writer.write('  draw_starfield= 1;\n')
            writer.write("}\n")
        reader.close()
        writer.close()

        if drawOrbits.get() == 1:
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

        if drawAxes.get() == 1:
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
            if drawStarfield.get() == 1:
                print("**Adding drawStarfield check")
                writer.write("  if (draw_starfield) drawStarfield();\n")
            if drawAxes.get() == 1:
                print("**Adding drawAxes check")
                writer.write("  if (draw_Axes) drawAxes();\n")
            writer.write("  glutSwapBuffers();\n")
            writer.write("}\n")
        reader.close()
        writer.close()

        print("Writing readSystem function")
        if readStyle.get() == 1:
          print("**Adding file reading")
          with open('readSystemFile.c', 'r') as reader:
              code = reader.read()
        elif readStyle == 2:
          print("**Adding cmd reading")
          with open('readSystemCmd.c', 'r') as reader:
              code = reader.read()
        with open('final.c', 'a') as writer:
            writer.write(code)
        reader.close()
        writer.close()

        if drawAnimation.get() == 1:
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

        if keyboardControl.get() == 1:
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
            if drawAnimation.get() == 1:
                print("**Adding animation")
                writer.write("  glutIdleFunc (animate);\n")
            if keyboardControl.get() == 1:
                print("**Adding keyboard control")
                writer.write("  glutKeyboardFunc (keyboard);\n")
                writer.write("  glutSpecialFunc (cursor_keys);\n")
            writer.write("  glutMainLoop();\n")
            writer.write("  return 0;\n")
            writer.write("}")
        reader.close()
        writer.close()

        messagebox.showinfo("Success", "The required variant was created!")

def toggle_interaction_dependencies():
    if check_keyboarControl['state'] == NORMAL:
        check_keyboarControl['state'] = DISABLED
        keyboardControlText.set("Keyboard Control - Requires interaction with the system!")
        keyboardControl.set(0)
    else:
        check_keyboarControl['state'] = NORMAL
        keyboardControlText.set("Keyboard Control")

    if check_drawMenu['state'] == NORMAL:
        check_drawMenu['state'] = DISABLED
        drawMenuText.set("Create Menu - Requires interaction with the system!")
        drawMenu.set(0)
    else:
        check_drawMenu['state'] = NORMAL
        drawMenuText.set("Create Menu")

    if check_drawOrbits['state'] == NORMAL:
        check_drawOrbits['state'] = DISABLED
        drawOrbitsText.set("Draw orbits - Requires having a menu!")
        drawOrbits.set(0)

    if check_drawStarfield['state'] == NORMAL:
        check_drawStarfield['state'] = DISABLED
        drawStarfieldText.set("Draw a starfield - Requires having a menu!")
        drawStarfield.set(0)

    if check_drawAxes['state'] == NORMAL:
        check_drawAxes['state'] = DISABLED
        drawAxesText.set("Draw system axes - Requires having a menu!")
        drawAxes.set(0)

    if check_multipleCamera['state'] == NORMAL:
        check_multipleCamera['state'] = DISABLED
        multipleCameraText.set("Have multiple camera views - Requires having a menu!")
        multipleCamera.set(0)

    if check_earthView['state'] == NORMAL:
        check_earthView['state'] = DISABLED
        earthViewText.set("Camera view from earth perspective - Requires multiple camera views!")
        earthView.set(0)

    if check_movieView['state'] == NORMAL:
        check_movieView['state'] = DISABLED
        movieViewText.set("Camera view moving in an established pattern - Requires multiple camera views!")
        movieView.set(0)

def toggle_menu_dependencies():
    if check_drawOrbits['state'] == NORMAL:
        check_drawOrbits['state'] = DISABLED
        drawOrbitsText.set("Draw orbits - Requires having a menu!")
        drawOrbits.set(0)
    else:
        check_drawOrbits['state'] = NORMAL
        drawOrbitsText.set("Draw orbits")

    if check_drawStarfield['state'] == NORMAL:
        check_drawStarfield['state'] = DISABLED
        drawStarfieldText.set("Draw a starfield - Requires having a menu!")
        drawStarfield.set(0)
    else:
        check_drawStarfield['state'] = NORMAL
        drawStarfieldText.set("Draw a starfield")

    if check_drawAxes['state'] == NORMAL:
        check_drawAxes['state'] = DISABLED
        drawAxesText.set("Draw system axes - Requires having a menu!")
        drawAxes.set(0)
    else:
        check_drawAxes['state'] = NORMAL
        drawAxesText.set("Draw system axes")

    if check_multipleCamera['state'] == NORMAL:
        check_multipleCamera['state'] = DISABLED
        multipleCameraText.set("Have multiple camera views - Requires having a menu!")
        multipleCamera.set(0)
    else:
        check_multipleCamera['state'] = NORMAL
        multipleCameraText.set("Have multiple camera views")

    if check_earthView['state'] == NORMAL:
        check_earthView['state'] = DISABLED
        earthViewText.set("Camera view from earth perspective - Requires multiple camera views!")
        earthView.set(0)

    if check_movieView['state'] == NORMAL:
        check_movieView['state'] = DISABLED
        movieViewText.set("Camera view moving in an established pattern - Requires multiple camera views!")
        movieView.set(0)

def toggle_multipleCamera_dependencies():
    if check_earthView['state'] == NORMAL:
        check_earthView['state'] = DISABLED
        earthViewText.set("Camera view from earth perspective - Requires multiple camera views!")
        earthView.set(0)
    else:
        check_earthView['state'] = NORMAL
        earthViewText.set("Camera view from earth perspective")

    if check_movieView['state'] == NORMAL:
        check_movieView['state'] = DISABLED
        movieViewText.set("Camera view moving in an established pattern - Requires multiple camera views!")
        movieView.set(0)
    else:
        check_movieView['state'] = NORMAL
        movieViewText.set("Camera view moving in an established pattern")

    if check_playerView['state'] == NORMAL:
        check_playerView['state'] = DISABLED
        playerViewText.set("User controlled camera - Requires multiple camera views and keyboard control!")
        playerView.set(0)
    elif keyboardControl.get() == 1:
        check_playerView['state'] = NORMAL
        playerViewText.set("User controlled camera")

def toggle_keyboardControl_dependencies():
    if check_playerView['state'] == NORMAL:
        check_playerView['state'] = DISABLED
        playerViewText.set("User controlled camera - Requires multiple camera views and keyboard control!")
        playerView.set(0)
    elif multipleCamera.get() == 1:
        check_playerView['state'] = NORMAL
        playerViewText.set("User controlled camera")

window = Tk()

######################## readStyle ######################################
readStyleFrame = Frame()
readStyle = IntVar()
readStyleLabelText = StringVar()
readStyleLabelText.set("How do you want to input planet data?: (Required)")
readStyleLabel = Label(master=readStyleFrame, textvariable=readStyleLabelText)
readStyleLabel.pack()
radio1_readStyle = Radiobutton(master=readStyleFrame, text="From file named 'sys'",
                               variable=readStyle, value=1)
radio1_readStyle.pack()
radio2_readStyle = Radiobutton(master=readStyleFrame, text="Manually from cmd",
                               variable=readStyle, value=2)
radio2_readStyle.pack()
readStyleFrame.pack()
######################## drawAnimation ######################################
drawAnimation = IntVar()
check_drawAnimation = Checkbutton(window, text = "Planet animation", variable = drawAnimation)
check_drawAnimation.pack()
######################## interaction ######################################
interaction = IntVar()
check_interaction = Checkbutton(window, text="Interaction with the system",
                                variable=interaction, command=toggle_interaction_dependencies)
check_interaction.pack()
######################## keyboardControl ######################################
keyboardControl = IntVar()
keyboardControlText = StringVar()
keyboardControlText.set("Keyboard Control - Requires interaction with the system!")
check_keyboarControl = Checkbutton(window, textvariable=keyboardControlText,
                                 variable=keyboardControl, command=toggle_keyboardControl_dependencies)
check_keyboarControl['state'] = DISABLED
check_keyboarControl.pack()
######################## drawMenu ######################################
drawMenu = IntVar()
drawMenuText = StringVar()
drawMenuText.set("Create Menu - Requires interaction with the system!")
check_drawMenu = Checkbutton(window, textvariable=drawMenuText, variable=drawMenu,
                              command=toggle_menu_dependencies)
check_drawMenu['state'] = DISABLED
check_drawMenu.pack()
######################## drawOrbits ######################################
drawOrbits = IntVar()
drawOrbitsText = StringVar()
drawOrbitsText.set("Draw orbits - Requires having a menu!")
check_drawOrbits = Checkbutton(window, textvariable=drawOrbitsText, variable=drawOrbits)
check_drawOrbits['state'] = DISABLED
check_drawOrbits.pack()
######################## drawStarfield ######################################
drawStarfield = IntVar()
drawStarfieldText = StringVar()
drawStarfieldText.set("Draw a starfield - Requires having a menu!")
check_drawStarfield = Checkbutton(window, textvariable=drawStarfieldText, variable=drawStarfield)
check_drawStarfield['state'] = DISABLED
check_drawStarfield.pack()
######################## drawAxes ######################################
drawAxes = IntVar()
drawAxesText = StringVar()
drawAxesText.set("Draw system axes - Requires having a menu!")
check_drawAxes = Checkbutton(window, textvariable=drawAxesText, variable=drawAxes)
check_drawAxes['state'] = DISABLED
check_drawAxes.pack()
######################## multipleCamera ######################################
multipleCamera = IntVar()
multipleCameraText = StringVar()
multipleCameraText.set("Have multiple camera views - Requires having a menu!")
check_multipleCamera = Checkbutton(window, textvariable=multipleCameraText,
                                   variable=multipleCamera, command=toggle_multipleCamera_dependencies)
check_multipleCamera['state'] = DISABLED
check_multipleCamera.pack()
######################## earthView ######################################
earthView = IntVar()
earthViewText = StringVar()
earthViewText.set("Camera view from earth perspective - Requires multiple camera views!")
check_earthView = Checkbutton(window, textvariable=earthViewText, variable=earthView)
check_earthView['state'] = DISABLED
check_earthView.pack()
######################## movieView ######################################
movieView = IntVar()
movieViewText = StringVar()
movieViewText.set("Camera view moving in an established pattern - Requires multiple camera views!")
check_movieView = Checkbutton(window, textvariable=movieViewText, variable=movieView)
check_movieView['state'] = DISABLED
check_movieView.pack()
######################## playerView ######################################
playerView = IntVar()
playerViewText = StringVar()
playerViewText.set("User controlled camera - Requires multiple camera views and keyboard control!")
check_playerView = Checkbutton(window, textvariable=playerViewText, variable=playerView)
check_playerView['state'] = DISABLED
check_playerView.pack()

btn_create = Button(window, text = "Create the code!", command = create_code)
btn_create.pack()

window.mainloop()
