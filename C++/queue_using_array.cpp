#include<iostream>
#include<vector>
using namespace std;
class Menu{
    protected:
        int n,elem,i;
        vector<int> vec;

    public:
       void menu(){
            cout<<endl<<"Choose an option "<<endl;
            cout<<"1. Add an element. "<<endl;
            cout<<"2. Remove an element. "<<endl;
            cout<<"3. Return queue. "<<endl;
            cout<<"4. Exit. "<<endl;
            cin>>n;

    }
};
class Flow :public Menu{
    public:
        void work();
        void add()
        {
            cout<<"enter element to add :"<<endl;
            cin>>elem;
            vec.push_back(elem);
        }
        void remove();
        void print();
        

};
void Flow :: remove(){
            if (vec.size()==0)cout<<"queue is empty. "<<endl;
            else {
                for (i=1;i<=vec.size();i++){
                    if (i==vec.size())
                    {
                        vec.pop_back();
                        break;
                    }

                    vec[i-1]=vec[i];
                }
                

            }
        }
void Flow :: print(){
    cout<<endl<<endl;
    for (i=0;i<vec.size();i++){
        cout<<vec[i]<<" ";
    }
    cout<<endl<<endl<<endl;

}
void Flow:: work(){
    n=6;
    while(n!=4){
        menu();
        if (n==1) add();
        else if (n==2) remove();
        else if (n==3) print();
        else if (n==4) break;
        else cout<<"enter valid option. "<<endl;
    }
}
int main(){
    Flow object;
    object.work();
    return 0;
}