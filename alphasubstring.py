s = "abcabcdefghlijglkdfj"
x = 0
count = 0
startIndex = 0
length = 0
while x < len(s) - 1:
    if (s[x] < s[x+1]):
        count += 1
    else:
        if count > length:
            length = count
            startIndex = x - length
        count = 0
    x += 1
length -= 1
x = 0
answer = ""
while x <= length + 1:
    answer += s[startIndex + x]
    x += 1
print("Longest substring in alphabetical order is: " + answer)