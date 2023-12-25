// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//R1 address
// R2 len
// Put your code here.
// implementing BUBBLE SORT

@i
M = 0
@j
M = 0
(OUTERLOOP)
@R2
D = M - 1  // D = len - 1
@i
D = D - M //  len - 1 - i 
@OUTERLOOPEND
D; JLE  // break if i < len - 1
@j 
M = 0
(INNERLOOP)
    @R2
    D = M
    @i // 16
    D = D - M 
    D = D - 1 // len - i - 1
    @j // 17
    D = D - M // len - i - 1 - j > 0 (non jump condition)
@INNERLOOPEND
    D; JLE

    // if (arr[j] > arr[j + 1]))
    @R1
    D = M
    @j
    A = M + D  // holds (base + j)
    D = M  // arr[j]
    @temp
    M = D // temp = arr[j]
    @R1
    D = M
    @j
    A = M + D // get address of arr[j]
    A = A + 1 // arr[j+1]
    D = M // arr[j + 1]
    @temp
    D = D - M  // D = arr[j+1] - arr[j] < 0

    @ENDIF
        D; JGE

        // swap(a[j],a[j+1])
        @j
        D = M
        @R1
        A = M + D
        A = A + 1 
        D = M // arr[j+1]
        A = A - 1
        M = D // arr[j] = arr[j+1]
        A = A + 1
        D = A
        @index //stores address [j+1]
        M = D 
        @temp
        D = M // arr[j]
        @index
        A = M
        M = D // arr[j+1] = temp
    (ENDIF)

@j
M = M + 1 // j++
@INNERLOOP
0; JMP
(INNERLOOPEND)

@i
M = M + 1 // i++
@OUTERLOOP
0; JMP
(OUTERLOOPEND)

// mark -1 when program finises

@R0
M = -1

(END)
@END
0; JMP // jump unconditionallly

