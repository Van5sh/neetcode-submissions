class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res=0;
        int minprice=INT_MAX;
        for(int price:prices){
            minprice=min(minprice,price);
            res=max(res,price-minprice);
        }
        return res;
    }
};
