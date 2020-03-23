# Book page 45
last_num = 0
current_num = 1
print(str(last_num))
print(str(current_num))
while True:
    next_num = current_num + last_num
    if next_num > 10000:
        break
    print(str(next_num))
    last_num = current_num
    current_num = next_num
