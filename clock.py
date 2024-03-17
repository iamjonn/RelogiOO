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
        '''Muda a hora do relógio. Se o valor for entre 0 e 23, imprime uma mensagem de erro.'''
        self.__horas = valor if 0 <= valor <= 23 else print("Hora inválida")
    @property
    def Minutos1(self):
        return f'{self.__minutos}'
    
    @Minutos1.setter
    def Minutos1(self, valor):
        '''Muda os minutos do relógio. Se o valor nao for entre 0 e 59, imprime uma mensagem de erro.'''
        self.__minutos = valor if 0 <= valor <= 59 else print("Minutos inválidos")
    
    @property
    def segundos1(self):
        return f'{self.__segundos}'
    
    @segundos1.setter
    def segundos1(self, valor):
        '''Muda os segundos do relógio. Se o valor nao for entre 0 e 59, imprime uma mensagem de erro.'''
        self.__segundos = valor if 0 <= valor <= 59 else print("Segundos inválidos")

    #def time(self):
        '''Retorna o horário atual do relógio.'''
        #return f'{self.__horas}:{self.__minutos}:{self.__segundos}'    
