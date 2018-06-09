def read_csv(input_file):
    full_data=[]
    for line in input_file:
        string=line.rstrip('\r\n')
        data = string.split(',')
        full_data.append((data))
    return(full_data)


if __name__=='__main__':
    with open('plik.csv', 'rt') as input_file:
        print(read_csv(input_file))

def csv_to_list(csv_file):
    return[line.rstrip('\r\n').split(',') for line in csv_file]

def csv_to_list2(csv_file):
    expected_len = None
    result=[]
    for line in csv_file:
        record = line.rstrip('\r\n').split(',')
        if expected_len is None:
            expected_len=len(record)
        elif len(record) != expected_len:
            raise ValueError('Malformed CSV file')
        result.append(record)
    return result

def csv_to_list3(csv_file):
    result = [csv_file.readline().rstrip('\r\n').split(',')]
    for line in csv_file:
        record = line.rstrip('\r\n').split(',')
        if len(record) != len(result[0]):
            raise ValueError('Malformed CSV file.')
        result.append(record)
    return result

if __name__=='__main__':
    with open('plik.csv') as csv_file:
        print(csv_to_list3(csv_file))
