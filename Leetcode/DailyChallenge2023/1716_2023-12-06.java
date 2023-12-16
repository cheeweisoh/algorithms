class Solution {
    public int totalMoney(int n) {
        int completeWeeks = n / 7;
        int completeWeeksMoney = (completeWeeks * 28) + ((completeWeeks * (completeWeeks - 1) * 7) / 2);

        int remainingDays = n - (completeWeeks * 7);
        int remainingMoney = (completeWeeks + 1) * remainingDays + (remainingDays * (remainingDays - 1)) / 2;

        return completeWeeksMoney + remainingMoney;
    }
}