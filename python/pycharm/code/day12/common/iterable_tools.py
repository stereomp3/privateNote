"""
    可迭代對象工具模塊
"""


class IterableHelper:
    """
        可迭代對象助手
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代對象中查找滿足條件的所有元素
            :param iterable: 可迭代對象，需要查找的數據
            :param func_condition: 數據類型，查找條件
            :return: 生成器對象
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def first(iterable, func_condition):
        """
            在可迭代對象中查找滿足條件的單個元素
            :param iterable: 可迭代對象，需要查找的數據
            :param func_condition: 數據類型，查找條件
            :return: 第一個元素
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable, func_condition):
        """
            在可迭代對象中查找滿足條件的單個元素
            :param iterable: 可迭代對象，需要查找的數據
            :param func_condition: 數據類型，查找條件
            :return: 第一個元素
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def get_count(iterable, func_condition):
        """
            在可迭代對象中，獲取滿足條件的元素數量
            :param iterable: 可迭代對象，需要查找的數據
            :param func_condition: 數據類型，查找條件
            :return: int類型 數量
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def select(iterable, func_handle):
        """
            通用的篩選方法
            :param iterable: 可迭代對象，需要篩選的數據
            :param func_handle: 篩選邏輯
            :return: 生成器對象
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def is_exists(iterable, func_condition):
        """
            判斷可迭帶對象中是否存在某個條件的對象
            :param iterable: 可迭代對象類型，需要篩選的數據
            :param func_condition: 查找條件
            :return: bool, True表示存在，False表示不存在
        """
        for item in iterable:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(iterable, func_handle):
        """
            根據指定邏輯累加可迭帶對象中的元素
            :param iterable: 可迭代對象類型，需要累加的數據
            :param func_handle: 累加邏輯
            :return: 數據類型，累加結果
        """
        result = 0
        for item in iterable:
            result += func_handle(item)
        return result

    # @staticmethod
    # def get_max(iterable, func_condition):
    #     """
    #         根據指定邏輯累加可迭帶對象中的元素
    #         :param iterable: 可迭代對象類型，需要累加的數據
    #         :param func_handle: 累加邏輯
    #         :return: 數據類型，累加結果
    #     """
    #     temp = 0
    #     pre_temp = 0
    #     for item in iterable:
    #         if pre_temp > temp:
    #             temp = pre_temp
    #         pre_temp = func_condition(item)
    #     return temp

    @staticmethod
    def get_max(iterable, func_condition):
        """
            根據條件在可迭帶對象中獲取最大元素
            :param iterable: 可迭代對象類型，需要查找的數據
            :param func_condition: 指定條件
            :return: 最大元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(max_value) < func_condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    # @staticmethod
    # def delete_all(iterable, func_condition):
    #     delete_list = []
    #     for i in range(len(iterable)):
    #         if func_condition(iterable[i]):
    #             delete_list.append(iterable[i])
    #     for item in delete_list:
    #         iterable.remove(item)

    @staticmethod
    def delete_all(iterable, func_condition):
        """
            根據條件刪除多個元素
            :param iterable: 可迭代對象類型，需要查找的數據
            :param func_condition: 刪除條件
            :return: 刪除元素的數量
        """
        count = 0
        for i in range(len(iterable)-1, -1, -1):
            if func_condition(iterable[i]):
                count += 1
                del iterable[i]
        return count

    @staticmethod
    def order_by(iterable, func_condition):
        """
            根據條件升序排列
            :param iterable: 可迭代對象類型，需要排序的數據
            :param func_condition: 比較條件
        """
        for i in range(len(iterable) - 1):
            for y in range(i+1, len(iterable)):
                if func_condition(iterable[i]) > func_condition(iterable[y]):
                    iterable[i], iterable[y] = iterable[y], iterable[i]
