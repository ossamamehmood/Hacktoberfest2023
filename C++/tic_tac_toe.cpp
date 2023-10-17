#include<iostream>
using namespace std;
char ar[3][3]={{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
int k;
bool test=true;
bool *ptr=&test;
string player1,player2;
#include<queue>
queue <int> a;


class Structure 
{
    public:
        Structure()
        {
            
            cout<<"Welcome to Tic Tac Toe game !!"<<endl;
            cout<<"Enter player1 name : "<<endl;
            cin>>player1;
            cout<<endl<<"Enter player2 name : "<<endl;
            cin>>player2;
            cout<<endl<<"The rules for game are same "<<endl;
            cout<<"You have to enter the row and column number to fill your mark"<<endl;
            cout<<"Row count is as 0th row , 1st row , 2nd row whereas "<<endl;
            cout<<"Column count is as 0th column , 1st column , 2nd column "<<endl;
            cout<<endl<<endl<<"Press any key and then enter to start the game. "<<endl;
            cin>>k;


        }
        void draw()
    {
        cout<<"Here is the sample ";
        cout<<"\n\n";
        cout<<endl<<"\t\t";

        for (int i=1;i<10;i++)
        {
            cout<<" "<<i<<' '<<'|';

            if (i%3==0)
            {
                cout<<endl<<"\t\t";
                cout<<"--------------"<<endl;
                cout<<"\t\t";
            }   
        }
    }  
};

class Mark :public Structure
{
    public:
    int r=0,c=0;
        void drawmark()
        {
            
            cout<<endl<<player1<<"'s turn "<<endl;
            cout<<endl<<"Enter row and column number "<<endl;
            cin>>r>>c;
            cout<<" "<<r<<" "<< c<<" ";
            cout<<"\n\n";
            cout<<endl<<"\t\t";
            for (int i=0;i<3;i++)
                {
                    for (int j=0;j<3;j++)
                    {
                        cout<<" "<<ar[i][j]<<' '<<'|';
                    } 
                    cout<<endl<<"\t\t";
                    cout<<"------------"<<endl;
                    cout<<"\t\t";    
                }
        }
        void drawmark1()
        {
            
            cout<<endl<<player2<<"'s turn "<<endl;
            cout<<endl<<"Enter row and column number "<<endl;
            cin>>r>>c;
            cout<<"2 "<<r<<" "<<c<<" ";

            ar[r][c]='o';
            cout<<"\n\n";
            cout<<endl<<"\t\t";
            for (int i=0;i<3;i++)
                {
                    for (int j=0;j<3;j++)
                    {
                        cout<<" "<<ar[i][j]<<' '<<'|';
                    } 
                    cout<<endl<<"\t\t";
                    cout<<"------------"<<endl;
                    cout<<"\t\t";    
                }
        }
};

class Check : public Mark
{
    public:
        void owin()
        {cout<<"owr";
            if ((ar[0][0]=='*'&& ar[0][1]=='*'&&ar[0][2]=='*') || (ar[1][0]=='*'&& ar[1][1]=='*'&&ar[1][2]=='*') || (ar[2][0]=='*'&& ar[2][1]=='*'&&ar[2][2]=='*') || (ar[0][0]=='*'&& ar[1][0]=='*'&&ar[2][0]=='*') || (ar[0][1]=='*'&& ar[1][1]=='*'&&ar[2][1]=='*') || (ar[0][0]=='*'&& ar[1][0]=='*'&&ar[2][0]=='*') || (ar[2][0]=='*'&& ar[1][1]=='*'&&ar[0][2]=='*') || (ar[0][0]=='*'&& ar[1][1]=='*'&&ar[2][2]=='*'))
            {
                cout<<endl<<player1<<" win the game";
                *ptr=false;
            }
        }
        void twin()
        {cout<<"twr";
            if ((ar[0][0]=='o'&& ar[0][1]=='o'&&ar[0][2]=='o') || (ar[1][0]=='o'&& ar[1][1]=='o'&&ar[1][2]=='o') || (ar[2][0]=='o'&& ar[2][1]=='o'&&ar[2][2]=='o') || (ar[0][0]=='o'&& ar[1][0]=='o'&&ar[2][0]=='o') || (ar[0][1]=='o'&& ar[1][1]=='o'&&ar[2][1]=='o') || (ar[0][0]=='o'&& ar[1][0]=='o'&&ar[2][0]=='o') || (ar[2][0]=='o'&& ar[1][1]=='o'&&ar[0][2]=='o') || (ar[0][0]=='o'&& ar[1][1]=='o'&&ar[2][2]=='o'))
            {
                cout<<endl<<player2<<" win the game";
                *ptr=false;
            }
        }

};

int main()
{
    
    Check obj;
    obj.draw();
    k=1;
    while(k!=5)
    {
            obj.drawmark();
            obj.owin();
            obj.drawmark1();
            obj.twin();
        
        k++;
    }
    
    return 0;
}