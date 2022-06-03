#include <iostream>
using namespace std;
 
int main(){
    int N, M;
    while(cin >> N >> M){
        int *goldMedal = new int[N];
        int *medal = new int[N];
        int *population = new int[N];
        double *goldMedalRate = new double[N];
        double *medalRate = new double[N];
        int *country = new int[M];
        for(int i=0; i<N; i++){
            cin >> goldMedal[i];
            cin >> medal[i];
            cin >> population[i];
            goldMedalRate[i] = (double) goldMedal[i] / (double) population[i];
            medalRate[i] = (double) medal[i] / (double) population[i];
        }
        for(int i=0; i<M; i++){
            cin >> country[i];
        }
        //计算排名
        for(int i=0; i<M; i++){
            int bestRanking = M + 1;
            int rankingMethod = 0;
            int ranking[4] = {1, 1, 1, 1};
            for(int j=0; j<M; j++){
                if(goldMedal[country[j]] > goldMedal[country[i]])
                    ranking[0] ++;
                if(medal[country[j]] > medal[country[i]])
                    ranking[1] ++;
                if(goldMedalRate[country[j]] > goldMedalRate[country[i]])
                    ranking[2] ++;
                if(medalRate[country[j]] > medalRate[country[i]])
                    ranking[3] ++;
            }
            for(int k=0; k<4; k++){
                if(bestRanking > ranking[k]){
                    bestRanking = ranking[k];
                    rankingMethod = k + 1;
                }
            }
            cout << bestRanking << ':' << rankingMethod << endl;
        }
        cout << endl;
    }
 
    return 0;
}