#include<iostream>
using namespace std;
int main() {
   int year = 2016;
   if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))
   cout<<year<<" is a leap year";
   else
   cout<<year<<" is not a leap year";
   return 0;
}
