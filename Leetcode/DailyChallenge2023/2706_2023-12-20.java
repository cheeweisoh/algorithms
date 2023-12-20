class Solution {
    public int buyChoco(int[] prices, int money) {
        int chocoOne = Math.min(prices[0], prices[1]);
        int chocoTwo = Math.max(prices[0], prices[1]);

        for (int i = 2; i < prices.length; i++) {
            if (prices[i] <= chocoOne) {
                chocoTwo = chocoOne;
                chocoOne = prices[i];
            }
            else if (prices[i] < chocoTwo) {
                chocoTwo = prices[i];
            }
        }

        int leftover = money - chocoOne - chocoTwo;
        
        if (leftover >= 0) {
            return leftover;
        }
        else {
            return money;
        }
    }
}