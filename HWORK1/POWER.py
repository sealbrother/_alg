pow = [None] * 10000  
pow[0] = 1  

def power2n_d(n):
    if n < 0:  
        raise ValueError("n 必須是非負整數")
    if pow[n] is not None: 
        return pow[n]
    pow[n] = 2 * power2n_d(n - 1)  
    return pow[n]
print('power2n_d(0) =', power2n_d(0))  # 1
print('power2n_d(5) =', power2n_d(5))  # 32
print('power2n_d(10) =', power2n_d(10))  # 1024
print('power2n_d(25) =', power2n_d(25))  # 33554432
print('power2n_d(40) =', power2n_d(40))  # 1099511627776