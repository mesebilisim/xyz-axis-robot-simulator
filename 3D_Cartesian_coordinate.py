import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import sys
import os

form = tk.Tk()
form.state("zoomed")


def ekrantemizle():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def noktabirgoster():
    bas1 = int(giris1x.get())
    bas2 = int(giris1y.get())
    bas3 = int(giris1z.get())
    
    a = plt.axes(projection="3d")
    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")
    x = []
    x.append(bas1)
    y = []
    y.append(bas2)
    z = []
    z.append(bas3)
    
    
    a.plot3D(x, y, z)
    

    a.scatter(x, y, z, c="r", marker="o")
    
    # ---------------------------------------

    plt.show()


def noktaikigoster():
    bas4 = int(giris2x.get())
    bas5 = int(giris2y.get())
    bas6 = int(giris2z.get())
    a = plt.axes(projection="3d")
    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")
    q = []
    q.append(bas4)
    w = []
    w.append(bas5)
    e = []
    e.append(bas6)
    a.plot3D(q, w, e)
    a.scatter(q, w, e, c="b", marker="o")
    # ---------------------------------------

    plt.show()
def ayniandagoster():
    bas1 = int(giris1x.get())
    bas2 = int(giris1y.get())
    bas3 = int(giris1z.get())
    bas4 = int(giris2x.get())
    bas5 = int(giris2y.get())
    bas6 = int(giris2z.get())
    a = plt.axes(projection="3d")
    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")
    x = []
    x.append(bas1)
    y = []
    y.append(bas2)
    z = []
    z.append(bas3)
    q = []
    q.append(bas4)
    w = []
    w.append(bas5)
    e = []
    e.append(bas6)
    a.plot3D(x, y, z)
    a.plot3D(q, w, e)
    a.scatter(x, y, z, c="r", marker="o")
    a.scatter(q, w, e, c="b", marker="o")
    # ---------------------------------------

    plt.show()
def openNewWindow():
    bas1 = int(giris1x.get())
    bas2 = int(giris1y.get())
    bas3 = int(giris1z.get())
    bas4 = int(giris2x.get())
    bas5 = int(giris2y.get())
    bas6 = int(giris2z.get())
    a = plt.axes(projection="3d")
    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")
    x = []
    x.append(bas1)
    y = []
    y.append(bas2)
    z = []
    z.append(bas3)
    q = []
    q.append(bas4)
    w = []
    w.append(bas5)
    e = []
    e.append(bas6)
    j = x + q
    k = y + w
    l = z + e
    a.plot3D(x, y, z)
    a.plot3D(q, w, e)
    a.plot3D(j, k, l)

    a.scatter(x, y, z, c="r", marker="o")
    a.scatter(q, w, e, c="b", marker="o")
    # ---------------------------------------

    plt.show()


label1 = tk.Label(text="1. NOKTA",
                  font="times 15"
                  )
label1.place(x=275, y=100)
label2 = tk.Label(text="X KOORDİNATI",
                  font="times 15"
                  )
label2.place(x=50, y=150)
giris1x = tk.Entry(form)
giris1x.place(x=60, y=200)
label3 = tk.Label(text="Y KOORDİNATI",
                  font="times 15"
                  )
label3.place(x=250, y=150)
giris1y = tk.Entry(form)
giris1y.place(x=260, y=200)
label4 = tk.Label(text="Z KOORDİNATI",
                  font="times 15"
                  )
label4.place(x=450, y=150)
giris1z = tk.Entry(form)
giris1z.place(x=460, y=200)

goster1 = tk.Button(text="1. noktayı göster", command=noktabirgoster)
goster1.place(x=650, y=200)

# ----------------------------------

label12 = tk.Label(text="2. NOKTA",
                   font="times 15"
                   )
label12.place(x=275, y=250)
label22 = tk.Label(text="X KOORDİNATI",
                   font="times 15"
                   )
label22.place(x=50, y=300)
giris2x = tk.Entry(form)
giris2x.place(x=60, y=350)
label32 = tk.Label(text="Y KOORDİNATI",
                   font="times 15"
                   )
label32.place(x=250, y=300)
giris2y = tk.Entry(form)
giris2y.place(x=260, y=350)
label42 = tk.Label(text="Z KOORDİNATI",
                   font="times 15"
                   )
label42.place(x=450, y=300)
giris2z = tk.Entry(form)
giris2z.place(x=460, y=350)

goster2 = tk.Button(text="2. noktayı göster", command=noktaikigoster)
goster2.place(x=650, y=350)
# ------------------------------------------------
cizgi = tk.Button(text="ÇİZGİ ÇİZ VE GÖSTER", command=openNewWindow)
cizgi.place(x=100, y=450)
yenile = tk.Button(text="AYNI ANDA GÖSTER", command=ayniandagoster)
yenile.place(x=400, y=450)
form.mainloop()
