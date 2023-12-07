from allow_vote import does_exist, vote
from utils import read_file

# if does_exist(12, 'sdasdsa', [2darray])

while True:
    id = input("Enter candidate id: ")
    data = read_file(['S.N', 'ID', 'Name', 'Party', 'Address'], 'candidate.txt')

    flag = False
    for lst in data:
        if id in lst:
            vote(id, lst)
            print("Voted")
            flag = True
            break

    if not flag:
        print("Cannot find candidate")