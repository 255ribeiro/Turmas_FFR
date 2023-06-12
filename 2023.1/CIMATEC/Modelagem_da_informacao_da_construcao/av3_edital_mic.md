# Modelagem da Informação da Construção

## Edital da AV3


### Atividade em equipe ( 4 ou 5 membros).

Podendo ser a mesma equipe do trabalho anterior

#### Descrição geral do trabalho

1. A equipe devera configurar e executar testes de *clash detection* conforme instruções. 
2. Para a execução dos testes **recomenda-se** a utilização do Software Navisworks Manage (licença educacional)

#### Arquivos para o teste

Serão usados os arquivos de exemplo disponíveis [aqui](./Sample.zip) ou [aqui](https://download.bimcollab.com/support/ZOOM/Sample.zip)

##### Preparando o Navisworks
1. Crie um arquivo do Navisworks .nwf Com o nome da sua equipe
2. Importe os 3 arquivos da pasta design no seu projeto
   1. Caso o Navisworks não seja capaz de abrir o formato, pesquise uma alternativa.
   2. É possível que o arquivo de MEP apareça com uma rotação diferente dos demais modelos. Pesquise uma maneira de corrigir isso com transformações.

   
##### Configurações do Teste de clash 1
1. Crie um teste de *clash* entre:
   1. Os elementos do arquivo de estrutura
   2. OS elementos do arquivo MEP
1. Utilize tolerância de 10 cm 
2. Use o tipo de teste como HARD
 
#### Relatório 01

1. Crie grupos de *clashes* de acordo com o elemento estrutural que foi detectado.
   1. Os *clashes* que encontrarem colunas, vigas ou elementos de fundação devem ser atribuídos ao grupo de trabalho MEP
   2. Os *clashes* que paredes estruturais devem ser atribuídos ao grupo STR
   3. Os *clashes* que encontrarem *limestone walls* deve ser atribuídos ao grupo de trabalho ARQ
   4. Caso Aparecem clashes entre lajes, elas deve ser marcados como *Resolved*

1. Exporte as configurações de clash em formato .xml  
1. Gere um relatório em formato html
1. Gere um relatório em formato .xml


##### Configurações do Teste de clash 2
1. Crie um teste de *clash* entre (clash 2a):
   1. Os elementos do arquivo de estrutura
   2. OS elementos do arquivo Ventilation
1. Crie um teste de *clash* entre (clash 2b):
   1. Os elementos do arquivo de estrutura
   2. OS elementos do arquivo Heating and Plumbimg 
 
#### Relatório 02

1. Atribua os *clashes* do arquivo Ventilation ao grupo de trabalho VEN
1. Atribua os *clashes* do arquivo Heating and Plumbimg ao grupo de trabalho HaP
1. Exporte as configurações dos clashes em formato .xml  
1. Gere os relatórios em formato html
1. Gere os relatórios em formato .xml


#### Produtos a serem entregues:

Um arquivo .ZIP contendo:

Todos os arquivos usados no trabalho

#### A data de entrega deve ser consultada no cronograma da disciplina
