# mips-simulator

## 任务描述

* 1.载入一个MIPS文件，生成与输入文件等效的汇编代码

* 2.通过指令模拟MIPS代码生成指令。它还应该在执行每个指令后生成/打印寄存器和数据存储器的内容。请参见示例模拟输出文件。
    * sample.txt:输入文件
    * simulation.txt:寄存器和数据存储器的内容变化情况
    * disassembly.txt:汇编代码

## 指令描述
Category-1
|区分指令类别-2位|opcode-4位|same as mips instruction|
| :-------| -------:| :-----:|
|01 | 操作码|同mips指令|


| 指令|编码 |
| :---|---:|
|J|0000|
|JR|0001|
|BEQ| 0010|
|BLTZ|0011|
|BGTZ|0100|
|BREAK|0101|
|SW|0110|
|LW|0111|
|SLL|1000|
|SRL|1001|
|SRA|1010|
|NOP|1011|


Category-2
![](./img/1.png)

| 指令|编码 |
| :---|---:|
|ADD|0000|
|SUB|0001|
|MUL| 0010|
|AND|0011|
|OR|0100|
|XOR|0101|
|NOR|0110|
|SLT|0111|
|ADDI|1000|
|ANDI|1001|
|ORI|1010|
|XORI|1011|
