from tkinter import *


def button_enter(food_type):
    command = food_type
    command = box.get()
    global calories_total
    global fat_total
    global carbs_total
    global protein_total
    if command == "Protein shake":
        Label(program, text=f"Protein shake").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 800
        fat_total += 35
        carbs_total += 59.7
        protein_total += 62

    elif command == "Sesame bars":
        Label(program, text="Sesame bars").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 400
        fat_total += 23
        carbs_total += 37
        protein_total += 9

    elif command == "Rice with chicken":
        Label(program, text="Rice with chicken").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 720
        fat_total += 14
        carbs_total += 100
        protein_total += 44

    elif command == "Noodles with chicken":
        Label(program, text="Noodles with chicken").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 900
        fat_total += 20
        carbs_total += 122
        protein_total += 50

    elif command == "Croissant":
        Label(program, text="Croissant").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 450
        fat_total += 28
        carbs_total += 28
        protein_total += 6

    elif command == "Pizza":
        Label(program, text="Pizza").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 257
        fat_total += 0
        carbs_total += 47.2
        protein_total += 8.8

    elif command == "Protein sandwich":
        Label(program, text="Protein sandwich").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 500
        fat_total += 20
        carbs_total += 44
        protein_total += 32

    elif command == "Sandwich":
        Label(program, text="Sandwich").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 450
        fat_total += 12
        carbs_total += 50
        protein_total += 20

    elif command == "Chicken burger":
        Label(program, text="Chicken burger").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 445
        fat_total += 20.9
        carbs_total += 49.2
        protein_total += 14.9

    elif command == "Egg":
        Label(program, text="Egg").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 72
        fat_total += 1.5
        carbs_total += 0.5
        protein_total += 6

    elif command == "Yoghurt":
        Label(program, text="Yoghurt").grid(column=0, padx=15, columnspan=4, sticky="w")
        calories_total += 300
        fat_total += 16
        carbs_total += 21
        protein_total += 16

    box.delete(0, END)


def button_finish():
    box.delete(0, END)
    global calories_total
    global fat_total
    global carbs_total
    global protein_total

    Label(program, text=" ").grid(column=0, columnspan=3)

    if calories_total < 3000:
        Label(program, text=f"Total Calories: {calories_total:.2f}", bd=1, fg="red").grid(padx=15, column=0, columnspan=3, sticky="w")
        Label(program, text=f"Protein: {protein_total:.2f}", bd=1, fg="red").grid(column=0, padx=15, columnspan=3, sticky="w")
        Label(program, text=f"Carbs: {carbs_total:.2f}", bd=1, fg="red").grid(column=0, padx=15, columnspan=3, sticky="w")
        Label(program, text=f"Fat: {fat_total:.2f}", bd=1, fg="red").grid(column=0, padx=15, columnspan=3, sticky="w")
    else:
        Label(program, text=f"Total Calories: {calories_total:.2f}", bd=1, fg="green").grid(padx=15, column=0, columnspan=3, sticky="w")
        Label(program, text=f"Protein: {protein_total:.2f}", bd=1, fg="green").grid(column=0, padx=15, columnspan=3, sticky="w")
        Label(program, text=f"Carbs: {carbs_total:.2f}", bd=1, fg="green").grid(column=0, padx=15, columnspan=3, sticky="w")
        Label(program, text=f"Fat: {fat_total:.2f}", bd=1, fg="green").grid(column=0, padx=15, columnspan=3, sticky="w")


def button_restart():
    for widget in program.winfo_children():
        widget.destroy()

    global enter
    global finish
    global restart
    global box

    # Define
    enter = Button(program, text="Enter", padx=4, pady=0, command=lambda: button_enter(box.get()))
    finish = Button(program, text="Finish", padx=4, pady=0, command=button_finish)
    restart = Button(program, text="Restart", padx=4, pady=0, command=button_restart)
    box = Entry(program, width=39, bg="white", borderwidth=2)

    # Put on screen
    enter.grid(row=2, column=0, padx=1, sticky="e")
    finish.grid(row=2, column=1, padx=1)
    restart.grid(row=2, column=2, padx=1, sticky="w")
    box.grid(row=1, column=0, padx=20, pady=10, columnspan=4)

    global calories_total
    global fat_total
    global carbs_total
    global protein_total

    calories_total = 0
    fat_total = 0
    carbs_total = 0
    protein_total = 0


# Main settings
program = Tk()
program.title("Nutrition calculator")
program.minsize(275, 350)
program.geometry(f"{250}x{350}+{700}+{250}")
program.bind("<Return>", button_enter)
program.bind("<=>", button_finish)

# Variables
calories_total = 0
carbs_total = 0
fat_total = 0
protein_total = 0

# Define the grid
program.columnconfigure(0, weight=1)
program.columnconfigure(1, weight=1)
program.columnconfigure(2, weight=1)

# Define
enter = Button(program, text="Enter", padx=4, pady=0, command=lambda: button_enter(box.get()))
finish = Button(program, text="Finish", padx=4, pady=0, command=button_finish)
restart = Button(program, text="Restart", padx=4, pady=0, command=button_restart)
box = Entry(program, width=39, bg="white", borderwidth=2)

# Put on screen
enter.grid(row=2, column=0, padx=1, sticky="e")
finish.grid(row=2, column=1, padx=1)
restart.grid(row=2, column=2, padx=1, sticky="w")
box.grid(row=1, column=0, padx=20, pady=10, columnspan=3)

# Keep program running
program.mainloop()
