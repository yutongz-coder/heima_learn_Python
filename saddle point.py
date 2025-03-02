import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 定义系统的方程
def predator_prey(vars, p, alpha, beta, r, K, d):
    x, y = vars
    dxdt = r * x * (1 - x / K) - (alpha * x * y) / (1 + beta * x)
    dydt = -d * y + (alpha * x * y) / (1 + beta * x)
    return [dxdt, dydt]

# 平衡点分析：解系统的方程
def find_equilibria(p, alpha, beta, r, K, d):
    # 定义方程组
    def equations(vars):
        x, y = vars
        eq1 = r * x * (1 - x / K) - (alpha * x * y) / (1 + beta * x)
        eq2 = -d * y + (alpha * x * y) / (1 + beta * x)
        return [eq1, eq2]

    # 使用 fsolve 求解平衡点
    eqs = fsolve(equations, [1.0, 1.0])  # 假设初始猜测为 [1.0, 1.0]
    return eqs

# 系统参数设置
r = 1.0
K = 10.0
alpha = 0.5
beta = 0.1
d = 0.1

# 计算不同 p (资源增长率 r) 下的平衡点
p_values = np.linspace(0.5, 2.0, 100)  # 改变 r 作为控制参数
equilibria = []

for p in p_values:
    eq = find_equilibria(p, alpha, beta, r, K, d)
    equilibria.append(eq)

equilibria = np.array(equilibria)

# 绘制丰度随参数变化的图（分叉图）
plt.figure(figsize=(8, 6))
plt.plot(p_values, equilibria[:, 0], label="Prey abundance (x)", color="blue")
plt.plot(p_values, equilibria[:, 1], label="Predator abundance (y)", color="red")
plt.xlabel('Parameter p (growth rate r)')
plt.ylabel('Abundance')
plt.title('Bifurcation Diagram')
plt.legend()
plt.grid(True)
plt.show()
