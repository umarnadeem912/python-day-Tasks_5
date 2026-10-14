# Spam Detector

# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

# A represents the country code and can be any number of digits.
# BBB represents the area code and will always be three digits.
# CCC and DDDD represent the local number and will always be three and four digits long, respectively.
# Determine if it's a spam number based on the following criteria:

# The country code is greater than 2 digits long or doesn't begin with a zero (0).
# The area code is greater than 900 or less than 200.
# The sum of first three digits of the local number appears within last four digits of the local number.
# The number has the same digit four or more times in a row (ignoring the formatting characters).
# Tests:

# 1. is_spam("+0 (200) 234-0182") should return False
# 2. is_spam("+091 (555) 309-1922") should return True.
# 3. is_spam("+1 (555) 435-4792") should return True.
# 4. is_spam("+0 (955) 234-4364") should return True.
# 5. is_spam("+0 (155) 131-6943") should return True.
# 6. is_spam("+0 (555) 135-0192") should return True.
# 7. is_spam("+0 (555) 564-1987") should return True
# 8. is_spam("+00 (555) 234-0182") should return False.


#code start here

def is_spam(num):
    parts = num.split()
    a = parts[0][1:]
    b = parts[1][1:-1]
    c, d = parts[2].split("-")

    # Rule 1: country code
    if len(a) > 2 or a[0] != "0":
        return True

    # Rule 2: area code
    b = int(b)
    if b > 900 or b < 200:
        return True

    # Rule 3: sum of first three local digits
    tot = 0
    for i in c:
        tot = tot + int(i)
    if str(tot) in d:
        return True

    # Rule 4: same digit 4 times in a row
    digits = ""
    for k in num:
        if k.isdigit():
            digits = digits + k
    for n in digits:
        if n * 4 in digits:
            return True

    return False


print(is_spam("+92 (10) 234-0182"))   # False
# print(is_spam("+091 (555) 309-1922")) # True
# print(is_spam("+1 (555) 435-4792"))   # True
# print(is_spam("+0 (955) 234-4364"))   # True
# print(is_spam("+0 (155) 131-6943"))   # True
# print(is_spam("+0 (555) 135-0192"))   # True
# print(is_spam("+0 (555) 564-1987"))   # True
# print(is_spam("+00 (555) 234-0182"))  # False