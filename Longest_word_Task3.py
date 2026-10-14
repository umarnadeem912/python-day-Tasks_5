# Longest Word

# Given a sentence, return the longest word in the sentence.

# Ignore periods (.) when determining word length.
# If multiple words are ties for the longest, return the first one that occurs.
# Tests:

# 1. get_longest_word("coding is fun") should return "coding".
# 2. get_longest_word("Coding challenges are fun and educational.") should return "educational"
# 3. get_longest_word("This sentence has multiple long words.") should return "sentence".


#code start here

def get_longest_word(word):
    a=word.replace(".","")
    a=a.split()
    longest=""
    for i in a:
        if len(i)>len(longest):
            longest=i
    return longest
print(get_longest_word("coding is fun."))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("This sentence has multiple long words."))