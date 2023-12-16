class Solution:
	def maxIceCream(self, costs: list, coins: int) -> int:
		"""Maximum Ice Cream Bars
  
        Args:
            costs (list): costs of ice cream bars, where costs[i] is the price of the i-th ice cream bar
            coins (int): coins to spend

        Returns:
            count (int): maximum number of ice cream bars that can be bought
		"""          
		costs.sort()
		count = 0
		for i in range(len(costs)):
			coins -= costs[i]
			
			if coins < 0:
				break
			else:
				count += 1
				
		return count