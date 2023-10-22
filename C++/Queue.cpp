#include <iostream>
// #include <queue>
using namespace std;

class queue{

    public:
    int* arr;
    int qfront ;
    int rear ;
    int size ;

    queue(){
        size = 100001;
        arr = new int[size];
        qfront = 0;
        rear = 0;
    }

    // PUSH / INSERT
    void enqueue(int data){
        if (rear == size)
        {
            cout << " QUEUE IS FULL ";
        }
        else{
            arr[rear] = data ;
            rear++ ;
        }
    }

    // POP
    int dequeue(){
        if (qfront == rear)
        {
           return -1;
        }
        else{
            int ans = arr[qfront];
            arr[qfront] = -1 ;
            qfront++;
            if (qfront == rear)
            {
                qfront=0;
                rear=0;
            } 
            return ans; 
        }
    }

    // FRONT
   int qwfront(){
        if (qfront == rear)
        {
            return -1;
        }
        else{     
            return arr[qfront];
        }
    }

    // CHECK EMPTY
    bool isEmpty(){
        if (qfront == rear)
        {
          return 1;
        }
        return 0;
    }


};

int main(){

    // queue <int> q;
    // q.push(1);
    // q.push(2);
    // q.push(3);
    // q.push(4);
    // q.push(5);

    // // while (!q.empty())
    // // {
    // //    int s = q.front();
    // //    cout << s << " ";
    // //    q.pop();
    // // }
    // cout << q.size() << endl;
    // cout << q.front() << endl ;
    // cout << q.back() << endl ;

queue q;
 
 q.enqueue(1);
  q.enqueue(2);
   q.enqueue(3);
    q.enqueue(4);
     q.enqueue(5);


    cout << q.qwfront() << endl;
    cout << q.qfront << endl;
    // cout << q.dequeue()<<endl;

   while (!q.isEmpty())
    {
       int s = q.qwfront() ;
       cout << s << " ";
       q.dequeue();
    }

    return 0;
}


// #include<iostream>
// using namespace std;
// #define size 10
// class queue{
//     public:
//     int arr[size];
//     int front;
//     int rear;

//     queue(){
//         front=rear=0;
//     }

//     bool isEmpty(){
//         if (front == rear)
//         {
//         return 1;
//         }
//         return 0;
//     }

//     void enqueue(int val){
//         if (rear == size)
//         {
//             cout << "Queue is Full "<<endl;
//         }else{
//             arr[rear] = val;
//             rear++;
//         }    
//     }

//     int dequeue(){
//         if (isEmpty())
//         {
//             return -1;
//         }
//         else{
//             int val = arr[front];
//             if(front > rear){
//                 front = rear = 0;
//             }else{
//                 front++;
//             }
//             return val;
//         }
//     }


//     int qwfront(){
//         if (front == rear)
//         {
//             return -1;
//         }
//         else{     
//             return arr[front];
//         }
//     }

//     void displayQueue()
//     { 
//         int i;
//         if(isEmpty()) {
//             cout << endl << "Queue is Empty!!" << endl;
//         }
//         else {
//             for(i=front; i<=rear-1; i++)
//             cout << arr[i] << " ";
//         }
//     }


// };

// int main(){

// queue q;
 
//  q.enqueue(1);
//   q.enqueue(2);
//    q.enqueue(3);
//     q.enqueue(4);
//      q.enqueue(5);
//      q.dequeue();

//     q.displayQueue();



//     return 0;
// }