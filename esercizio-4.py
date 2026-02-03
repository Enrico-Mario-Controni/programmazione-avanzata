import networkx as nx
"""Dato un grafo orientato e pesato, implementare una funzione ricorsiva che trovi tutti i cammini validi da un nodo start a un nodo end che rispettino tutti i seguenti vincoli:

1) Il cammino deve usare solo archi con peso minore o uguale a una soglia S

2) Il cammino deve contenere almeno 3 archi (quindi almeno 4 nodi)

3) Il cammino non può visitare più di una volta lo stesso nodo

4) Il cammino deve passare obbligatoriamente per un nodo obbligatorio

5) Se non esistono cammini validi, la funzione deve restituire una lista vuota

La funzione deve restituire:

una lista di cammini

ogni cammino è una lista di nodi, ordinata da start a end"""


def PercorsiValidi(start,end,soglia,obbligatorio,cammino):

    nodo=start
    if nodo==end:
        if len(cammino)>=4 and obbligatorio in cammino:
            return [cammino]

        else:
            return []

    percorsi=[]

    for vicino in G.successors(nodo):

        peso= G[nodo][vicino]["weight"]

        if peso <= soglia and vicino not in cammino:

            cammini=PercorsiValidi(vicino,end,soglia,obbligatorio,cammino+[vicino])
            percorsi.extend(cammini)

    return percorsi





if __name__ == "__main__":

    G = nx.DiGraph()

    G.add_edge("A", "B", weight=2)
    G.add_edge("A", "C", weight=4)
    G.add_edge("B", "D", weight=3)
    G.add_edge("C", "D", weight=1)
    G.add_edge("B", "E", weight=2)
    G.add_edge("E", "F", weight=3)
    G.add_edge("F", "D", weight=2)
    G.add_edge("C", "F", weight=2)

    start = "A"
    end = "D"
    obbligatorio = "F"
    S = 3

    print(PercorsiValidi(start,end,S,obbligatorio, [start]))