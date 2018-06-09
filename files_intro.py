my_file = None
try:
    my_file=open('plik.txt', 'rt')
    data = my_file.read()
    print(data)
except OSError as err:
    print('Error :', str(err))
finally:
    if my_file is not None:
        print('Zamykam')
        my_file.close()
print()

try:
    with open('plik2.txt') as my_file:
        print(my_file.read())
except OSError as err:
    print(err)

with open('plik3.txt', 'wt') as out_file:
    out_file.write('jakiś tekst')

with open('plik.txt') as my_file:
    lines = my_file.readlines()
    print(lines)

with open('plik.txt') as my_file:
    for line in my_file:
        print(line)

text = 'some text\n'
print(text.strip('\r\n'))