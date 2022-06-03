#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int ip1a=0,ip1b=0,ip1c=0,ip1d=0;
    int maska=0,maskb=0,maskc=0,maskd=0;
    char ch;
    string inputstr;
    stringstream ss;

    cin>>inputstr;
    ss<<inputstr;
    ss>>ip1a>>ch>>ip1b>>ch>>ip1c>>ch>>ip1d;
    ss.clear();
    ss.str("");

    cin>>inputstr;
    ss<<inputstr;
    ss>>maska>>ch>>maskb>>ch>>maskc>>ch>>maskd;
    ss.clear();
    ss.str("");

    int N;
    cin>>N;
    while(N--){
        int ip2a=0,ip2b=0,ip2c=0,ip2d=0;
        cin>>inputstr;
        ss<<inputstr;
        ss>>ip2a>>ch>>ip2b>>ch>>ip2c>>ch>>ip2d;
        ss.clear();
        ss.str("");
        if(((maska&ip1a)==(maska&ip2a))&&
        ((maskb&ip1b)==(maskb&ip2b))&&
        ((maskc&ip1c)==(maskc&ip2c))&&
        ((maskd&ip1d)==(maskd&ip2d)))
            cout<<"INNER"<<endl;
        else
            cout<<"OUTER"<<endl;
    }
    return 0;
}