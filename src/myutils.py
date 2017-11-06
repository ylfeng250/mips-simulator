"""
辅助工具类
-数据读取 read_bin
-解析指令 parse_instructions
"""
# 输入二进制文件，返回指令列表
def read_bin(filename):
    instructions = []
    with open(filename,"r") as fin:
        for line in fin:
            instructions.append(line.strip())
    return instructions

# 解析指令
def parse_instructions(instructions,flags,opCodes,rs,rt,rd,shiftAmt,functionCode):
    flags = 0
    
def test():
    filename = input("请输入二进制文件:\n")
    instructions = read_bin(filename)
    print(instructions[0][:2])
if __name__ == "__main__":
    test()
    