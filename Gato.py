from Animal import Animal
import datetime

class Gato(Animal):
    def Resumen(self):
        fecha = datetime.datetime.now()
        if self.estado == True:
             return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia)  + ", Gato , vivo." 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia) +  ", Gato , muerto." 
        
    def Comer(self,gramos):
        self.energia = self.energia + (12 + gramos)
        fecha = datetime.datetime.now()
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Gracias. Ahora mi energia es: " + str(self.energia) 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Muy tarde. Ya me mori" 
        
    def Jugar(self,tiempo):
        pass
    