def recomendar_menu_guloso(receitas, orcamento_maximo):
    receitas_enriquecidas = []

    for receita in receitas:
        custo = receita.get('custo_estimado', 0)
        avaliacao = receita.get('avaliacao', 0)
        receita_enriquecida = receita.copy()
        receita_enriquecida['densidade'] = avaliacao / custo if custo > 0 else 0
        receitas_enriquecidas.append(receita_enriquecida)

    receitas_ordenadas = sorted(receitas_enriquecidas, key=lambda x: x['densidade'], reverse=True)

    menu_recomendado = []
    custo_total = 0.0
    avaliacao_total = 0.0

    for receita in receitas_ordenadas:
        if custo_total + receita.get('custo_estimado', 0) <= orcamento_maximo:
            menu_recomendado.append(receita)
            custo_total += receita.get('custo_estimado', 0)
            avaliacao_total += receita.get('avaliacao', 0)

    return menu_recomendado, custo_total, avaliacao_total