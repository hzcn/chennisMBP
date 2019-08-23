a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#1数组中直接添加符号，再数组转字符串
a.insert(0, '(')
a.insert(4, ') ')
a.insert(8, '-')
result1 = (''.join(str(i) for i in a))
print(result1)
#2将数组分成三个部分转成字符串，在带符号的.format模版中嵌套这三个字符串片段
str1 = ''.join(str(i) for i in b[0:3])
str2 = ''.join(str(i) for i in b[3:6])
str3 = ''.join(str(i) for i in b[6:10])
result2 = '({}) {}-{}'.format(str1,str2,str3)
print(result2)
#3数组直接转成字符串，将带引的字符串直接加入到字符串中
c = ''.join(str(i) for i in c)
result3 = '(' + c[0:3] + ')' + ' ' + c[3:6] + '-' + c[6:10]
print(result3)
#4数组直接转成字符串，在字符串中直接加入三个符号
d = ''.join(map(str, d))
result4 = '(%s) %s-%s' % (d[0:3], d[3:6], d[6:10])
print(result4)
#5直接在已经排好的模版中嵌套数字
result5 = '({}{}{}) {}{}{}-{}{}{}{}'.format(*d)
print(result5)
#6跟方法5类似，用的是元组的方法
result6 = '(%i%i%i) %i%i%i-%i%i%i%i' % tuple(e)
print(result6)

