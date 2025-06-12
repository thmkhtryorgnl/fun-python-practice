try:    
    age = int(input("How old are you? "))
    if age <= 18:
        raise Exception("Sorry kiddo, this content is for 18+ only.") #We are create exception error
    elif age >= 70:
        a = input("Please share your wisdom with me: ")
        print(f"{a}")
    else:
        print("I'm a hacker... and I'm coming to eat you! 😈")
except ValueError:
    raise ValueError("Come on, just enter a number, please :)") # Value error when entered age is not integer(etc. hi)
else:
    print("Thanks for enter integer") #It runs when Try correctly runs
finally:
    print("At the end of the day, you're still human.")
