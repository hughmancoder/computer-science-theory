/*
 C++ program to print the digitalRoot
The digital root of 12345 is 6, since 1+2+3+4+5 = 15, and 1+5 = 6
*/

#include <iostream>
#include <string>
using namespace std;

int digitalRoot(int number)
{
    if (number <= 0) return 0;
    if (number > 0 and number <= 9)
    {
        return number;
    }
    int sum = 0;
    while (number) // extract all digits from number
    {
        sum += number % 10;
        number /= 10;
    }
    return digitalRoot(sum);
}

int main()
{
    int num = 12345;

    cout << "digital root is: ";
    cout << digitalRoot(num);
}

