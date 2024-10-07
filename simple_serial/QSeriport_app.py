# from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo

# #扫描所有串口
# def scan_port ():
#     comlist = QSerialPortInfo.availablePorts();
#     com_name =[]
#     for info in comlist:
#         com_name.append(info.portName())
#     return com_name ;



# class uartAPP(QSerialPort):
#     def __init__(self):
#         super(QSerialPort.self).__init__()
#         self.setBaudRate(115200)
#         self.setDataBits(8)
        
#     def uartSend(self, data):
#         self.write(data)
        
#     def setPortName(self,data):
#         self.setPortName(data)
        
    