import  serial
import serial.tools.list_ports



class serialApp   ( ):
    def  _init_(self):
        self.serialPort = serial.Serial( )
        self.baudrate = [9600, 115200]
        self.portlist = [ ]


    def updatePort(self):
            self.portlist = [port.device for port  in serial.tools.list_ports.comports ()]
            print (self.portlist)


    def conectSerial(self):
        except:
            print("Houve um erro ao abrir  a serial")



    def readSerial(self):
        dataRead = self .serialPort.read(10).decode('utf-8')
        print(dataRead)



    def sendSerial(self, data):
        if(self.serialPort.isOpen( ):
           dadoSend = str(self.data)+ '\n'
           self.serialPort.write(dadoSend.encode( ))
           self.serialPort.flushOutput( )


    def closeSerial(self):
            self.serialPort.close()

           



        
