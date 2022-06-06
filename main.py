#MIT License
#
#Copyright (c) 2022 iraaz4321
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


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
