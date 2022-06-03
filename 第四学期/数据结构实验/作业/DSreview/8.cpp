#include <iostream>
#include <string>
//#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    string s1;
    getline(cin,s1);
    //transform(s1.begin(),s1.end(),s1.begin(),::tolower);
    for (int i=0;i<s1.size();i++)
	    s1[i]=tolower(s1[i]);
    string a,b;
    while(getline(cin,a)){
        b=a;
        //transform(b.begin(),b.end(),b.begin(),::tolower);
        for(int i=0;i<b.size();i++)
			b[i]=tolower(b[i]);
        int t;
        t=b.find(s1);
        while(t!=string::npos){
            a.erase(t,s1.size());
            b.erase(t,s1.size());
            t=b.find(s1);
        }
        t=b.find(" ");
        while (t!=string::npos){
			a.erase(t,1);
			b.erase(t,1);
			t=b.find(" ");
		}
        cout<<a<<endl;
    }
    return 0;
}