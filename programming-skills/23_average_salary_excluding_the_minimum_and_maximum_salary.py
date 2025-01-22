class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_salary = sorted(salary)
        low_max_salary = sorted_salary[1:-1]
        calclated_salary = sum(low_max_salary) / len(low_max_salary)
        return float(calclated_salary)