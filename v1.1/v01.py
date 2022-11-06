from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def Fourier(N,type,flag):
    

    img_font = {'family': 'Microsoft YaHei',
                'size': 12,
                'weight': 'bold',
                }
    plt.legend(loc='upper right')

    L = sym.pi  # 周期的一半
    n, x = sym.symbols('n x')  # 创建符号

    if type == 1:
        print('下面拟合方波')
        fx = sym.sign(x)  
    elif type == 2:
        print('下面拟合锯齿波')
        fx = x
    elif type == 3:
        print('下面拟合梯形波')
        fx =  sym.Piecewise((-3*x/sym.pi-3, x < -2*sym.pi/3),(-1,sym.And(x > -2*sym.pi/3,x < -1*sym.pi/3)),(3*x/sym.pi,sym.And(x > -1*sym.pi/3,x < sym.pi/3)),(1,sym.And(x > sym.pi/3,x < 2*sym.pi/3)),(-3*x/sym.pi+3,x > 2*sym.pi/3))
    elif type == 4:
        print('下面拟合三角波')
        fx = sym.Piecewise((x*2/sym.pi, sym.And(x < sym.pi/2,x >-sym.pi/2)),(-x*2/sym.pi+2,x > sym.pi/2),(-x*2/sym.pi-2,x < -sym.pi/2))
    elif type == 5:
        print('下面拟合全波整流')
        fx = abs(sym.sin(x)) 
    elif type == 6:
        print('下面拟合半波整流')
        fx = sym.Piecewise((sym.sin(x), sym.And(x < sym.pi,x > 0)),(0,sym.And(x > -sym.pi,x < 0))) 

    a0 = (1/(2*L))*sym.integrate(fx, (x, -L, L))
    window2.BarValue(1)
    print(a0)
    an = (1/L)*sym.integrate(fx*sym.cos((n*sym.pi*x)/(L)), (x, -L, L))
    window2.BarValue(2)
    bn = (1/L)*sym.integrate(fx*sym.sin((n*sym.pi*x)/(L)), (x, -L, L))
    window2.BarValue(3)

    a = []
    b = []
    a.append(a0)
    b.append(0)

    for i in range(1, N):
        a.append(an.subs(n, i))
        b.append(bn.subs(n, i))
    window2.BarValue(4)

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
    window2.BarValue(5)

    if flag ==1:
        plt.plot(t, y, linewidth=0.5*(10-j), label='N={}'.format(i))     
    plt.xlabel("x", fontproperties=img_font)
    plt.ylabel("F(x)", fontproperties=img_font, rotation=360)
    plt.grid(alpha=0.5)
    
    if flag != 0:
        plt.show()
    window2.BarValue(6)

    return Fx
number = 0
class Main_01:
    type=0

    def __init__(self):

        self.ui = QUiLoader().load('01.ui')

        self.ui.FB_Button.setIcon(QIcon('方波.png'))
        self.ui.FB_Button.setIconSize(QSize(100, 100))

        self.ui.JC_Button.setIcon(QIcon('锯齿波.png'))
        self.ui.JC_Button.setIconSize(QSize(100, 100))

        self.ui.TX_Button.setIcon(QIcon('梯形波.png'))
        self.ui.TX_Button.setIconSize(QSize(100, 100))

        self.ui.SJ_Button.setIcon(QIcon('三角波.png'))
        self.ui.SJ_Button.setIconSize(QSize(100, 100))

        self.ui.QB_Button.setIcon(QIcon('全波整流.png'))
        self.ui.QB_Button.setIconSize(QSize(100, 100))

        self.ui.BB_Button.setIcon(QIcon('半波整流.png'))
        self.ui.BB_Button.setIconSize(QSize(100, 100))

        self.ui.FB_Button.clicked.connect(self.handle_FB)

        self.ui.JC_Button.clicked.connect(self.handle_JC)

        self.ui.TX_Button.clicked.connect(self.handle_TX)

        self.ui.SJ_Button.clicked.connect(self.handle_SJ)

        self.ui.QB_Button.clicked.connect(self.handle_QB)

        self.ui.BB_Button.clicked.connect(self.handle_BB)


    def handle_FB(self):
        self.type = 1
        open_new_window()
        self.ui.close()

    def handle_JC(self):
        self.type = 2
        open_new_window()
        self.ui.close()

    def handle_TX(self):
        self.type = 3
        open_new_window()
        self.ui.close()

    def handle_SJ(self):
        self.type = 4
        open_new_window()
        self.ui.close()

    def handle_QB(self):
        self.type = 5
        open_new_window()
        self.ui.close()

    def handle_BB(self):
        self.type = 6
        open_new_window()
        self.ui.close()

def open_new_window():
    
    # 显示新窗口
    window2.ui.show()
    app.exec_()
        
class Window_02:
   
    def __init__(self):

        x = sym.symbols('x')
        self.ui = QUiLoader().load('02_1.1.ui')

        self.ui.ani_Button.clicked.connect(self.cal)
        self.ui.displayfx_Button.clicked.connect(self.handle_display_fx)

        self.ui.progressBar.setRange(0,5)

        self.F = x

    def cal(self):

        number = self.ui.Spin_N.value()
        # print(Main_01.type,number)
        Fourier(number,Main_01.type,1)

        
    def BarValue(self,i):
        self.ui.progressBar.setValue(i)
        
    def handle_display_fx(self):

        number = self.ui.Spin_N.value()

        self.F = Fourier(number,Main_01.type,0)
        self.ui.textEdit.setPlainText(str(self.F))
        print('Fx:',str(self.F))


if __name__ == '__main__':

    app = QApplication([])
 
    app.setWindowIcon(QIcon('应用图标.png'))
    Main_01 = Main_01()
    window2 = Window_02()
    Main_01.ui.show()
    app.exec_()



