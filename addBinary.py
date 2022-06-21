class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            base = x ^ y
            carry = (x & y) << 1
            x, y = base, carry
            print(1)
        return bin(x)[2:]
    
#space 0(max(N,M)) to keep the answer
#time o(N+ M) time conversersion for ints to bin 
