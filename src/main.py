from myutils import *

def main():
    # 输入文件名称
    filename = input("please input bin file\nfor example:sample.txt,you just input sample\n")
    filename = filename + ".txt"
    outputFileName = filename
    currentAddress = [256] # 地址从256开始
    instructions = read_bin(filename) # 获取所有的指令集
    flags = [] # 标志位，判断属于哪一类标志
    opCodes = [] # 操作码
    rs = [] # 源寄存器
    rt = [] # 源寄存器 
    rd = [] # 目的寄存器
    shiftAmts = [] # 在移位指令中表示移位
    functionCodes = [] # 功能码
    regValues = [0] * 32 # 保存32个寄存器中的值 32个寄存器用5个二进制表示
    memoryValues = [0] * 40 # 保存内存值
    count = [0]
    # 输出文件的命名格式
    # disOut = open(outputFileName + '_dis.txt', 'w')
    # simOut = open(outputFileName + '_sim.txt', 'w')

    # 解析指令
    for instrcution in instructions:
        currentAddress[0] += 4
        parse_instructions(instrcution,flags,opCodes,rs,rt,rd,shiftAmts,functionCodes)

    # test

    # for i in range(len(instructions)):
    #     print(instructions[i])
    #     print(flags[i])
    #     print(opCodes[i])
    #     print(rs[i])
    #     print(rt[i])
    #     print(rd[i])
    #     print(shiftAmts[i])
    #     print(functionCodes[i])

    # breakindex
    breakIndex = find_break(instructions) # break之后是data

    # Reset PC
    currentAddress[0] = 256


if __name__ == "__main__":
    main()