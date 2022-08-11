# EASY
#basic caeser cypher
l= []
st = input()
no = int(input())
for i in st:
    if (ord(i)>=ord('a') and ord(i) <= ord('z')):
        k = (ord(i) - ord('a') + no ) % 26 + ord('a')
        l.append(chr(k))
    elif (ord(i)>= ord('A') and ord(i) <= ord('Z')):
        k = (ord(i) - ord('A') + no ) % 26 + ord('A')
        l.append(chr(k))
    elif (ord(i) >=ord('0') and ord(i)<= ord('9')):
        k = (ord(i) - ord('0') + no ) % 10 + ord('0')
        l.append(chr(k))
    else:
        l.append(i)
print("".join(l))
