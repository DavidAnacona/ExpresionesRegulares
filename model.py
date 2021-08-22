#Requerido para uso de expresiones regulares
import re 

class Model:

    def __init__(self):
        self.correo = r'([a-zA-Z0-9._-]+)@([\w]+)\.([a-zA-Z])+'
        self.entero = r'^[+-]?\d+$'
        self.real = r'^[+-]?[\d]+\.?([\d]*$)'
        self.notacion = r'^[+-]?[0-9]*\.?\d+([eE][+-]?\d+)'

    def verificacionCorreo(self, value):
        if(re.search(self.correo, value)):
            return 'Correo valido'
        else:
            return 'Correo invalido'

    def verificacionEntero(self, value):
        if(re.search(self.entero, value)):
            return 'Entero valido'
        else:
            return 'Entero invalido'
    
    def verificacionReal(self, value):
        if(re.search(self.real, value)):
            return 'Real valido'
        else:
            return 'Real invalido'

    def verificacionNotacion(self, value):
        if(re.search(self.notacion, value)):
            return 'Notación cientifica valido'
        else:
            return 'Notación cientifica invalido'