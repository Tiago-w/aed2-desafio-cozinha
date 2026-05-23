class TabelaHash:
    def __init__(self, tamanho_inicial=100):
        self.tamanho = tamanho_inicial
        self.tabela = [[] for _ in range(self.tamanho)]

    def _calcular_hash(self, conteudo_texto):
        # A soma total é a nossa "Assinatura Forte" (ex: 2845)
        soma = sum(ord(char) for char in conteudo_texto)
        # O resto da divisão é apenas o índice da gaveta (ex: 5)
        indice = soma % self.tamanho
        
        return soma, indice

    def gerar_assinatura(self, nome, ingredientes):
        ingredientes_str = "".join(sorted(ingredientes)).lower()
        conteudo = f"{nome.lower()}{ingredientes_str}"
        
        # Agora retornamos as duas informações
        return self._calcular_hash(conteudo)

    def inserir(self, id_receita, nome, ingredientes):
        assinatura_forte, indice = self.gerar_assinatura(nome, ingredientes)
        
        # Guardamos a assinatura_forte na tupla, não o índice!
        self.tabela[indice].append((id_receita, assinatura_forte))
        print(f"✅ [Hash] Receita '{nome}' guardada na posição {indice}.")

    def verificar_integridade(self, id_receita, nome, ingredientes_atuais):
        assinatura_atual_forte, indice = self.gerar_assinatura(nome, ingredientes_atuais)
        
        for tupla in self.tabela[indice]:
            id_salvo, assinatura_salva_forte = tupla
            
            if id_salvo == id_receita:
                # O PULO DO GATO: Achou o ID? Agora compara se a soma total bate!
                # Mesmo que o índice seja igual, a soma da palavra "Pimenta" vai denunciar a sabotagem.
                if assinatura_salva_forte == assinatura_atual_forte:
                    return True
                else:
                    return False
                    
        return False