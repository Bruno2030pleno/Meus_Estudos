class Ponto:
    MAX_X = 500
    MAX_Y = 250
    def __init__(self,x, y):
        self.x = x
        self.y = y
    @classmethod
    def mostrar_limites(cls):
        print(f"Território vai até {cls.MAX_X} x {cls.MAX_Y}")



a = Ponto(2, 3) 
a.mostrar_limites()      