stock = {'\nStrandmok Cap-toe Oxford': 5, 'McAllister Wingtip Oxford': 2, 'Strand Cap-toe Oxford': 7,
         'Cambridge Cordovan Wingtip': 3, 'Bartlett Cap-toe Oxford': 11, 'Nike': 11, 'Puma': 14, 'Rebook': 21,
         'Adidas': 18, 'Jordan': 31}

salesRep = []

# Create menu
def menu():
    print('\nPress 1: To add shoes to stock.')
    print('Press 2: To check shoe stock.')
    print('Press 3: To sale shoes from stock.')
    print('Press q: To exit.')
    return input('\nWhat would you like to do? ')

run = menu()

while True:
    if run == '1':
        addStock = input('\nShoes to be added to stock: ')
        amount = int(input('Quantity of shoes to be added to stock: '))
        stock[addStock] = amount
        run = menu()

    elif run == '2':
        for key, value in stock.items():
            print('{}: {}'.format(key, value))
        run = menu()

    elif run == '3':
        shoes = input('\nShoes to be sold: ')
        person = input('Sales representative: ')
        if shoes in stock:
            if person in salesRep:
                print('\nHi, {}! Keep up the good work.'.format(person))
                run = menu()
            else:
                if stock[shoes] > 0:
                    stock[shoes] -= 1
                    salesRep.append(person)
                    print("\n{} sold a pair of {} shoes. You're on a role!".format(person, shoes))
                    run = menu()
                else:
                    print('{}, please check your input because we do not currently have {} in stock at this time.'
                          .format(person, shoes))
                    run = menu()
        else:
            print("The pair of {}'s are out of stock at this time".format(shoes))
            run = menu()

    elif run == 'q':
            break

print('\nTransaction compete.')
