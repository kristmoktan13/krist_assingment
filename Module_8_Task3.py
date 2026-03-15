import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kathmandu123",
    database="flight_game"
)
cursor = connection.cursor()
def get_airport(icao):
    cursor.execute(
        "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s",
        (icao,)
    )
    return cursor.fetchone()
icao1 = input("Enter ICAO code of the first airport: ").strip().upper()
icao2 = input("Enter ICAO code of the second airport: ").strip().upper()
result1 = get_airport(icao1)
result2 = get_airport(icao2)
if not result1:
    print(f"Airport '{icao1}' not found.")
elif not result2:
    print(f"Airport '{icao2}' not found.")
else:
    name1, lat1, lon1 = result1
    name2, lat2, lon2 = result2
    distance = geodesic((lat1, lon1), (lat2, lon2)).kilometers
    print(f"\nDistance between {name1} and {name2}:")
    print(f"{distance:.2f} km")
cursor.close()
connection.close()