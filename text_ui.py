from classes import Materia
def text_ui():
    n_materie=input("quante materie devi preparare? ")
    materie=[]
    for i in range(int(n_materie)):
        nome_materia=input("inserisci il nome della materia  ")
        data_esame=input("inserisci la data dell'esame GG/MM/AAAA  ")
        rating=input("inserisci la valutazione dell'importanza della materia (range [0;1])  ")
        ore_indicative=input("inserisci le ore indicative per la materia  ")
        carico_stimato=input("inserisci carico stimato (xs s m l xl)")
        materia=Materia(nome_materia, data_esame, rating, ore_indicative,carico_stimato)
        materie.append(materia)
        print(f"hai inserito la materia {materia.nome_materia}")
        