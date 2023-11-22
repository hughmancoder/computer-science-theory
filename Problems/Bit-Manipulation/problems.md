# Bit Manipulation

## 5.1 Insertion

**Problem:** Given two 32-bit numbers, N and M, and two bit positions, i and j, write a method to insert M into N such that M starts at bit j and ends at bit i. Assume that the bits j through i have enough space to fit all of M.

**Example:**  
Input: N = 10000000000, M = 10011, i = 2, j = 6  
Output: N = 10001001100

## 5.2 Binary to String

**Problem:** Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR."

## 5.3 Flip Bit to Win

**Problem:** You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.

**Example:**  
Input: 1775 (or 11011101111)  
Output: 8

## 5.4 Next Number

**Problem:** Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.

## 5.5 Debugger

**Problem:** Explain what the following code does: `((n & (n - 1)) == 0)`.

## 5.6 Conversion

**Problem:** Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

**Example:**  
Input: 29 (or 11101), 15 (or 01111)  
Output: 2

## 5.7 Pairwise Swap

**Problem:** Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 9 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc.).

## 5.8 Draw Line

**Problem:** A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. Implement a function that draws a horizontal line from (x1, y) to (x2, y) on the screen. The screen has width w, divisible by 8.

**Method Signature:** `drawLine(byte[] screen, int width, int x1, int x2, int y)`
