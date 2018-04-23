from  pyb  import ADC,Pin


def analogRead(Pin_numb):  self = ADC(Pin(Pin_numb))  return self.read()    def digitalRead(Pin_numb):  self = Pin(Pin_numb,Pin.IN)  return self.value()
  
    