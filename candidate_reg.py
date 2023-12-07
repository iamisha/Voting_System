from utils import create_unique, read_file, write_file
from tabulate import tabulate

FILE_NAME = 'doc_files/candidate.txt'

headers = ['S.N', 'ID', 'Name', 'Party', 'Address']

class Candidate:
    
    @classmethod
    def does_exist(cls, id):

        data = read_file(headers, FILE_NAME)

        for lst in data:
            if id in lst:
                return 1, data.index(lst), lst
        
        return 0, 0, 0
        
    @classmethod
    def add(cls, name, party, address, update=False, idx=None):
        lst = [name, party, address]

        data = read_file(headers, FILE_NAME)

        unq = create_unique(*lst)
        lst = [unq]+lst

        if not update:
            if lst in data:
                raise Exception("Already Exists")

            data.append(lst)

        else:
            data[idx] = lst

        write_file(data, headers, FILE_NAME)     

    @classmethod
    def delete(cls, id):
        
        data = read_file(headers, FILE_NAME)

        stat, idx, _ = cls.does_exist(id)

        if stat:
            data.pop(idx)
            print("Deleted")
            write_file(data, headers, FILE_NAME)
            return
            
        print("Cannot find data")
    
    def show(self):
        data = read_file(headers=headers, FILE_NAME=FILE_NAME)
        print(tabulate(data, headers=headers))