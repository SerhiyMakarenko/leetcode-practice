class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []
        for account in accounts:
            wealth_list.append(sum(account))

        return max(wealth_list)