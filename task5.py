s = int(input("Input: "))
bin1 = bin(s)
rList = []
for i in list(bin1)[2:]:
    if i == '0':
        rList.append('1')
    else:
        rList.append('0')
r = ''.join(rList)
print("Output:", int(r, 2))

