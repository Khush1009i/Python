# Match -Case Statements("Switch"): An alternative to using many 'elif' statements
# execute some code if a value matches a a 'case'
# Benefits: cleaner & syntax is more readable


def is_weekend(day):
    match day :
        case "Saturday" | "Sunday":
            return True       
        case "Monday" | "Tuesday"| "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False


print(is_weekend("Sunday"))
        

