from tabulate import tabulate
import getpass

class AdminLogin:
    def __init__(self):
        self.username = ""
        self.password = ""

    def authenticate(self):
        while True:
            self.username = input("Enter your username: ")
            self.password = getpass.getpass("Enter your password: ")

            with open("login_info.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    if (
                        lines[i].strip() == f"Username: {self.username}"
                        and lines[i + 1].strip() == f"Password: {self.password}"
                    ):
                        print("Authentication successful!")
                        return
                print("Invalid username or password. Please try again.")
class Constitution:
    constituencies = []

    @classmethod
    def add_constituency(cls):
        constituency_name = input("Enter Constituency Name: ")
        election_date = input("Enter Date of Election (YYYY/MM/DD): ")

        with open("schedule.txt", "a") as file:
            file.write(f"{constituency_name}\t{election_date}\n")

        print("Constituency added successfully.")
        
    @classmethod
    def get_latest_election_date(cls):
        with open("schedule.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("No constituencies added yet.")

        latest_date = max(line.split("\t")[1].strip() for line in lines)
        return latest_date

    @classmethod
    def show_constituencies(cls):
        with open("schedule.txt", "r") as file:
            lines = file.readlines()
            data = [line.strip().split("\t") for line in lines]

        header = ["S.N","Constituency", "Date of Election (YYYY/MM/DD)"]
        numbered_data1 = [[i + 1] + data[i] for i in range(len(data))]
        print(tabulate(numbered_data1, headers=header, tablefmt="grid"))

    @classmethod
    def add_candidates(cls):
        candidate_name = input("Enter Candidate Name: ")
        political_party = input("Enter Political Party: ")
        candidacy_from = input("Enter Candidacy From: ")

        if cls.constituency_exists(candidacy_from):
            with open("candidatelist.txt", "a") as file:
                file.write(f"{candidate_name}\t{political_party}\t{candidacy_from}\n")

            print("Candidate added successfully.")
        else:
            print(f"Error: Constituency '{candidacy_from}' does not exist.")

    @classmethod
    def constituency_exists(cls, constituency_name):
        with open("schedule.txt", "r") as file:
            lines = file.readlines()
            constituencies = [line.split("\t")[0] for line in lines]

        return constituency_name in constituencies

    @classmethod
    def show_candidates(cls):
        with open("candidatelist.txt", "r") as file:
            lines = file.readlines()
            data = [line.strip().split("\t") for line in lines]

        header = ["S.N", "Name of Candidate", "Political Party", "CandidacyFrom"]
        numbered_data = [[i + 1] + data[i] for i in range(len(data))]

        print(tabulate(numbered_data, headers=header, tablefmt="grid"))
