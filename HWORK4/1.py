import numpy as np
def riemann_integral(f, nx, ny, nz):
    #檢查
    if nx <= 0 or ny <= 0 or nz <= 0:
        raise ValueError("nx, ny, and nz must be positive integers.")
    dx = 1 / nx
    dy = 1 / ny
    dz = 1 / nz
    integral = 0.0
    #中點積分法
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                integral += f(x, y, z) * dx * dy * dz
    return integral
if __name__ == "__main__":
    #動態
    print("請輸入函數 f(x, y, z) (例如 '3*x**2 + y**2 + 2*z**2'):")
    func_input = input("f(x, y, z) = ")
    f = lambda x, y, z: eval(func_input) #動態函數
    try:
        nx, ny, nz = 100, 100, 100  
        result = riemann_integral(f, nx, ny, nz)
        print(f"黎曼積分法結果 (nx={nx}, ny={ny}, nz={nz}): {result}")
    except Exception as e:
        print(f"發生錯誤: {e}")