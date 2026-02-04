

        distance, cammino = self.path_find(nodo, -1,[nodo])




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





def get_neighbors_weighted(self, squadra_selezionata):

    weighted_map=dict()

    nodi_adiacenti= self.G.neighbors(squadra_selezionata)

    for nodo in nodi_adiacenti:
        peso_arco= self.G[squadra_selezionata][nodo]["peso"]
        weighted_map[nodo]= peso_arco

    sorted_weighted_map = dict(sorted(weighted_map.items(), key=lambda x: x[1], reverse=True))

    return sorted_weighted_map




