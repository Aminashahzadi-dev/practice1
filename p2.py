word = "Programming"

print(word[::-1])
print(word[:3], word[-3:])
print("m count:", word.lower().count("m"))


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("level"))
print(is_palindrome("python"))
