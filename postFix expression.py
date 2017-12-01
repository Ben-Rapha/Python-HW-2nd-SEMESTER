#KINGSLEY .OTTO
#CSI 33
#HOMEWORK 8
#WRITE A FUNCTION THAT ACCEPT VALID POSTFIX EXPRESSION AND EVALUATE IT


def postFE(text):
    text = text.split()
    Lenth = len(text)
    stack = []
    for i in range (Lenth):
        if text[i].isdigit():
            stack.append(int(text[i]))
        elif text[i] =="+":
            firstD = stack.pop()
            sencD = stack.pop()
            stack.append(int(firstD)+int(sencD))
        elif text[i] =="*":
            firstD = stack.pop()
            sencD = stack.pop()
            stack.append(int(firstD)*int(sencD))
        elif text[i] =="/":
            firstD = stack.pop()
            sencD = stack.pop()
            stack.append(int(firstD)/int(sencD))
        elif text[i] =="-":
            firstD = stack.pop()
            sencD = stack.pop()
            stack.append(int(firstD)-int(sencD))
            
    return stack.pop()


def main():
    text = "7 8 + 3 6 + /"
    text = postFE(text)
    print(text)

main()

"""
0.6
"""

