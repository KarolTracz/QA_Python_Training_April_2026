"""
Write a function that takes a string as input
and returns a dictionary containing the characters that appear 3 or more times consecutively,
along with the count of their occurrences.
"""

def count_repeating_chars(s: str):
    """
    Example:
    If the input string is "aaabbbcccdddeeefff", the output should be {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3}.
    If the input string is "abcdefgh", the output should be an empty dictionary {}.
    """
    result = {}

    prev_char: str = ''
    counter = 0
    for i, char in enumerate(s):
        if char == prev_char:
            counter += 1
            prev_char = char
        else:
            if prev_char not in result.keys() and counter >= 3:
                result[prev_char] = counter
            elif prev_char in result.keys() and counter >= 3:
                result[prev_char] += counter

            counter = 1
            prev_char = char

        if i == (len(s) - 1) and counter >= 3 and char not in result.keys():
            result[prev_char] = counter
        elif i == (len(s) - 1) and counter >= 3 and char in result.keys():
            result[prev_char] += counter

    return result

print(count_repeating_chars("aaabbbcccdddeeefff")) # {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3}
print(count_repeating_chars("abcdefgh")) # {}
print(count_repeating_chars("aaaaabbbbbcccccddddd")) # {'a': 5, 'b': 5, 'c': 5, 'd': 5}
print(count_repeating_chars("")) # {}
print(count_repeating_chars("aaabbbcccdddeee")) # {}
print(count_repeating_chars("aaaabbbbccccddddeeeeffffgggg")) # {'a': 4, 'b': 4, 'c': 4, 'd': 4, 'e': 4, 'f': 4, 'g': 4}

