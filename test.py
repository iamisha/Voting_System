from candidate_reg import Candidate

cn = Candidate()

while True:
    choice = int(input("Enter: "))

    if choice == 1:
        name = input("ENter name: ")
        party = input("ENter party: ")
        address = input("ENter address: ")
        cn.add(name, party, address)
    
    elif choice==2:
        id = input("Enter id: ")

        stat, idx, lst = cn.does_exist(id)



        if not stat:
            print("DOes not exist")
            continue
        else:

            ch = int(input("What to update: "))

            name = lst[1]
            party = lst[2]
            address = lst[3]

            if ch == 1:
                name = input("ENter name: ")
            elif ch==2:
                party = input("ENter party: ")
            else:
                address = input("ENter address: ")
            


            cn.add(name, party, address, update=True, idx=idx)
    
    elif choice == 3:
        id = input("ENter id: ")
        cn.delete(id)
    
    else:
        continue




