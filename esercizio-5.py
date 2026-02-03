def ricorsione(self, nodo_iniziale, nodo_finale, lunghezza_richiesta, lista_parziale, peso_corrente):
    if nodo_iniziale == nodo_finale:
        if lunghezza_richiesta == len(lista_parziale):
            return lista_parziale, peso_corrente

        else:
            return None, -1

    else:

        miglior_percorso = None
        miglior_peso = -1

        vicini = self.G.successors(nodo_iniziale)  # ciò permette di rispettare il vincolo:
        # Il cammino attraversi gli archi rispettando i versi;

        for nodo_vicino in vicini:

            peso = self.G[nodo_iniziale][nodo_vicino]["peso"]

            if nodo_vicino in lista_parziale:
                continue

            cammini, peso_finale = self.ricorsione(nodo_vicino, nodo_finale, lunghezza_richiesta,
                                                   lista_parziale + [nodo_vicino], peso_corrente + peso)

            if peso_finale > miglior_peso:
                miglior_peso = peso_finale
                miglior_percorso = cammini

        return miglior_percorso, miglior_peso

"""----------------------------------------------------------------------------------------------------------------"""

def ricorsione(self):

    best_distance=0
    best_path=[]

    nodi=self.G.nodes()

    self.dizionario_coordinate= self.get_coordinate()

    for nodo in nodi:

        distance, cammino = self.path_find(nodo, -1,[nodo])

        if distance > best_distance:
            best_distance=distance
            best_path=cammino

    return  best_distance,best_path



def path_find(self, nodo, peso_precedente, lista_cammino):

    distanza=0
    cammino= lista_cammino.copy()

    successori=self.G.neighbors(nodo)


    for el in successori:
        peso= self.G[nodo][el]["peso"]

        lat1, lng1 = self.dizionario_coordinate[nodo.lower()]
        lat2, lng2 = self.dizionario_coordinate[el.lower()]

        distanza_corrente = distance.geodesic((lat1, lng1), (lat2, lng2)).km



        if peso > peso_precedente and el not in lista_cammino  :


                totale, path = self.path_find(el, peso, lista_cammino+[el])

                if totale + distanza_corrente > distanza:
                    distanza= totale + distanza_corrente
                    cammino=path

    return distanza, cammino

"""--------------------------------------------------------------------------------------------------------------------"""


def get_connected_components(self,nodo):

    connections= nx.node_connected_component(self.G,nodo)

    contatore_componenti=0

    contatore_minuti=0

    self.dizionario_connessi={}

    for el in connections:

        contatore_componenti +=1

        contatore_minuti += sum(DAO.get_connected_time(el)) #cosi non da errore per il decimal[...]

        self.dizionario_connessi[el]= sum(DAO.get_connected_time(el))

    return contatore_minuti, contatore_componenti




def call_ricorsione(self, album_partenza, dTOT):

    self.album_iniziale = set(nx.node_connected_component(self.G, album_partenza))
    best_cammino, best_durata_cammino, best_durata = self.ricorsione(dTOT, album_partenza, [album_partenza],0)


    return best_cammino, best_durata_cammino, best_durata



def ricorsione(self, dTOT, album_corrente, lista_parziale, somma_durata_album):

    somma_corrente = somma_durata_album + self.dizionario_connessi[album_corrente]

    best_cammino = lista_parziale
    best_durata_cammino=len(lista_parziale)
    best_durata= somma_corrente

    for nodo in self.G.neighbors(album_corrente):

        if nodo in self.album_iniziale and nodo not in lista_parziale:


            nuova_somma= somma_corrente + self.dizionario_connessi[nodo]

            if nuova_somma > dTOT:
                continue

            cammino, durata_cammino, durata =self.ricorsione( dTOT, nodo, lista_parziale + [nodo], somma_corrente)

            if durata > best_durata or (durata == best_durata and durata_cammino > best_durata_cammino):

                best_cammino = cammino
                best_durata_cammino = len(cammino)
                best_durata= durata


        else:
            continue

    return best_cammino, best_durata_cammino, best_durata


"""---------------------------------------------------------------------------------------------------------------------"""


def get_neighbors_weighted(self, squadra_selezionata):

    weighted_map=dict()

    nodi_adiacenti= self.G.neighbors(squadra_selezionata)

    for nodo in nodi_adiacenti:
        peso_arco= self.G[squadra_selezionata][nodo]["peso"]
        weighted_map[nodo]= peso_arco

    sorted_weighted_map = dict(sorted(weighted_map.items(), key=lambda x: x[1], reverse=True))

    return sorted_weighted_map


def ricorsione(self, nodo_partenza):

    cammino, peso=self.get_path(nodo_partenza, 0, inf, [nodo_partenza])

    return cammino, peso



def get_path(self, nodo_partenza, peso_corrente, peso_precedente, lista_parziale):

    best_cammino = lista_parziale
    best_weight = peso_corrente

    if len(list(self.G.neighbors(nodo_partenza))) > 0: #perche neighbor non restituisce una lista

        for successore in self.G.neighbors(nodo_partenza):
            peso_arco= self.G[nodo_partenza][successore]["peso"]

            if peso_arco < peso_precedente and successore not in lista_parziale:

                cammino, peso=self.get_path(successore, peso_corrente + peso_arco, peso_arco,
                                            lista_parziale + [successore])

                if peso > best_weight:
                    best_cammino = cammino
                    best_weight = peso


            else:
                continue


    return best_cammino, best_weight



