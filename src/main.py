from myutils import *

def main():
    # 输入文件名称
    filename = input("please input bin file\nfor example:sample.txt,you just input sample\n")
    outputFileName = filename + ".txt"
    currentAddress = [256] # 地址从256开始
    instructions = read_bin(outputFileName) # 获取所有的指令集
    flags = [] # 标志位，判断属于哪一类标志
    opCodes = [] # 操作码
    rs = [] # 源寄存器
    rt = [] # 源寄存器 
    rd = [] # 目的寄存器
    shiftAmts = [] # 在移位指令中表示移位
    functionCodes = [] # 功能码
    regValues = [0] * 32 # 保存32个寄存器 32个寄存器用5个二进制表示
    memoryValues = [0] * 60 # 保存内存值
    count = [0]
    # 输出文件的命名格式
    disOut = open(filename + '_dis.txt', 'w')
    simOut = open(filename + '_sim.txt', 'w')

    # 解析指令
    for instrcution in instructions:
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

    # 转汇编代码
    for instrcution in instructions:
        i = int((currentAddress[0] / 4) - 64)
        flag = checkFlag(flags[i])
        if outputDis(instrcution,currentAddress,flag,opCodes[i],rs[i],rt[i],rd[i],shiftAmts[i],functionCodes[i],i,disOut):
            break;
        currentAddress[0] += 4

    # breakindex
    dataAddress = currentAddress[0] + 4# 数据段开始的地址
    print(dataAddress)
    breakIndex = int((dataAddress-256)/4) # break之后是data
    print(breakIndex)
    # 打印数据
    dataInstructions = instructions[breakIndex:] # 获取数据部分
    i = 0
    for data in dataInstructions:
        bits = 32
        currentAddress[0] = currentAddress[0] + 4
        j = int((currentAddress[0] / 4) - 64)
        print(flags[j][0:1])
        if flags[j][0:1] == '0':
            disOut.write(data + '\t' + str(currentAddress[0]) + '\t' + str(int(data, 2)) + '\n')
            memoryValues[i] = int(data, 2)
        else:
            disOut.write(data + '\t' + str(currentAddress[0]) + '\t' + str(int(data, 2) - (1<<bits)) + '\n')
            memoryValues[i] = int(data, 2) - (1<<bits)
        i = i + 1
    
    currentAddress[0] = 256
    
    # 执行语句
    isBreak = False
    while isBreak != True:
        i = int((currentAddress[0] / 4) - 64)
        flag = checkFlag(flags[i])
        # Make sure we are only executing instructions before the break
        isBreak = outputSim(dataAddress,currentAddress, flag, opCodes[i], rs[i], rt[i], rd[i], shiftAmts[i],
                                     functionCodes[i], regValues, memoryValues, count, simOut)
        if isBreak:
            break
if __name__ == "__main__":
    main()