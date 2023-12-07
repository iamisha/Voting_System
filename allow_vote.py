from utils import read_file, write_file

headers = ['S.N', 'ID', 'Name', 'Party', 'Address', 'Count']

FILE_NAME = 'votecount.txt'

def does_exist(sno, password, data):
    for lst in data: 
        if sno in lst:
            if password in lst:
                return 1, lst
    return 0, 0

def vote(candidate_id, lst):
    data = read_file(headers, FILE_NAME)

    for x in data:
        if candidate_id in x:
            x[-1] = str(int(x[-1])+1)
            write_file(data, headers, FILE_NAME)
            return
    
    lst.append('1')

    data.append(lst)
    write_file(data, headers, FILE_NAME)
    return


