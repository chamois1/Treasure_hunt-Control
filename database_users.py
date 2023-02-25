import sqlite3
import easy_game.one_two_cells as one_two_cells

def end_game(new_move):
    conn = sqlite3.connect('search_treasures.db')

    cursor = conn.cursor()

    # оновлення значення останнього рядка таблиці
    cursor.execute("UPDATE users SET move = ? WHERE ROWID = (SELECT MAX(ROWID) FROM users)", (new_move,))

    # збереження змін до бази даних
    conn.commit()

    # закриття з'єднання з базою даних
    conn.close()

    print(f"Гра закінчена, вам знадобилось {new_move} ходів, щоб закінчити цю гру")

