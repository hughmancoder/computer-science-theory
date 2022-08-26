#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;

class Karatsuba
{
public:
    std::string schoolAddition(std::string a, std::string b, int B);
    std::string schoolSubtraction(std::string a, std::string b, int B);
    std::string singleDigitMultiplication(std::string a, std::string b, int B);
    std::string partialProduct(std::string a, char b, int B);
    std::string karatsuba(std::string a, std::string b, int B);
    std::string DecimalMultiplication(std::string a, std::string b, int B);
    std::string schoolMultiplication(std::string a, std::string b, int B);
    std::string removeLeadingZeros(std::string s);
    void alignNumbers(std::string &a, std::string &b);
    int toDecimal(std::string S, int B);
    int division(std::string a, std::string b, int B);
};

int main()
{
    Karatsuba k;
    std::string a, b;
    int B;
    std::cin >> a >> b >> B;

    /*
    cout << k.schoolAddition(a, b, B) << endl;
    cout << k.schoolSubtraction(a, b, B) << endl;
    
    cout << "school multiplication" << endl;
    cout << " " << k.schoolMultiplication(a, b, B) << endl;

    cout << "karatsuba multiplication" << endl;
    string mult = k.karatsuba(a, b, B);
    cout << mult << endl;

    cout << "cleaned output" << endl;
    cout << k.removeLeadingZeros(mult) << endl;
    */
    
    std::cout << k.schoolAddition(a, b, B) << " "
              << k.removeLeadingZeros(k.karatsuba(a, b, B)) << " "
              << k.division(a, b, B);

    return 0;
}

std::string Karatsuba::removeLeadingZeros(std::string s)
{
    int i = 0;
    for (i = 0; i < s.size(); i++)
    {
        if (s[i] != '0')
        {
            break;
        }
    }
    return s.substr(i, s.size());
}

void Karatsuba::alignNumbers(std::string &a, std::string &b)
{
    int len_A = a.length(), len_B = b.length();
    int dif = abs(len_A - len_B);

    if (len_A > len_B) // align numbers by padding front
    {
        b = std::string(dif, '0') + b;
    }
    else
    {
        a = std::string(dif, '0') + a;
    }
}

// School Method for Integer Addition
std::string Karatsuba::schoolAddition(std::string a, std::string b, int Base)
{
    std::string sum = "";
    int temp = 0; // current addition result
    int carry = 0;
    int A, B;
    alignNumbers(a, b);

    while (a.size() > 0 and b.size() > 0)
    {
        A = a[a.size() - 1] - '0';
        B = b[b.size() - 1] - '0';

        temp = carry + A + B;
        carry = temp / Base;
        temp = temp % Base;

        // prepend calculation to sum
        sum = char(temp + '0') + sum;

        // move on
        a.pop_back();
        b.pop_back();
    }

    // check for carry overflow
    if (carry > 0)
    {
        sum = char(carry + '0') + sum;
    }

    return sum;
}

std::string Karatsuba::schoolSubtraction(std::string a, std::string b, int Base)
{
    // a - b, both numbers are assumed to be positive
    if (b.length() > a.length())
    {
        std::swap(a, b);
    }

    alignNumbers(a, b);
    std::string sub;
    int temp = 0; // subtraction result
    int carry = 0;
    int A, B; // two digits respectively

    while (a.size() > 0 and b.size() > 0)
    {
        A = a[a.size() - 1] - '0';
        B = b[b.size() - 1] - '0';
        temp = A - B + carry;

        if (temp < 0)
        {
            carry = -1;
            temp += Base;
        }
        else
        {
            carry = 0;
        }
        // add to front

        sub = char(temp + '0') + sub;

        a.pop_back();
        b.pop_back();
    }
    return sub;
}

// convert a number from given base to base 10
int Karatsuba::toDecimal(std::string S, int B)
{
    int n = S.length();
    int pow = 1, res = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        // only works up to base 10
        res += (S[i] - '0') * pow;
        pow *= B;
    }
    return res;
}

std::string Karatsuba::partialProduct(std::string a, char b, int base)
{
    std::string res = "";
    int digit;
    int temp;
    int carry = 0;
    int multiplicand = b - '0';

    for (int i = a.length() - 1; i >= 0; i--)
    {
        temp = (a[i] - '0') * multiplicand + carry;

        carry = temp / base;
        digit = temp % base;
        res = char(digit + '0') + res;
    }
    if (carry > 0)
    {
        res = char(carry + '0') + res;
    }
    return res;
}

std::string Karatsuba::schoolMultiplication(std::string a, std::string b, int base)
{
    int n = b.size();
    std::string offset = "";
    std::string res = "";
    std::string temp = "";
    for (int i = n - 1; i >= 0; i--)
    {
        temp = partialProduct(a, b.at(i), base) + offset;
        offset += "0";
        res = schoolAddition(res, temp, base);
    }
    return res;
}

// Karatsuba Algorithm for Integer Multiplication
std::string Karatsuba::karatsuba(std::string a, std::string b, int B)
{
    int n = std::max(a.size(), b.size());

    alignNumbers(a, b);

    // cout << a << " " << b << endl;

    if (n < 4)
    {
        return schoolMultiplication(a, b, B);
    }

    int k = n / 2;

    // high and low bits
    std::string a_h = a.substr(0, k);
    std::string a_l = a.substr(k, a.size());

    std::string b_h = b.substr(0, k);
    std::string b_l = b.substr(k, b.size());

    // let p1, p2, p3 , p4 denote the parts of karatsuba multiplication
    std::string p1 = karatsuba(a_h, b_h, B) + string(2 * (n - k), '0');
    std::string p2 = karatsuba(schoolAddition(a_h, a_l, B), schoolAddition(b_h, b_l, B), B);
    std::string p3 = schoolAddition(karatsuba(a_h, b_h, B), karatsuba(a_l, b_l, B), B);
    std::string p4 = karatsuba(a_l, b_l, B);

    // evaluating parts
    std::string p2_p3 = schoolSubtraction(p2, p3, B) + string((n - k), '0');

    // cout << p1 << " " << p2_p3 << " " << p4 << endl;

    // add all parts to compute p1 + p2_p3 + p4
    return schoolAddition(schoolAddition(p1, p2_p3, B), p4, B);
}

// postgraduate only
int Karatsuba::division(std::string a, std::string b, int B)
{
    return 0;
}

// converts multiplication in given base to base 10 (unused)
std::string Karatsuba::DecimalMultiplication(std::string a, std::string b, int B)
{
    // we evaluate normally
    int i1, i2;
    if (B != 10)
    {
        i1 = toDecimal(a, B);
        i2 = toDecimal(b, B);
    }
    else
    {
        i1 = stoi(a);
        i2 = stoi(b);
    }
    return std::to_string(i1 * i2);
}