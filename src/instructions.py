# 获取寄存器的名字
def getRegName(rs):
    if int(rs, base=2) >= 0 and int(rs, base=2) <= 31:
        registerName = 'R' + str(int(rs, base=2))
    return registerName

# J
def case_J(rs, rt, rd, shiftAmt, functionCode):
    instructionArgs = '#'
    # 需要左移2位
    instructionArgs = '#' + str(int(rs + rt + rd + shiftAmt + functionCode+"00", base=2))
    return instructionArgs

# JR
def case_JR(rs, rt, rd, shiftAmt, functionCode):
    instructionArgs = getRegName(rs)
    return instructionArgs






switch={
    'J':case_J,
    'JR':case_JR
}