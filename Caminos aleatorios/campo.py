class Campo:

    def __init__(self):
        self.coordenadas_de_borracho = {}
        # Creo un diccionario para guardar coordenadas
    
    def agregar_borracho(self, borracho, coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada
        # Ingreso la coordenada
    
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        # Doy la orden a borracho para que genere valores.
        # Creo varible que vea el diccionario e indique la ultima coordenada
        # Creo otra variable que indica el siguiente movimiento
        self.coordenadas_de_borracho[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borracho[borracho]
        # Obtiene las coordenadas del diccionario