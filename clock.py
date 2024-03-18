class Clock:

    def __init__(self, horas=0, minutos=0, segundos=0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos
    
    @property
    def hora1(self):
        return f'{self.__horas}'
    
    @hora1.setter
    def hora2(self, valor):
        '''Muda a hora do relógio. Se o valor nao for entre 0 e 23, imprime uma mensagem de erro.'''
        self.__horas = valor if 0 <= valor <= 23 else print("Hora inválida")

    def soma_hora(self, valor):
        '''soma a hora do relógio com o hora passada.'''
        self.__horas = (self.__horas + valor) % 24    

    @property
    def Minutos1(self):
        return f'{self.__minutos}'
    
    @Minutos1.setter
    def Minutos1(self, valor):
        '''Muda os minutos do relógio. Se o valor nao for entre 0 e 59, imprime uma mensagem de erro.'''
        self.__minutos = valor if 0 <= valor <= 59 else print("Minutos inválidos")

    def soma_minuto(self, valor):
        '''soma os minutos do relógio com o minutos passada.'''
        total_minutos = self.__minutos + valor
        self.__minutos = total_minutos % 60
        self.soma_hora(total_minutos // 60)     
    
    @property
    def segundos1(self):
        return f'{self.__segundos}'
    
    @segundos1.setter
    def segundos1(self, valor):
        '''Muda os segundos do relógio. Se o valor nao for entre 0 e 59, imprime uma mensagem de erro.'''
        self.__segundos = valor if 0 <= valor <= 59 else print("Segundos inválidos")

      

    def time(self):
        '''Retorna o horário atual do relógio.'''
        return f'{self.__horas:02}:{self.__minutos:02}:{self.__segundos:02}'    
