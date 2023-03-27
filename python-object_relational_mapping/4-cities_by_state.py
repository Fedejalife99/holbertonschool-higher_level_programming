#!/usr/bin/env python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <mysql username> <mysql password> <database name>")
    exit(1)

  db = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=sys.argv[1],
                       passwd=sys.argv[2],
                       db=sys.argv[3])

  cursor = db.cursor()

  cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

  rows = cursor.fetchall()

  for row in rows:
    print(row)

  cursor.close()
  db.close()