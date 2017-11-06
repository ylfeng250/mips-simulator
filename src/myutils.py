"""
辅助工具类
-数据读取 read_bin
-解析指令 parse_instructions
"""
from instructions import *
opc = {
    "0000": ['J', 'ADD'],
    "0001": ['JR', 'SUB'],
    "0010": ['BEQ', 'MUL'],
    "0011": ['BLTZ', 'AND'],
    "0100": ['BGTZ', 'OR'],
    "0101": ['BREAK', 'XOR'],
    "0110": ['SW', 'NOR'],
    '0111': ['LW', 'SLT'],
    '1000': ['SLL', 'ADDI'],
    '1001': ['SRL', 'ANDI'],
    '1010': ['SRA', 'ORI'],
    '1011': ['NOP', 'XORI']
}


# 输入二进制文件，返回指令列表
def read_bin(filename):
    instructions = []
    with open(filename, "r") as fin:
        for line in fin:
            instructions.append(line.strip())
    return instructions


# 解析指令
# 2     4       5       5       5       5           5
#flag   opCodes rs      rt      rd      shiftAmt    functionCode
def parse_instructions(instruction, flags, opCodes, rs, rt, rd, shiftAmt,
                       functionCode):
    flags.append(instruction[0:2])  # 前两位用来区分是Category-1指令还是Category-2指令
    opCodes.append(instruction[2:6])  # 四位操作码
    rs.append(instruction[6:11])
    rt.append(instruction[11:16])
    rd.append(instruction[16:21])
    shiftAmt.append(instruction[21:26])
    functionCode.append(instruction[26:])


# break之后是数据部分
def find_break(instructions):
    count = 0
    for instruction in instructions:
        if instruction != "01010100000000000000000000001101":
            count += 1
        else:
            count += 1
            break
    return count  # 数据段的开头


# 检查属于第几类指令 0-Category-1    1-Category-2
def checkFlag(flag):
    k = 0
    if flag == '01':
        k = 0
    else:
        k = 1
    return int(k)


# 生成disassembly.txt  i是当前的指令地址
def outputDis(instruction, currentAddress, flag, opCode, rs, rt, rd, shiftAmt,
              functionCode, i, outFile):

    instructionName = ""  # 指令名
    instructionArgs = ""  # 指令参数
    instructionName = opc[opCode][flag]  # 获取指令名称

    instructionArgs = switch[instructionName](rs, rt, rd, shiftAmt,
                                              functionCode)
    print(instructionArgs)

    return False


def test():
    filename = input("请输入二进制文件:\n")
    instructions = read_bin(filename)
    print(instructions[0][:2])


if __name__ == "__main__":
    test()
