#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int N,M;
    while(cin>>N>>M){
        int *goldMedalSum=new int[N];
        int *medalSum=new int[N];
        int *population=new int[N];
        double *goldMedalRate=new double[N];
        double *medalRate=new double[N];
        int *countryNumber=new int[M];
        for(int i=0;i<N;i++){
            cin>>goldMedalSum[i];
            cin>>medalSum[i];
            cin>>population[i];
            goldMedalRate[i]=double(goldMedalSum[i])/double(population[i]);
            medalRate[i]=double(medalSum[i])/double(population[i]);
        }
        for(int i=0;i<M;i++)
            cin>>countryNumber[i];
        for(int i=0;i<M;i++){
            int bestRank=M+1;
            int rankingMethod=0;
            int rank[4]={1,1,1,1};
            for(int j=0;j<M;j++){
                if(goldMedalSum[countryNumber[j]]>goldMedalSum[countryNumber[i]])
                    rank[0]++;
                if(medalSum[countryNumber[j]]>medalSum[countryNumber[i]])
                    rank[1]++;
                if(goldMedalRate[countryNumber[j]]>goldMedalRate[countryNumber[i]])
                    rank[2]++;
                if(medalRate[countryNumber[j]]>medalRate[countryNumber[i]])
                    rank[3]++;
            }
            for(int k=0;k<4;k++)
                if(bestRank>rank[k]){
                    bestRank=rank[k];
                    rankingMethod=k+1;
                }
            cout<<bestRank<<":"<<rankingMethod<<endl;
        }
        cout<<endl;
    }   
    return 0;
}