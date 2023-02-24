import easy_game.one_two_cells as one_two_cells
from easy_game.table_words import arr_shuffled
from main import number_zero_zero

import sys


from database_users import end_game

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
def four_five():
    new_arr = arr_shuffled[-1:]

    print('4, 5 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('там стінка')
    
    elif xid == 'go left':
        four_three()

    elif xid == 'go up':
        three_five()

    elif xid == 'go down':
        print('там стінка, оберіть іншу клітинку')
        four_five()

    elif xid == 'dig':
        print('У вас немає лопати')
        four_five()
        
    elif xid == 'search':
        reward_xid = str([new_arr[0][4]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            print('Ой стінка')
            end_game(total_call_count)

        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)

        else:
            print('нічого немає')
            four_five()




@count_calls
def four_four():
    new_arr = arr_shuffled[-1:]

    print('4, 4 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('там стінка')
    
    elif xid == 'go left':
        four_three()

    elif xid == 'go up':
        one_two_cells.zero_number_five()

    elif xid == 'go down':
        print('там стінка')
        four_four()

    elif xid == 'dig':
        print('У вас немає лопати')
        four_four()

    elif xid == 'search':
        reward_xid = str([new_arr[0][3]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            print('Ой стінка')
            end_game(total_call_count)

        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)
        else:
            print('нічого немає')
            four_four()




@count_calls
def four_three():
    new_arr = arr_shuffled[-1:]

    print('4, 3 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        four_four()
    
    elif xid == 'go left':
        four_two()

    elif xid == 'go up':
        three_three()

    elif xid == 'go down':
        four_three()
        print('там стінка')

    elif xid == 'dig':
        print('У вас немає лопати')
        four_three()
        
    elif xid == 'search':
        reward_xid = str([new_arr[0][2]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            print('Ой стінка')
            end_game(total_call_count)

        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)

        else:
            print('нічого немає')
            four_three()





@count_calls
def four_two():
    new_arr = arr_shuffled[-1:]

    print('4, 2 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        four_three()
    
    elif xid == 'go left':
        four_one()

    elif xid == 'go up':
        three_two()

    elif xid == 'go down':
        print('там стінка')
        four_two()


    elif xid == 'dig':
        print('У вас немає лопати')
        four_two()

    elif xid == 'search':
        reward_xid = str([new_arr[0][1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            four_five()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)


@count_calls
def four_one():
    new_arr = arr_shuffled[-1:]

    print('4, 1 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        four_two()
    
    elif xid == 'go left':
        print('Там стінка')

    elif xid == 'go up':
        three_one()

    elif xid == 'go down':
        print('там стінка')
        four_one()

    elif xid == 'dig':
        print('У вас немає лопати')
        four_one()

    elif xid == 'search':
        reward_xid = str([new_arr[0][0]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            four_four()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)


@count_calls
def three_five():
    new_arr = arr_shuffled[-2:]

    print('3, 5 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('там стінка')
    
    elif xid == 'go left':
        three_four()

    elif xid == 'go up':
        one_two_cells.two_five()

    elif xid == 'go down':
        four_five()

    elif xid == 'dig':
        print('У вас немає лопати')
        three_five()
        
    elif xid == 'search':
        reward_xid = str([new_arr[0][4]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду\nОй стінка')
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)


@count_calls
def three_four():
    new_arr = arr_shuffled[-2:]

    print('3, 4 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        three_five()
    
    elif xid == 'go left':
        three_three()

    elif xid == 'go up':
        one_two_cells.two_four()

    elif xid == 'go down':
        four_four()

    elif xid == 'dig':
        print('У вас немає лопати')
        three_four()

    elif xid == 'search':
        reward_xid = str([new_arr[0][3]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            four_two()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)


@count_calls
def three_three():
    new_arr = arr_shuffled[-2:]

    print('3, 3 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        three_four()
    
    elif xid == 'go left':
        three_two()

    elif xid == 'go up':
        one_two_cells.two_three()

    elif xid == 'go down':
        four_three()

    elif xid == 'dig':
        print('У вас немає лопати')
        three_three()

    elif xid == 'search':
        reward_xid = str([new_arr[0][2]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            four_one()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)



@count_calls
def three_two():
    new_arr = arr_shuffled[-2:]

    print('3, 2 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        three_three()
    
    elif xid == 'go left':
        three_one()

    elif xid == 'go up':
        one_two_cells.two_two()

    elif xid == 'go down':
        four_two()

    elif xid == 'dig':
        print('У вас немає лопати')
        three_two()

    elif xid == 'search':
        reward_xid = str([new_arr[0][1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            three_five()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)


@count_calls
def three_one():
    new_arr = arr_shuffled[-2:]

    print('3, 1 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        three_two()
    
    elif xid == 'go left':
        print('Там стінка')

    elif xid == 'go up':
        one_two_cells.two_one()

    elif xid == 'go down':
        four_one()

    elif xid == 'dig':
        print('У вас немає лопати')
        three_one()

    elif xid == 'search':
        reward_xid = str([new_arr[0][0]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            three_five()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)
        
        else:
            print('нічого немає')
        




@count_calls
def zero_number_five():
    new_arr = arr_shuffled[:-1]

    print('0, 5 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        print('там стінка')
    
    elif xid == 'go left':
        one_two_cells.zero_number_four()

    elif xid == 'go up':
        print('там стінка')

    elif xid == 'go down':
        one_two_cells.one_five()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        zero_number_four()

    elif xid == 'search':
        reward_xid = str([new_arr[0][4]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)
        
        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_two_cells.one_three()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)
        else:
            print('нічого немає')  
            
            




@count_calls
def zero_number_four():
    new_arr = arr_shuffled[:-1]

    print('0, 4 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        one_two_cells.zero_number_five()
    
    elif xid == 'go left':
        number_zero_three()

    elif xid == 'go up':
        print('там стінка')

    elif xid == 'go down':
        one_two_cells.one_four()
        
    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        zero_number_four()

    elif xid == 'search':
        reward_xid = str([new_arr[0][3]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_two_cells()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)
                
        else:
            print('нічого немає')
            zero_number_four()


            

@count_calls
def number_zero_three():
    new_arr = arr_shuffled[:-1]

    print('0, 3 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        one_two_cells.zero_number_four()
    
    elif xid == 'go left':
        number_zero_two()

    elif xid == 'go up':
        print('стінка')

    elif xid == 'go down':
        one_two_cells.one_three()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        number_zero_three()

    elif xid == 'search':
        reward_xid =  str([new_arr[0][2]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_two_cells.one_one()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)
        else:
            print('нічого немає')
            zero_number_four()




@count_calls
def number_zero_two(): # 0, 2 - клітинка
    new_arr = arr_shuffled[:-1]

    print('0, 2 - клітинка')
    xid = input('Які ваші дії?\nВедіть команду: ')  
    if xid == 'go right':
        number_zero_three()
    
    elif xid == 'go left':
        number_zero_zero()

    elif xid == 'go up':
        print('там стінка')

    elif xid == 'go down':
        three_two()

    # dig - search
    elif xid == 'dig':
        print('У вас немає лопати')
        number_zero_two()

    elif xid == 'search':
        reward_xid = str([new_arr[0][1]]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(reward_xid)

        if reward_xid == 'Вода':
            print('у вас вода, тепер ви на 2 хода попереду')
            one_two_cells.zero_number_five()
        elif reward_xid == 'Скарб':
            print('Ви знайшли скарб, ви перемогли')
            end_game(total_call_count)

        else:
            print('нічого немає')
            number_zero_three()

