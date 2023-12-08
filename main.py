from admin import AdminLogin, Constitution
from voters import Result, VoteCasting, VotersLogin, VoterCount
from add_voters import VoterSystem
from tabulate import tabulate

# new
from candidate_reg import Candidate
import allow_vote
from utils import read_file, write_file

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
            #voter_login = VotersLogin()
            #voter_login.login()
            voter_portal('voter_login')
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
        print("3.1) Update Candidate")
        print("3.2) Delete candidate")
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
            name = input("Enter name: ")
            party = input("Enter party: ")
            address = input("Enter address: ")
            cn.add(name, party, address)

        elif choice == '3.1':
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
              

        elif choice == '3.2':
            id = input("ENter id: ")
            cn.delete(id)

        elif choice == '4':
            cn.show()

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
        # print("3) Show all Voter List")
        # print("4) Search Voter")
        print("3) Vote")
        print("#) Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            Constitution.show_constituencies()
        elif choice == '2':
            cn.show()
        # elif choice == '3':
        #     VoterSystem().view_voter_list()
        # elif choice == '4':
        #     voter_sno = input("Enter Voter SNO: ")
        #     VoterSystem().search_voter_details(voter_sno)
        #new
        elif choice == '3':
            headers = ['sno', 'name', 'dob', 'address', 'password', 'vote_status']
            sno = input("Enter sno: ")
            password = input("Enter password: ")

            dat = read_file(headers=None, FILE_NAME='doc_files/voterlist.txt')

            stat, v_lst = allow_vote.does_exist(sno, password, dat)
            
            if stat:
                if v_lst[-1] == '0':
                    id = input("Enter candidate id: ")

                    stat, _, lst = cn.does_exist(id)

                    if stat:
                        allow_vote.vote(id, lst)

                        idx = dat.index(v_lst)

                        v_lst[-1] = '1'

                        dat[idx] = v_lst

                        write_file(dat, headers, 'doc_files/voterlist.txt')
                        print("Voted")
                    else:
                        print("Cannot find candidate")       
            else:
                print("Already voted")    


        elif choice == '#':
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def show_results():
    Result.show_results()

if __name__ == "__main__":
    main()
