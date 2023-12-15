from tkinter import *


def button_enter(food):
    command = box.get()
    global calories_total
    global fat_total
    global carbs_total
    global protein_total
    if command == "Protein shake":
        Label(program, text="Protein shake").grid(column=0, columnspan=5)
        calories_total += 800
        fat_total += 35
        carbs_total += 59.7
        protein_total += 62

    elif command == "Sesame bars":
        Label(program, text="Sesame bars").grid(column=0, columnspan=5)
        calories_total += 400
        fat_total += 23
        carbs_total += 37
        protein_total += 9

    elif command == "Rice with chicken":
        Label(program, text="Rice with chicken").grid(column=0, columnspan=5)
        calories_total += 720
        fat_total += 14
        carbs_total += 100
        protein_total += 44

    elif command == "Noodles with chicken":
        Label(program, text="Noodles with chicken").grid(column=0, columnspan=5)
        calories_total += 900
        fat_total += 20
        carbs_total += 122
        protein_total += 50

    elif command == "Croissant":
        Label(program, text="Croissant").grid(column=0, columnspan=5)
        calories_total += 450
        fat_total += 28
        carbs_total += 28
        protein_total += 6

    elif command == "Pizza":
        Label(program, text="Pizza").grid(column=0, columnspan=5)
        calories_total += 257
        fat_total += 0
        carbs_total += 47.2
        protein_total += 8.8

    elif command == "Protein sandwich":
        Label(program, text="Protein sandwich").grid(column=0, columnspan=5)
        calories_total += 500
        fat_total += 20
        carbs_total += 44
        protein_total += 32

    elif command == "Sandwich":
        Label(program, text="Sandwich").grid(column=0, columnspan=5)
        calories_total += 450
        fat_total += 12
        carbs_total += 50
        protein_total += 20

    elif command == "Chicken burger":
        Label(program, text="Chicken burger").grid(column=0, columnspan=5)
        calories_total += 445
        fat_total += 20.9
        carbs_total += 49.2
        protein_total += 14.9

    elif command == "Egg":
        Label(program, text="Egg").grid(column=0, columnspan=5)
        calories_total += 72
        fat_total += 1.5
        carbs_total += 0.5
        protein_total += 6

    elif command == "Yoghurt":
        Label(program, text="Yoghurt").grid(column=0, columnspan=5)
        calories_total += 300
        fat_total += 16
        carbs_total += 21
        protein_total += 16

    box.delete(0, END)


def button_finish(a):
    box.delete(0, END)
    global calories_total
    global fat_total
    global carbs_total
    global protein_total

    if calories_total < 3000:
        Label(program, text=f"Total Calories: {calories_total}\nProtein: {protein_total}\nCarbs: {carbs_total}"
                            f"\nFat: {fat_total}", fg="red").grid(pady=10, column=0, columnspan=5)
    else:
        Label(program, text=f"Total Calories: {calories_total}\nProtein: {protein_total}\nCarbs: {carbs_total}"
                            f"\nFat: {fat_total}", fg="green").grid(pady=10, column=0, columnspan=5)


# Main settings
program = Tk()
program.title("Nutrition calculator!")
program.minsize(275, 350)
program.geometry(f"{250}x{350}+{700}+{250}")
program.bind("<Return>", button_enter)
program.bind("<=>", button_finish)

# Variables
calories_total = 0
carbs_total = 0
fat_total = 0
protein_total = 0

# Define
enter = Button(program, text="Enter", padx=4, pady=0, command=button_enter)
finish = Button(program, text="Finish", padx=4, pady=0, command=button_finish)
box = Entry(program, width=39, bg="white")
count = Label

# Put on screen
enter.grid(row=2, column=4, padx=1)
finish.grid(row=2, column=5, padx=1)
box.grid(row=1, column=0, padx=20, pady=10, columnspan=10)

# Keep program running
program.mainloop()

