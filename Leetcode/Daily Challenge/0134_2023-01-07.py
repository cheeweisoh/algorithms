class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        """Gas Station

        Args:
            gas (list): gas[i] is the amount of gas at the i-th gas station
            cost (list): cost[i] is the amount of gas to travel from the i-th station to the next (i+1)-th station

        Returns:
            start (int): starting gas station's index if possible to travel the circuit, otherwise -1
        """
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            if tank < 0:
                tank = 0
                start = i + 1
                
        return start