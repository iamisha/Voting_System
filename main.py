from admin import AdminLogin, Constitution
from voters import VotersLogin, VoteCasting, Result, VoterCount
from add_voters import Voterlist
from tabulate import tabulate

# new
from candidate_reg import Candidate
import allow_vote
from utils import read_file

cn = Candidate()
######################################


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
        #new
        print("4) Update Candidate")
        print("5) Delete candidate")
        ###############################
        print("6) Show Candidates")
        print("7) Add Voters")
        print("8) Show Voter List")
        print("9) Participants")
        print("#) Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            Constitution.add_constituency()
        elif choice == '2':
            Constitution.show_constituencies()

#new
        elif choice == '3':
            name = input("Enter name: ")
            party = input("Enter party: ")
            address = input("Enter address: ")
            cn.add(name, party, address)

        elif choice == '4':
            id = input("Enter id: ")

            stat, idx, lst = cn.does_exist(id)

            if not stat:
                print("DOes not exist")
                continue
            else:
                ch = int(input("What to update:\n\t1) name\n\t 2) party \n\t3) address "))

                name = lst[1]
                party = lst[2]
                address = lst[3]

                if ch == 1:
                    name = input("Enter name: ")
                elif ch==2:
                    party = input("Enter party: ")
                else:
                    address = input("Enter address: ")
                
                cn.add(name, party, address, update=True, idx=idx)
              

        elif choice == '5':
            id = input("ENter id: ")
            cn.delete(id)

        elif choice == '6':
            cn.show()

################################################################################

        elif choice == '7':
            Voterlist.add_voter()
        elif choice == '8':
            Voterlist.show_voter_list_admin()
        elif choice == '9':
            VoterCount.count_voters()
        elif choice == '#':
            print("Going back to main menu.")
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
            pass
        elif choice == '2':
            Constitution.show_candidates()
            pass
        elif choice == '3':
           Voterlist.show_voter_list()
        elif choice == '4':
            # Implement search voter logic
            pass

        #new
        elif choice == '5':
            headers = ['sno', 'name', 'dob', 'address', 'passowrd', 'voted']
            sno = input("Enter sno: ")
            password = input("Enter username: ")

            dat = read_file(headers=None, FILE_NAME='voterlist.txt')

            stat, lst = allow_vote.does_exist(sno, password, dat)
            
            if stat:

                if lst[-1] == '0':
                    id = input("Enter candidate id: ")

                    stat, _, lst = cn.does_exist(id)

                    if stat:
                        allow_vote.vote(id, lst)
                        print("Voted")
                    else:
                        print("Cannot find candidate")       
            else:
                print("Already voted")    


#######################################################################

        elif choice == '#':
            print("Going back to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def show_results():
    Result.show_results()

if __name__ == "__main__":
    main()

