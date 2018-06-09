def lines_histogram(input):
    result={}
    with open(input,'rt') as my_file:
        for line in my_file:
            string=line.rstrip('\r\n')
            result[len(string)]=result.get(len(string,0) +1
    return result

def lines_histogram2(input_file):
    result={}
    for line in input_file:
        string = len(line.rstrip('\r\n'))
        result[string] = result.get(string, 0) + 1
    return result

if __name__=='__main__':
    path = input('Podaj ścieżkę: ')
    try:
        print(lines_histogram(path))
    except OSError as err:
        print(err)

    try:
        with open(path, 'rt') as input_file:
            print(lines_histogram2(input_file))
    except OSError as err:
        print(err)