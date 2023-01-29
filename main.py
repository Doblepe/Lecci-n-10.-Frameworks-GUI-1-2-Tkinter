import tkinter as tk

ventana = tk.Tk()
ventana.title("Aplicación Tkinter")
ventana.resizable(0,0)
ventana.geometry("1080x900")
ventana.config(bg="#C0E7E7")

bread = 0
def add_bread():
    global bread
    bread +=1

milk = 0
def add_milk():
    global milk
    milk +=1

sugar = 0 
def add_sugar():
    global sugar
    sugar +=1

def show_kart():
    global bread
    global milk
    global sugar
    print (f"{bread} bread units, {milk} milk units, {sugar} sugar units ")

def clear_kart():
    global bread
    bread=0
    global milk
    milk=0
    global sugar
    sugar = 0
    return bread,sugar,milk 

def pay_kart():
    global bread
    global milk
    global sugar
    result = bread * 1+ milk*1.5 + sugar * 0.5
    print (f"El total a pagar es de {result}")
    return result

btn_add_bread = tk.Button(ventana, fg="white", bg="#1D6FC2", text="add bread to kart for 1$", width=20, height=6, command= add_bread).grid(row=1, column=1)
btn_add_milk = tk.Button(ventana, fg="white", bg="#1D6FC2", text="add milk to kart for 1.5$", width=20, height=6, command= add_milk).grid(row=1, column=2)
btn_add_sugar = tk.Button(ventana, fg="white", bg="#1D6FC2", text="add sugar to kart for 0.5$", width=20, height=6, command= add_sugar).grid(row=1, column=3)

btn_show_kart = tk.Button(ventana, fg="white", bg="#1D6FC5", text="Show Kart", width=20, height=6, command= show_kart).grid(row=3, column=3)

btn_clean_kart = tk.Button(ventana, fg="white", bg="#1D6F33", text="Clean Kart", width=20, height=6, command= clear_kart).grid(row=3, column=2)

btn_pay_kart = tk.Button(ventana, fg="white", bg="#1D6F77", text="Pay Kart", width=20, height=6, command= pay_kart).grid(row=3, column=1)

#tk.Label(ventana, text="Añada sus productos al carrito").pack()

# v1= tk.IntVar()
# v2 = tk.IntVar()
# v3 = tk.IntVar()

# tk.Checkbutton(ventana, text="Opción 1", variable=v1).grid (row=0, column=0)

# btn_add_bread.pack()
# btn_add_milk.pack()
# btn_add_sugar.pack()
# btn_show_kart.pack()
# btn_clean_kart.pack()
# btn_pay_kart.pack()

ventana.mainloop()