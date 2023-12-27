// and01 VM Test file; does not compare, but generates a .cmp file for the given .vm file
// Run using VMEmulator

load and01.vm,
output-file and01.cmp,
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

repeat 2 {        // Change this number to cover the number of instructions in the VM test file
  vmstep;
}

output;
    