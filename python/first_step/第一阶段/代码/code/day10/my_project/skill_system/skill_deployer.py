
import sys

sys.path.append("/home/tarena/month01/code/day10/my_project")
print(sys.path)

from common.list_helper import ListHelper


class SkillDeployer:
    def deploy(self):
        print("释放技能")


ListHelper.get_elements()