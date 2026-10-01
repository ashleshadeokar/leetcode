class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_bill, ten_bill = 0, 0
        for b in bills:
            if b == 5:
                five_bill += 1
            elif b == 10:
                five_bill, ten_bill = five_bill - 1, ten_bill + 1
            elif ten_bill > 0:
                five_bill, ten_bill = five_bill - 1, ten_bill - 1
            else:
                five_bill -= 3
            if five_bill < 0:
                return False
        return True