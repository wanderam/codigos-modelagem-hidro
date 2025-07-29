# Códigos - Modelagem hidrológica

Códigos Python (*Jupyter notebooks*) para processar e analisar dados de recarga de aquífero das sub-bacias PCJ, referentes ao período de janeiro de 1985 a dezembro de 2020, estimados por meio de modelagem hidrológica, com os modelos hidrológicos [**SWAT**](https://swat.tamu.edu/) e **SWAT-MODFLOW** ([Bailey et al. 2016](https://onlinelibrary.wiley.com/doi/full/10.1002/hyp.10933)). Através dos códigos foram gerados mapas de recarga de aquífero média mensal, mapa de carga hidráulica para o final do período de simulação, bem como as séries temporais de recarga de ambos os modelos hidrológicos. As bacias hidrográficas de estudo foram:

- Atibaia (somente região de cabeceira) (1.136,7 $km^2$)
- Camanducaia (1.040,1 $km^2$)
- Capivari (1.276,9 $km^2$)
- Corumbataí (1.704,2 $km^2$)
- Jundiaí (1.125,2 $km^2$)

O código nomeado *"sep_hidrograma.ipynb"* foi escrito para separar o hidrograma de vazão em escoamento de base e escoamento superficial. Para realizar a separação do hidrograma, utilizou-se a biblioteca Python *Hydrograph-py* ([Terink 2019](https://app.readthedocs.org/projects/hydrograph-py/downloads/pdf/latest/)).

Complementarmente elaborou-se um aplicativo com a finalidade de apresentar de forma interativa os resultados desse projeto bem como possibilitar o acesso às séries de vazão, escoamento de base e mapas de recarga de aquíferos. O aplicativo pode ser acessado [aqui](https://hidroapp-ubrzbjvsapplgmsjp96xwbx.streamlit.app/).

Este é um projeto para divulgar os procedimentos realizados, bem como os resultados da tese intitulada **DESEMPENHO DO MODELO HIDROLÓGICO SWAT NAS BACIAS HIDROGRÁFICAS DOS RIOS PIRACICABA, CAPIVARI E JUNDIAÍ: UMA ANÁLISE DO ESCOAMENTO DE BASE E DA RECARGA DE AQUÍFERO** desenvolvida no Programa de Pós-Graduação (PPG) do [Instituto Agronômico de Campinas (IAC)](https://www.iac.sp.gov.br/). <br>
![Logo-IAC](https://www.forumcampinas.org.br/wp-content/uploads/2014/11/iac-1.png "IAC")
