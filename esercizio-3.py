import networkx as nx


def PercorsiValidi(start,end,soglia,cammino):

    nodo = start
    if nodo==end:
        if len(cammino)>=3:
            return [cammino]
        else:
            return []

    percorsi=[]

    for vicino in G.successors(nodo):
        peso=G[nodo][vicino]["weight"]

        if peso>soglia and vicino not in cammino :

            cammini = PercorsiValidi(vicino,end,soglia,cammino+[vicino])
            percorsi.extend(cammini)

    return percorsi

def CostoPercorso(cammino):

    costo=0

    for el in range(len(cammino)-1):
        costo += G[cammino[el]][cammino[el+1]]["weight"]
        #così calcolo ogni peso di ogni singolo arco e lo aggiungo così da avere un peso complessivo

    return costo

def PercorsiMinimi(start,end,soglia):

    percorsi= PercorsiValidi(start,end,soglia,[start])#lista di percorsi(nodi da... a...)

    if not percorsi:
        return []

    minimo=percorsi[0]#prendo il primo percorso nella lista e lo impongo come riferimento

    costo_min=CostoPercorso(minimo)#calcolo il costo del primo percorso della lista

    for p in percorsi[1:]: #per i percorsi validi dal secondo in poi...
        costo_p = CostoPercorso(p)#calcolo il costo di del percorso (di tutto gli elementi del percorso)
        if costo_p < costo_min:
            minimo = p
            costo_min = costo_p

    return minimo





if __name__ == '__main__':
    G = nx.DiGraph()

    G.add_edge("A", "B", weight=5)
    G.add_edge("A", "C", weight=3)
    G.add_edge("B", "D", weight=6)
    G.add_edge("C", "D", weight=2)
    G.add_edge("B", "E", weight=5)
    G.add_edge("E", "D", weight=5)

    start = "A"
    end = "D"
    S = 4

    risultato = PercorsiMinimi(start, end, S)
    print(risultato)