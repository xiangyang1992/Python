
def reverseWords(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]

    outinput = ' '.join(inputwords)
    return outinput


if __name__ == '__main__':
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)