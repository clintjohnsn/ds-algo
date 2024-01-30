# shift a string k chars
s = input()
k =int(input())
shiftedString = []

shiftedString = s[k:]
shiftedString = shiftedString + s[:k]
print(shiftedString)