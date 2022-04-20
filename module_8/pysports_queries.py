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
  
# execute your query
cursor.execute("SELECT team_id, team_name, mascot FROM team")
  
# fetch all the matching rows 
result = cursor.fetchall()
  
# loop through the rows
print("--- DISPLAYING TEAM RECORDS ---")
for row in result:
    print("Team ID = ", row[0], )
    print("Team Name = ", row[1])
    print("Mascot  = ", row[2])
    print("\n")

print("\n")
# execute your query
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
  
# fetch all the matching rows 
result = cursor.fetchall()
  
# loop through the rows
print("--- DISPLAYING PLAYER RECORDS ---")
for row in result:
    print("Player ID = ", row[0], )
    print("First Name = ", row[1])
    print("Last Name  = ", row[2])
    print("Team ID  = ", row[3])
    print("\n")

input("\n\n Press any key to continue...")