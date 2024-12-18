def main():

    holidaylist = []

    choice = 0
    while choice != 4:
        print("** Holiday Management **")
        print("1) Add Holidays")
        print("2) Lookup a Holiday")
        print("3) Display Holidays")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a Holiday")
            nHoliday = input("Enter the name of Holiday >>> ")
            nDaynumbers = input("Enter the number of days >>> ")
            holidaylist.append([nHoliday, nDaynumbers])

        elif choice == 2:
            print("Lookup a Holiday...")
            keyword = input("Enter Holiday: ")
            found = False
            for index, holiday in enumerate(holidaylist):

                if keyword in holiday:
                    print("Holiday found:", holiday)
                    print("1) Edit Holiday")
                    print("2) Delete Holiday")
                    sub_choice = int(input("Enter your choice: "))

                    if sub_choice == 1:
                        new_name = input("Enter new name for the Holiday: ")
                        new_days = input("Enter new number of days: ")
                        holidaylist[index] = [new_name, new_days]
                        print("Holiday updated successfully!")

                    elif sub_choice == 2:
                        del holidaylist[index]
                        print("Holiday deleted successfully!")

                    found = True
                    break

            if not found:
                print("Holiday not found!")

        elif choice == 3:
            print("Displaying all Holidays....")
            for holiday in holidaylist:
                print(holiday)

        elif choice == 4:
            print("Quitting program")

    print("Program has Terminated!")


if __name__ == "__main__":
    main()
