class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b = prices[0];
        int p = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < b) {
                b = prices[i];
            } else if (prices[i] - b > p) {
                p = prices[i] - b;
            }
        }
        return p;
    }
};