import pandas as pd
import os

# Caminho dos arquivos - Ajustado para rodar dentro da pasta do projeto
input_file = "Base de Dados - Campeonato-brasileiro-full.csv"
output_file = "brasileirao_clean.csv"

def clean_data():
    if not os.path.exists(input_file):
        print(f"❌ Erro: Arquivo {input_file} não encontrado no diretório atual ({os.getcwd()})")
        return

    print(f"📦 Carregando dados de: {input_file}...")
    df = pd.read_csv(input_file)

    # 1. Tratamento de Valores Nulos
    cols_to_fill = ['formacao_mandante', 'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante']
    for col in cols_to_fill:
        df[col] = df[col].fillna('Não Informado')

    # 2. Conversão de Tipos
    df['data'] = pd.to_datetime(df['data'])
    
    # 3. Feature Engineering: Cálculo de Pontos
    def calculate_points(row, side):
        if row['vencedor'] == '-':
            return 1 # Empate
        elif row['vencedor'] == row[side]:
            return 3 # Vitória
        else:
            return 0 # Derrota

    df['pontos_mandante'] = df.apply(lambda row: calculate_points(row, 'mandante'), axis=1)
    df['pontos_visitante'] = df.apply(lambda row: calculate_points(row, 'visitante'), axis=1)

    # Adicionando vencedor_local para facilitar EDA
    def get_vencedor_local(row):
        if row['vencedor'] == '-': return 'Empate'
        if row['vencedor'] == row['mandante']: return 'Mandante'
        return 'Visitante'
    
    df['vencedor_local'] = df.apply(get_vencedor_local, axis=1)

    # 4. Feature Engineering: Estatísticas de Gols
    df['total_gols'] = df['mandante_placar'] + df['visitante_placar']
    
    # 5. Salvar o arquivo limpo
    df.to_csv(output_file, index=False)
    print(f"✅ Sucesso! Arquivo salvo em: {output_file}")
    print(f"📊 Linhas processadas: {len(df)}")

if __name__ == "__main__":
    clean_data()
