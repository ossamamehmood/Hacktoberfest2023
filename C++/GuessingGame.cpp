#include <iostream>
using namespace std;

int main(){
      int luckyNum = 7;
      int guess;
      int guessCount = 0;
      int limit = 3;
      bool isLimit = false;

      while(luckyNum != guess && !isLimit){
        if(guessCount < limit){
        cout<<"Enter your guess: ";
        cin>>guess;
        guessCount++;
        }else {
        isLimit = true;
        }
      }
      if(isLimit == true){
        cout<<"You lost"<<endl;
      }else{
      cout<<"You won!"<<endl;
}
     
  return 0;
}




