import tkinter as tk
import sys
import os

form = tk.Tk()
form.state("zoomed")

def degis():
    pass
def nokta():
    bas1=giris1.get()
    bas2=giris2.get()
    bas3 = int(bas1)+10
    bas4 = int(bas2)+10

    w.create_oval(bas1, bas2,bas3 ,bas4, fill="blue", width=1)
def nokta2():
    bas5=giris3.get()
    bas6=giris4.get()
    bas7 = int(bas5)+10
    bas8 = int(bas6)+10

    w.create_oval(bas5, bas6,bas7,bas8, fill="blue", width=1)
def cizgicek():
    bas1 = giris1.get()
    bas2 = giris2.get()
    bas3 = int(bas1) + 10
    bas4 = int(bas2) + 10
    bas5 = giris3.get()
    bas6 = giris4.get()
    bas7 = int(bas5) + 10
    bas8 = int(bas6) + 10
    w.create_line(bas1, bas2, bas5, bas6, fill="blue", width=1)
def ekrantemizle():

    python = sys.executable
    os.execl(python, python, *sys.argv)
w =tk.Canvas(width=1000, height=1000,bd=0,highlightthickness=0)
w.configure(bg="black")
w.place(x=500,y=30)

j=0
cor=480
while j<10:
    label = tk.Label(text=j*100, font="times 20")
    label.place(x=cor-10, y=-7)
    j+=1
    cor+=100
k=1
cor1=110
while k<11:
    label1 = tk.Label(text=k*100, font="times 20")
    label1.place(x=450, y=cor1)
    cor1+=100
    k+=1
i = 0
x1=100
y1=100
while i<10:

    w.create_line(x1, 0, x1, 1000, fill="red")
    w.create_line(0, x1, 1000, x1, fill="red")

    x1+=100
    i += 1

giris1 = tk.Entry()
giris1.place(x=100 , y = 100)
kordix1=giris1.get()
label1=tk.Label(text="nokta x1:",
                font="times 15"
                )
label1.place(x=4,y=90)
giris2 = tk.Entry()
giris2.place(x=100 , y = 200)

label2=tk.Label(text="nokta y1:",
                font="times 15"
                )
label2.place(x=4,y=190)
noktakoy1 =tk.Button(text = "1.noktayı koy",command=nokta)
noktakoy1.place(x=100,y=250)
giris3 = tk.Entry()
giris3.place(x=100 , y = 300)
label3=tk.Label(text="nokta x2:",
                font="times 15"
                )
label3.place(x=4,y=290)
giris4 = tk.Entry()
giris4.place(x=100 , y = 400)
label4=tk.Label(text="nokta y2:",
                font="times 15"
                )
label4.place(x=4,y=400)
noktakoy2 =tk.Button(text = "2.noktayı koy",command=nokta2)
noktakoy2.place(x=100,y=450)

cizgicek = tk.Button(text = "noktaları birleştir",command = cizgicek)
cizgicek.place(x = 100 ,y=500)

temizle= tk.Button(text = "temizle ve yeniden başlat",command = ekrantemizle)
temizle.place(x=100 , y=600)

form.mainloop()
