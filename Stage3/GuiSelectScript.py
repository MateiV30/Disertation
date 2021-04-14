from tkinter import messagebox
from tkinter import *

def create_code():
    if selectedVariant.get() == 0:
            messagebox.showerror("Error", "Selecting a variant is required!")
    else:
        print("{} {}".format("selectedVariant =", selectedVariant.get()))

        findCounter = 1
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
                                                                        if findCounter == selectedVariant.get():
                                                                            print("{}{}".format("Found variant: ", findCounter))
                                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                        findCounter = findCounter+1
                                                                    elif user == "no":
                                                                        if findCounter == selectedVariant.get():
                                                                            print("{}{}".format("Found variant: ", findCounter))
                                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user))
                                                                        findCounter = findCounter+1
                                                    else:
                                                        if findCounter == selectedVariant.get():
                                                            print("{}{}".format("Found variant: ", findCounter))
                                                            print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view))
                                                        findCounter = findCounter+1
                                else:
                                    if findCounter == selectedVariant.get():
                                        print("{}{}".format("Found variant: ", findCounter))
                                        print("File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{}".format(read, animation, interact, keyboard, menu))
                                    findCounter = findCounter+1
                    else:
                        if findCounter == selectedVariant.get():
                            print("{}{}".format("Found variant: ", findCounter))
                            print("File:{} Animation:{} Interaction:{}".format(read, animation, interact))
                        findCounter = findCounter+1

        messagebox.showinfo("Success", "The required variant was created!")

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

window = Tk()
text=Text()
scrollbar = Scrollbar(window, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
text.pack(fill=BOTH, expand=True)


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

selectedVariant = IntVar()
counter = 1
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
                                                                radio = Radiobutton(window, text="File:{} Animation:{} Interaction:{} Keyboard:{} Menu:{} Orbits:{} Axes:{} Starfield:{} View:{} Movie:{} Earth:{} User:{}".format(read, animation, interact, keyboard, menu, orbit, axe, starfield, view, movie, earth, user),
                                                                                               variable=selectedVariant, value=counter)
                                                                #radio.pack()
                                                                text.window_create("end", window=radio)
                                                                text.insert("end", "\n")
                                                                counter = counter+1
                                                            elif user == "no":
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
