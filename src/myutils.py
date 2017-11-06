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
# 2     4       5       5       5       5           5
#flag   opCodes rs      rt      rd      shiftAmt    functionCode
def parse_instructions(instruction,flags,opCodes,rs,rt,rd,shiftAmt,functionCode):
    flags.append(instruction[0:2]) # 前两位用来区分是Category-1指令还是Category-2指令
    opCodes.append(instruction[2:6]) # 四位操作码
    rs.append(instruction[6:11])
    rt.append(instruction[11:16])
    rd.append(instruction[16:21])
    shiftAmt.append(instruction[21:26])
    functionCode.append(instruction[26:])
   
def test():
    filename = input("请输入二进制文件:\n")
    instructions = read_bin(filename)
    print(instructions[0][:2])
if __name__ == "__main__":
    test()
    