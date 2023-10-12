#include <iostream>

#define size 5

int main()
{
    int arr[size] = { 5, 4, 3, 2, 1 };
    int temp;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << std::endl;
    }
    
    return 0;
}
