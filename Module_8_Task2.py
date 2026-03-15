import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kathmandu123",
    database="flight_game"
)
cursor = connection.cursor()
country = input("Enter area code: ").strip().upper()
cursor.execute("""
    SELECT type,COUNT(*) AS total
    FROM airport
    WHERE iso_country= %s
    GROUP BY type
    ORDER BY type
""", (country,))
results = cursor.fetchall()
if results:
    print(f"\nAirports in {country}:")
    for airport_type, count in results:
        print(f"  {count} {airport_type}")
else:
    print("No airports found for that country code.")
cursor.close()
connection.close()