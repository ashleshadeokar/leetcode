class Solution:
    def reverse(self, x: int) -> int:
        def recc(n, rev):
            if n == 0:
                return rev
            
            rev = rev * 10 + n % 10
            return recc(n // 10, rev)

        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse_num = recc(x, 0)
        reverse_num *= sign 

        if reverse_num < -( 1 << 31)  or reverse_num > (1 << 31) -1:
            return 0

        return reverse_num
