import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Malik$12",
            database="flight_game"
        )
    except Error as e:
        print("Connection error:", e)
        return

    try:
        cursor = connection.cursor()
        country = input("Enter country code (for example FI): ").strip().upper()

        query = """
            SELECT type, COUNT(*) 
            FROM airport 
            WHERE iso_country = %s 
            GROUP BY type 
            ORDER BY type;
        """
        cursor.execute(query, (country,))
        results = cursor.fetchall()

        if results:
            print(f"Airports in {country}:")
            for row in results:
                print(f"{row[0]}: {row[1]}")
        else:
            print("No airports found for that country code.")
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        connection.close()

if __name__ == "__main__":
    main()
