"""
    一張紙(0.01毫米)對折多少次，才會超過珠穆朗瑪峰(8844.43米)
"""
times = 0
paper = 0.00001
# thickness = 1e-5
mountain = 8844.43

while paper < mountain:
    paper *= 2
    times += 1
print(times)