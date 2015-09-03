import re

def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", (sentence.lower()))


    min = 0
    max = len(sentence) - 1
    #scan sentence for equality
    while True:
        #all characters checked??? return true
        if min > max:
            return True;

        a = sentence[min]
        b = sentence[max]

        #if they are not equal, return False
        if a != b:
            return False;

        #move to the middle from both ends
        min += 1
        max -= 1




def main():
    #ask for sentence
    sentence = input("Please give me a sentence you think is a palindrome ")
    is_palindrome(sentence)
    check = is_palindrome(sentence)
    if check:
        print("{} is a palindrome".format(sentence))
    else:
        print("{} is not a palindrome".format(sentence))

if __name__ == '__main__':
    main()
