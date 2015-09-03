import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome

    a = re.sub(r'[^A-Za-z]', "", sentence).lower()
    b = a[::-1]

    if a == b:
        return True
    else:
        return False

def main():
    # TODO: put your input/output code here
    sentence = input("Input text here: ")
    if is_palindrome(sentence) == True:
        print("'{}' is a palindrome.".format(sentence))
    else:
        print("'{}' is not a palindrome.".format(sentence))

if __name__ == '__main__':
    main()
