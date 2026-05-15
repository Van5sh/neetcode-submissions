class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res=0;
        for(int i=0;i<prices.size();i++){
            for(int j=i;j<prices.size();j++){
                if(prices[i]<prices[j]){
                    res=max(res,abs(prices[i]-prices[j]));
                }
            }
        }
        return res;
    }
};
