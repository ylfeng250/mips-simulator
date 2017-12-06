"""
辅助工具类
-数据读取 read_bin
-解析指令 parse_instructions
-find_break 返回代码段的结尾即数据段的起点
-checkFlag 检测输入什么类型的指令
-outputDis 输出dis文件
-outputSim 输出Sim文件
"""
import instructions
import changeRegValues

# 根据flag判断是第一类操作还是第二类操作，然后映射操作符
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


# break之后是数据部分---暂时没有用了

def find_break(instructions):
    count = 0
    for instruction in instructions:
        if instruction[0:7] != "010101":
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
              functionCode, i, disOut):
    instructionName = opc[opCode][flag]  # 获取指令名称
    instructionArgs = instructions.switch[instructionName](rs, rt, rd, shiftAmt,functionCode) # 获取指令参数
    if instructionName != 'BREAK':
        disOut.write( instruction + '\t' + str(currentAddress[0]) + '\t' + instructionName+ ' ' + str(instructionArgs) + '\n')
    else:# break指令没有操作数
        disOut.write( instruction + '\t' + str(currentAddress[0]) + '\t' + instructionName + '\n')
    # Check if instruction is a break instruction
    if instructionName == 'BREAK':
        return True

# 执行命令 生成sim文件
def outputSim(dataAddress,currentAddress, flag, opCode, rs, rt, rd, shiftAmt,
                       functionCode, regValues, memoryValues, count, simOut):
    instructionName = opc[opCode][flag]  # 获取指令名称
    instructionArgs = instructions.switch[instructionName](rs, rt, rd, shiftAmt,functionCode) # 获取指令参数
    returnFlag = False # 是否结束标志
    
    if instructionName == 'BREAK':
        returnFlag = True
    simOut.write("--------------------" + '\n')
    if instructionName != 'BREAK':
        simOut.write("Cycle:" + str(count[0] + 1) + '\t' + str(currentAddress[0]) + '\t' + instructionName + ' ' + instructionArgs + '\n')
    else:
        simOut.write("Cycle:" + str(count[0] + 1) + '\t' + str(currentAddress[0]) + '\t' + instructionName + '\n')
    simOut.write('\n')

    changeRegValues.switch[instructionName](rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress)
    
    simOut.write('Registers' + '\n')
    simOut.write('R00:' + '\t' + str(regValues[0]) + '\t' + str(regValues[1]) + '\t' + str(regValues[2])
                    + '\t' + str(regValues[3]) + '\t' + str(regValues[4]) + '\t' + str(regValues[5]) + '\t'
                    + str(regValues[6]) + '\t' + str(regValues[7]) + '\n')
    simOut.write('R08:' + '\t' + str(regValues[8]) + '\t' + str(regValues[9]) + '\t' +
                    str(regValues[10]) + '\t' + str(regValues[11]) + '\t' + str(regValues[12]) + '\t' +
                    str(regValues[13]) + '\t' + str(regValues[14]) + '\t' + str(regValues[15]) + '\n')
    simOut.write('R16:' + '\t' + str(regValues[16]) + '\t' + str(regValues[17]) + '\t' +
                    str(regValues[18]) + '\t' + str(regValues[19]) + '\t' + str(regValues[20]) + '\t' +
                    str(regValues[21]) + '\t' + str(regValues[22]) + '\t' + str(regValues[23]) + '\n')
    simOut.write('R24:' + '\t' + str(regValues[24]) + '\t' + str(regValues[25]) + '\t' +
                    str(regValues[26]) + '\t' + str(regValues[27]) + '\t' + str(regValues[28]) + '\t' +
                    str(regValues[29]) + '\t' + str(regValues[30]) + '\t' + str(regValues[31]) + '\n')
    simOut.write('\n')
    simOut.write('Data' + '\n')
    simOut.write(str(dataAddress)+':\t' + str(memoryValues[0]) + '\t' + str(memoryValues[1]) + '\t' + str(memoryValues[2]) + '\t' +
                    str(memoryValues[3]) + '\t' + str(memoryValues[4]) + '\t' + str(memoryValues[5]) + '\t' +
                    str(memoryValues[6]) + '\t' + str(memoryValues[7]) + '\n')
    simOut.write(str(dataAddress+32)+':\t' + str(memoryValues[8]) + '\t' + str(memoryValues[9]) + '\t' + str(memoryValues[10]) + '\t' +
                    str(memoryValues[11]) + '\t' + str(memoryValues[12]) + '\t' + str(memoryValues[13]) + '\t' +
                    str(memoryValues[14]) + '\t' + str(memoryValues[15]) + '\n')
    simOut.write(str(dataAddress+64)+':\t' + str(memoryValues[16]) + '\t' + str(memoryValues[17]) + '\t' + str(memoryValues[18]) + '\t' +
                    str(memoryValues[19]) + '\t' + str(memoryValues[20]) + '\t' + str(memoryValues[21]) + '\t' +
                    str(memoryValues[22]) + '\t' + str(memoryValues[23]) + '\n')
    simOut.write('\n')

    count[0] = count[0] + 1

    return returnFlag



                                

def test():
    filename = input("请输入二进制文件:\n")
    instructions = read_bin(filename)
    print(instructions[0][:2])


if __name__ == "__main__":
    test()
