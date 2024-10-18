import copy

from tagger import Tagger

# 在传值被修改了的事情上有问题
def draw(data):
    # 用于将数据绘制好看。输入是严格的长度相等的二维list
    
    def chinese_len(s):
        # 默认的len()会将中文字符长度视为1，但我们希望将其长度视为2

        length = 0
        for char in s:
            # 判断字符是否是中文字符
            if '\u4e00' <= char <= '\u9fff':  # 基本的汉字范围
                length += 2
            else:
                length += 1
        return length

    data = copy.deepcopy(data)

    item_len = len(data[0])

    item_max = [0] * item_len
    for item in data:
        for i in range(item_len):
            item_max[i] = max(item_max[i], chinese_len(item[i]))

    print(item_max)

    for item in data:
        for i in range(item_len):
                le = len(item[i])
                cle = chinese_len(item[i])
                if le == cle:    # 没有中文字符
                    item[i] = item[i].center(item_max[i] + 2)
                else:                                       # 有中文字符
                    item[i] = item[i].center(item_max[i] + 2 - (cle - le))

    # 绘制数据之间的表格行
    str_line = '+'
    for i in range(item_len): str_line += ('-' * (item_max[i] + 2) + '+')
    
    # 输出绘制图
    print(str_line)
    for item in data:
        print(end='|')
        for i in range(item_len):
            print(item[i], end='|')
        print()

        print(str_line)



if __name__ == '__main__':
    tagger = Tagger()

    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/456.txt')
    # tagger.projectImport('testdata')

    # data = [['我的世界', '22', '3'],['44', '555555', '6']]
    # draw(data)

    table = tagger.getProjectsTableByTags(["a96a87c8-3606-4a39-9684-81a0e2d8954e"])
    # print(table)
    draw(table)

    # while(1):
    #     inp = input()
    #     op = inp.split(" ")

    #     if op[0] == "imppro":
    #         pass
    #     elif op[0] == "exppro":
    #         pass
    #     elif op[0] == "delpro":
    #         pass
    #     elif op[0] == "shopros":
    #         pass
    #     elif op[0] == "cretag":
    #         pass
    #     elif op[0] == "deltag":
    #         pass
    #     elif op[0] == "rentag":
    #         pass
    #     elif op[0] == "addtag":
    #         pass
    #     elif op[0] == "remtag":
    #         pass
    #     elif op[0] == "shotags":
    #         pass
    #     elif op[0] == "exit": break