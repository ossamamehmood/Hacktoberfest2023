#include <iostream>
using namespace std;
class Stack
{
    int top = -1;
    char arr[100] = {0};

public:
    bool IsEmpty()
    {
        if (top == -1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool IsFull()
    {
        if (top == (sizeof(arr) / sizeof(arr[0])) - 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    void push(int data) // 1
    {
        if (IsFull())
        {
            cout << "Stack Overflow" << endl;
        }
        else
        {
            top++;
            arr[top] = data;
        }
    }
    char pop()
    { // 2
        if (IsEmpty())
        {
            cout << "Stack Underflow" << endl;
        }
        else
        {
            char popObj = arr[top];
            arr[top] = 0;
            top--;
            return popObj;
        }
    }
    char peek() // 3
    {
        if (IsEmpty())
        {
            cout << "Stack Underflow" << endl;
        }
        else
        {
            cout << endl;
            return arr[top];
        }
    }
    int getSize()
    {
        return top + 1;
    }
    void display() // 4
    {
        if (IsEmpty())
        {
            cout << "No elements added" << endl;
        }
        else
        {
            for (int i = 0; i <= top; i++)
            {
                if (arr[i] == 0)
                {
                    continue;
                }
                else
                {
                    cout << arr[i];
                }
            }
        }
    }
};

bool parenthesisChecker(string s)
{
    Stack st;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{')
        {
            st.push(s[i]);
        }

        else if (s[i] == ')' && !st.IsEmpty() && st.peek() == '(')
        {
            st.pop();
        }
        else if (s[i] == '}' && !st.IsEmpty() && st.peek() == '{')
        {
            st.pop();
        }
        else if (s[i] == ']' && !st.IsEmpty() && st.peek() == '[')
        {
            st.pop();
        }
        else
        {
            return false;
        }
    }

    if (st.IsEmpty())
    {
        return true;
    }
}
int main()
{
    string s;
    cin >> s;

    if (parenthesisChecker(s))
    {
        cout << "Valid" << endl;
    }
    else
    {
        cout << "Not valid" << endl;
    }

    return 0;
}