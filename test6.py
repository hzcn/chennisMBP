text = input('请输入内容')
index = 0
index_len = len(text)
total = 0
while True:
    val = text[index]
    flag = val.isdigit()
    if flag:
        total += 1
    if index == index_len - 1:
        break
    index = index + 1

print(total)
