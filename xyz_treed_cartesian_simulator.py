# 23.10.2020
# Project Name: XYZ 3D CARTESİAN SİMULATOR
# Project Destination : G-CODE PARSER
# Author : DOGUKAN DUGUN


from tkinter.filedialog import *

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
import threading

from matplotlib.figure import Figure

text1 = ""


def SelectFile():
    file1 = askopenfilename()
    global text1
    text1 = file1
    btwritefile.invoke()
    if file1:
        text2.config(text=file1)

    else:
        text2.config(text="File Not Selected")


def WriteFile():
    linenumber = 0
    gcode = open(text1, "r", encoding="utf-8")

    for i in gcode:
        linenumber += 1

    gcode = open(text1, "r", encoding="utf-8")
    kline = 0
    i = 0



    global corx
    corx = []
    global cory
    cory = []
    global corz
    corz = []

    while kline < linenumber:

        kline += 1
        # print(str(kline) + ". satıra girdi-----------")
        global z
        z = gcode.readline()

        # print(z, end="")
        while i < len(z) + 1:

            # print(str(kline) + ".satırda")
            # print(str(i) + ".indexe baktı")

            if z[i] == ";" or i == len(z) - 1:

                i = 0
                break

            elif z[i] == "Z":
                counter2 = 0
                s = i

                while z[s] != " " and i < len(z) - 1:
                    i += 1
                    counter2 += 1
                    s += 1
                i = i - counter2

                corz.append(z[i + 1:i + counter2])
            elif z[i] == "X":
                counter2 = 0

                s = i

                while z[s] != " ":
                    counter2 += 1
                    s = s + 1

                corx.append(z[i + 1:i + counter2])

            elif z[i] == "Y":
                counter2 = 0
                s = i

                while z[s] != " " and i < len(z) - 2:
                    i += 1
                    counter2 += 1
                    s += 1
                i = i - counter2

                cory.append(z[i + 1:i + counter2])

            i += 1

    for ii in range(0, len(corx)):
        corx[ii] = float(corx[ii])
    for ii in range(0, len(cory)):
        try:
            cory[ii] = float(cory[ii])
        except ValueError:
            cory[ii] = cory[ii - 1]

    for ii in range(0, len(corz)):
        corz[ii] = float(corz[ii])

    global corx_iter
    corx_iter = iter(corx)
    global cory_iter
    cory_iter = iter(cory)

    global corz_iter
    corz_iter = iter(corz)
    # print("VAR OLAN TÜM X KORDİNATLARI :", end="")
    # print(corx)
    # print("VAR OLAN TÜM Y KORDİNATLARI :", end="")
    # print(cory)
    # print("VAR OLAN TÜM Z KODLARI :", end="")
    # print(corz)


# --------------------------------------------------------------------------------------------------------------
form = tk.Tk()
form.state("zoomed")
fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=form)
canvas.get_tk_widget().place(x=600, y=10)
a = fig.add_subplot(projection='3d')
form.title("XYZ CARTESIAN COORDINATE SIMULATOR")
t = 1
a.plot(5, 5)

a.set_xlabel("x koordinatı")
a.set_ylabel("y koordinatı")
a.set_zlabel("z koordinatı")

x = [235, -235]
y = [-235, -235]
z = [-235, -235]

x1 = [-235, 235]
y1 = [235, 235]
z1 = [-235, -235]

x2 = [0, 0]
y2 = [235, 235]
z2 = [-235, 235]

x3 = [0, 0]
y3 = [-235, -235]
z3 = [-235, 235]

x4 = [0, 0]
y4 = [235, -235]
z4 = [0, 0]

a.plot3D(x, y, z, c="b")
a.plot3D(x1, y1, z1, c="b")
a.plot3D(x2, y2, z2, c="g")
a.plot3D(x3, y3, z3, c="g")
a.plot3D(x4, y4, z4)

a.scatter(0, 0, 0, c="r", s=250)
a.scatter(0, -235, -235, c="b")
a.scatter(0, 235, -235, c="b")
a.scatter(0, -235, 0, c="g")
a.scatter(0, 235, 0, c="g")


def run1():
    tt = threading.Thread(target=run2)
    tt.start()


def run2():
    counter4 = 0

    global g
    global speed2, speed3
    speed2 = entry1.get()
    speed3 = float(speed2)
    global gcode1
    gcode1 = open(text1, "r", encoding="utf-8")
    while counter4 < len(corx) and counter4 < len(cory) and counter4 < len(corz):
        # print(type(speed3))
        time.sleep(speed3)
        g = gcode1.readline()
        listbox.insert(END, g)
        listbox.selection_clear(0, END)
        listbox.selection_set(listbox.size() - 1, listbox.size() - 1)
        listbox.see(END)
        counter4 += 1
        point1.invoke()


def run3():
    coordinatex = int(axisentryx.get())
    coordinatey = int(axisentryy.get())
    coordinatez = int(axisentryz.get())
    coordinatexeksi = -(coordinatex)
    coordinateyeksi = -(coordinatey)
    coordinatezeksi = -(coordinatez)

    x = [coordinatex, coordinatexeksi]
    y = [coordinatexeksi, coordinatexeksi]
    z = [coordinatexeksi, coordinatexeksi]

    x1 = [coordinatexeksi, coordinatex]
    y1 = [coordinatex, coordinatex]
    z1 = [coordinatexeksi, coordinatexeksi]

    x2 = [0, 0]
    y2 = [coordinatex, coordinatex]
    z2 = [coordinatexeksi, coordinatex]

    x3 = [0, 0]
    y3 = [coordinatexeksi, coordinatexeksi]
    z3 = [coordinatexeksi, coordinatex]

    x4 = [0, 0]
    y4 = [coordinatex, coordinatexeksi]
    z4 = [0, 0]

    bas1 = next(corx_iter)
    bas2 = next(cory_iter)
    bas3 = next(corz_iter)

    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.get_tk_widget().place(x=600, y=10)
    a = fig.add_subplot(projection='3d')
    t = 1
    a.plot(5, 5)
    a.set_xlabel("coordinate x")
    a.set_ylabel("coordinate y")
    a.set_zlabel("coordinate z")

    x2 = []
    x2.append(bas1)
    x2.append(bas1)
    x3 = []
    x3.append(bas1)
    x3.append(bas1)
    x4 = []
    x4.append(bas1)
    x4.append(bas1)
    z4 = []
    z4.append(bas3)
    z4.append(bas3)

    a.plot3D(x, y, z, c="b")
    a.plot3D(x1, y1, z1, c="b")
    a.plot3D(x2, y2, z2, c="g")
    a.plot3D(x3, y3, z3, c="g")
    a.plot3D(x4, y4, z4)

    a.scatter(bas1, bas2, bas3, c="r", s=250)
    a.scatter(bas1, coordinatexeksi, coordinatexeksi, c="b")
    a.scatter(bas1, coordinatex, coordinatexeksi, c="b")
    a.scatter(bas1, coordinatexeksi, bas3, c="g")
    a.scatter(bas1, coordinatex, bas3, c="g")


speed = 0.3
label4 = tk.Label(text="SPEED:",
                  font="times 15"
                  )
label4.place(x=100, y=345)
entry1 = tk.Entry(form)
entry1.insert(0, 0.3)
entry1.place(x=175, y=350)
axisentryx = tk.Entry(form)
axisentryx.place(x=150, y=375)
axisentryy = tk.Entry(form)
axisentryy.place(x=300, y=375)
axisentryz = tk.Entry(form)
axisentryz.place(x=450, y=375)
axislabel = tk.Label(text="AXİS WİDTH:",
                     font="times 15")
axislabel.place(x=25, y=370)
axislabel2 = tk.Label(text="x",
                      font="times 15")

axislabel2.place(x=280, y=370)
axislabel3 = tk.Label(text="x",
                      font="times 15")
axislabel3.place(x=430, y=370)
text3 = tk.Label(text="Plase Select Process File")
text3.place(x=175, y=250)
text2 = tk.Label(text="File Not Selected")
text2.place(x=175, y=275)
point1 = tk.Button(text="göster", command=run3)
btrun = tk.Button(text="RUN", command=run1)
btrun.place(x=175, y=450)
btfile = tk.Button(text="Click to select a file", command=SelectFile)
btfile.place(x=175, y=300)
btwritefile = tk.Button(text="dosya yaz", command=WriteFile)
corx = tk.Label(text="COORDİNATE X",
                font="times 10")
corx.place(x=160, y=400)
cory = tk.Label(text="COORDİNATE Y",
                font="times 10")
cory.place(x=315, y=400)
corz = tk.Label(text="COORDİNATE Z",
                font="times 10")
corz.place(x=460, y=400)
listbox = tk.Listbox(form, width=50, height=10)
listbox.place(x=1300, y=160)
scrollbar = Scrollbar(form)
scrollbar.place(x=1605, y=160, height=320)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

form.mainloop()
