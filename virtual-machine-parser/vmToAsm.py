import os
from VMTranslator import VMTranslator

# automated test scripts
testDirectory = "tests"

def toAsmTest(name, ticks):
    return """// {name} Test file; compares with the results from generated from the VM test file.
// Run using CPUEmulator

load {name}.asm,
output-file {name}.out,
compare-to {name}.cmp,
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[2]%D1.6.1 RAM[3]%D1.6.1 RAM[4]%D1.6.1
            RAM[256]%D1.6.1 RAM[257]%D1.6.1 RAM[258]%D1.6.1
            RAM[300]%D1.6.1 RAM[301]%D1.6.1
            RAM[400]%D1.6.1 RAM[401]%D1.6.1 
            RAM[3000]%D1.6.1 RAM[3001]%D1.6.1
            RAM[3010]%D1.6.1 RAM[3011]%D1.6.1;

set RAM[0] 256,     // stack pointer
set RAM[1] 300,     // base address of the local segment
set RAM[2] 400,     // base address of the argument segment
set RAM[3] 3000,    // base address of the this segment
set RAM[4] 3010,    // base address of the that segment

repeat {ticks} {{    // Change this number to cover the number of instructions in the asm test file
    ticktock;
}}

output;
    """.format(name=name, ticks=ticks)

def toVMTest(name, ticks):
    return """// {name} VM Test file; does not compare, but generates a .cmp file for the given .vm file
// Run using VMEmulator

load {name}.vm,
output-file {name}.cmp,
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[2]%D1.6.1 RAM[3]%D1.6.1 RAM[4]%D1.6.1
            RAM[256]%D1.6.1 RAM[257]%D1.6.1 RAM[258]%D1.6.1
            RAM[300]%D1.6.1 RAM[301]%D1.6.1
            RAM[400]%D1.6.1 RAM[401]%D1.6.1 
            RAM[3000]%D1.6.1 RAM[3001]%D1.6.1
            RAM[3010]%D1.6.1 RAM[3011]%D1.6.1;

set RAM[0] 256,     // stack pointer
set RAM[1] 300,     // base address of the local segment
set RAM[2] 400,     // base address of the argument segment
set RAM[3] 3000,    // base address of the this segment
set RAM[4] 3010,    // base address of the that segment

repeat {ticks} {{        // Change this number to cover the number of instructions in the VM test file
  vmstep;
}}

output;
    """.format(name=name, ticks=ticks)


for filename in os.listdir(testDirectory):
    split = filename.split(".")
    if len(split) > 1 and split[1] == "vm" and split[0] != "ExampleTest":
        
        with open(testDirectory + "/" + filename, 'r') as originFile:
            with open(testDirectory + "/" + split[0] + ".asm", 'w') as f:
                end = "\n(END)\n@END\n0;JMP"
                f.writelines([VMTranslator.vmLineToAsm(line) for line in originFile] + [end])

        with open(testDirectory + "/" + filename, 'r') as originFile:
            with open(testDirectory + "/" + split[0] + "VM.tst", 'w') as f:
                f.write(toVMTest(split[0], len(originFile.readlines())))
        
        with open(testDirectory + "/" + split[0] + ".asm", 'r') as code:
            with open(testDirectory + "/" + split[0] + "Asm.tst", 'w') as f:
                f.write(toAsmTest(split[0], len(code.readlines())))
