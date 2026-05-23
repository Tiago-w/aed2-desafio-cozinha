#cria o nó da árvore
class NoTrie:
    def __init__(self):
        self.filhos = {}                                       
        self.fim_palavra = False                             
        self.receitas_ids = []                                 

#contrói a árvore
class ArvoreTrie:
    def __init__(self):                                        
        self.raiz = NoTrie()                                  

    def inserir(self, palavra, id_receita):                   
        palavra = palavra.lower()                              
        no_atual = self.raiz                                   

        for letra in palavra:                                  
            if letra not in no_atual.filhos:
                no_atual.filhos[letra] = NoTrie()
            no_atual = no_atual.filhos[letra]

        no_atual.fim_palavra = True                                  

        if id_receita not in no_atual.receitas_ids:
            no_atual.receitas_ids.append(id_receita)

    def _coletar_ids(self, no, lista_resultados):   # só um "_" indica que é função de uso interno
        if no.fim_palavra:      
            lista_resultados.extend(no.receitas_ids)
    
        for filho in no.filhos.values():
            self._coletar_ids(filho, lista_resultados)
    def buscar_prefixo(self, prefixo):
        prefixo = prefixo.lower()
        no_atual = self.raiz

        for letra in prefixo:
            if letra not in no_atual.filhos:
                return []
            no_atual = no_atual.filhos[letra]

        resultados = []
        self._coletar_ids(no_atual, resultados)
        vistos = set()
        ids_unicos = []
        for rid in resultados:
            if rid not in vistos:
                vistos.add(rid)
                ids_unicos.append(rid)
        return ids_unicos