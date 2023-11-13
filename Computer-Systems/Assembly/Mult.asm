// mult r1 and r2, store in r0
@R1
D = M
@mult // used to count multiplication
M = D
@POS
D; JGT
@NEG
D; JLT
@0 // initialise R0 to 0
M = 0

(POS)
(LOOP)
    @mult // if MULT = 0, we break
    D = M 
    M = M - 1 // mult--;
    @END
    D; JEQ // if MULT = 0, break
    @R2
    D = M // get value from R2
    @R0
    M = M + D
@LOOP
0; JMP

(NEG)
(LOOP2)
    @mult
    D = M 
    M = M +1
    @END
    D; JEQ // if MULT = 0 break
    @R2
    D = M 
    @R0
    M = M - D
@LOOP2
0; JMP

(END)
0; JMP // unconditional jump (infinite loop)


