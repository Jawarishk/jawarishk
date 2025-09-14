import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ankkalinna',
         user='root',
         password='Malik$12',
         autocommit=True
 )

    cursor = connection.cursor()

    while True:
        icao = input("Enter ICAO code (or press Enter to quit): ").strip().upper()
        if icao == "":
            break

        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao,))
        result = cursor.fetchone()

        if result:
            print(f"Airport: {result[0]}, Location: {result[1]}")
        else:
            print("No airport found with that ICAO code.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()