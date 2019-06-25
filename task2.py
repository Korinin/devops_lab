def is_year_4(year_1):
    """Return True if number is divisible, otherwise False"""
    if year_1 % 4:
        return False
    else:
        return True


def is_year_400(year1):
    """Return True if number is divisible (100 and 400), otherwise False"""
    if year1 % 100 == 0:
        if year1 % 400:
            return False
        else:
            return True
    else:
        return True


def is_year_100(year1):
    """Return True if number is divisible, otherwise False"""
    if year1 % 100:
        return False
    else:
        return True


def is_year_leap(year1):
    """"Return True if number is divisible (4 or 400), otherwise False"""
    if is_year_4(year1) and is_year_400(year1):
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == "__main__":
    year1 = int(input("input a year: "))
    is_year_leap(year1)
