c=input()
vowels=['a','e','i','o','u']
if c.isalpha():
    c=c.lower()
    if c in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
