import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações de estilo para portfólio sênior (Dark Theme para combinar com o MkDocs Neon)
plt.style.use('dark_background')
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#1e1e1e", "figure.facecolor": "#121212"})

base_path = "analise-campeonato-brasileiro"
input_file = os.path.join(base_path, "brasileirao_clean.csv")
assets_path = os.path.join(base_path, "docs/assets")

# Garante que a pasta de assets exista
os.makedirs(assets_path, exist_ok=True)

def run_advanced_eda():
    if not os.path.exists(input_file):
        print("❌ Erro: Execute o data_cleaning.py primeiro.")
        return

    print(f"📈 Iniciando EDA Avançada e Teste de Hipóteses: {input_file}...")
    df = pd.read_csv(input_file)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year
    df['total_gols'] = df['mandante_placar'] + df['visitante_placar']
    
    # --- HIPÓTESE 1: A QUEDA DO "HOME ADVANTAGE" ---
    # Pergunta: A vantagem de jogar em casa está diminuindo com o tempo (melhor logística, gramados, VAR)?
    home_adv_yearly = df.groupby('ano').apply(lambda x: (x['vencedor'] == x['mandante']).mean()).reset_index(name='taxa_vitoria_home')
    
    plt.figure(figsize=(12, 6))
    sns.regplot(data=home_adv_yearly, x='ano', y='taxa_vitoria_home', color='#00ffcc', scatter_kws={'s':100}, line_kws={"color": "red"})
    plt.axhline(home_adv_yearly['taxa_vitoria_home'].mean(), color='white', linestyle='--', alpha=0.5, label=f"Média Histórica: {home_adv_yearly['taxa_vitoria_home'].mean():.2%}")
    plt.title('Regressão: Tendência do Home Advantage no Brasileirão', fontsize=14, color='#00ffcc')
    plt.ylabel('Taxa de Vitória do Mandante')
    plt.xlabel('Temporada')
    plt.legend()
    plt.savefig(os.path.join(assets_path, "home_advantage_regression.png"))
    plt.close()

    # --- HIPÓTESE 2: O "TETO DE GOLS" E A VITÓRIA ---
    # Pergunta: Existe um número de gols que garanta estatisticamente a vitória?
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='vencedor_local', y='total_gols', palette="viridis")
    plt.title('Distribuição de Gols por Tipo de Resultado', fontsize=12, color='#00ffcc')
    plt.xlabel('Quem Venceu (Mandante/Visitante/Empate)')
    plt.ylabel('Total de Gols na Partida')
    plt.savefig(os.path.join(assets_path, "goals_distribution_result.png"))
    plt.close()

    # --- HIPÓTESE 3: CORRELAÇÃO DE PONTOS ---
    # Verificando se ataques mais positivos garantem melhores colocações (Proxy por média de pontos)
    equipes_stats = df.groupby('mandante').agg({
        'pontos_mandante': 'mean',
        'mandante_placar': 'mean'
    }).rename(columns={'pontos_mandante': 'media_pontos', 'mandante_placar': 'media_gols_pro'})

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=equipes_stats, x='media_gols_pro', y='media_pontos', size='media_pontos', hue='media_pontos', palette='magma', sizes=(50, 400))
    plt.title('Correlação: Eficiência Ofensiva vs. Conquista de Pontos (Mandante)', fontsize=12, color='#00ffcc')
    plt.savefig(os.path.join(assets_path, "offensive_efficiency_correlation.png"))
    plt.close()

    print("\n✅ EDA Avançada Concluída com Sucesso.")
    print(f"📊 Insights gerados: {len(os.listdir(assets_path))} assets disponíveis.")

if __name__ == "__main__":
    run_advanced_eda()
