import sqlite3 as sq
import variables as var


def write_score():
    nick = "'" + var.NICKNAME + "'"

    with sq.connect('assets/top_users.db') as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS top_users (name TEXT, score INTEGER)')
        cur.execute(f"SELECT * FROM top_users WHERE name = {nick}")
        ans = cur.fetchall()

        if len(ans) == 0:
            cur.execute(f'INSERT INTO top_users VALUES {(var.NICKNAME, var.SCORE)}')
        elif var.SCORE > ans[0][1]:
            cur.execute(f'UPDATE top_users SET score = {var.SCORE} WHERE name = {nick}')
