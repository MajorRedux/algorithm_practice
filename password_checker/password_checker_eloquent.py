"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

password_checker('A1213pokl') == False
password_checker('bAse730onE') == True
password_checker('asasasasasasasaas') == False
password_checker('QWERTYqwerty') == False
password_checker('123456123456') == False
password_checker('QwErTy911poqqqq') == True
"""

import re

DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def password_checker(data):
    """
    Return True if password strong and False if not
    
    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False
    
    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False
        
    return True

if __name__ == '__main__':
    assert password_checker('A1213pokl')==False, 'First'
    assert password_checker('bAse730onE4')==True, 'Second'
    assert password_checker('asasasasasasasaas')==False, 'Third'
    assert password_checker('QWERTYqwerty')==False, 'Fourth'
    assert password_checker('123456123456')==False, 'Fifth'
    assert password_checker('QwErTy911poqqqq')==True, 'Sixth'
