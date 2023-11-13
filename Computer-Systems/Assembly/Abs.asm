// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)
// Put your code here.

    @R1
    // get number in R1
    D = M
    // test if positive
    @POS 
    D; JGE
    // otherwise invert D
    D = -D
(POS)
    @0
    M = D
(END)
    @END    
    0; JMP
