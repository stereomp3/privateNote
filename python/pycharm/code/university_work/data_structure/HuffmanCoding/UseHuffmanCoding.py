from HuffmanCoding import HuffmanCoding
import sys

path = "README.txt"  # 這邊可以用我的介紹檔案做測試

h = HuffmanCoding(path)

output_path = h.compress()  # 先做壓縮
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)  # 再做解壓縮
print("Decompressed file path: " + decom_path)