class clasificadorMetricas():
    def __init__(self):
        self.patron = None
        self.clases = None
        self.representantes = None

    def setPatron(self, patron):
        self.patron = patron
    
    def setClases(self, clases):
        self.clases = clases
        self.calcularRepresentantes()

    def calcularRepresentantes(self):
        representantes = {}
        for key in self.clases:
            representanteClase = []
            for patrones in self.clases[key]:
                suma = 0
                for x in patrones:
                    suma += x 

                suma = suma / len(patrones)
                representanteClase.append(suma)

            representantes[key] = representanteClase

        self.representantes = representantes
 
    def getRepresentantes(self):
        print('Representantes calculados:', self.representantes)
        return self.representantes

    def cityBlock(self):
        distancias = []
        distanciaMenor = 0
        clasePertenciente = 'c1'
        for key in self.representantes:
            #sumaDeCoordenada = 0
            sumatoria = 0
            for i in range(len(self.representantes[key])):
                sumatoria += abs(self.patron[i] - self.representantes[key][i])
            
            print('Distancia de {}: {}'.format(key, sumatoria))
            distancias.append(sumatoria)
            if key == 'c1':
                distanciaMenor = sumatoria

            if sumatoria < distanciaMenor:
                distanciaMenor = sumatoria
                clasePertenciente = key

        return clasePertenciente, distancias

    def ecuclidea(self):
        pass

    def infinito(self):
        pass
            