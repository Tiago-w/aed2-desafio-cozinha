import json
import os

from hash import TabelaHash
from trie import ArvoreTrie
from guloso import recomendar_menu_guloso

def carregar_dados():
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_atual, "..", "data", "dataset.json")
    
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Ficheiro de base de dados não encontrado em {caminho_arquivo}.")
        return []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    receitas = carregar_dados()
    if not receitas:
        return

    investigador = TabelaHash(tamanho_inicial=10)
    busca_rapida = ArvoreTrie()
    
    for r in receitas:
        id_receita = r.get('id')
        nome = r.get('nome')
        ingredientes = r.get('ingredientes')

        if id_receita is None or nome is None or ingredientes is None:
            continue

        investigador.inserir(id_receita, nome, ingredientes)
        busca_rapida.inserir(nome, id_receita)

    while True:
        print("\n" + "="*45)
        print("MENU PRINCIPAL")
        print("="*45)
        print("1. Modo Consulta Rápida (Árvore Trie)")
        print("2. Modo Investigação (Tabela Hash)")
        print("3. Modo Chef - Recomendação (Guloso)")
        print("0. Sair")
        print("="*45)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n- MODO BUSCA RÁPIDA -")
            termo = input("Digite o prefixo da receita: ")
            resultados = busca_rapida.buscar_prefixo(termo)
            if resultados:
                print(f"Receitas encontradas: {resultados}")
            else:
                print("Nenhuma receita encontrada com esse prefixo.")

        elif opcao == "2":
            print("\n- MODO INVESTIGAÇÃO -")
            print("Vamos verificar a integridade da 'Omelete Francesa' (R001)...")
            alvo = next((receita for receita in receitas if receita.get('id') == 'R001'), receitas[0])

            status_ok = investigador.verificar_integridade(alvo['id'], alvo['nome'], alvo['ingredientes'])
            print(f"Original: {'Íntegra' if status_ok else 'Corrompida'}")

            print("Simulando fraude (adicionando 'Pimenta')...")
            fraudados = alvo['ingredientes'].copy()
            fraudados.append("Pimenta")
            status_fraude = investigador.verificar_integridade(alvo['id'], alvo['nome'], fraudados)
            print(f"Sabotada: {'Íntegra' if status_fraude else 'Corrompida'}")

        elif opcao == "3":
            print("\n- MODO CHEF -")
            try:
                orcamento = float(input("Insira o orçamento máximo disponível (Ex: 30.00): "))
                menu, custo_final, avaliacao_final = recomendar_menu_guloso(receitas, orcamento)
                
                print("\nMENU RECOMENDADO:")
                for prato in menu:
                    print(f" -> {prato['nome']} (Custo: R$ {prato['custo_estimado']:.2f} | Avaliação: {prato['avaliacao']})")
                print(f"\nResumo: Custo Total = R$ {custo_final:.2f} | Satisfação Total = {avaliacao_final:.1f}")
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "0":
            print("A encerrar o sistema. Au revoir!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()