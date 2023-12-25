// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1
// A = M // AD = M 
D = M

@R0 // min value
M = D

@R2 // gets index value
D = M

(LOOP)
@END
D; JEQ 

@R0 
D = M // gets min values

// R1 stores the location of memory
@R1 // holds the index
A = M // gets address of register 20


@R0
D = M

@R1
A = M
D = D - M

@GETMIN
D; JLT

@R1 //index of array
A  = M // changes frame of reference so that we get the value at ram 21 instead of 21
D = M // RAM[21] // changes frame of reference
@R0
M = D

(GETMIN)

@R1 // 20 
M = M + 1 // 20 + 1

@R2
MD = M - 1 

@LOOP // never put another at register after label
0; JMP // unconditional jump

(END)
@END
0; JMP