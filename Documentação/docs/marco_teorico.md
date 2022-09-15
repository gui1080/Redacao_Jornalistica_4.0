# Redação Jornalística 4.0

## Motivação

Redações Jornalísticas são um caso de estudo ideal para a modelagem de um processo intensivo em conhecimento, por conta da velocidade na qual os processos devem lidar com uma grande quantidade de informação além de uma grande quantidade de partes envolvidas.

É muito complexo o processo de observar e mapear como este o workflow funciona na vida real. Se mostra recorrente não só que o processo não ocorra da mesma maneira entre iterações, mas que o mesmo mude estruturalmente em tempo de execução, diferenciando-se de um processo clássico. Neste momento surgem Decisões de difícil resolução, assim é necessário um sistema que documente e dê suporte para a visualização e execução de uma tarefa no contexto da Redação Jornalística moderna.

# Processo Estruturados e Processos Não Estruturados

As seguintes imagens apresentam por objetivo diferenciar um Processso Estruturado de um Processo Não Estruturado.

![Estruturado](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documenta%C3%A7%C3%A3o/estruturado.jpeg?raw=true)

Um processo Estruturado apresenta uma divisão clara entre as partes envolvidas, o que elas fazem e quando elas realizam a sua ação.

![Não Estruturado](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documenta%C3%A7%C3%A3o/n_estruturado.jpeg?raw=true)

Esta nova maneira de representar um processo acaba por ser mais completa ao definir o que acontece no caso de estudo em questão. Quando uma informação chega na Redação Jornalística, ela deve ser rápidamente tratada. Caso a informação que se deseje publicar ou armazenar seja tratada por meio de um processo Estruturado, existe uma chance muito grande que se perca o momento ideal de publicação da matéria, ou que ela acabe "presa" em uma parte do processo. Na realidade o ambiente descrito é altamente dinâmico e colaborativo, logo a estrutura de "Piscina para Lazer" em contraste com a estrutura de "Piscina Olímpica" é mais eficiênte ao levantar o funcionamento deste ambiente. Na "Piscina para Lazer", os processos são boias que flutuam podendo avançar ou regredir em termos de execução, e os Agentes envolvidos acabam por colaborar com uma tarefa na medida na qual a urgência existe.

É com essa mentalidade que se enxergou o desenvolvimento deste software de suporte, também visando suporte semântico.

*Fonte das imagens: João Pedro Souza Nunes.*

### Visão do Produto

_PARA_ Jornalistas e Empresas de Comunicação.

_QUE_ precisam produzir, recuperar, armazenar, distribuir e divulgar conteúdo multimídia.

O News Room 4.0 _É UM_  CMS (content management system) sistema de gerenciamento de conteúdo semântico e inteligente.

_QUE_ produz conteúdo e realiza gestão eficiente dele através  do entendimento das regras operacionais da redação jornalística.

_AO CONTRÁRIO_ dos jornais tradicionais que têm uma produção jornalística "engessada" ou dos jornais digitais que não têm um sistema de produção fluida.

O _NOSSO PRODUTO_ traz a organização de produções e processos de forma dinâmica para a distribuição de notícias em variadas plataformas de comunicação.

### Usuários

Cinco principais usuários: Jornalista , Fotógrafo, Revisor, Editor e CDOC.

#### 1 - Jornalista

- Quer escrever sua matéria jornalística.
- Login no sistema. 
- Começa a preencher um formulário para a produção jornalística de acordo com o guia abaixo.

![Input](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documenta%C3%A7%C3%A3o/user_input.png?raw=true)

#### 2 - Fotógrafo

- Classificação das fotos de acordo com as necessidades das matérias

#### 3 - Revisor 

- Revisa o texto.

#### 4 - Editor 

- Aprova a matéria para a publicação ou arquiva. 

#### 5 - Centro de documentação (CDOC)

- Arquiva todas as matérias jornalísticas publicadas ou não, bem como as outras mídias.
- É muito comum que um processo na Redação Jornalística realize um trabalho mas que não seja vinculado na mídia.

![Documentacao](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documenta%C3%A7%C3%A3o/cdoc.png?raw=true)

## Estrutura do projeto final

A visão do projeto para a primeira sprint prevê a construção de uma API em Django/Python, para que exista suporte a comunicação com Frontent feito em React. A linguagem Python se mostra mais moldável e foi excolhida com o objetivo de dar suporte para anotação semântica de informações, com o uso de ontologias.

![Arquitetura](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documenta%C3%A7%C3%A3o/arq.jpg?raw=true)