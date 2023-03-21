# 文件对象
# 在python中用open()可以创建一个文件对象。
# open()使用方法：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

参数说明:
file:  # 必需，文件路径（相对或者绝对路径）
mode:  # 可选，文件打开模式 （常用）
buffering:  # 设置缓冲
encoding:  # 一般使用utf8 （常用）
errors:  # 报错级别
newline:  # 区分换行符（一般不用）
closefd:  # 传入的文件参数类型（一般不用）
opener:  # 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符
# 例
f = open('1.txt','r') #这是一般的使用形式
# f现在是一个文件对象
# 1.txt是文件路径（打开的文件在这个py文件的同目录下）
# r是文件打开模式

# 打开模式

# 单独打开模式
t：文本模式 (默认)。f = open('1.txt','t')
b：二进制模式（用于打开音频、视频、图片等的模式）。f = open('1.txt','b')
+：打开一个文件进行更新(可读可写，这个一般不单独使用)。
r：以只读方式打开文件，读取的文件如果不存在会报错（FileNotFoundError: [Errno 2] No such file or directory: '1.txt'）。
文件的指针将会放在文件的开头。这是默认模式。f = open('1.txt','r')
w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。f = open('1.txt','a')

# 组合打开模式
# rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。f = open('1.txt','rb')
#
# r+：打开一个文件用于读写，如果操作的文件不存在会报错。文件指针将会放在文件的开头（）。f = open('1.txt','r+')
#
# rb+：以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。f = open('1.txt','rb+')
#
# wb：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片，视频，音频等。
#
# w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#
# ab：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。f = open('1.txt','ab')
#
# a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。f = open('1.txt','a+')
#
# ab+：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。f = open('1.txt','ab+')


# 读写

# 读
#第一种
file.read([size])从文件读取指定的字节数，如果未给定或为负则读取所有。
# 例1
f = open('1.txt', 'r')
content = f.read()
print('content: ' + content1)
f.close() # 当文件结束使用后记住需要关闭文件

# 例2
f = open('1.txt', 'r')
content = f.read(2)
print('content: ' + content)
f.close() # 当文件结束使用后记住需要关闭文件

# 第二种
file.readline([size])读取整行，包括 “\n” 字符。 # 被读取走就不会再读取
# 例1
f = open('1.txt', 'r')
content = f.readline()
print('content: ' + content)
f.close() # 当文件结束使用后记住需要关闭文件
# content:
# 12345

# 例2
f = open('1.txt', 'r')
content1 = f.readline()
content2 = f.readline()
print('content1: \n' + content1)
print('content2: \n' + content2)
f.close() # 当文件结束使用后记住需要关闭文件
# content1:
# 12345

# content2:
# 67890

# 例3
f = open('1.txt', 'r')
content1 = f.readline(3)
content2 = f.readline()
print('content1: \n' + content1)
print('content2: \n' + content2)
f.close() # 当文件结束使用后记住需要关闭文件
# content1:
# 123
# content2:
# 45

# 第三种
file.readlines([sizeint])读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。

# 例1
f = open('1.txt', 'r')
content = f.readlines()
print('content: ',content)
f.close() # 当文件结束使用后记住需要关闭文件
#content:  ['12345\n', '67890\n', '12345\n', '67890']

# 例2
f = open('1.txt', 'r')
content = f.readlines(5)
print('content: ',content)
f.close() # 当文件结束使用后记住需要关闭文件
# content:  ['12345\n']


# 写
# 第一种
file.write(str)将字符串写入文件，返回的是写入的字符长度。
# 例
f = open('1.txt', 'w')
f.write("abcd")
f.close() # 当文件结束使用后记住需要关闭文件

f = open('1.txt', 'r')
print(f.read())
f.close()
# abcd


#第二种
file.writelines(sequence)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
# 例
f = open('1.txt', 'w')
f.writelines("ab\ncd")
f.close() # 当文件结束使用后记住需要关闭文件

f = open('1.txt', 'r')
print(f.read())
f.close
# ab
# cd



