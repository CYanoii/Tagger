from tagger import Tagger 

if __name__ == '__main__':
    tagger = Tagger()

    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/456.txt')
    # tagger.projectImport('testdata')

    while(1):
        inp = input()
        op = inp.split(" ")

        if op[0] == "imppro":
            pass
        elif op[0] == "exppro":
            pass
        elif op[0] == "delpro":
            pass
        elif op[0] == "shopros":
            pass
        elif op[0] == "cretag":
            pass
        elif op[0] == "deltag":
            pass
        elif op[0] == "rentag":
            pass
        elif op[0] == "addtag":
            pass
        elif op[0] == "remtag":
            pass
        elif op[0] == "shotags":
            pass
        elif op[0] == "exit": break