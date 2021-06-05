from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(name = 'Freddy')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho.camina)
        simular_caminata = caminata(campo, boracho, pasos)
        distancias.append(round(simular_caminata, 1))
    return distancias

def caminata(campo, boracho, pasos):
    inicio = campo.obtener_coordenada(boracho)

    for _ in range(pasos):
        campo.mover_borracho(boracho)
    return inicio.distancias(campo.obtener_coordenada(boracho))
    
  

def main(distancias_de_caminata, numero_intentos, tipo_borracho):
   
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_intentos, BorrachoTradicional)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = max(distancias)
        print('Tipo: ' + tipo_borracho.__name__ + ' Caminata aleatoria de: ' + str(pasos) + ' pasos') 
        print('Media = ' + str(distancia_media))
        print('Max = ' + str(distancia_maxima))
        print('Min = ' + str(distancia_minima))
    
        
if __name__ == '__main__':

    distancias_de_caminata = [10, 100, 1000]
    numero_intentos = 10
    main(distancias_de_caminata, numero_intentos, BorrachoTradicional)
