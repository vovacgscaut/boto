

import re
print(re)
words="cet,cross,cat,combo,acces,net"
res=len(words)
print(res)



start = -1
count = 0
buk=input("введите букву:" )
while True:
    start = words.find(buk, start+1)
    if start == -1:
        break
    count += 1

print("Количество вхождений символа в строку: ", count )
buk=input("введите букву:" )
print(buk)
while True:
    word_list = re.findall(r'\b\w+\b', words)
    rse_word=len(word_list)
    print("Количество слов в строке:", rse_word)
    print(word_list)
        #     if buk==True:
        # print(word_list)

    input('press any key for exit')
    break
