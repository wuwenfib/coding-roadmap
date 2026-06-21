/*
59. 螺旋矩阵 II
中等
相关标签
premium lock icon
相关企业
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20
*/
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> res;
    res.resize(n);
    for(int i = 0 ; i < n ;i++){
        res[i].resize(n);
    }
    int start_x = 0 ;
    int start_y = 0;
    int idx = 0;
    int x = 1;
    while(idx < n/2){
        for(int i = start_y; i<n-idx-1;i++){
            res[start_x][i]=x++;
        }

        for(int i = start_x;i<n-idx-1;i++){
            res[i][n-idx-1] = x++;
        }

        for(int i = n-idx-1;i>idx;i--){
            res[n-idx-1][i] = x++;
        }

        for(int i = n-idx-1;i>idx;i--){
            res[i][idx]=x++;
        }
        start_x++;
        start_y++;
        idx++;
    }
    if(n%2 == 1){
        res[n/2][n/2] = n*n;
    }
    return res;
    
}

int main(){

    auto res = generateMatrix(5);
    for(auto v : res){
        for(auto d:v){
            std::cout<<d<<" ";
        }
        std::cout<<std::endl;
    }
    std::cout<<endl;
    return 0;
}