
#include<bits/stdc++.h>
using namespace std;

class BIT{
public:
    int size;
    vector<int> v;
    BIT(int s) {
        size = s;
        v.resize(s, 0);
    }
    void update(int i, int delta) {
        while(i < size) {
            v[i] += delta;
            i += i & (-i);
        }
    }
    int sum(int i) {
        int s = 0;
        while(i > 0) {
            s += v[i];
            i -= i & (-i);
        }
        return s;
    }
};

int main(){
    BIT* t = new BIT(1001);
    t->update(1, 3);
    t->update(4, 2);
    t->update(2, 1);
    cout << t->sum(3) << endl;
}


