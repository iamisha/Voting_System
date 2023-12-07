import hashlib
import base64

def create_unique(*args):
    combined_string = "_".join(args)
    hashed = hashlib.sha256(combined_string.encode()).digest()
    encoded_id = base64.urlsafe_b64encode(hashed)[:15].decode("utf-8")
    return encoded_id

def write_file(data, headers, FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        lst = [[str(i+1)]+x for i, x in enumerate(data)]

        flat = [','.join(x) for x in lst]

        flat.insert(0, ','.join(headers))

        lst = '\n'.join(flat)

        f.write(lst)

    print("Written successfully")

def read_file(headers=None, FILE_NAME=None):
    with open(FILE_NAME, 'r+') as f:
        lines = f.readlines()

        if len(lines) == 0:
            print("No data in file")
            if headers:
                f.write(','.join(headers))
                return []
            return []
        
    raw_data = lines[1:]

    if len(raw_data) == 0:
        return []

    return [x.strip().split(',')[1:] for x in raw_data]
