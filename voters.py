from tabulate import tabulate
import os

class VotersLogin:
    @classmethod
    def login(cls):
        voter_sno = input("Enter Voter's Serial Number: ")
        password = input("Enter Password: ")

        with open("voterlist.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                voter_info = line.strip().split("\t")
                if voter_info[0] == voter_sno and voter_info[-1] == password:
                    print("Login successful!")
                    return True
            print("Invalid Voter Serial Number or Password.")
            return False

class VoteCasting():
    @classmethod
    def cast_vote(cls, constituency_name):
        voter_sno = input("Enter Voter's Serial Number: ")

        if cls.has_already_voted(voter_sno):
            print("You have already cast a vote.")
            return

        candidacy_from = input("Enter Candidacy From (Location): ")
        candidate_name = input("Enter Candidate Name: ")

        with open("candidatelist.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                candidate_info = line.strip().split("\t")
                if candidate_info[0] == candidate_name and candidate_info[2] == candidacy_from:
                    print("Vote cast successfully!")
                    cls.record_vote(candidate_name)
                    cls.record_voted(voter_sno)
                    return
            print("Invalid Candidate or Location.")

    @staticmethod
    def has_already_voted(voter_sno):
        voted_file_path = "voted.txt"


        if not os.path.exists(voted_file_path):
            with open(voted_file_path, "w"):
                pass

        with open(voted_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                voted_voter_sno = line.strip()
                if voted_voter_sno == voter_sno:
                    return True
        return False

    @staticmethod
    def record_voted(voter_sno):
        with open("voted.txt", "a") as file:
            file.write(f"{voter_sno}\n")

    @staticmethod
    def record_vote(candidate_name):
        with open("votecount.txt", "a") as file:
            file.write(f"{candidate_name}\n")

class Result:
    @classmethod
    def show_results(cls):
        votes_count = cls.count_votes()
        if votes_count:
            header = ["Candidate Name", "Total Votes"]
            table_data = [[candidate, votes] for candidate, votes in votes_count.items()]
            print(tabulate(table_data, headers=header, tablefmt="grid"))
        else:
            print("No votes recorded yet.")

    @staticmethod
    def count_votes():
        votes_count = {}
        with open("votecount.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                candidate_name = line.strip()
                votes_count[candidate_name] = votes_count.get(candidate_name, 0) + 1
        return votes_count
    
    @staticmethod
    def show_winner():
        votes_count = Result.count_votes()
        if votes_count:
            winner = max(votes_count, key=votes_count.get)
            print(f"The winner is {winner} with {votes_count[winner]} votes.")
        else:
            print("No votes recorded yet.")

class VoterCount:
    @classmethod
    def count_voters(cls):
        with open("voterlist.txt", "r") as file:
            lines = file.readlines()
            total_voters = len(lines)
            print(f"Total number of voters: {total_voters}")

