import mysql.connector


# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="blood_donor_db"
    )

# Add a donor
def add_donor(name, blood_type, contact):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, blood_type, contact) VALUES (%s, %s, %s)", (name, blood_type, contact))
    conn.commit()
    conn.close()

# Find donors by blood type
def find_donors(blood_type):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name, contact FROM donors WHERE blood_type = %s", (blood_type,))
    results = cursor.fetchall()
    conn.close()
    return results

# Main menu
def main():
    while True:
        print("Blood Donor Finder")
        print("1. Add Donor")
        print("2. Find Donors by Blood Type")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            blood_type = input("Enter blood type: ")
            contact = input("Enter contact: ")
            add_donor(name, blood_type, contact)
            print("Donor added successfully!")

        elif choice == '2':
            blood_type = input("Enter blood type to search: ")
            donors = find_donors(blood_type)
            if donors:
                print("Donors with blood type", blood_type)
                for donor in donors:
                    print(f"Name: {donor[0]}, Contact: {donor[1]}")
            else:
                print("No donors found with blood type", blood_type)

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
