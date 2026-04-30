test_string = "Hello, my password is: 'aAAaBbbBBCCCddd', cooool, right?"
expected_result = "Hello, my password is: '***a***BB******', c***ol, right?"

def test_me(string: str) -> str:
    new_string = ''

    prev_char = ''
    counter = 1
    for char in string:
        if char.lower() == prev_char.lower():
            counter += 1
            prev_char = char
        else:
            prev_char = char
            counter = 1

        if counter >= 3:
            new_string = new_string[:-2] + '***'
            counter = 0
        else:
            new_string += char

    return new_string

if test_me(test_string) == expected_result:
    print("You did well: %s" % expected_result)
else:
    print("You got:\n%s\nTry again..." % test_me(test_string))