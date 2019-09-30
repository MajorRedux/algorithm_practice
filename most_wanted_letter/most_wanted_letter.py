import re

def most_wanted_letter(text: str) -> str:
    s_text = re.sub(r"\d+|\W+", "", text.lower())
    text_dict = {i: s_text.lower().count(i) for i in set(s_text.lower())}
    max_key = max(text_dict, key=lambda k: text_dict[k])
    print(max_key)
    for items in sorted(text_dict.items()):
        if items[1] == text_dict[max_key]:
            return items[0]
    if len(set(text_dict.values())) == True:
        max_key = sorted(s_text)[0]
        if text[-1].isalpha() == False:
            return max_key
    return max_key

if __name__ == '__main__':
    #print("Example:")
    #print(checkio("Hello World!"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_wanted_letter("Hello World!") == "l", "Hello test"
    assert most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert most_wanted_letter("One") == "e", "All letter only once."
    assert most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted_letter("abe") == "a", "The First."
    assert most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    assert most_wanted_letter("Lorem ipsum dolor sit amet") == "m", "Two of the same."
