"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""

"""
Input: string
Output: boolean
Restrictions:
password >= 10
at least one digit (int)
uppercase letter
lowercase letter
only ascii latin latters & ints
"""

def checkio(data: str) -> bool:
    if len(data) < 10:
        #return print("length")
        return False
    if ascii_check(data) == False:
        #return print("ascii")
        return False
    if digit_check(data) == False:
        #return print("digit")
        return False
    if upper_check(data) == False:
        #return print("upper")
        return False
    if lower_check(data) == False:
        #return print("lower")
        return False
    return True

def digit_check(data):
    digit_exist = 0
    for character in data:
        try:
            if type(int(character)) == type(int(0)):
                digit_exist += 1
                #print("+1")
        except:
            digit_exist += 0
            #print("+0")
    #print(len(data))
    #print(digit_exist)
    if len(data) == digit_exist:
        return False
    if digit_exist > 0:
        return True

    return False
    
def upper_check(data):
    if data.isupper() == True:
        return False
    for character in data:
        if character.isupper() == True:
            return True

def lower_check(data):
    if data.islower() == True:
        return False
    for character in data:
        if character.islower() == True:
            return True

def ascii_check(data):
    isascii = lambda s: len(s) == len(s.encode())

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
