from datetime import datetime
from tabulate import tabulate
from admin import AdminLogin, Constitution
import uuid
import os
import getpass

class VoterSystem:
    def __init__(self):
        self.voter_list_file = "doc_files/voterlist.txt"
        self.voter_data = []

    def register_voter(self):
        voter_sno = self.generate_voter_sno()
        name = input("Enter Name of Voter: ")
        dob = input("Enter Date of Birth (yyyy/mm/dd): ")
        address = input("Enter Address: ")
        password = getpass.getpass("Enter Password: ")

        if self.check_eligibility(dob):
            voter_entry = f"{voter_sno}\t{name}\t{dob}\t{address}\t{password}\n"
            with open(self.voter_list_file, "a") as file:
                file.write(voter_entry)
            print("Voter registered successfully!")
        else:
            print("Voter is not eligible due to age.")

    def update_voter_details(self, voter_sno, new_password):
        updated_data = []
        with open(self.voter_list_file, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                if data[0] == voter_sno:
                    data[-1] = new_password
                updated_data.append("\t".join(data))
        
        with open(self.voter_list_file, "w") as file:
            file.write("\n".join(updated_data))
        print("Voter details updated successfully!")

    def delete_voter(self, voter_sno):
        temp_file = "doc_files/temp_voterlist.txt"
        with open(self.voter_list_file, "r") as file, open(temp_file, "w") as temp:
            for line in file:
                data = line.strip().split("\t")
                if data[0] != voter_sno:
                    temp.write(line)

        os.remove(self.voter_list_file)
        os.rename(temp_file, self.voter_list_file)
        print("Voter details deleted successfully!")

    def search_voter_details(self, voter_sno):
        with open(self.voter_list_file, "r") as file:
            voter_data = [line.strip().split("\t") for line in file]

        for data in voter_data:
            if data[0] == voter_sno:
                # Replace the password with '*' characters
                data[-1] = '*' * len(data[-1])
                headers = ["Voter SNO", "Name", "Date of Birth", "Address", "Password"]
                print(tabulate([data], headers=headers, tablefmt="grid"))
                return

        print("Voter not found.")

    def check_eligibility(self, dob):
        birth_year = int(dob.split("/")[0])
        current_year = datetime.now().year
        return current_year - birth_year > 18
    
    def view_voter_list(self):
        print("Voter List:")
        with open(self.voter_list_file, "r") as file:
            voter_data = [line.strip().split("\t") for line in file]

        # Replace the password with '*' characters
        for data in voter_data:
            data[-1] = '*' * len(data[-1])

        headers = ["Voter SNO", "Name", "Date of Birth", "Address", "Password"]
        print(tabulate(voter_data, headers=headers, tablefmt="grid"))


    @classmethod
    def show_voter_list_admin(cls):
        with open("doc_files/voterlist.txt", "r") as file:
            lines = file.readlines()
            data = [line.strip().split("\t") for line in lines]

        header = ["Voter SNO", "Name of Voter", "Date of Birth", "Address", "Password"]
        print(tabulate(data, headers=header, tablefmt="grid"))


    @classmethod
    def generate_voter_sno(cls):
        if not os.path.exists("doc_files/voterlist.txt"):
            with open("doc_files/voterlist.txt", "w"):
                pass

        with open("doc_files/voterlist.txt", "r") as file:
            lines = file.readlines()

        if lines:
            last_serial_number = int(lines[-1].split("\t")[0])
            voter_sno = last_serial_number + 1
        else:
            voter_sno = 1

        return voter_sno

        numbered_data1 = [[i + 1] + data[i] for i in range(len(data))]
        return str(len(numbered_data1) + 1)
    
    def generate_password(self):
        password = str(uuid.uuid4().int)[:8]
        return password

