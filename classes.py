from datetime import datetime

class Materia:
    '''classe che rappresenta una materia universitaria
    nome_materia: nome della materia
    data_esame: data dell'esame GG/MM/AAAA
    rating: valutazione importanza della materia
    ore_indicative: ore indicative per la materia
    carico stimato: carico di materiale della materia stimato in xs s m l xl'''
    def __init__(self,nome_materia, data_esame,rating,ore_indicative,carico_stimato):
        self.nome_materia=nome_materia
        self.data_esame = datetime.strptime(data_esame, "%d/%m/%Y")
        self.rating=rating
        self.ore_indicative=int(ore_indicative)
        self.carico_stimato=carico_stimato
        self.ore_effettive=0
        
    def info(self):
        print(f"Materia: {self.nome_materia}, Data Esame: {self.data_esame}, Rating: {self.rating}, Ore Indicative: {self.ore_indicative}")
        
    
    
