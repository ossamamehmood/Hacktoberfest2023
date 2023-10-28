#include <iostream> //using std:: as its a better practice
int main(){
    
    int previous=0; //Initialize the first number in the sequence
    int current=0; //Initialize the second number in the sequence

    std::cout<<previous<<std::endl<<current<<std::endl;
    for (int i = 2; i < 10; i++){
        int next = previous+current;
        std::cout<<next<<std::endl;
        previous=current;
        current=next;   //updating values after each iteration
    }

    return 0;
}