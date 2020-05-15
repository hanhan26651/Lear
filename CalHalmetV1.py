#CalHamletV1.py
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for c in "!@#$%^&*(),./<>?:{};'[]`~'-=_+\|":
        txt = txt.replace(c ," ")
    return  txt

hamletTxt =getText()
words = hamletTxt.split()   #将分词按空格间隔返回到一个列表
counts = {}
for word in words:  #计算词语数
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())    #将字典类型转换成列表类型,便于操作
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

