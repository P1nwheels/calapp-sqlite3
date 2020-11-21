import sqlite3
import random
from string import ascii_uppercase, ascii_lowercase

TABLE_CREATION = "CREATE TABLE IF NOT EXISTS foods (ID INTEGER, name TEXT, calories INTEGER)"
ADD_FOOD = "INSERT INTO foods (ID, name, calories) VALUES (?, ?, ?);"
GET_CALORIES = "SELECT calories FROM foods;"
GET_FOODS = "SELECT * FROM foods;"
REMOVE_FOOD = "DELETE FROM foods WHERE ID = ?;"
CLEAR_FOODS = "DELETE FROM foods;"
GEN_OPTIONS = ascii_uppercase+ascii_lowercase

def get_connection(path):
    return sqlite3.connect(path)

def create_table(conn):
    with conn:
        conn.execute(TABLE_CREATION)

def gen_id():
    return "".join(random.choices(GEN_OPTIONS, k=5))

def add_food(conn, ID, name, calories):
    with conn:
        conn.execute(ADD_FOOD, (ID, name, calories))

def show_foods(conn):
    with conn:
        calorieSum = sum([i[0] for i in conn.execute(GET_CALORIES).fetchall()])
        for i in conn.execute(GET_FOODS):
            print(f"ID: {i[0]} | Name: {i[1]} | Calories: {i[2]}\n")
        print("Calories eaten so far: ", calorieSum) 
        print(f"Calories left: {1500-calorieSum}\n")

def remove_food(conn, ID):
    with conn:
        conn.execute(REMOVE_FOOD, (ID,))

def clear_foods(conn):
    with conn:
        conn.execute(CLEAR_FOODS)
