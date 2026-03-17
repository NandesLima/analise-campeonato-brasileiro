import pandas as pd
import os

# Caminho dos arquivos
base_path = "analise-campeonato-brasileiro"
input_file = os.path.join(base_path, "Base de Dados - Campeonato-brasileiro-full.csv")
output_file = os.path.join(base_path, "brasileirao_clean.csv")

def clean_data():
    print(f"📦 Carregando dados de: {input_file}...")
    df = pd.read_csv(input_file)

    # 1. Tratamento de Valores Nulos
    # Formações e Técnicos muitas vezes estão vazios em jogos antigos
    cols_to_fill = ['formacao_mandante', 'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante']
    for col in cols_to_fill:
        df[col] = df[col].fillna('Não Informado')

    # 2. Conversão de Tipos
    df['data'] = pd.to_datetime(df['data'])
    
    # 3. Feature Engineering: Cálculo de Pontos (Regra do Futebol)
    def calculate_points(row, side):
        if row['vencedor'] == '-':
            return 1 # Empate
        elif row['vencedor'] == row[side]:
            return 3 # Vitória
        else:
            return 0 # Derrota

    df['pontos_mandante'] = df.apply(lambda row: calculate_points(row, 'mandante'), axis=1)
    df['pontos_visitante'] = df.apply(lambda row: calculate_points(row, 'visitante'), axis=1)

    # 4. Feature Engineering: Estatísticas de Gols
    df['total_gols'] = df['mandante_placar'] + df['visitante_placar']
    
    # 5. Salvar o arquivo limpo para o Power BI
    df.to_csv(output_file, index=False)
    print(f"✅ Sucesso! Arquivo processado salvo em: {output_file}")
    print(f"📊 Linhas processadas: {len(df)}")

if __name__ == "__main__":
    clean_data()
