class TabelaHash:
    def __init__(self, tamanho_inicial=100):
        self.tamanho = tamanho_inicial
        self.tabela = [[] for _ in range(self.tamanho)]

    def _calcular_hash(self, conteudo_texto):
        soma = sum(ord(char) for char in conteudo_texto)
        indice = soma % self.tamanho
        
        return soma, indice

    def gerar_assinatura(self, nome, ingredientes):
        ingredientes_str = "".join(sorted(ingredientes)).lower()
        conteudo = f"{nome.lower()}{ingredientes_str}"

        return self._calcular_hash(conteudo)

    def inserir(self, id_receita, nome, ingredientes):
        assinatura_forte, indice = self.gerar_assinatura(nome, ingredientes)
        self.tabela[indice].append((id_receita, assinatura_forte))
        print(f"[Hash] Receita '{nome}' guardada na posição {indice}.")

    def verificar_integridade(self, id_receita, nome, ingredientes_atuais):
        assinatura_atual_forte, indice = self.gerar_assinatura(nome, ingredientes_atuais)

        for tupla in self.tabela[indice]:
            id_salvo, assinatura_salva_forte = tupla

            if id_salvo == id_receita:
                if assinatura_salva_forte == assinatura_atual_forte:
                    return True
                else:
                    return False

        return False