# J
def case_J(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    immediate = rs + rt + rd + shiftAmt + functionCode + "00"
    currentAddress[0] = (int(immediate, 2))

# JR
def case_JR(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    currentAddress[0] = (int(rs+"00", 2))

# BEQ if rs = rt then branch
def case_BEQ(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    offset = rd + shiftAmt + functionCode + "00"
    if regValues[int(rs, 2)] == regValues[int(rt, 2)]:
        currentAddress[0] = currentAddress[0] + int(offset, 2) + 4
    else:
        currentAddress[0] = currentAddress[0] + 4 

# BLTZ
def case_BLTZ(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    offset = rd + shiftAmt + functionCode + "00"
    if regValues[int(rs, 2)] < 0:
        currentAddress[0] = currentAddress[0] + int(offset,2) + 4
    else:
        currentAddress[0] = currentAddress[0] + 4

# BGTZ
def case_BGTZ(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    offset = rd + shiftAmt + functionCode + "00"
    if regValues[int(rs, 2)] > 0:
        currentAddress[0] = currentAddress[0] + int(offset,2) + 4
    else:
        currentAddress[0] = currentAddress[0] + 4

# BREAK
def case_BREAK(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    currentAddress[0] += 4

# SW
def case_SW(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    offset = rd + shiftAmt + functionCode
    # print(int((regValues[int(rs, 2)] + int(offset, 2))
    #                  / 4) - int(dataAddress/4))
    memoryValues[int((regValues[int(rs, 2)] + int(offset, 2))
                     / 4) - int(dataAddress/4)] = regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4


# LW rt = memory[base+offset]
def case_LW(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    offset = rd + shiftAmt + functionCode
    # print(int((regValues[int(rs, 2)] + int(offset, 2))
    #                  / 4) - int(dataAddress/4))
    regValues[int(rt, 2)] = memoryValues[int((regValues[int(rs, 2)] + int(offset, 2))
                     / 4) - int(dataAddress/4)]
    currentAddress[0] = currentAddress[0] + 4

# SLL rd = rt << shiftAmt
def case_SLL(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    mask = (2**32) - 1
    # 左移会有溢出
    regValues[int(rd, 2)] = (regValues[int(rt, 2)] << int(shiftAmt, 2)) & mask
    currentAddress[0] = currentAddress[0] + 4

# SRL rd = rt >> sa
def case_SRL(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = (regValues[int(rt, 2)] >> int(shiftAmt[i], 2))
    currentAddress[0] = currentAddress[0] + 4

# SRA rd = rt >> sa
def case_SRA(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = (regValues[int(rt, 2)] >> int(shiftAmt[i], 2))
    currentAddress[0] = currentAddress[0] + 4

# NOP
def case_NOP(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    currentAddress[0] = currentAddress[0] + 4

# ADD rd = rs + rt
def case_ADD(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] + regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# SUB rd = rs - rt
def case_SUB(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] - regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# MUL rd = rs * rt
def case_MUL(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] * regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# AND rd = rs AND rt
def case_AND(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] & regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# OR rd = rs or rt
def case_OR(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] | regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# XOR rd = rs XOR rt
def case_XOR(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = regValues[int(rs, 2)] ^ regValues[int(rt, 2)]
    currentAddress[0] = currentAddress[0] + 4

# NOR rd = rs NOR rt
def case_NOR(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    regValues[int(rd, 2)] = ~(regValues[int(rs, 2)] | regValues[int(rt, 2)])
    currentAddress[0] = currentAddress[0] + 4

# SLT
def case_SLT(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    if regValues[int(rs, 2)] < regValues[int(rt, 2)]:
        regValues[int(rd, 2)] = 1
    else:
        regValues[int(rd, 2)] = 0
    currentAddress[0] = currentAddress[0] + 4

# ADDI rt = rs + immediate
def case_ADDI(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    immediate = rd + shiftAmt + functionCode
    regValues[int(rt, 2)] = regValues[int(rs, 2)] + int(immediate,2)
    currentAddress[0] = currentAddress[0] + 4

# ANDI rt = rs AND immediate
def case_ANDI(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    immediate = rd + shiftAmt + functionCode
    regValues[int(rt, 2)] = regValues[int(rs, 2)] & int(immediate,2)
    currentAddress[0] = currentAddress[0] + 4

# ORI rt = rs or immediate
def case_ORI(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    immediate = rd + shiftAmt + functionCode
    regValues[int(rt, 2)] = regValues[int(rs, 2)] | int(immediate,2)
    currentAddress[0] = currentAddress[0] + 4

# XORL rt = rs XOR immediate
def case_XORI(rs, rt, rd, shiftAmt,functionCode,regValues,memoryValues,dataAddress,currentAddress):
    immediate = rd + shiftAmt + functionCode
    regValues[int(rt, 2)] = regValues[int(rs, 2)] ^ int(immediate,2)
    currentAddress[0] = currentAddress[0] + 4

switch={
    'J':case_J,
    'JR':case_JR,
    'BEQ':case_BEQ,
    'BLTZ':case_BEQ,
    'BGTZ':case_BGTZ,
    'BREAK':case_BREAK,
    'SW':case_SW,
    'LW':case_LW,
    'SLL':case_SLL,
    'SRL':case_SRL,
    'SRA':case_SRA,
    'NOP':case_NOP,
    'ADD':case_ADD,
    'SUB':case_SUB,
    'MUL':case_MUL,
    'AND':case_AND,
    'OR':case_OR,
    'XOR':case_XOR,
    'NOR':case_NOR,
    'SLT':case_SLT,
    'ADDI':case_ADDI,
    'ANDI':case_ANDI,
    'ORI':case_ORI,
    'XORI':case_XORI,
}