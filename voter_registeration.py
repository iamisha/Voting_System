# voter_registration.py

import csv
import datetime

def register_voter():
    try:
        # Collect voter details
        sno = generate_serial_number()
        name = input("Enter the name of the voter: ")
        dob = input("Enter the date of birth (yyyy/mm/dd): ")
        address = input("Enter the address: ")
        password = input("Set a password: ")

        # Check eligibility based on age
        if calculate_age(dob) < 18:
            print("Sorry! Only individuals above 18 years of age are eligible to register as voters.")
            return

        # Write voter details to the CSV file
        with open('doc_files/voterlist.csv', 'a', newline='') as csvfile:
            fieldnames = ['VoterSNO', 'Name', 'DateOfBirth', 'Address', 'Password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty, write header if needed
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write voter details
            writer.writerow({'VoterSNO': sno, 'Name': name, 'DateOfBirth': dob, 'Address': address, 'Password': password})

            print("Voter registered successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def generate_serial_number():
    # In a real system, this could involve generating a unique identifier
    # For simplicity, let's assume a sequential serial number.
    with open('doc_files/voterlist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        return str(sum(1 for row in reader) + 120)

def calculate_age(dob):
    birth_date = datetime.datetime.strptime(dob, "%Y/%m/%d")
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Example usage
register_voter()
generate_serial_number()

