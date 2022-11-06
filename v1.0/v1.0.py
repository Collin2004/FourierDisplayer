import fourier
import sympy as sym
import numpy as np
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon

number = 0
class Main_01:
    type=0

    

    def __init__(self):

        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
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



        

    def open_new_window(self):
        # 实例化另外一个窗口
        self.window2 = Window_02()
        # 显示新窗口
        self.window2.ui.show()
        # 关闭自己
        self.ui.close()

    def handle_FB(self):
        self.type = 1
        self.open_new_window()

    def handle_JC(self):
        self.type = 2
        self.open_new_window()

    def handle_TX(self):
        self.type = 3
        self.open_new_window()

    def handle_SJ(self):
        self.type = 4
        self.open_new_window()

    def handle_QB(self):
        self.type = 5
        self.open_new_window()

    def handle_BB(self):
        self.type = 6
        self.open_new_window()

    

class Window_02:
   
    def __init__(self):

        x = sym.symbols('x')
        self.ui = QUiLoader().load('02.ui')
        self.ui.ani_Button.clicked.connect(self.cal)
        self.ui.displayfx_Button.clicked.connect(self.handle_display_fx)
        self.F = x

    def cal(self):

        number = self.ui.Spin_N.value()
        # print(Main_01.type,number)
        fourier.Fourier(number,Main_01.type,1)

        
    
        
    def handle_display_fx(self):

        number = self.ui.Spin_N.value()

        self.F = fourier.Fourier(number,Main_01.type,0)
        self.ui.textEdit.setPlainText(str(self.F))
        print('Fx:',str(self.F))



if __name__ == '__main__':

    app = QApplication([])
 
    app.setWindowIcon(QIcon('应用图标.png'))
    Main_01 = Main_01()
    Main_01.ui.show()
    app.exec_()



