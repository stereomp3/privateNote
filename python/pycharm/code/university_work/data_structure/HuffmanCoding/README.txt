參考資料: 

Huffman Coding Python Implementation: https://bhrigu.me/post/huffman-coding-python-implementation/

Huffman coding: https://en.wikipedia.org/wiki/Huffman_coding

繳交的python code參考至Huffman Coding Python Implementation，內含有個人註解

> !! 點選UseHuffmanCoding.py可以將本文件壓縮成bin檔案，然後解壓縮成REAdME_decompressed.txt



# 說明:

 **Huffman coding** 是無損數據壓縮技術之一，常處理編寫工作。它根據輸入字符的出現頻率為輸入字符分配可變長度代碼。如果字符出現的頻率越高，則給字符的碼越短，相反則字符號碼越長。



* 資料壓縮

假設我們要給一個英文單字**"F O R G E T"**進行霍夫曼編碼，而每個英文字母出現的頻率分別如下

Symbol			F		O		R		G		E		T

Frequency	  2		3		 4		 4		5 		7

CODE			  000	001	100	101	011	111



接下來就是找最小節點相加!

step1: 2+3 = 5     (5, 4, 4, 5, 7)

step2: 4+4 = 8     (5, 8, 5, 7)

step3: 5+5 = 10   (10, 8, 7)

step4: 8+7 = 15   (10, 15)

final: 10+15 = 25 (25)    --> 只剩一個，結束

最後的樹就會長的像這樣:

​				   25

​			10		       15

​		5		         8

​	2	      3	     5	4	   4	 7

​      F              O       E   R           G           T





* 資料解壓縮

霍夫曼碼樹的解壓縮就是將得到的前置碼（Prefix Huffman code; 就是0和1(判斷是左子節點還是右子節點)）轉換回符號，通常藉由樹的追蹤（Traversal），將接收到的位元串（Bits stream）一步一步還原。但是要追蹤樹之前，必須要先重建霍夫曼樹；某些情況下，如果每個符號的權重可以被事先預測，那麼霍夫曼樹就可以預先重建，並且儲存並重複使用，否則，傳送端必須預先傳送霍夫曼樹的相關資訊給接收端。

最簡單的方式，就是預先統計各符號的權重並加入至壓縮之位元串，但是此法的運算量花費相當大，並不適合實際的應用。若是使用Canonical encoding，則可精準得知樹重建的資料量只占*B*2^*B*位元（其中B為每個符號的位元數（bits））。如果簡單將接收到的位元串一個位元一個位元的重建，例如：'0'表示父節點，'1'表示終端節點，若每次讀取到1時，下8個位元則會被解讀是終端節點（假設資料為8-bit字母），則霍夫曼樹則可被重建，以此方法，資料量的大小可能為2~320位元組不等。雖然還有很多方法可以重建霍夫曼樹，但因為壓縮的資料串包含"trailing bits"，所以還原時一定要考慮何時停止，不要還原到錯誤的值，如在資料壓縮時時加上每筆資料的長度等



# 討論:



Q: 為甚麼可以減少資料量?

A: '0'與'1'分別代表指向左子節點與右子節點，最後為完成的二元樹共有**n**個終端節點(一開始的元素)點與**n-1**個非終端節點，去除了不必要的符號並產生最佳的編碼長度，先把樹狀結構轉乘01組成的值，再把它轉成byte組成的資料變成 bin檔，資料量就可以少很多了。


Q: 資料要如何還原?

透過樹去反推，先用bin檔還原成 01的檔案(Prefix Huffman code)，再把它還原成字符，就可以完整的還原資料了


Python 主要程式碼解析:

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


    def decompress(self, input_path):
        """
            主要呼叫函數，處理檔案的解壓縮
            :param input_path: .txt檔傳入的文字內容
            :return: 輸出檔案，還原原本的資料
        """
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
    	# 輸出文字檔   ???_decompressed_text
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
    
            byte = file.read(1)
            while (len(byte) > 0):  # 讀取文檔
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
    
            encoded_text = self.remove_padding(bit_string)  # 把文件byte 轉成 Prefix Huffman code
    
            decompressed_text = self.decode_text(encoded_text)  # 把 0 1 編碼轉乘 文字出現次數 的 值， 利用樹狀結構去回推 (reverse_mapping)
    
            output.write(decompressed_text)  # 寫入文字檔   ???_decompressed_text
    
        print("Decompressed")
        return output_path

