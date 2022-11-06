import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

x,y = sym.symbols('x,y')
y = sym.cos(x)   # 计算对应的 y
# plt.title('y=|x|')    # 图像名称
# plt.xlabel('x')    # x轴标签
# plt.ylabel('y')    # y轴标签
sym.plot(y)
# plt.show()    # 显示图像