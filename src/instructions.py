# 获取寄存器的名字
def getRegName(rs):
    if int(rs, base=2) >= 0 and int(rs, base=2) <= 31:
        registerName = 'R' + str(int(rs, base=2))
    return registerName

# J
def case_J(rs, rt, rd, shiftAmt, functionCode):
    instructionArgs = '#'
    instructionArgs = '#' + str(int(rs + rt + rd + shiftAmt + functionCode, base=2) << 2)
    return instructionArgs

# JR
def case_JR(rs, rt, rd, shiftAmt, functionCode):
    instructionArgs = getRegName(rs)
    return instructionArgs

# BEQ
def case_BEQ(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    offset = rd + shiftAmt + functionCode + "00"
    instructionArgs = rsName + ', ' + rtName + ', #' + str(int(offset,2))
    return instructionArgs

# BLTZ
def case_BLTZ(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    offset = rd + shiftAmt + functionCode + "00"
    instructionArgs = rsName + ', #' + str(int(offset,base=2))
    return instructionArgs

# BGTZ
def case_BGTZ(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    offset = rd + shiftAmt + functionCode + "00"
    instructionArgs = rsName + ', #' + str(int(offset,base=2))
    return instructionArgs

def case_BREAK(rs, rt, rd, shiftAmt, functionCode):
    # BREAK 操作数
    return ""

# SW
def case_SW(rs, rt, rd, shiftAmt, functionCode):
    rtName = getRegName(rt)
    base = getRegName(rs)
    offset = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', '+ str(int(offset,base=2)) + '(' + base + ')'
    return instructionArgs

# LW
def case_LW(rs, rt, rd, shiftAmt, functionCode):
    rtName = getRegName(rt)
    base = getRegName(rs)
    offset = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', '+ str(int(offset,base=2)) + '(' + base + ')'
    return instructionArgs

# SLL
def case_SLL(rs, rt, rd, shiftAmt, functionCode):
    sa = str(int(shiftAmt,base=2))
    rdName = getRegName(rd)
    rtName = getRegName(rt)
    instructionArgs = rdName + ', ' + rtName + ', #' + sa
    return instructionArgs

# SRL
def case_SRL(rs, rt, rd, shiftAmt, functionCode):
    sa = str(int(shiftAmt,base=2))
    rdName = getRegName(rd)
    rtName = getRegName(rt)
    instructionArgs = rdName + ', ' + rtName + ', #' + sa
    return instructionArgs

# SRA
def case_SRA(rs, rt, rd, shiftAmt, functionCode):
    sa = str(int(shiftAmt,base=2))
    rdName = getRegName(rd)
    rtName = getRegName(rt)
    instructionArgs = rdName + ', ' + rtName + ', #' + sa
    return instructionArgs

# NOP
def case_NOP(rs, rt, rd, shiftAmt, functionCode):
    return ""

# ADD
def case_ADD(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# SUB
def case_SUB(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# MUL
def case_MUL(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# AND
def case_AND(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# OR
def case_OR(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# XOR
def case_XOR(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# NOR
def case_NOR(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# SLT
def case_SLT(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    rdName = getRegName(rd)
    instructionArgs = rdName + ', ' + rsName + ', ' + rtName
    return instructionArgs

# ADDI
def case_ADDI(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    immediate = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', ' + rsName + ', #' + str(int(immediate,base=2))
    return instructionArgs

# ANDI
def case_ANDI(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    immediate = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', ' + rsName + ', #' + str(int(immediate,base=2))
    return instructionArgs

# ORI
def case_ORI(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    immediate = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', ' + rsName + ', #' + str(int(immediate,base=2))
    return instructionArgs

# XORL
def case_XORI(rs, rt, rd, shiftAmt, functionCode):
    rsName = getRegName(rs)
    rtName = getRegName(rt)
    immediate = rd + shiftAmt + functionCode
    instructionArgs = rtName + ', ' + rsName + ', #' + str(int(immediate,base=2))
    return instructionArgs

switch={
    'J':case_J,
    'JR':case_JR,
    'BEQ':case_BEQ,
    'BLTZ':case_BLTZ,
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