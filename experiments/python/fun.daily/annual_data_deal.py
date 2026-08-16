# 年度个人评分表处理程序
with open("d:/data.txt", encoding="utf-8") as fp:
    data_dict = dict()
    table_head = fp.readline().split()
    for line in fp:
        raw_data = line.split()
        namex = raw_data[0]
        name_datas = data_dict.get(namex, []) 
        name_datas.insert(0,raw_data[1:])
        data_dict[namex] = name_datas

    for namex,item in data_dict.items():
        print(namex)
        zipped_list = list(zip(*item))
        for index,tuplex in enumerate(zipped_list):
            tmp_dict = dict()
            for elem in tuplex:
                count = tmp_dict.get(elem, 0)
                tmp_dict[elem] = count + 1
            print("\t",table_head[index+1],tmp_dict)  

"""
年度个人评分表处理程序说明
data.txt文件格式依赖:
文件需排版为表格格式，且用空格隔开，第一项为姓名，后续为各项指标的得分，示例如下
姓名      技能1st     技能2nd     技能3rd     技能4th
gaoshan     a           b           c            d
hongxue     a           a           a            b
gaoshan     a           b           c            d
hongxue     a           a           a            b
gaoshan     c           b           c            d
hongxue     d           a           c            b
gaoshan     b           a           a            d
hongxue     d           d           a            b

文件输出结果为各项指标的得分统计
guoyuan
     技能1st {'c': 1, 'a': 2, 'b': 1}
     技能2nd {'a': 1, 'b': 3}
     技能3rd {'c': 3, 'a': 1}
     技能4th {'d': 4}
wangyan
     技能1st {'d': 2, 'a': 2}
     技能2nd {'d': 1, 'a': 3}
     技能3rd {'c': 1, 'a': 3}
     技能4th {'b': 4} 

Author: gy 2015.12.18 
"""            
        
           