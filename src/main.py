import json
import os

# Importando as estruturas que vocês criaram
from hash import TabelaHash
from trie import ArvoreTrie

def carregar_dados():
    # Como o main.py está dentro de src/, precisamos voltar uma pasta (..) 
    # para achar a pasta data/ onde está o dataset.json
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_atual, "..", "data", "dataset.json")
    
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Erro: Arquivo de banco de dados não encontrado em {caminho_arquivo}.")
        return []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("="*40)
    print("👨‍🍳 INICIANDO O SISTEMA DO JACQUIN")
    print("="*40)
    
    receitas = carregar_dados()
    if not receitas:
        return

    # Instanciando as estruturas da dupla
    investigador = TabelaHash(tamanho_inicial=10)
    busca_rapida = ArvoreTrie()
    
    print("\n--- CARREGANDO RECEITAS NO MOTOR ---")
    for r in receitas:
        # Inserindo na Hash do Gustavo
        investigador.inserir(r['id'], r['nome'], r['ingredientes'])
        
        # Inserindo na Trie do Tiago (usamos o nome da receita para a busca)
        busca_rapida.inserir(r['nome'], r['id'])

    # ---------------------------------------------------------
    # TESTE 1: A Trie do Tiago (Modo Consulta Rápida)
    # ---------------------------------------------------------
    print("\n--- 🔍 TESTE: MODO BUSCA RÁPIDA (TRIE) ---")
    termo_busca = "ome"
    resultados_trie = busca_rapida.buscar_prefixo(termo_busca)
    print(f"Procurando pelo prefixo '{termo_busca}':")
    if resultados_trie:
        print(f"✔️ Encontrado IDs: {resultados_trie}")
    else:
        print("❌ Nenhuma receita encontrada.")

    # ---------------------------------------------------------
    # TESTE 2: A Hash do Gustavo (Modo Investigação)
    # ---------------------------------------------------------
    print("\n--- 🕵️ TESTE: MODO INVESTIGAÇÃO (HASH) ---")
    receita_alvo = receitas[0]  # Vamos testar a Omelete Francesa (R001)
    
    # Simulação A: Verificando a receita original
    status_ok = investigador.verificar_integridade(
        receita_alvo['id'], 
        receita_alvo['nome'], 
        receita_alvo['ingredientes']
    )
    print(f"Status da '{receita_alvo['nome']}' original: {'✔️ Íntegra' if status_ok else '❌ Corrompida'}")

    # Simulação B: Alguém sabotou o banco de dados e adicionou Pimenta
    print("\n[ALERTA] Inserindo 'Pimenta' secretamente na receita...")
    ingredientes_fraudados = receita_alvo['ingredientes'].copy()
    ingredientes_fraudados.append("Pimenta")
    
    status_sabotada = investigador.verificar_integridade(
        receita_alvo['id'], 
        receita_alvo['nome'], 
        ingredientes_fraudados
    )
    print(f"Status da '{receita_alvo['nome']}' após sabotagem: {'✔️ Íntegra' if status_sabotada else '❌ Corrompida (Fraude Detectada!)'}")
    print("="*40)

if __name__ == "__main__":
    main()