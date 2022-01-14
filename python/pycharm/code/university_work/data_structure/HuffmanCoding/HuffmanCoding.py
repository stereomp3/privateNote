import heapq
import os

"""
author: Bhrigu Srivastava
website: https:bhrigu.me
chinese annotation: 110910541
"""


# 這裡出現的目的是讓下面class HuffmanCoding 裡面 class HeapNode 的if (not isinstance(other, HeapNode)):可以正常運作
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if (other == None):
            return False
        if (not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq


class HuffmanCoding:  # 可以創建霍夫曼碼
    def __init__(self, path):
        self.path = path  # 接收文件路徑
        self.heap = []  # 使用在 heapq.heappush(self.heap, node)，接收最下層的終端節點
        self.codes = {}  # 霍夫曼碼樹 dict[char] = 0 || 1， 0代表是左子節點，1代表是右子節點
        self.reverse_mapping = {}

    class HeapNode:  # 霍夫曼碼樹節點連接
        def __init__(self, char, freq):
            self.char = char  # 儲存字元
            self.freq = freq  # 儲存字元出現次數
            self.left = None  # 樹狀結構紀錄
            self.right = None

        # defining comparators less_than and equals
        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if (other == None):
                return False
            if (not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq

    # functions for compression:

    def make_frequency_dict(self, text):
        """
            統計各個字符在檔案中出現的次數
            :param text: .txt檔傳入的文字內容
            return: 各個字符出現次數
        """
        frequency = {}  # 創建字典，主要是存取text裡面的字出現的次數
        for character in text:
            if not character in frequency:
                frequency[character] = 0  # 一開始創建，初始值為0
            frequency[character] += 1  # 每重複一次就加一
        return frequency

    def make_heap(self, frequency):
        """
            利用 heapq.heappush、 self.heap、 class HeapNode 製作 霍夫曼碼樹 的最下層(終端節點)
            :param frequency: 各個字符出現次數
        """
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)  # 把資料丟入霍夫曼碼樹

    def merge_nodes(self):
        """
           利用 heapq.heappush、 self.heap、 class HeapNode 製作 霍夫曼碼樹 的其他層(非終端節點)
       """
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)  # 把最小的兩個終端節點相加
            merged.left = node1  # 節點相連
            merged.right = node2

            heapq.heappush(self.heap, merged)  # 把資料丟入霍夫曼碼樹

    def make_codes_helper(self, root, current_code):
        """
            把相連接的資料用 0、1 表示他是 左子節點 還是 右子節點
            :param root: .txt檔傳入的文字內容
            :param current_code: .txt檔傳入的文字內容
            :return: 在沒有資料或是在root.char都已經填過值十，回傳null，
        """
        if (root == None):
            return

        if (root.char != None):  # 把每個相連接的地方分別填入0、1
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        """
            使用 self.make_codes_helper
        """
        root = heapq.heappop(self.heap)  # 取得最下層的內容
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        """
            把壓縮好(self.codes[char])的資料傳回
            :param text: .txt檔傳入的文字內容
            :return: self.codes裡面的內容
        """
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]  # 把上面 make_codes 填入的那些 0 1傳入到 encoded_text
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        """
            進行編碼
            :param encoded_text: self.codes裡面的內容
            :return: 轉成特殊編碼
        """
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)  # 把char轉成byte
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        """
            取得byte編碼內容
            :param padded_encoded_text: 特殊編碼
            :return: byte編碼
        """
        if (len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        """
            主要呼叫函數，處理檔案的壓縮
            :return: 各個字符出現次數
        """
        filename, file_extension = os.path.splitext(self.path)  # 取得輸入的文件
        output_path = filename + ".bin"  # 輸出的壓縮檔名稱

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)  # 創建字典
            self.make_heap(frequency)  # 利用 heapq.heappush、 self.heap、 class HeapNode 製作 霍夫曼碼樹 的最下層(終端節點)
            self.merge_nodes()  # 利用 heapq.heappush、 self.heap、 class HeapNode 製作 霍夫曼碼樹 的其他層(非終端節點)
            self.make_codes()  # 把相連接的資料用 0、1 表示他是 左子節點 還是 右子節點

            encoded_text = self.get_encoded_text(text)  # 把壓縮好(self.codes[char])的資料傳回
            padded_encoded_text = self.pad_encoded_text(encoded_text)  # 進行編碼

            b = self.get_byte_array(padded_encoded_text)  # 取得byte編碼內容
            output.write(bytes(b))  # 寫入檔案 .bin  ???.bin

        print("Compressed")
        return output_path

    """ functions for decompression: """

    def remove_padding(self, padded_encoded_text):
        """
            把文件byte 轉成 Prefix Huffman code
            :param padded_encoded_text: byte code
            :return: 把 byte 轉成 正常編碼
        """
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        """
            把 0 1 編碼轉乘 文字出現次數 的 值， 利用樹狀結構去回推 (reverse_mapping)
            :param encoded_text: 正常編碼
            :return: 壓縮文檔文字
        """
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        """
            主要呼叫函數，處理檔案的解壓縮
            :param input_path: .txt檔傳入的文字內容
            :return: 輸出檔案，還原原本的資料
        """
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_d" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:  # open 輸出文字檔   ???_decompressed_text
            bit_string = ""

            byte = file.read(1)
            while (len(byte) > 0):  # 讀取文檔
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)  # 把文件byte 轉成 Prefix Huffman code

            decompressed_text = self.decode_text(encoded_text)  # 把 0 1 編碼轉乘 文字出現次數 的 值， 利用樹狀結構去回推 (reverse_mapping)

            output.write(decompressed_text)  # 寫入文字檔

        print("Decompressed")
        return output_path
