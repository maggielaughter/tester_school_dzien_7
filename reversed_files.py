def reversed1(path_put, path_save):
    try:
        with open(path_put) as my_file:
            data=my_file.read()
            reversed(data)

        with open(path_save, 'wt') as my_file:
            my_file.write(data[::-1])
    except OSError as err:
        print(err)

reversed1('plik.txt', 'plik4.txt')