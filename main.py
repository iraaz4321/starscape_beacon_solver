import sqlite3
import time
import copy

con = sqlite3.connect("starscape_pro.db")

cur = con.cursor()


def find_beacon(first_color, second_color, third=None):
    start = time.time()
    c = cur.execute("SELECT id, connected_i From systems where spectral=? AND security='Wild' AND connection_count=?", [first_color, len(second_color)]).fetchall()

    possible = []

    for x in c:
        connected = list(map(int, x[1].split(",")))
        second_colors = copy.deepcopy(second_color)
        for connected_system in connected:
            sql = f"Select spectral from systems where id={connected_system};"
            color = cur.execute(sql).fetchone()[0]
            if color in second_colors:
                second_colors.remove(color)
            else:
                break
        else:
            possible.append(x[0])

    if third is not None:
        print(possible)
        for x in possible:
            third_colors = copy.deepcopy(third)
            system_col = third_colors.pop(0)
            sql = f"Select name from systems where id={x} AND connection_count={len(third_colors)} AND spectral='{system_col}';"
            c = cur.execute(sql).fetchone()
            if c is None:
                print(x)
                possible.remove(x)
            else:
                print(c[0])

    name_list = []
    for system_id in possible:
        sql = f"Select name from systems where id={system_id};"
        name_list.append(cur.execute(sql).fetchone()[0])

    print(name_list)



    end = time.time()

    print("Time took: ", end-start)

first_color = "A"
second_colors = ["B", "B", "G", "G"]
third_colors = ["B", "A", "G", "G"]
find_beacon(first_color, second_colors, third_colors)
