import os

import tools

class Tagger():
    def __init__(self):
        self.projects_path = os.path.join('projects')
        self.tags_path = os.path.join('tags')
        self.tags_dict_path = os.path.join(self.tags_path, 'tags.json')
        self.tags = tools.readJson(self.tags_dict_path)
    
    def projectImport(self, src_strpath):
        """
        导入项目
        src_strpath: 字符串类型的资源路径（文件/文件夹均可）

        异常情况:
        导入资源路径不存在
        """
        src_path = os.path.join(src_strpath)

        if tools.judgePathType(src_path) == 0:
            print(f"[tagger] 所提供资源路径 '{src_strpath}' 不存在。")
            return
        
        project_uuid = tools.getNewUuid()
        project_path = tools.createDirectory(self.projects_path, project_uuid)
        tools.copyFileOrDirectory(src_path, project_path)

        project_info = {'name': os.path.basename(src_path),
                        'uuid': project_uuid, 
                        'tags': []
                        }
        project_info_path = os.path.join(project_path, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)

    def projectExport(self, uuid, dst_strpath):
        """
        导出项目
        uuid: 待导出项目的uuid
        dst_strpath: 字符串类型的目标路径（文件夹）

        异常情况:
        项目uuid不存在
        目标路径不正确（不存在/非文件夹）
        """
        dst_path = os.path.join(dst_strpath)

        if tools.judgePathType(dst_path) == 2:
            info = self.getInfoByUuid(uuid)
            project_path = os.path.join(self.projects_path, uuid, info['name'])
            tools.copyFileOrDirectory(project_path, dst_path)
        else:
            print(f"[tagger] 所提供目标路径 '{dst_strpath}' 不正确。")
            
    def projectDelete(self, uuid):
        """
        删除项目
        uuid: 待删除项目的uuid

        异常情况:
        项目uuid不存在
        """
        info = self.getInfoByUuid(uuid) # 没有考虑到不存在的情况
        pass

    def showProjects(self, tags=[]):
        """
        根据所选标签展示数据
        tags: 所选标签uuid列表

        异常情况:
        
        """
        uuids = tools.getSubdirectoryNames(self.projects_path)
        for uuid in uuids:
            info = self.getInfoByUuid(uuid)

            if set(tags).issubset(set(info['tags'])) :  # 先将有序列表转换成无序集合后再进行比较
                formatted_name = info['name'].ljust(16)
                formatted_uuid = info['uuid'].ljust(40)
                formatted_tags = []
                for tag in info['tags']:  
                    if tag in self.tags:  # 确保键在映射字典中  
                        formatted_tags.append(self.tags[tag])  
                    else:  
                        # 如果键不在映射字典中，你可以选择忽略它、添加默认值或抛出异常  
                        # 这里我们添加一个默认值（例如None）  
                        formatted_tags.append(None)
                print(f'{formatted_name} {formatted_uuid} {formatted_tags}')

    def showTags(self):
        """
        展示所有标签

        异常情况:
        
        """
        pass

    def getInfoByUuid(self, uuid):
        """
        通过uuid查询信息
        uuid: 待查询信息的项目的uuid

        异常情况:
        项目uuid不存在
        """
        # 没有考虑到不存在的情况
        path = os.path.join(self.projects_path, uuid, uuid + '.json')
        info = tools.readJson(path)
        return info
    
    def createTag(self, tag_name):
        """
        创建一个标签
        tag_name: 待创建标签的名字

        异常情况:
        标签名已存在
        """
        if any(tag_name == value for value in self.tags.values()):
            print(f"[tagger] 已经存在名为 '{tag_name}' 的标签了。")
            return
        
        tag_uuid = tools.getNewUuid()
        self.tags[tag_uuid] = tag_name
        tools.writeJson(self.tags, self.tags_dict_path)

    def deleteTag(self, uuid):
        """
        删除一个标签
        uuid: 待删除标签的uuid

        异常情况:
        标签uuid不存在
        """
        self.tags.pop(uuid)
        tools.writeJson(self.tags, self.tags_dict_path)

    def renameTag(self, uuid, tag_name):
        """
        重命名一个标签
        uuid: 待重命名标签的uuid

        异常情况:
        标签uuid不存在
        重命名标签名已存在
        """
        if any(tag_name == value for value in self.tags.values()):
            print(f"[tagger] 已经存在名为 '{tag_name}' 的标签了。")
            return

        self.tags[uuid] = tag_name
        tools.writeJson(self.tags, self.tags_dict_path)

    def addTag(self, project_uuid, tag_uuid):
        """
        为一个项目添加一个标签

        异常情况:
        项目uuid不存在
        标签uuid不存在
        项目已有本标签
        """
        project_info = self.getInfoByUuid(project_uuid)
        project_info['tags'].append(tag_uuid)

        project_info_path = os.path.join(self.projects_path, project_uuid, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)

    def removeTag(self, project_uuid, tag_uuid):
        """
        为一个项目移除一个标签

        异常情况:
        项目uuid不存在
        标签uuid不存在
        项目未拥有本标签
        """
        project_info = self.getInfoByUuid(project_uuid)
        project_info['tags'].reomve(tag_uuid)

        project_info_path = os.path.join(self.projects_path, project_uuid, project_uuid + '.json')
        tools.writeJson(project_info, project_info_path)