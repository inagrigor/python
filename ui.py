
from logger2 import input_data, print_data
def interface():
    print ("Buna ziua, ati nimerit la botul informational a lui GeekBrains \n 1 - introducerea datelor \n 2 - extragerea de date")
    command = int(input('introduceti numarul '))  # variabila prin care primim date de la consoli
    while command != 1 and command != 2:
        print ("numarul nu este introds corect ")
        command = int(input('introduceti numarul '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    

        