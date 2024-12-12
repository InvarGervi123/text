import string
import time
text = "Hello world i am a wonder woman and you are my little bigfoot"
temp = ""
sum = 0
for ch in text:
    for i in string.printable:
        if i == ch or ch == ' ':
            time.sleep(0.02)
            print(temp+i)
            temp +=ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)
        sum = sum + 1
print(sum)