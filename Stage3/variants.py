cameraView = ["single", "multiple"]
interactions = ["yes", "no"]
keyboards = ["yes", "no"]
menus = ["yes", "no"]
reading = ["file", "cmd"]
orbits = ["yes", "no"]
axes = ["yes", "no"]
starfields = ["yes", "no"]
animations = ["yes", "no"]
movies = ["yes", "no"]
earths = ["yes", "no"]
users = ["yes", "no"]

f = open("variants.txt", "w")

counter = 0
for read in reading:
    for animation in animations:
        for interact in interactions:
            if interact == "yes":
                for keyboard in keyboards:
                    for menu in menus:
                        if menu == "yes":
                            for orbit in orbits:
                                for axe in axes:
                                    for starfield in starfields:
                                        for view in cameraView:
                                            if view == "multiple":
                                                for movie in movies:
                                                    for earth in earths:
                                                        for user in users:
                                                            if keyboard == "yes":
                                                                f.write("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}\n".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                counter = counter+1
                                                            elif user == "no":
                                                                f.write("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}\n".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                counter = counter+1
                                            else:
                                                f.write("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{}\n".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view))
                                                counter = counter+1
                        else:
                            f.write("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{}\n".format(read, animation, interact, keyboard, menu))
                            counter = counter+1
            else:
                f.write("File:{} Animation:{} Interaction:{}\n".format(read, animation, interact))
                counter = counter+1

print("{}{}".format("Number of variants: ", counter))

f.close()
