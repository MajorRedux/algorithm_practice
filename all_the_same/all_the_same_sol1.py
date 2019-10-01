from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    z = False
    for x in elements:
        for y in elements:
            if x == y:
                z += 0
            else:
                z += 1
    if z > 0:
        z = False
    else:
        z = True
    return z

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True