from admin import AdminLogin, Constitution
from voters import Result, VoteCasting, VotersLogin, VoterCount
from add_voters import VoterSystem
from tabulate import tabulate


def main():
    print("Welcome To Nepal Government E-Voting Panel, Vote for Great Country")

    while True:
        user_type = input(" A for Admin \n B for Voter \n C for Result \n Q to Quit \n ").upper()

        if user_type == 'A':
            admin_login = AdminLogin()
            admin_login.authenticate()
            admin_portal(admin_login)
        elif user_type == 'B':
            voter_login = VotersLogin()
            voter_login.login()
            voter_portal(voter_login)
        elif user_type == 'C':
            show_results()
        elif user_type == 'Q':
            print("Exiting the E-Voting System.")
            break
        else:
            print("Invalid input. Please select A, B, C, or Q.")

def admin_portal(admin_login):
    while True:
        print("\nAdmin Portal:")
        print("1) Add Constituency")
        print("2) Show Constituency")
        print("3) Add Candidates")
        print("4) Show Candidates")
        print("5) Add Voters")
        print("6) Show Voter List")
        print("7) Update Voter List")
        print("8) Delete Voter List")
        print("9) Participants")
        print("#) Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            Constitution.add_constituency()
        elif choice == '2':
            Constitution.show_constituencies()
        elif choice == '3':
            Constitution.add_candidates()
        elif choice == '4':
            Constitution.show_candidates()
        elif choice == '5':
            VoterSystem().register_voter()
        elif choice == '6':
            VoterSystem().view_voter_list()
        elif choice == '7':
            voter_sno = input("Enter Voter SNO: ")
            new_password = input("Enter New Password: ")
            VoterSystem().update_voter_details(voter_sno, new_password)
        elif choice == '8':
            voter_sno = input("Enter Voter SNO: ")
            VoterSystem().delete_voter(voter_sno)
        elif choice == '9':
            VoterCount.count_voters()
        elif choice == '#':
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def voter_portal(voter_login):
    while True:
        print("\nVoter Portal:")
        print("1) Show Constituency")
        print("2) Show Candidates")
        print("3) Show all Voter List")
        print("4) Search Voter")
        print("5) Vote")
        print("#) Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            Constitution.show_constituencies()
        elif choice == '2':
            Constitution.show_candidates()
        elif choice == '3':
            VoterSystem().view_voter_list()
        elif choice == '4':
            voter_sno = input("Enter Voter SNO: ")
            VoterSystem().search_voter_details(voter_sno)
        elif choice == '5':
            VoteCasting.cast_vote("Constituency_Name")
            pass
        elif choice == '#':
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def show_results():
    Result.show_results()

if __name__ == "__main__":
    main()
