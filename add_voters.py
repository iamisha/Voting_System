from datetime import datetime
from tabulate import tabulate
#from admin import AdminLogin, Constitution
import uuid
#import os
import getpass
from utils import read_file, write_file

class VoterSystem:
    def __init__(self):
        self.voter_list_file = "doc_files/voterlist.txt"
        self.voter_data = []
        self.headers = ['SN', 'sno', 'name', 'dob', 'address', 'password', 'vote_status']

    def register_voter(self):
        voter_sno = self.generate_voter_sno()
        name = input("Enter Name of Voter: ")
        dob = input("Enter Date of Birth (yyyy/mm/dd): ")
        address = input("Enter Address: ")
        password = getpass.getpass("Enter Password: ")

        if self.check_eligibility(dob):
            
            voter_entry = [voter_sno, name, dob, address, password, '0']
        #     with open(self.voter_list_file, "a") as file:
        #         file.write(voter_entry)
            
            data = read_file(headers=None, FILE_NAME=self.voter_list_file)

            data.append(voter_entry)

            write_file(data, self.headers, self.voter_list_file)

            print("Voter registered successfully!")
        else:
            print("Voter is not eligible due to age.")

    def update_voter_details(self, voter_sno, new_password):
        # with open(self.voter_list_file, "r") as file:
        #     for line in file:
        #         data = line.strip().split("\t")
        #         if data[0] == voter_sno:
        #             data[-1] = new_password
        #         updated_data.append("\t".join(data))
        
        # with open(self.voter_list_file, "w") as file:
        #     file.write("\n".join(updated_data))

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        for lst in data:
            if lst[0] == voter_sno:
                idx = data.index(lst)
                data[idx][-2]=new_password
                write_file(data, headers=self.headers)
                print("Voter details updated successfully!")
                return
        
        print("SNO not found")

    def delete_voter(self, voter_sno):
        # temp_file = "doc_files/temp_voterlist.txt"
        # with open(self.voter_list_file, "r") as file, open(temp_file, "w") as temp:
        #     for line in file:
        #         data = line.strip().split("\t")
        #         if data[0] != voter_sno:
        #             temp.write(line)

        # os.remove(self.voter_list_file)
        # os.rename(temp_file, self.voter_list_file)

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        for lst in data:
            if lst[0] == str(voter_sno):
                if lst[-1] == '1':
                    print("VOter has already voted cannot delete")
                    return
                else:
                    data.remove(lst)
                    print("Removed voter")
                    write_file(data, headers=self.headers, FILE_NAME=self.voter_list_file)
                    print("Voter details deleted successfully!")
                    return

        
    def search_voter_details(self, voter_sno):
        # with open(self.voter_list_file, "r") as file:
        #     voter_data = [line.strip().split("\t") for line in file]

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        for lst in data:
            if lst[0] == voter_sno:
                # Replace the password with '*' characters
                lst[-2] = '*' * len(lst[-2])
                #headers = ["Voter SNO", "Name", "Date of Birth", "Address", "Password"]
                print(tabulate([lst], headers=self.headers, tablefmt="grid"))
                return

        print("Voter not found.")

    def check_eligibility(self, dob):
        birth_year = int(dob.split("/")[0])
        current_year = datetime.now().year
        return current_year - birth_year > 18
    
    def view_voter_list(self):
        print("Voter List:")
        # with open(self.voter_list_file, "r") as file:
        #     voter_data = [line.strip().split("\t") for line in file]

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        # Replace the password with '*' characters
        for lst in data:
            lst[-2] = '*' * len(lst[-2])

        
        #headers = ["Voter SNO", "Name", "Date of Birth", "Address", "Password"]
        print(tabulate(data, headers=self.headers[1:], tablefmt="grid"))

    def show_voter_list_admin(self):
        # with open("doc_files/voterlist.txt", "r") as file:
        #     lines = file.readlines()
        #     data = [line.strip().split("\t") for line in lines]

        # header = ["Voter SNO", "Name of Voter", "Date of Birth", "Address", "Password"]

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        print(tabulate(data, headers=self.headers, tablefmt="grid"))


    def generate_voter_sno(self):
        # if not os.path.exists("doc_files/voterlist.txt"):
        #     with open("doc_files/voterlist.txt", "w"):
        #         pass

        # with open("doc_files/voterlist.txt", "r") as file:
        #     lines = file.readlines()

        data = read_file(headers=None, FILE_NAME=self.voter_list_file)

        if data:
            last_serial_number = int(data[-1][0])
            voter_sno = last_serial_number + 1
        else:
            voter_sno = 100

        return str(voter_sno)

        # numbered_data1 = [[i + 1] + data[i] for i in range(len(data))]
        # return str(len(numbered_data1) + 1)
    
    def generate_password(self):
        password = str(uuid.uuid4().int)[:8]
        return password

