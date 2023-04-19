Análise - Campeonato Brasileiro Série A
======================================

Projeto de modelagem de dados e visualization utilizando o Power BI, analisando partidas do campeonato brasileiro desde a mudaça de seu formato que foi em 2003 até 2021.

Tem dois objetivos principais:

O primeiro proposto pelo consultor da [DNC](https://www.linkedin.com/school/escoladnc/),  [Eduardo Inocencio](https://www.linkedin.com/in/eduardoinocencio/), trata de responder questões de análise geral dos times que participaram do campeonato dentre os períodos de 2003 e 2021.

* Quais os times e estados com maior números de gols?

* Qual o número de gols visitante e mandante ao decorrer dos meses e a média de gols?

* Uma tabela contendo todos os técnicos.

* Quais os 5 times mandantes com maior número de gols?

* Quais os 5 times visitantes com maior número de gols?

* Quais os 5 estados mandantes com maior número de gols?

* Quais os 5 estados visitantes com maior número de gols?



Para o segundo objetivo perguntei a um amigo que gosta de futebol o que ele queria saber de informação, em resumo ele queria conseguir visualizar o desempenho do time que ele torce ao decorrer dos anos.

* Comparar os 3 melhores times do ano.

* Comparar os 4 piores times do ano.

* Qual a formação mais utilizada do time selecionado?

* Qual a formação que permitiu mais vitórias do time selecionado?

* Em qual estádio o time teve mais vitórias?

* Qual o técnico que trouxe mais vitórias ao time?

* Quantos gols foram feitos no total, em casa e como visitante?

* Quantas derrotas, vitórias e empates?

* Qual a pontuação total do time?



## Requisitos

* Power BI desktop



## Dados

* Utilizada planilha .CSV com os dados de todos os jogos de 2003 a 2021 do campeonato brasileiro série A.

[Base de Dados - Campeonato-brasileiro-full.csv](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/Base%20de%20Dados%20-%20Campeonato-brasileiro-full.csv)


## Modelagem

* Foram excluídos os dados que não seriam utilizados e feitas as tratativas necessárias.

* A planilha foi divida no modelo DIM-FACT do Power Bi para facilitar carregar os dados, caso seja feita uma atualização.

![](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/modelagem-dados.png)


## Objetivos

### Dashboard de análises gerais

![](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/an%C3%A1lise-geral.png)


### Dashboard de análise dos times

![](https://github.com/NandesLima/analise-campeonato-brasileiro/blob/master/an%C3%A1lise-times.png)