import os
import uuid
import shutil
import json

import errors

def judgePathType(path):
    """
    功能
    判断一个路径的类型

    返回值
    1: 这个路径代表一个文件
    2: 这个路径代表一个目录

    传出异常
    PathNotExistError: 路径不存在
    """
    # 检查路径是否存在
    if not os.path.exists(path):
        raise errors.PathNotExistError(f"路径 '{path}' 不存在。")
    # 检查路径是否是文件  
    if os.path.isfile(path):
        return 1
    # 如果不是文件，则是目录
    return 2

def getNewUuid():
    """
    功能
    返回一个字符串类型的uuid

    返回值
    str类型的uuid

    传出异常
    无
    """
    return str(uuid.uuid4())

def createDirectory(path, directory_name):
    """
    功能
    在指定路径下创建一个目录

    返回值
    完整的目录路径

    传出异常
    PathNotExistError: 指定路径不存在
    PathAlreadyExistError: 目录已存在
    """
    try:
        # 检查指定路径是否存在
        judgePathType(path)
    except errors.PathNotExistError:
        raise

    # 拼接完整的目录路径
    full_path = os.path.join(path, directory_name)

    # 检查目录是否已经存在
    if os.path.exists(full_path):
        raise errors.PathAlreadyExistError(f"文件夹 '{full_path}' 已存在。")
    
    # 使用os.makedirs来创建目录，可以设置exist_ok为True以避免文件已存在时的错误
    os.makedirs(full_path, exist_ok=True)
    return full_path

def copyFileOrDirectory(src, dst):
    """
    功能
    复制文件或目录到目标目录路径下

    返回值
    无

    传出异常
    PathNotExistError: 待复制路径不存在
    PathNotExistError: 目标路径不存在
    PathTypeError: 目标路径不是目录
    PathAlreadyExistError: 文件在目标目录路径下已存在
    PathAlreadyExistError: 目录在目标目录路径下已存在
    """
    if not os.path.exists(src):
        raise errors.PathNotExistError(f"路径 '{src}' 不存在。")
    if not os.path.exists(dst):
        raise errors.PathNotExistError(f"路径 '{src}' 不存在。")
    if judgePathType(dst) != 2:
        raise errors.PathTypeError(f"路径 '{dst}' 不是一个目录。")

    full_path = os.path.join(dst, os.path.basename(src))
    src_path_tpye = judgePathType(src)

    if os.path.exists(full_path):
        if src_path_tpye == 1:
            raise errors.PathAlreadyExistError(f"文件 '{full_path}' 已存在。")
        elif src_path_tpye == 2:
            raise errors.PathAlreadyExistError(f"目录 '{full_path}' 已存在。")

    # 如果是文件，直接复制
    if src_path_tpye == 1:
        shutil.copy2(src, dst)  # copy2保留元数据，如时间戳
        print(f"File resource '{src}' copied to '{dst}'.")
    # 如果是文件夹，递归复制
    elif src_path_tpye == 2:
        shutil.copytree(src, full_path)
        print(f"Directory resource '{src}' copied to '{dst}'.")

def deleteFileOrDirectory(path):
    """
    功能
    删除路径所指的文件或目录

    返回值
    无

    传出异常
    PathNotExistError: 路径不存在
    """
    try:
        path_type = judgePathType(path)
    except errors.PathNotExistError as e:
        raise errors.PathNotExistError(f"路径 '{path}' 不存在。")
    
    if path_type == 1:
        os.remove(path)
    else:
        shutil.rmtree(path)

def writeJson(data, path):
    """
    功能
    将数据封装到json文件中。如果文件不存在，它将被创建；如果文件已经存在，它的内容将被新数据覆盖

    返回值
    无

    传出异常
    DataTypeError: 数据类型错误，不是字典类型
    """
    if isinstance(data, dict) == False:
        raise errors.DataTypeError("数据类型错误，不是字典类型。")

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        # ensure_ascii=False参数确保非ASCII字符（如中文）被正确写入文件，而不是被转义。
        # indent=4参数用于美化输出，它会在JSON对象中添加缩进和换行符，使文件内容更易读。

def readJson(path):
    """
    功能
    读取一个json文件

    返回值
    数据字典

    传出异常
    PathNotExistError: 路径不存在
    PathTypeError: 路径并非json文件
    """
    if not os.path.exists(path):
        raise errors.PathNotExistError(f"路径 '{path}' 不存在。")
    
    if not path.endswith('.json'):
        raise errors.PathTypeError(f"路径 '{path}' 并非json文件。")

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def getSubdirectoryNames(path):
    """
    功能
    获取某目录路径下一级的所有目录名称

    返回值
    数据列表

    传出异常
    PathNotExistError: 路径不存在
    PathTypeError: 路径并非目录
    """
    if not os.path.exists(path):
        raise errors.PathNotExistError(f"路径 '{path}' 不存在。")
    
    if judgePathType(path) != 2:
        raise errors.PathTypeError(f"路径 '{path}' 并非目录。")

    subfolder_names = []
    # 列出指定目录下的所有文件和文件夹  
    for item in os.listdir(path):
        # 构建完整路径
        item_path = os.path.join(path, item)
        # 检查是否为文件夹
        if os.path.isdir(item_path):
            subfolder_names.append(item)
    return subfolder_names

def openFileOrDirectory(path):
    """
    功能
    打开文件或目录(目前可能仅适用于Windows系统)

    传出异常
    PathNotExistError: 路径不存在
    """
    if not os.path.exists(path):
        raise errors.PathNotExistError(f"路径 '{path}' 不存在。")
    
    os.startfile(path)


if __name__ == '__main__':
    # try:
    #     createDirectory("abcd", "efgh")
    # except errors.PathNotExistError as e:
    #     print(f'tools.py: {e}')
    # except errors.DirectoryAlreadyExistError as e:
    #     print(f'tools.py: {e}')

    # json_data = {1:'123'}
    # json_path = os.path.join('jsontest.json')
    # writeJson(json_data, json_path)

    # json_path = os.path.join('jsontest.json')
    # data = readJson(json_path)
    # print(data)

    # path = os.path.join('projects')
    # data = getSubdirectoryNames(path)
    # print(data)

    # path = os.path.join('projects', '32538231-5445-4368-8aed-33492cdabc7e', '456.txt')
    # openFileOrDirectory(path)
    # path = os.path.join('projects')
    # openFileOrDirectory(path)

    # path = os.path.join('123.txt')
    # deleteFileOrDirectory(path)
    # path = os.path.join('123')
    # deleteFileOrDirectory(path)
    pass
