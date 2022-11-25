# Mod of 4 and not divisble by 100
# Mod of 400 should be zero

def identify_leap_year(year):
    try:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    except:
        print("Invalid input")

def main():
    try:
        year_input = int(input("Enter a year : "))
    except:
        print("Invalid Input")

    print(identify_leap_year(year_input))

main()