#include<iostream>
#include<iomanip>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<sstream>
using namespace std;
int main()
{
    char w1[101];
    fgets(w1, sizeof(w1), stdin);
    int p = strlen(w1);
    char* pa = w1;
    for (int i = 0;i < p;i++)
    {
        if (*(pa+i) <= 122 && *(pa+i) >= 97)
        {
            w1[i] = w1[i] - 32;
        }
    }
    cout << w1;
    return 0;
}