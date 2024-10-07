import sys
import binascii
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo
from ui import Ui_Form
from PyQt5.QtWidgets import QApplication ,QMainWindow,QWidget
from PyQt5.QtGui import QIcon
import QSeriport_app
from PyQt5.QtCore import QTimer



class myWindowForm(QMainWindow,Ui_Form):
    def __init__(self):
        super(myWindowForm,self).__init__()
        self.setupUi(self)
        # 设置实例
        self.createItems()
        # 设置信号与槽函数
        self.createSlot()
        self.initPortList()
        self.uartRxbuf = bytes();

    def createItems(self):
        self.com =  QSerialPort();
        self.rxtimer = QTimer()

        
# 初始化串口号
    def initPortList(self):
        comlist = QSerialPortInfo.availablePorts();
        com_name =[]
        for info in comlist:
            com_name.append(info.portName())
        self.uart_name.addItems(com_name)
        
        
    def createSlot(self):
        self.com_open.clicked.connect(self.com_open_button_clicked)  #打开串口
        self.clear_log.clicked.connect(self.slot_clear_log) # 清空日志
        self.btn_ask_vol.clicked.connect(self.slot_ask_vol_ins)  # 按钮按下
        self.com.readyRead.connect(self.timer_start)
        self.rxtimer.timeout.connect(self.getData)
        
    def com_open_button_clicked(self):
        self.com.setBaudRate(115200)
        self.com.setPortName(self.uart_name.currentText())
        if self.com.open(QSerialPort.ReadWrite) == True:
            self.com_open.setText('串口已经打开')
            self.showLog("串口打开成功")
            self.com_open.setEnabled(False)
            self.uart_name.setEnabled(False)
        else :
            self.showLog('串口异常')
            
    def showLog(self,data):
        self.log.append(data)

    def closeEvent(self, event):
        if self.com.isOpen():
            self.com.close()
        super(myWindowForm, self).closeEvent(event)
        
    def slot_clear_log ( self ):
        self.log.clear();
    
    
    def slot_ask_vol_ins(self):
        ins = self.str2hex_toSend('aabb')
        self.com.write(ins)
    
    def str2hex_toSend(self,data):
        ins = data 
        hex_data = binascii.a2b_hex(ins)
        return hex_data        

    #超时接收 
    def timer_start(self):
        self.rxtimer.start(50)
        rx_data =bytes(self.com.readAll())
        self.uartRxbuf = self.uartRxbuf + rx_data ;
        print('缓冲区有数据')
        
        
    def getData(self):
        self.rxtimer.stop();
        print(self.uartRxbuf)
        self.uartRxbuf = bytes();

    

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = myWindowForm()
    myWin.setWindowIcon(QIcon("dog.ico"))
    myWin.setWindowTitle("456")
    myWin.show()
    sys.exit(app.exec_())

