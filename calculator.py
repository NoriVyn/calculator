import tkinter as tk

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Champ d'entrée
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Boutons numériques
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Bouton de reset
clear_btn = tk.Button(root, text='C', width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Lancement de la boucle
root.mainloop()

