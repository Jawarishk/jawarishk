import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    """Fetch airport coordinates from the database based on ICAO code"""
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            database="flight_game",
            user="root",  # Change if needed
            password="Malik$12"  # Your password
        )

        cursor = connection.cursor()

        query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return (result[0], result[1])
        else:
            return None

    except mysql.connector.Error as error:
        print(f"Error connecting to MariaDB: {error}")
        return None


def main():
    print("Airport Distance Calculator")
    print("===========================")
    icao1 = input("Enter the first ICAO code: ").strip().upper()
    icao2 = input("Enter the second ICAO code: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 is None:
        print(f"Airport with ICAO code {icao1} not found in the database.")
        return

    if coords2 is None:
        print(f"Airport with ICAO code {icao2} not found in the database.")
        return

    distance_km = geodesic(coords1, coords2).kilometers

    print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")


if __name__ == "__main__":
    main()