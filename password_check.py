import string


def check_password_strength(password):

    score = 0
    length = len(password)

    if length >= 8:
        score += 1

        has_number = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_symbol = any(char in string.punctuation for char in password)

        if has_number:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_symbol:
            score += 1

    return score


while True:
    user_password = input("Enter your password: ")
    if len(user_password) < 8:
        print("Password is too short")
        continue

    final_score = check_password_strength(user_password)

    if final_score <= 2:
        print(
            f"Weak password. Your score is {final_score} out of 5 possible to obtain."
        )
    elif final_score <= 4:
        print(
            f"Medium password. Your score is {final_score} out of 5 possible to obtain."
        )
    else:
        print(
            f"Strong password. Your score is {final_score} out of 5 possible to obtain."
        )

    print("Do you want to try another password? (y/n):")
    if input().lower() == "n":
        break
