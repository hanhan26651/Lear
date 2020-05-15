import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","不可","二人","不能","如此"} # 整理废词集合
words= jieba.lcut(txt)  # 通过jieba库分词,返回列表
counts ={}
for word in words:          # 下面对词库列表进行优化
    if len(word) == 1:      # 一个字的词忽略
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相曰":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1 #并进行计数
for word in excludes:       # 对字典删除废词
    del counts[word]
items = list(counts.items())    # 将字典数据键值对列表化!
items.sort(key=lambda x:x[1],reverse = True)    #从大到小排列
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
