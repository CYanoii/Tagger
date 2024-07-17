class PathNotExistError(Exception):  
    def __init__(self, message="路径不存在。"):
        super().__init__(message) # 调用基类的构造器
        self.message = message
    
    def __str__(self):
        # 当打印异常对象时，将调用此方法
        return f"{self.__class__.__name__}: {self.message}"

class PathAlreadyExistError(Exception):  
    def __init__(self, message="路径已存在。"):
        super().__init__(message) # 调用基类的构造器
        self.message = message
    
    def __str__(self):
        # 当打印异常对象时，将调用此方法
        return f"{self.__class__.__name__}: {self.message}"

class PathTypeError(Exception):  
    def __init__(self, message="路径格式错误，并非指定的文件或目录或特定后缀文件。"):
        super().__init__(message) # 调用基类的构造器
        self.message = message
    
    def __str__(self):
        # 当打印异常对象时，将调用此方法
        return f"{self.__class__.__name__}: {self.message}"

class DataTypeError(Exception):  
    def __init__(self, message="数据类型错误。"):
        super().__init__(message) # 调用基类的构造器
        self.message = message
    
    def __str__(self):
        # 当打印异常对象时，将调用此方法
        return f"{self.__class__.__name__}: {self.message}"