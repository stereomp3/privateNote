"""
    模块相关概念
"""
# __all__变量：定义可导出成员，仅对from xx import *语句有效。
from my_project.skill_system import *

skill_manager.SkillManager().generate()

# __doc__变量：文档字符串。
print(skill_manager.__doc__)

# __file__变量：模块对应的文件路径名。
print(__file__)

# __name__变量：模块自身名字，可以判断是否为主模块。

print(__name__)# __main__










