from random import randint, shuffle
def generate_password(length):
    length = max(length, 12)
    special_char = "~!@#$%^&*()_+ "
    password = [
        str(randint(0, 9)),
        chr(randint(65, 90)),
        chr(randint(97, 122)),
        special_char[randint(0, 13)],
    ]
    shuffle(password)
    while len(password) < length:
        opt = randint(1, 4)
        match opt:
            case 1:
                password.append(str(randint(0, 9)))
            case 2:
                password.append(chr(randint(65, 90)))
            case 3:
                password.append(chr(randint(97, 122)))
            case 4:
                password.append(special_char[randint(0, 13)])
        shuffle(password)
    password = "".join(password)
    return password

length = int(input(Enter password length you want generate: ))
the_password = generate_password(length)
print(f"Your generated password is: {the_password}")
