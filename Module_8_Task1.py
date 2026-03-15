import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kathmandu123",
    database="flight_game"
)
cursor = connection.cursor()
icao = input("Enter ICAO code: ").strip().upper()
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
result = cursor.fetchone()
if result:
    name, town = result
    print(f"Airport name: {name}")
    print(f"Location: {town}")
else:
    print("No airport found with that ICAO code.")
cursor.close()
connection.close()