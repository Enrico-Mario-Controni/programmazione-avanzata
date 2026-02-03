import networkx as nx


def CamminiPossibili(nodo, end, cammino):
    if nodo == end:
        return [cammino]

    cammini = []

    for vicino in G.successors(nodo):
        nuovi_cammini = CamminiPossibili(vicino, end, cammino + [vicino])
        cammini.extend(nuovi_cammini)

    return cammini

def Sicurezza(nodo, end, sicuri, cammino):

    if nodo == end:
        return [cammino]

    percorsi=[]
    for vicino in G.successors(nodo):
        if vicino in sicuri:
            nuovi_percorsi=Sicurezza(vicino, end, sicuri, cammino+[vicino])
            percorsi.extend(nuovi_percorsi)

    return percorsi

def PercorsiSoglia(start,end,soglia,cammino):
    nodo = start
    if nodo==end:
        return [cammino]

    percorsi=[]

    for vicino in G.successors(nodo):

        peso=G[nodo][vicino]["weight"]
        if peso>soglia and vicino not in percorsi:
            cammini=PercorsiSoglia(vicino,end,soglia,cammino+[vicino])
            percorsi.extend(cammini)

    return percorsi

def PercorsiMinimi(start,end,soglia,cammino):

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

            cammini = PercorsiMinimi(vicino,end,soglia,cammino+[vicino])
            percorsi.extend(cammini)

    return percorsi





if __name__ == '__main__':

    G = nx.DiGraph()

    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("B", "D")
    G.add_edge("C", "D")

    start = "A"
    end = "D"

    print(CamminiPossibili(start, end,[start]))

    G = nx.DiGraph()
    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("B", "D")
    G.add_edge("C", "D")
    G.add_edge("B", "E")
    G.add_edge("E", "D")

    start = "A"
    end = "D"
    sicuri = ["A", "B", "C", "D"]

    print(Sicurezza(start, end, sicuri, [start]))

    G.add_edge("A", "B", weight=5)
    G.add_edge("A", "C", weight=3)
    G.add_edge("B", "D", weight=6)
    G.add_edge("C", "D", weight=2)
    G.add_edge("B", "E", weight=1)
    G.add_edge("E", "D", weight=4)

    start = "A"
    end = "D"
    S = 4

    print(PercorsiSoglia(start,end,S,[start]))

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

    print(PercorsiMinimi(start,end,S,[start]))





