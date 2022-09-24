import random
from datetime import timedelta, date

# this function will generate a random employee from the list
def employeeGenerator():
    # below is the list of employee the system will generate
    employee = ["Luan Kinh Nguyen #1603579", "Phu Thi Vu #1262597", "Nguyet Thi Quach #1586492",
                 "Hoa LeThai Nguyen #1235739"]
    return random.choice(employee)
#"Le Thi Nguyen #1213281"

# this function generate the date for the loop
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# this is the main function
def main():

    # init the date
    start_date = date(2022, 9, 1)
    end_date = date(2022, 11, 1)

    # init the date name and license number
    print("date\t\tTime\t\t\tName and License Number")
    print("-------\t\t----------\t\t--------------------")
    for single_date in daterange(start_date, end_date):
        randomtime = random.randint(10, 18)
        randomMinutes = random.randint(1, 59)
        # if the hour is before 12 this will excecute the amount of repetition
        if randomtime < 12:
            print(single_date.strftime("%m/%d/%Y\t"), (str(randomtime) + ":" + str(randomMinutes) + " AM \t"),
                  employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
            if randomtime == 10:
                if randomMinutes == 14 or 15 or 16 or 17 or 19:
                    endHour = randomtime - random.randint(6, 8)
                    endminutes = random.randint(0, 45)
                    print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                          employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
                endHour = randomtime - random.randint(3, 5)
                endminutes = random.randint(0, 45)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")

            if randomtime == 11:
                endHour = randomtime - random.randint(4, 6)
                endminutes = random.randint(0, 50)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
        # if the hour is 12
        elif randomtime == 12:
            print(single_date.strftime("%m/%d/%Y\t"), (str(randomtime) + ":" + str(randomMinutes) + " PM \t"),
                  employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
            endHour = randomtime - random.randint(5, 7)
            endminutes = random.randint(0, 45)
            print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                  employeeGenerator(), "\t.\t \t \t \t ✓\t")
        # if the hour is after 12 then it will generate a random employee and random time
        elif randomtime > 12:
            tempTime = randomtime - 12
            print(single_date.strftime("%m/%d/%Y\t"), (str(tempTime) + ":" + str(randomMinutes) + " PM \t"),
                  employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
            if randomtime == 13:
                if randomMinutes == 24 or 39 or 35 or 10 or 15:
                    endHour = randomtime - random.randint(9, 10)
                    endminutes = random.randint(0, 59)
                    print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                          employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
                endHour = randomtime - 12 + random.randint(4, 6)
                endminutes = random.randint(0, 45)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
            if randomtime == 14:
                if randomMinutes == 16 or 41 or 2 or 1 or 7:
                    endHour = randomtime - random.randint(9, 11)
                    endminutes = random.randint(40, 59)
                    print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                          employeeGenerator(), "\t.\t ✓\t ✓\t ✓\t \t")
                endHour = randomtime - 12 + random.randint(4, 5)
                endminutes = random.randint(25, 50)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
            if randomtime == 15:
                endHour = randomtime - 12 + random.randint(2, 4)
                endminutes = random.randint(0, 54)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
            if randomtime == 16:
                endHour = randomtime - 12 + random.randint(1, 3)
                endminutes = random.randint(20, 59)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
            if randomtime == 17:
                endHour = randomtime - 12 + random.randint(1, 2)
                endminutes = random.randint(30, 59)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")
            if randomtime == 18:
                endHour = randomtime - 12 + 1
                endminutes = random.randint(25, 55)
                print(single_date.strftime("%m/%d/%Y\t"), (str(endHour) + ":" + str(endminutes) + " PM \t"),
                      employeeGenerator(), "\t.\t \t \t \t ✓\t")


# execute the code function
if __name__ == '__main__':
    main()




