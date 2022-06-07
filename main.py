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

conn = sqlite3.connect("starscape_pro.db")

def color_only_solve(main, colors, connected:int =0):
    if connected == 0:
        possible = conn.execute("SELECT id, connected_i, spectral, name, security FROM systems WHERE security='Wild' and spectral=?", [main]).fetchall()
    else:
        possible = conn.execute("SELECT id, connected_i, spectral, name, security FROM systems WHERE security='Wild' and spectral=? and connection_count=?", [main, connected]).fetchall()

    possible_s = []
    for system in possible:
        connected = conn.execute(f"SELECT id, connected_i, spectral FROM systems WHERE id IN ({system[1]})").fetchall()
        con = set()
        col = []
        level2 = [system[0]]
        for color in connected:
            if color[2] not in colors:
                break
            else:
                level2.append(color[0])
        for i in connected:
            col.append(i[2])
            for x in list(map(int, i[1].split(","))):
                if x not in level2:
                    con.add(str(x))

        connnected_2 = conn.execute(f"SELECT id, connected_i, spectral FROM systems WHERE id IN ({','.join(con)})").fetchall()
        for color in connnected_2:
            if color[2] not in colors:
                break
            else:
                col.append(color[2])
        if sorted(col) == sorted(colors):
            possible_s.append(system[3])
    return possible_s

