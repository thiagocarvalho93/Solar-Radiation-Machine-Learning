# Solar Radiation Machine Learning

### Objetivo
A partir de um conjunto de dados do *DataLogger* da estação meteorológica, desenvolver um modelo de *Machine Learning* capaz de, a partir das variáveis climáticas, determinar o valor da irradiação direta normal (DNI) para um determinado período de tempo.
Este valor, então, será utilizado posteriormente para cálculos de projeto de uma usina heliotérmica.

---
### Arquivos

1. CR1000.csv - **Dados** do *Datalogger* da Estação Meteorológica.
2. Tratamento-de-Dados.ipynb - Utilizou-se o Pandas e outras ferramentas para **importar e tratar** os dados da tabela do *DataLogger*. Além disso, foram calculadas, a partir dos dados, variáveis adicionais referentes à **posição do Sol** e **Radiação Extraterrestre**.
3. Features-Engineering.ipynb - Análise gráfica e qualitativa dos dados.
4. Estimating, Forecasting e Nowcasting.ipynb - **Desenvolvimento** e **análise** dos modelos de *Machine Learning* propriamente ditos a partir dos dados tratados. 
