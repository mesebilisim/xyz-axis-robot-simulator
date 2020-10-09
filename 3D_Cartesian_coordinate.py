import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
import threading
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

form = tk.Tk()
form.state("zoomed")
fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=form)
canvas.get_tk_widget().place(x=600, y=10)
a = fig.add_subplot(projection='3d')
t = 1
a.plot(1, 1)
x = []

y = []

z = []


a.scatter(x, y, z, c="r", marker="o")






def noktabirgoster():
    bas1 = int(giris1x.get())
    bas2 = int(giris1y.get())
    bas3 = int(giris1z.get())

    x.append(bas1)

    y.append(bas2)

    z.append(bas3)

    # ---------------------------------------

    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.get_tk_widget().place(x=600, y=10)
    a = fig.add_subplot(projection='3d')
    t = 1
    a.plot(1, 1)
    # a.plot3D(x, y, z)
    a.scatter(x, y, z, c="r", marker="o")
    # a.plot3D(q, w, e)

    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")

    a.plot3D(x, y, z)






label2 = tk.Label(text="X KOORDİNATI",
                  font="times 15"
                  )
label2.place(x=50, y=100)
giris1x = tk.Entry(form)
giris1x.place(x=60, y=150)
label3 = tk.Label(text="Y KOORDİNATI",
                  font="times 15"
                  )
label3.place(x=250, y=100)
giris1y = tk.Entry(form)
giris1y.place(x=260, y=150)
label4 = tk.Label(text="Z KOORDİNATI",
                  font="times 15"
                  )
label4.place(x=450, y=100)
giris1z = tk.Entry(form)
giris1z.place(x=460, y=150)

goster1 = tk.Button(text="ekle ve göster", command=noktabirgoster)
goster1.place(x=275, y=200)


form.mainloop()

