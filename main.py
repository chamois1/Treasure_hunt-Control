from tabulate import tabulate
import sqlite3

from easy_game.zero_three_four_cells_ import *
from easy_game.one_two_cells import *


from easy_game.table_words import chunks, arr_shuffled


def easy_game():
    global data

    # Список переможців

    connect = sqlite3.connect('search_treasures.db')
    cursor = connect.cursor()


    cursor.execute("SELECT * FROM users") 
    data = cursor.fetchall()
    print("Список переможців\n", data) 
    number_zero_zero()



def number_zero_zero():
    while True: 
        user = input('Ведіть кординату, у форматі (1, 0 або 2,3): ')

        
        if user == '0, 1':
            new_arr = arr_shuffled[:-1]

            xid = input('Які ваші дії?\nВедіть команду: ')   

            if xid == 'go right':
                number_zero_two()
        
            elif xid == 'go left':
                print('там стінка')

            elif xid == 'go up':
                print('там стінка')

            elif xid == 'go down':
                one_one()

            # dig - search
            elif xid == 'dig':
                print('Тільки на вищих рівнях доступно')
            elif xid == 'search':
                print('Ви получили: ', str([new_arr[0][:1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))

            
        

        elif user == '0, 2':
            number_zero_two()
        elif user == '0, 3':
            number_zero_three()
        elif user == '0, 4':
            zero_number_four()
        elif user == '0, 5':
            zero_number_five()
        
        # 1...

        elif user == '1, 1':
            one_one()
        elif user == '1, 2':
            one_two()
        elif user == '1, 3':
            one_three()
        elif user == '1, 4':
            one_four()
        elif user == '1, 5':
            one_five()
        
        # 2...

        elif user == '2, 1':
            two_one()
        elif user == '2, 2':
            two_two()
        elif user == '2, 3':
            two_three()
        elif user == '2, 4':
            two_four()
        elif user == '2, 5':
            two_five()

        # 3...

        elif user == '3, 1':
            three_one()
        elif user == '3, 2':
            three_two()
        elif user == '3, 3':
            three_three()
        elif user == '3, 4':
            three_four()
        elif user == '3, 5':
            three_five()

        # 4...

        elif user == '4, 1':
            four_one()
        elif user == '4, 2':
            four_two()
        elif user == '4, 3':
            four_three()
        elif user == '4, 4':
            four_four()
        elif user == '4, 5':
            four_five()
        

        else:
            print('Немає такого кординату, або команди')



def dataBase():
    global choice_complexity_game

    while True:
        # Connect dataBase SQL
        connect = sqlite3.connect('search_treasures.db')
        cursor = connect.cursor()

        # Table list users
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            complexity TEXT,
            move INTEGER
        )""")

        # user input
        choice_complexity_game = input('Ведіть складність гри, легкий, середній або складний: ')
        if choice_complexity_game == 'легкий':
            write_in_database()
        else:
            print('Немає такого')
            dataBase()
        

            
def write_in_database():
    connect = sqlite3.connect('search_treasures.db')
    cursor = connect.cursor()

    choice_nickname = input('Ведіть ваш нікнейм: ')

    
    cursor.execute(f"SELECT name FROM users WHERE name LIKE '%{choice_nickname}%'")
    data = cursor.fetchone()


    # checking in DataBase user
    if data is None:
        cursor.execute("INSERT INTO users (name, complexity)values(?, ?);", [choice_nickname, choice_complexity_game])
        connect.commit()
        easy_game()
    else:
        print("Таке ім'я вже існує, придумайте інше")
        choice_nickname = input('Ведіть ваш нікнейм: ')
        write_in_database()


dataBase()
