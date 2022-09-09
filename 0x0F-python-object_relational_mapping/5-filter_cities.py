#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities RIGHT JOIN states"
                " ON cities.state_id = states.id WHERE "
                "states.name = '{}'".format(sys.argv[4]))
    result = cur.fetchall()
    print(", ".join(row for row in result)
    cur.close()
    db.close()