from clock import Clock

timer = Clock()
timer.hora2 = 22
timer.Minutos1 = 50
timer.segundos1 = 40
print(timer.hora1 + ":", end=" ")
timer.soma_hora = 23
print(timer.Minutos1 + ":", end=" ")
print(timer.segundos1)

print(timer.time())



