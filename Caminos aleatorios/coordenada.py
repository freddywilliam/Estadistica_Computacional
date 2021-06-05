
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    # Cojo la coordenada anterior y le sumo la nueva.
    # Calculo donde estamos - otra coordenada
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada
        delta_y = self.y - otra_coordenada

        return(delta_x**2 + delta_y**2)**0.5