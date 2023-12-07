
from modules.voter_registeration import VoterSystem

voter_system = VoterSystem()

while True:
    print("1. Register Voter")
    print("2. Update Voter Details")
    print("3. Search Voter Details")
    print("4. View Voter List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        voter_system.register_voter()
    elif choice == "2":
        voter_sno = input("Enter Voter SNO to update: ")
        new_password = input("Enter new password: ")
        voter_system.update_voter_details(voter_sno, new_password)
    elif choice == "3":
        voter_sno = input("Enter Voter SNO to search: ")
        voter_system.search_voter_details(voter_sno)
    elif choice == "4":
        voter_system.view_voter_list()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
