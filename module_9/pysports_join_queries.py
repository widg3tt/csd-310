# Kyle Jones
# 4/28/22
# Module 9.2
# https://github.com/widg3tt/csd-310

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "kyle",
    "password": "Landon.1",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor= db.cursor()

sql = "SELECT player_id, first_name, last_name, team_name \
       FROM player \
       INNER JOIN team \
       ON player.team_id = team.team_id"

cursor.execute(sql)

result = cursor.fetchall()

# loop through the rows
print("--- DISPLAYING PLAYER RECORDS ---")
for row in result:
    print("Player ID = ", row[0], )
    print("First Name = ", row[1])
    print("Last Name  = ", row[2])
    print("Team Name  = ", row[3])
    print("\n")

#Closing the connection
db.close()

input("Press any key to continue...")
