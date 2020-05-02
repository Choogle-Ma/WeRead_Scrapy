import json
from pprint import pprint

with open("/home/mahj/Project/WeRead_Scrapy/category.json", 'r') as f:
    data = json.load(f)

countdata = {}

for t in data:
    category = str(t['category'])
    count = t['totalCount']
    countdata[category] = count

# pprint(countdata)

# with open('count.json', 'w') as f:
#     json.dump(countdata, f, ensure_ascii=False, indent=2)

catlist = set()
for i in countdata:
    cate = i[0:-5]
    catlist.add(cate)

result = {}
for j in catlist:
    num = 0
    sumnum = 0
    for i in countdata:
        cate = i[0:-5]
        type_t = i[-5:]
        if type_t != '00000' and cate == j:
           num += countdata[i]
        elif type_t == '00000' and cate == j:
            sumnum = countdata[i]
        else:
            pass

    print("sumnum:" + str(sumnum))
    print("plusnum:" + str(num))




