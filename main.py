from tagger import Tagger 

if __name__ == '__main__':
    tagger = Tagger()

    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/123.txt')
    # tagger.projectImport('testdata/456.txt')
    # tagger.projectImport('testdata')

    # print(tagger.getInfoByUuid('6f6b9282-4f33-4152-ad3d-14d19a81fe48'))

    tagger.showProjects()

    # tagger.deleteTag("43acbe02-9e53-485a-9c0e-ffa2ee2801e3")
    # tagger.createTag('我的世界')

    # tagger.addTag('32538231-5445-4368-8aed-33492cdabc7e', "a96a87c8-3606-4a39-9684-81a0e2d8954e")

    tagger.showProjects(["a96a87c8-3606-4a39-9684-81a0e2d8954e"])