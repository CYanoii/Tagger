import os

import tools
import errors

class Tagger():
    def __init__(self):
        self.projects_path = os.path.join('projects')
        self.data_path = os.path.join('data')
        self.tags_dict_path = os.path.join(self.data_path, 'tags.json')
        self.tags = tools.readJson(self.tags_dict_path)
    
    def importProject(self, src_strpath):
        """
        导入项目
        src_strpath: 字符串类型的资源路径（文件/文件夹均可）

        处理异常
        PathNotExistError: 导入资源路径不存在
        """
        src_path = os.path.join(src_strpath)

        try:
            tools.judgePathType(src_path)
        except errors.PathNotExistError as e:
            print("[Tagger/projectImport] ", e)
            return
        
        project_uuid = tools.getNewUuid()
        project_path = tools.createDirectory(self.projects_path, project_uuid)
        tools.copyFileOrDirectory(src_path, project_path)

        project_info = {'name': os.path.basename(src_path),
                        'uuid': project_uuid,
                        'tags': []
                        }
        project_info_path = os.path.join(self.data_path, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)

    def exportProject(self, uuid, dst_strpath):
        """
        导出项目
        uuid: 待导出项目的uuid
        dst_strpath: 字符串类型的目标路径（文件夹）

        处理异常
        PathNotExistError: 目标路径不存在
        PathTypeError: 目标路径不是目录
        UuidNotExistError: 项目uuid不存在
        """
        dst_path = os.path.join(dst_strpath)

        try:
            if tools.judgePathType(dst_path) != 2:
                raise errors.PathTypeError(f"路径 '{dst_path}' 不是目录。")
        except errors.PathNotExistError as e:
            print("[Tagger/projectExport] ", e)
            return
        except errors.PathTypeError as e:
            print("[Tagger/projectExport] ", e)
            return

        try:
            info = self.__getInfoByUuid(uuid)
        except errors.UuidNotExistError as e:
            print("[Tagger/projectExport] ", e)
            return

        project_path = os.path.join(self.projects_path, uuid, info['name'])
        tools.copyFileOrDirectory(project_path, dst_path)
        
    def deleteProject(self, uuid):
        """
        删除项目
        uuid: 待删除项目的uuid

        处理异常
        UuidNotExistError: 项目uuid不存在 未实现
        """
        info = self.__getInfoByUuid(uuid) # 没有考虑到不存在的情况
        pass
    
    def createTag(self, tag_name):
        """
        创建一个标签
        tag_name: 待创建标签的名字

        处理异常
        NameAlreadyExistError: 标签名已存在
        """
        try:
            if any(tag_name == value for value in self.tags.values()):
                raise errors.NameAlreadyExistError(f"已经存在名为 '{tag_name}' 的标签了。")
        except errors.NameAlreadyExistError as e:
            print("[tagger/createTag] ", e)
            return
        
        tag_uuid = tools.getNewUuid()
        self.tags[tag_uuid] = tag_name
        tools.writeJson(self.tags, self.tags_dict_path)

    def deleteTag(self, uuid):
        """
        删除一个标签
        uuid: 待删除标签的uuid

        处理异常
        UuidNotExistError: 标签uuid不存在
        """
        try:
            if uuid not in self.tags:
                raise errors.UuidNotExistError(f"标签uuid '{uuid}' 不存在。")
        except errors.UuidNotExistError as e:
            print("[tagger/deleteTag] ", e)
            return

        self.tags.pop(uuid)
        tools.writeJson(self.tags, self.tags_dict_path)

    def renameTag(self, uuid, tag_name):
        """
        重命名一个标签
        uuid: 待重命名标签的uuid

        处理异常
        UuidNotExistError: 标签uuid不存在
        NameAlreadyExistError: 重命名标签名已存在
        """
        try:
            if uuid not in self.tags:
                raise errors.UuidNotExistError(f"标签uuid '{uuid}' 不存在。")
        except errors.UuidNotExistError as e:
            print("[tagger/renameTag] ", e)
            return
        try:
            if any(tag_name == value for value in self.tags.values()):
                raise errors.NameAlreadyExistError(f"已经存在名为 '{tag_name}' 的标签了。")
        except errors.NameAlreadyExistError as e:
            print("[tagger/renameTag] ", e)
            return

        self.tags[uuid] = tag_name
        tools.writeJson(self.tags, self.tags_dict_path)

    def addTag(self, project_uuid, tag_uuid):
        """
        为一个项目添加一个标签

        处理异常
        UuidNotExistError: 项目uuid不存在
        UuidNotExistError: 标签uuid不存在
        NameAlreadyExistError: 项目已有本标签
        """
        try:
            project_info = self.__getInfoByUuid(project_uuid)
        except errors.UuidNotExistError as e:
            print("[tagger/addTag] ", e)
            return

        try:
            if tag_uuid not in self.tags:
                raise errors.UuidNotExistError(f"标签uuid '{tag_uuid}' 不存在。")
        except errors.UuidNotExistError as e:
            print("[tagger/addTag] ", e)
            return

        try:
            if any(tag_uuid == uuid for uuid in project_info['tags']):
                raise errors.NameAlreadyExistError(f"'{project_uuid}' 项目已经存在uuid为 '{tag_uuid}' 的标签了。")
        except errors.NameAlreadyExistError as e:
            print("[tagger/addTag] ", e)
            return

        project_info['tags'].append(tag_uuid)

        project_info_path = os.path.join(self.data_path, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)

    def removeTag(self, project_uuid, tag_uuid):
        """
        为一个项目移除一个标签

        处理异常
        UuidNotExistError: 项目uuid不存在
        UuidNotExistError: 标签uuid不存在
        NameNotExistError: 项目未拥有本标签
        """
        try:
            project_info = self.__getInfoByUuid(project_uuid)
        except errors.UuidNotExistError as e:
            print("[tagger/removeTag] ", e)
            return

        try:
            if tag_uuid not in self.tags:
                raise errors.UuidNotExistError(f"标签uuid '{tag_uuid}' 不存在。")
        except errors.UuidNotExistError as e:
            print("[tagger/removeTag] ", e)
            return
        
        try:
            if not any(tag_uuid == uuid for uuid in project_info['tags']):
                raise errors.NameNotExistError(f"'{project_uuid}' 项目不存在uuid为 '{tag_uuid}' 的标签。")
        except errors.NameNotExistError as e:
            print("[tagger/removeTag] ", e)
            return

        project_info['tags'].reomve(tag_uuid)

        project_info_path = os.path.join(self.data_path, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)

    # ==========展示函数==========

    def showProjectsByTags(self, tags=[]):
        """
        展示包含所选标签uuid标签集的项目数据
        tags: 所选标签uuid列表

        处理异常
        UuidNotExistError: 项目uuid不存在
        """
        uuids = tools.getSubdirectoryNames(self.projects_path)
        for uuid in uuids:
            try:
                info = self.__getInfoByUuid(uuid)
            except errors.UuidNotExistError as e:
                print("[Tagger/showProjects] ", e)
                return

            if set(tags).issubset(set(info['tags'])) :  # 先将有序列表转换成无序集合后再进行比较
                formatted_name = info['name'].ljust(16)
                formatted_uuid = info['uuid'].ljust(40)
                formatted_tags = []
                for tag in info['tags']:
                    if tag in self.tags:  # 确保键在映射字典中
                        formatted_tags.append(self.tags[tag])
                    else:
                        #!!!!
                        # 如果键不在映射字典中，说明这是一个被删除的标签。既然存在，则本项目需要被整理
                        formatted_tags.append("已删除标签") # 添加一个默认值
                        # self.__OrganizeProjectTags()
                print(f'{formatted_name} {formatted_uuid} {formatted_tags}')

    def showTagNames(self):
        """
        展示所有标签名

        处理异常
        无
        """
        for _, value in self.tags.items():
            print(value)

    # ==========内部函数==========

    def __getInfoByUuid(self, uuid):
        """
        通过uuid查询信息
        uuid: 待查询信息的项目的uuid

        处理异常
        UuidNotExistError: 项目uuid不存在
        """
        path = os.path.join(self.data_path, uuid + '.json')
        try:
            info = tools.readJson(path)
        except errors.PathNotExistError as e:
            raise errors.UuidNotExistError(f"项目uuid '{uuid}' 不存在。") from e
        except errors.PathTypeError as e:
            raise errors.UuidNotExistError(f"项目uuid '{uuid}' 不存在。") from e

        return info

    def __getUuidByTagName(self, TagName):
        """
        通过标签名获取其标签uuid
        TagName: 待获取标签uuid的的标签名

        处理异常
        待定
        """
        pass

    def __organizeProjectTags(self, uuid):
        """
        整理uuid项目的标签集信息
        uuid: 待整理标签集的项目的uuid

        处理异常
        待定
        """
        pass