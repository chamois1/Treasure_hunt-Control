from easy_game.table_words import arr_shuffled


import easy_game.zero_three_four_cells_ as zero_three_four_cells_
from easy_game.zero_three_four_cells_ import *

from database_users import end_game

import sys


# Якщо ходів було 5 - завершуємо
total_call_count = 0 # лічильник, скільки ходів вже було 1, 2, 3... 4... (ходи рахуються, більше за рахунок функцій - функції це ходи)

def count_calls(func):
    def wrapper(*args, **kwargs):
        global total_call_count
        total_call_count += 1
        
        if total_call_count >= 5:
            sys.exit(f"Гра закінчена, {end_game(total_call_count)}")

        return func(*args, **kwargs)
    return wrapper


# Декоратор @count_call рахує скільки функцій було виконано

@count_calls
def two_five():
    new_arr = arr_shuffled[-1:]

    print('2, 5 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('там стінка, оберіть інший хід')
        two_five()
    
    elif xid == 'go left':
        two_four()

    elif xid == 'go up':
        zero_three_four_cells_.zero_number_five()

    elif xid == 'go down':
        zero_three_four_cells_.three_five()

    elif xid == 'dig':
        print('У вас немає лопати')
        two_five()

    elif xid == 'search':
        reward_xid = str([new_arr[0][4]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            three_three()

        elif reward_xid == 'Скарб':
            end_game(total_call_count)


        else:
            print('Нічого немає')
            three_one()



@count_calls
def two_four():
    new_arr = arr_shuffled[-1:]

    print('2, 4 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        two_five()
    
    elif xid == 'go left':
        two_three()

    elif xid == 'go up':
        one_four()


    elif xid == 'go down':
        zero_three_four_cells_.three_four()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        two_four()

    elif xid == 'search':
        reward_xid = str([new_arr[0][3]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            number_zero_zero()

        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            two_five()




@count_calls
def two_three():
    new_arr = arr_shuffled[-1:]

    print('2, 3 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        two_four()
    
    elif xid == 'go left':
        two_two()

    elif xid == 'go up':
        one_three()

    elif xid == 'go down':
        zero_three_four_cells_.three_three()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        two_three()

    elif xid == 'search':
        reward_xid = str([new_arr[0][2]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_five()


        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            two_four()








@count_calls
def two_two():
    new_arr = arr_shuffled[-1:]


    print('2, 2 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        two_three()
    
    elif xid == 'go left':
        two_one()

    elif xid == 'go up':
        one_two()

    elif xid == 'go down':
        zero_three_four_cells_.three_two()



    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        two_two()

    elif xid == 'search':
        reward_xid = str([new_arr[0][1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_five()


        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            two_three()






@count_calls
def two_one():
    new_arr = arr_shuffled[-1:]


    print('2, 1 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        two_two()
    
    elif xid == 'go left':
        print('стінка')
        two_one()

    elif xid == 'go up':
        one_one()

    elif xid == 'go down':
        zero_three_four_cells_.three_one()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        two_one()

    elif xid == 'search':
        reward_xid = str([new_arr[0][0]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_four()


        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            two_two()




@count_calls
def one_five():
    

    new_arr = arr_shuffled[:-1]

    print('1, 5 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('Там стінка, оберіть інший хід')
        one_five()
    
    elif xid == 'go left':
        one_four()

    elif xid == 'go up':
        zero_three_four_cells_.zero_number_five()

    elif xid == 'go down':
        two_five()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        one_five()
        
    elif xid == 'search':
        reward_xid = str([new_arr[1][4]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_three()
        

        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            two_one()




@count_calls
def one_four():
    new_arr = arr_shuffled[:-1]


    print('1, 4 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        one_five()
    
    elif xid == 'go left':
        one_three()

    elif xid == 'go up':
        zero_three_four_cells_.zero_number_four()

    elif xid == 'go down':
        two_four()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        one_four()

    elif xid == 'search':
        reward_xid = str([new_arr[1][3]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_three()
    
        elif reward_xid == 'Скарб':
            end_game(total_call_count)


        else:
            print('нічого немає')
            one_five()



@count_calls
def one_three():
    new_arr = arr_shuffled[:-1]

    print('1, 3 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        one_four()
    
    elif xid == 'go left':
        one_two()

    elif xid == 'go up':
        two_two()

    elif xid == 'go down':
        two_three()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        one_three()

    elif xid == 'search':
        reward_xid = str([new_arr[1][2]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            two_one()
        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            one_four()



        

@count_calls
def one_two():
    new_arr = arr_shuffled[:-1]

    print('1, 2 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        one_three()
    
    elif xid == 'go left':
        one_one()

    elif xid == 'go up':
        zero_three_four_cells_.number_zero_two()

    elif xid == 'go down':
        two_two()
    
    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        one_two()

    elif xid == 'search':
        reward_xid =  str([new_arr[0][1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_five()

        elif reward_xid == 'Скарб':
            end_game(total_call_count)

        else:
            print('нічого немає')
            one_three()



 
@count_calls
def one_one(): # 1, 0 - клітинка
    new_arr = arr_shuffled[:-1]

    xid = input('Які ваші дії?\nВедіть команду: ')  
    print('1, 0 - клітинка')

    if xid == 'go right':
        one_two()
    
    elif xid == 'go left':
        print('там стінка, оберіть інший хід')
        one_one()

    elif xid == 'go up':
        zero_three_four_cells_.number_zero_zero()

    elif xid == 'go down':
        two_one()


    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        one_one()

    elif xid == 'search':
        reward_xid = str([new_arr[1][0]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_four()

        elif reward_xid == 'Скарб':
            end_game(total_call_count)
        else:
            print('нічого немає')
            one_one()

