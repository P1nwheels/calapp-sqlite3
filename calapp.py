#!/usr/bin/python3
import bscene
import os

TXTCOLOR = "\033[33m"
MENU = """1. Add food
2. Show foods
3. Remove food
4. Clear foods
5. Exit
> """

def menu():
    conn = bscene.get_connection(".foods.db")
    bscene.create_table(conn)

    while (inp := int(input(TXTCOLOR + MENU))) != 5:
        os.system("clear" if os.name != "nt" else "cls")
        if inp == 1:
            name = input(TXTCOLOR + "Name of food: ")
            calories = int(input(TXTCOLOR + "Amount of calories: "))
            bscene.add_food(conn, bscene.gen_id(), name, calories)
        elif inp == 2:
            bscene.show_foods(conn)
        elif inp == 3:
            bscene.show_foods(conn)
            ID = input(TXTCOLOR + "ID to remove: ")
            bscene.remove_food(conn, ID)
        elif inp == 4:
            if input(TXTCOLOR + "Are you sure? [Y/N] ").lower() == "y":
                bscene.clear_foods(conn)
        else:
            print(TXTCOLOR + "Not a valid input.")

if __name__ == "__main__":
    menu()
