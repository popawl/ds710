import re
import string
import csv
        

def say_piglatin(w):

    v = ('a','e','i','o','u')
    r = re.compile(r'^\b(\w+)\b$', re.ASCII)
    m = re.match(r, w)

    if m:
        s = m.group(1).lower()
        front = list(s)
        back = []
        if s[0] in v:
            complete = s + 'yay'
        elif s[0] == 'q' and s[1] == 'u':
            complete = s[2:] + s[0:2] + 'ay'
        else:
            back.append(s[0])
            front.remove(s[0])
            for letter in s[1:]:
                if letter in v or letter == 'y':
                    break
                back.append(letter)
                front.remove(letter)
            pieces = front + back + ['ay']    
            complete = ''.join(pieces)
        if m.group(1)[0].isupper():
            complete = complete.capitalize()
        return complete
    else:
        print("Opps! Please enter a valid word")
