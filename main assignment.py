# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("\nWelcome to BookMyShow")

acc = input("\nDO YOU HAVE A ACCOUNT (Y/N)")
em = []
if acc == 'y' or acc == 'yes' or acc == 'Y' or acc == 'YES':
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    pas = input("\nENTER YOUR PASSWORD:-")
    otp = int(input("\nENTER A OTP CODE ON YOUR EMAIL AND PHONE NO:-"))

    print("\n-------LOGIN SUCCESSFUL-------")

else:
    nam = input("\nENTER YOUR FULL NAME:-")
    pn = int(input("\nENTER YOUR PHONE NO:-"))
    city = input("\nENTER YOUR CITY NAME:-")
    state = input("\nENTER YOUR STATE:-")
    em = input("\nENTER YOUR EMAIL ID:-")
    e.append(em)
    passw = input("\nENTER YOUR PASSWORD:-")
    print(f"\nOTP SEND TO {pn} AND {em}")
    ot = int(input("\nENTER THE OTP NO:-"))

    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
print("\n THESE ARE THE LATEST MOVIES----")
query1 = "select movies from movies"
x = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = int(input('Enter number of Row - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

class chart:
    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j + 1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat / Total_seat) * 100
        return percentage


class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    x = int(input('Select Option - '))
    if x == 1:
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num) + 1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num) + 1, end='  ')
                else:
                    print(int(num) + 1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif x == 2:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, Row + 1) and Column_number in range(1, Seats + 1):
            if table_of_chart[str(Row_number - 1)][str(Column_number)] == 'S':
                if Row * Seats <= 60:
                    prize_of_ticket = 10
                elif Row_number <= int(Row / 2):
                    prize_of_ticket = 10
                else:
                    prize_of_ticket = 8
                print('prize_of_ticket - ', '$', prize_of_ticket)
                conform = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    elif x == 3:
        print('Number of purchased Ticket - ', Booked_seat)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', prize_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()

    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
            if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    else:
        print()
        print('***  Invalid Input  ***')
        print()

print("\n THESE ARE THE LATEST MOVIES----")
query1 = "select movies from movies"
my_cursor.execute(query1)
for a in my_cursor:
    print(a)

name = []
mname = input("\n WHICH MOVIE YOU WANT TO WATCH :-")
tik = int(input("\n ENTER NUMBER OF TICKETS YOU WANT :-"))
for b in range(tik):
    nam = input("\nENTER NAME :-")
    name.append(nam)

hall = []
date = []
timing = []
charges = []
query2 = "select hall from movies where movies = '{}' ".format(mname)
my_cursor.execute(query2)
for c in my_cursor:
    hall.append(c)

query3 = "select date from movies where movies = '{}'".format(mname)
my_cursor.execute(query3)
for d in my_cursor:
    date.append(d)

query4 = "select timing from movies where movies = '{}'".format(mname)
my_cursor.execute(query4)
for e in my_cursor:
    timing.append(e)

query5 = "select charges*{} from movies where movies = '{}'".format(tik, mname)
my_cursor.execute(query5)
for f in my_cursor:
    charges.append(f)

seatnum = random.randint(1, 100)

print(f"YOU HAVE TO PAY {charges} RUPEES")
pay = input("TO PAY ENTER (P) :-")

print("\nyour ticket is hear - ")

if tik == 1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum}")
    print(f"your ticket has been send to your email {em}")

if tik > 1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum} to {seatnum + (tik - 1)}")
    print(f"your ticket has been send to your email {em}")