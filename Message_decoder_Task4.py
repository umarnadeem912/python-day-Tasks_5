# Message Decoder

# Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

# A positive number means the message was shifted forward in the alphabet.
# A negative number means the message was shifted backward in the alphabet.
# Case matters, decoded characters should retain the case of their encoded counterparts.
# Non-alphabetical characters should not get decoded.


# Tests:

# 1. decode("Xlmw mw e wigvix qiwweki.", 4) should return "This is a secret message."
# 2. decode("Byffi Qilfx!", 20) should return "Hello World!"
# 3. decode("Zqd xnt njzx?", -1) should return "Are you okay?"


# code start here


def decode(mess,num):
    word=""
    for i in mess:
        if i.isalpha():
            if i.isupper():
                base="A"
            else:
                base="a"  
            n=ord(i)-ord(base)
            pri=(n-num)%26
            pri=chr((pri)+ord(base))
            word=word+pri
        else:
            word=word+i
    return word
print(decode("Xlmw mw e wigvix qiwweki.", 4))
print(decode("Byffi Qilfx!", 20))
print(decode("Zqd xnt njzx?", -1))