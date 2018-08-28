chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.' "
check = 'It was a bright cold day in April, and the clocks were striking thirteen.'

for char in chars:
    count = check.count(char)
    if count > 0:
        print(char, count)
        count = {}
for s in check:
    if count.has_keys(s):
        count[s] +=1
    else:
        count[s] = 1
for key in count:
    if count[key] > 1:
        print(key, count[key])
