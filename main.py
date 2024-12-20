import copy

from tagger import Tagger
import tools



if __name__ == '__main__':
    tagger = Tagger()

    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/456.txt')
    # tagger.projectImport('testdata')

    table = tagger.getProjectsTableByTags(["a96a87c8-3606-4a39-9684-81a0e2d8954e"])
    tools.draw2DList(table, header=['项目名称', 'Uuid', '标签'], add_id=True)

    table = tagger.getAllTagsTable()
    tools.draw2DList(table, header=['标签名称', 'Uuid'], add_id=True)

    # print(tagger.getUuidByTagName('我的世界'))

    # tagger.openProject('32538231-5445-4368-8aed-33492cdabc7e')
    # tagger.openProject('efd639b4-637a-4bc0-9904-82cc2ae45ed0')

    # tagger.deleteProject('eff349a7-0c79-4376-a01b-a387ebde022d')

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