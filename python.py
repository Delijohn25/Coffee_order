import tkinter as tk

def calculate_price():
    price = 0
    if coffee_type.get() == "Espresso":
        price = 2.0
    elif coffee_type.get() == "Cappucino":
        price = 3.0
    elif coffee_type.get() == "Americano":
        price = 3.5
    elif coffee_type.get() == "greek":
        price = 2.5
    elif coffee_type.get() == "greek double":
        price = 3.5

    if size.get() == "Μεγάλο":
        price += 1

    if sugar.get():
        price += 0.5

    if milk.get():
        price += 0.5
    
    if cinnamon.get():
        price += 0.5

    if booze.get():
        price += 1

        label_price.config(text=f"Συνολικό κόστος {price:.2f}$")

root = tk.Tk()
root.title("Παραγγελία καφέ")
root.geometry("300x300")

coffee_type = tk.StringVar(value="Espresso")
tk.Label(root, text="Επέλεξε τι καφέ θές:", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Espresso (2$)", variable=coffee_type, value="Espresso").pack()
tk.Radiobutton(root, text="Cappucino (3$)", variable=coffee_type, value="Cappucino").pack()
tk.Radiobutton(root, text="Americano (3.5$)", variable=coffee_type, value="Americano").pack()
tk.Radiobutton(root, text="Ελληνικός (2.5$)", variable=coffee_type, value="greek").pack()
tk.Radiobutton(root, text="Ελληνικός διπλός(3.5$)", variable=coffee_type, value="greek double").pack()

size = tk.StringVar(value="Μικρό")
tk.Label(root, text="Μέγεθος ποτηριού:", font=("Arial", 12)).pack()
spinbox = tk.Spinbox(root, values=("Μικρό", "Μεγάλο"))
spinbox.pack()

sugar = tk.IntVar()
milk = tk.IntVar()
cinnamon = tk.IntVar()
booze = tk.IntVar()
tk.Checkbutton(root, text="Ζάχαρη (+0.5$)", variable=sugar).pack()
tk.Checkbutton(root, text="Γάλα (+0.5$)", variable=milk).pack()
tk.Checkbutton(root, text="Κανέλα (+0.5$)", variable=cinnamon).pack()
tk.Checkbutton(root, text="Αλκοόλ (+1$)", variable=booze).pack()

tk.Button(root, text="Υπολογισμός", font=("Arial", 12), bg="brown", fg="white", command=calculate_price).pack(pady=10)

label_price = tk.Label(root, text="Συνολικό κόστος: 0.00$", font=("Arial", 12))
label_price.pack()
root.mainloop()