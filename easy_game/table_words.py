import random
from tabulate import tabulate


def chunks(lst, n):
    # Розбити список lst на списки довжини n
    return [lst[i:i+n] for i in range(0, len(lst), n)]

all_lists = [
    ['Вода'],
    [''],
    ['Вода', 'Скарб']   
]


elements = [random.choice(lst) for lst in all_lists]

# Перевірка на наявність дублів
while len(set(elements)) != len(elements):
    elements = [random.choice(lst) for lst in all_lists]



arr = [
    [elements[0], '', '', elements[1]],
    [elements[2], '', '', elements[0], ''],
    ['', elements[2], '', '', elements[1]],
    ['', '', elements[1], '', elements[2]],
    [elements[0], elements[2], '', '', '', '']
]


# arr = [
#     ['', '', '', ''],
#     ['', '', '', '', ''],
#     ['', '', '', '', ''],
#     ['', '', '', '', ''],
#     ['', '', '', '', '', '']
# ]



arr_flat = sum(arr, [])
random.shuffle(arr_flat)


arr_shuffled = chunks(arr_flat, 5)


umns = ['1', '2', '3', '4', '5']
print(tabulate(arr_shuffled, headers=umns, tablefmt="fancy_grid", showindex="always") + '\nКорісні команди\n search, go "up, down, left, right", "dig')




