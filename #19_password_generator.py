from random import randint, shuffle
def generatePassword(length):
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
    print(password)
    return password

assert len(generatePassword(8)) == 12

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in "abcdefghijklmnopqrstuvwxyz":

        hasLowercase = True

    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        hasUppercase = True

    if character in "1234567890":

        hasNumber = True

    if character in "~!@#$%^&*()_+ ":

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial