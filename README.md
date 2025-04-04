# Códigos - Modelagem hidrológica

Códigos Python (*Jupyter notebooks*) para processar e analisar dados de recarga de aquífero das sub-bacias PCJ, referentes ao período de janeiro de 1985 a dezembro de 2020, estimados por meio de modelagem hidrológica, com os modelos hidrológicos [**SWAT**](https://swat.tamu.edu/) e **SWAT-MODFLOW** ([Bailey et al. 2016](https://onlinelibrary.wiley.com/doi/full/10.1002/hyp.10933)). Através dos códigos foram gerados mapas de recarga de aquífero média mensal, mapa de carga hidráulica para o fim do período de simulação, bem como as séries temporais de recarga de ambos os modelos hidrológicos. As bacias hidrográficas de estudo foram:

- Atibaia (somente região de cabeceira) (1.136,7 $km^2$)
- Camanducaia (1.040,1 $km^2$)
- Capivari (1.276,9 $km^2$)
- Corumbataí (1.704,2 $km^2$)
- Jundiaí (1.125,2 $km^2$)

O código nomeado *sep_hidrograma.ipynb* foi escrito para separar o hidrograma de vazão em fluxo de base e escoamento superficial. Para realizar a separação do hidrograma, utilizou-se a biblioteca Python *Hydrograph-py* ([Terink W, 2019](https://app.readthedocs.org/projects/hydrograph-py/downloads/pdf/latest/)).

Foi desenvolvido um aplicativo via web para divulgação dos resultados de fluxo de base e recarga de aquífero. O app pode ser acessado [aqui](https://hidroapp-ubrzbjvsapplgmsjp96xwbx.streamlit.app/).

Este é um projeto da tese desenvolvida na Pós-Graduação do [Instituto Agronômico de Campinas (IAC)](https://www.iac.sp.gov.br/). <br>
![Logo-IAC](https://www.forumcampinas.org.br/wp-content/uploads/2014/11/iac-1.png "IAC")
