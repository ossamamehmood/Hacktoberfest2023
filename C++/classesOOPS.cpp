#include <iostream>
using namespace std;

class employee {
public:
	int emp_num;
	float emp_comp;
	employee() {
		emp_num = 0;
		emp_comp = 0;
	}
public:
	void setemp_num(int& a) {
		emp_num = a;
	}
	void setemp_comp(float& b) {
		emp_comp = b;
	}
	void show_data() {

		cout << "employee id" << emp_num;
		cout << "employee compensation" << emp_comp;

	}

};

int main()
{
	employee emp;
	int id[3];
	float comp[3];
	for (int i = 0; i < 3; i++) {
		cout << "enter employees id:" << endl;
		cin >> id[i];
	}
	for (int i = 0; i < 3; i++) {
		cout << "enter employee compensation " << endl;
		cin >> comp[i];

	}
	emp.setemp_num(*id);
	emp.setemp_comp(*comp);



	return 0;
}