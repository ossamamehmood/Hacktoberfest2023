#include<iostream>
using namespace std;

class Hacktober
{
	private:
		int a;
	
	public:
		Hacktober()
		{
			a=0;
		}
		Hacktober(int a)
		{
			this->a=a;
		}
		Hacktober operator ++ ()
		{
			++a;
			return Hacktober(a);
		}
		void display()
		{
			cout << a;
		}
};

int main()
{
	Hacktober obj,obj2;
	obj2 = ++obj;
	obj2.display();
	
	return 0; 
}
