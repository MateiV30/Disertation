from tkinter import messagebox
from tkinter import *

cameraView = [1, 2]#["single", "multiple"]
interactions = [1, 2]#["yes", "no"]
keyboards = [1, 2]
menus = [1, 2]
reading = [1, 2]#["file", "cmd"]
orbits = [1, 2]
axes = [1, 2]
starfields = [1, 2]
animations = [1, 2]
movies = [1, 2]
earths = [1, 2]
users = [1, 2]


def create_code():
    if selectedVariant.get() == 0:
            messagebox.showerror("Error", "Selecting a variant is required!")
    else:
        print("{} {}".format("selectedVariant =", selectedVariant.get()))

        findCounter = 1
        for read in reading:
            for animation in animations:
                for interact in interactions:
                    if interact == 1:
                        for keyboard in keyboards:
                            for menu in menus:
                                if menu == 1:
                                    for orbit in orbits:
                                        for axe in axes:
                                            for starfield in starfields:
                                                for view in cameraView:
                                                    if view == 2:
                                                        for movie in movies:
                                                            for earth in earths:
                                                                for user in users:
                                                                    if keyboard == 1:
                                                                        if findCounter == selectedVariant.get():
                                                                            print("{}{}".format("Found variant: ", findCounter))
                                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                            readStyle.set(read)
                                                                            drawAnimation.set(animation)
                                                                            keyboardControl.set(keyboard)
                                                                            interaction.set(interact)
                                                                            drawMenu.set(menu)
                                                                            drawOrbits.set(orbit)
                                                                            drawStarfield.set(starfield)
                                                                            drawAxes.set(axe)
                                                                            multipleCamera.set(view)
                                                                            earthView.set(earth)
                                                                            movieView.set(movie)
                                                                            playerView.set(user)
                                                                        findCounter = findCounter+1
                                                                    elif user == 2:
                                                                        if findCounter == selectedVariant.get():
                                                                            print("{}{}".format("Found variant: ", findCounter))
                                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                            readStyle.set(read)
                                                                            drawAnimation.set(animation)
                                                                            keyboardControl.set(keyboard)
                                                                            interaction.set(interact)
                                                                            drawMenu.set(menu)
                                                                            drawOrbits.set(orbit)
                                                                            drawStarfield.set(starfield)
                                                                            drawAxes.set(axe)
                                                                            multipleCamera.set(view)
                                                                            earthView.set(earth)
                                                                            movieView.set(movie)
                                                                            playerView.set(user)
                                                                        findCounter = findCounter+1
                                                    else:
                                                        if findCounter == selectedVariant.get():
                                                            print("{}{}".format("Found variant: ", findCounter))
                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view))
                                                            readStyle.set(read)
                                                            drawAnimation.set(animation)
                                                            keyboardControl.set(keyboard)
                                                            interaction.set(interact)
                                                            drawMenu.set(menu)
                                                            drawOrbits.set(orbit)
                                                            drawStarfield.set(starfield)
                                                            drawAxes.set(axe)
                                                            multipleCamera.set(view)
                                                            earthView.set(earth)
                                                            movieView.set(movie)
                                                            playerView.set(user)
                                                        findCounter = findCounter+1
                                else:
                                    if findCounter == selectedVariant.get():
                                        print("{}{}".format("Found variant: ", findCounter))
                                        print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{}".format(read, animation, interact, keyboard, menu))
                                        readStyle.set(read)
                                        drawAnimation.set(animation)
                                        keyboardControl.set(keyboard)
                                        interaction.set(interact)
                                        drawMenu.set(menu)
                                        drawOrbits.set(orbit)
                                        drawStarfield.set(starfield)
                                        drawAxes.set(axe)
                                        multipleCamera.set(view)
                                        earthView.set(earth)
                                        movieView.set(movie)
                                        playerView.set(user)
                                    findCounter = findCounter+1
                    else:
                        if findCounter == selectedVariant.get():
                            print("{}{}".format("Found variant: ", findCounter))
                            print("File:{} Animation:{} Interaction:{}".format(read, animation, interact))
                            readStyle.set(read)
                            drawAnimation.set(animation)
                            keyboardControl.set(keyboard)
                            interaction.set(interact)
                            drawMenu.set(menu)
                            drawOrbits.set(orbit)
                            drawStarfield.set(starfield)
                            drawAxes.set(axe)
                            multipleCamera.set(view)
                            earthView.set(earth)
                            movieView.set(movie)
                            playerView.set(user)
                        findCounter = findCounter+1

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
            if drawOrbits.get() == 1:
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


window = Tk()

readStyle = IntVar()
drawAnimation = IntVar()
interaction = IntVar()
keyboardControl = IntVar()
drawMenu = IntVar()
drawOrbits = IntVar()
drawStarfield = IntVar()
drawAxes = IntVar()
multipleCamera = IntVar()
earthView = IntVar()
movieView = IntVar()
playerView = IntVar()

text=Text()
scrollbar = Scrollbar(window, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
text.pack(fill=BOTH, expand=True)


selectedVariant = IntVar()
counter = 1
for read in reading:
    for animation in animations:
        for interact in interactions:
            if interact == 1:
                for keyboard in keyboards:
                    for menu in menus:
                        if menu == 1:
                            for orbit in orbits:
                                for axe in axes:
                                    for starfield in starfields:
                                        for view in cameraView:
                                            if view == 2:
                                                for movie in movies:
                                                    for earth in earths:
                                                        for user in users:
                                                            if keyboard == 1:
                                                                radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user),
                                                                                               variable=selectedVariant, value=counter)
                                                                #radio.pack()
                                                                text.window_create("end", window=radio)
                                                                text.insert("end", "\n")
                                                                counter = counter+1
                                                            elif user == 2:
                                                                radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user),
                                                                                               variable=selectedVariant, value=counter)
                                                                #radio.pack()
                                                                text.window_create("end", window=radio)
                                                                text.insert("end", "\n")
                                                                counter = counter+1
                                            else:
                                                radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view),
                                                                               variable=selectedVariant, value=counter)
                                                #radio.pack()
                                                text.window_create("end", window=radio)
                                                text.insert("end", "\n")
                                                counter = counter+1
                        else:
                            radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{}".format(read, animation, interact, keyboard, menu),
                                                           variable=selectedVariant, value=counter)
                            #radio.pack()
                            text.window_create("end", window=radio)
                            text.insert("end", "\n")
                            counter = counter+1
            else:
                radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{}".format(read, animation, interact),
                                               variable=selectedVariant, value=counter)
                #radio.pack()
                text.window_create("end", window=radio)
                text.insert("end", "\n")
                counter = counter+1


btn_create = Button(window, text = "Create the code!", command = create_code)
btn_create.pack()

window.mainloop()
