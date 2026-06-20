from vending_machine import VendingMachine

quit = False

list1 = [["Coke",10,3.50],["Sprite",8,3.50],["Ruffles Plain",23,2.25]]
list2 = [["Pokemon Pack 1",22,10.95],["Pokemon Pack 2",10,99.95]]

machine1 = VendingMachine(list1)
machine2 = VendingMachine(list2)
machines = [machine1,machine2]

print("\n--------- Welcome! ---------")

while not quit:
    valid_choice = False

    print("\n==== Vending Machine 1 ====")
    print(machine1)

    print("==== Vending Machine 2 ====")
    print(machine2)

    print("1. Add Money  2. Vend  3. Refund  4. Quit")

    try:
        choice = int(input("Choice: "))

        if choice < 4 and choice > 0:
            machine_choice = int(input("Which Machine? "))

            if machine_choice == 1 or machine_choice == 2:
                machine = machines[machine_choice-1]

                if choice == 1:
                    amount = float(input("How much? "))
                    print(machine.insert_money(amount))
                elif choice == 2:
                    product_num = int(input("Which Item? "))
                    print(machine.vend(product_num))
                elif choice == 3:
                    print(machine.return_credit())
            else:
                print("\nInvalid Option. Try Again.")
        elif choice == 4:
            print("\nGoodbye!")
            quit = True
        else:
            print("\nInvalid Option. Try Again.")

    except TypeError:
        print("\nInvalid Option. Try Again.")
    except ValueError:
        print("\nInvalid Option. Try Again.")






