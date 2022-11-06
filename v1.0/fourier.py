import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import math



#分段函数：sympy.Piecewise((表达式, 条件)...)
#与运算：sympy.And(...)，注意sympy不可以-1<x<1
#定积分：sympy.integrate(f,(val1,i1,f1)...)

def Fourier(N,type,flag):
    

    # 设置 图像字体信息
    img_font = {'family': 'Microsoft YaHei',
                'size': 12,
                'weight': 'bold',
                }
    plt.legend(loc='upper right')


    # N = 10  # 拟合的阶数

    L = sym.pi  # 周期的一半
    n, x = sym.symbols('n x')  # 创建符号

    

    if type == 1:
        print('下面拟合方波')
        fx = sym.sign(x)  # 创建符号表达式 即要进行傅里叶级数分解的函数， 这里采用的是 符号函数
    elif type == 2:
        print('下面拟合锯齿波')
        fx = x
    elif type == 3:
        fx =  sym.Piecewise((-3*x/sym.pi-3, x < -2*sym.pi/3),(-1,sym.And(x > -2*sym.pi/3,x < -1*sym.pi/3)),(3*x/sym.pi,sym.And(x > -1*sym.pi/3,x < sym.pi/3)),(1,sym.And(x > sym.pi/3,x < 2*sym.pi/3)),(-3*x/sym.pi+3,x > 2*sym.pi/3))                             
        # print(fx)

    elif type == 4:
        fx = sym.Piecewise((x*2/sym.pi, sym.And(x < sym.pi/2,x >-sym.pi/2)),(-x*2/sym.pi+2,x > sym.pi/2),(-x*2/sym.pi-2,x < -sym.pi/2)) 

    elif type == 5:
        fx = abs(sym.cos(x))# 全波整流

        # sym.Piecewise((sym.cos(2*x), x < 0.25*math.pi),(-sym.cos(2*x),x > 0.25*math.pi))

    elif type == 6:
        fx = sym.Piecewise((sym.cos(2*x), x < 0.25*sym.pi),(-sym.cos(2*x),x > 0.25*sym.pi)) # 半波整流

 



    # fx = x

    a0 = (1/(2*L))*sym.integrate(fx, (x, -L, L))
    print(a0)
    an = (1/L)*sym.integrate(fx*sym.cos((n*sym.pi*x)/(L)), (x, -L, L))
    print(an)
    bn = (1/L)*sym.integrate(fx*sym.sin((n*sym.pi*x)/(L)), (x, -L, L))
    print(bn)

    a = []
    b = []
    a.append(a0)
    b.append(0)

    for i in range(1, N):
        a.append(an.subs(n, i))
        b.append(bn.subs(n, i))

    t = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)

    Fx = a0
    for i in range(1, N):
        if a[i] == 0 and b[i] == 0:
            continue
        
        Fx = Fx + a[i]*sym.cos((i*sym.pi*x)/(L)) + b[i]*sym.sin((i*sym.pi*x)/(L))
        if flag == 0:
            for j in t:
                Fx.subs(x, j)
        else:
            y = []
            for j in t:
                y.append(Fx.subs(x, j))



    if flag ==1:
        plt.plot(t, y, linewidth=0.5*(10-j), label='N={}'.format(i))     
    plt.xlabel("x", fontproperties=img_font)
    plt.ylabel("F(x)", fontproperties=img_font, rotation=360)
    plt.grid(alpha=0.5)
    
    if flag != 0:
        plt.show()

    return Fx




    # 图像显示设置

    #plt.title("傅里叶级数拟合正弦函数", fontproperties=img_font)