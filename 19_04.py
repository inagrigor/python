
def input_surname():
    return input('Introduceti numele de familei:  ').title()

def input_name():
    return input('Introduceti numele:  ').title()

def input_patronymic():
    return input('Introduceti patronymic:  ').title()

def input_phone():
    return input('Introduceti phone:  ')

def input_address():
    return input('Introduceti adresa (orasul):  ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'
    
def add_contact(): # 
    contact_str = create_contact() # creem contact ca  string si il pastram in variabila
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str) # adaugam un contact
        
def create_list_contacts():# citeste failurile pastreaza text in varialbila, 
    with open("phonebook.txt", 'r', encoding='utf-8') as file: 
        all_contacts_str = file.read() # citim toate contactele in forma de un string
        return  all_contacts_str.rstrip().split('\n\n') # extragem string de contacte transformat in list
        
def print_contacts(cont_list=create_list_contacts()):
    for n, contact in enumerate(cont_list, 1):
        print(n, contact)
    
def search_contact():
    print(
            'Variante posibile de cautare:\n'
            '1. dupa numele de familie\n'
            '2. dupa numele\n'
            '3. dupa patronymicul\n'
            '4. dupa numarul de telefon\n'
            '5. dupa addresa(oras)\n'
            )
    
    var = input('Introduceti o varianta de cautare: ')
    while var not in ('1', '2', '3', '4', '5'):
            print ('introducerea incorecta')
            var = input('Introduceti o varianta de cautare: ')
            
    i_var = int(var) - 1 #transformam in int obtinem index
    search = input('introduceti datele de cautare: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file: # citim file
        contacts_str = file.read()
    # print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(list_contacts)
    
    for str_contact in contacts_list:
        lst_contact = str_contact.split()
        if search in lst_contact[i_var]:
            
            print(str_contact)
            
def copy_contact():
    contacts_list = create_list_contacts()
    
    print_contacts(contacts_list)
    
    one_copy_cont = int(input('Alegeti un contact dupa numarul de copiere: '))
    print()
    
    with open("phonebook_copy.txt", 'a', encoding='utf-8') as file:
        file.write(f'\n{contacts_list[one_copy_cont - 1]}\n')
            
          
        
    
def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass
    var = 0
    while var != '5':
        print(
            'Variante posibile:\n'
            '1. adaugam contact \n'
            '2. extragem pe ecran \n'
            '3. cautarea de contact\n'
            '4. copierea de contacte\n'
            '5. iesire'
            )
        print()
        var = input('Introduceti o varianta de actiune: ')
        while var not in ('1', '2', '3', '4', '5'):
            print ('introducerea incorecta')
            var = input('Introduceti o varianta de actiune: ')
        
        print()
        
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()  
            case '5':
                print('Iesire')
                
                
        print()
        
        
        
if __name__ == '__main__':
    interface()