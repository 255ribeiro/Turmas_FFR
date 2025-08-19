# Modelagem da Informação da Construção

## Edital da AV2

### Atividade em equipe ( 4 ou 5 membros)

Podendo ser a mesma equipe do trabalho anterior

#### Descrição geral do trabalho

1. A equipe deve elaborar um projeto simplificado no Editor (Revit, Archicad, ...) a sua escolha e exportar para IFC
2. A verificação do IFC será feita pelo BimCollab.

#### Descrição do projeto

Um projeto de dois pavimentos desenvolvido em 3 arquivos do Editor escolhido:

##### Arquivos do projeto
1. Um arquivo base para georreferenciar os demais
1. Um para o modelo arquitetônico
2. Um para o modelo de estrutura
   
##### O projeto deve apresentar:

Uma casa de dois pavimentos, no terreno indicado, contendo:

1. Pav. térreo: Sala de estar, jantar, cozinha, um sanitário ou lavado e área de serviço
2. Pav. Superior: dois quartos e um banheiro ou duas suites.

#### Simplificações:
1. O terreno deve ser modelado como um plano
2. A cobertura pode ser representada por uma laje (ou cobertura) simples com camada única
3. O projeto de estrutura deve conter pilares e vigas de sustentação do primeiro pavimento e da cobertura. Todos os elementos de fundação podem ser desconsiderados.

#### Especificações de exportação dos arquivos IFC
1. O grupo deve representar uma empresa de projeto e/ou construção. A organização deve ter um nome e este nome deve ser exportado para o IFC de forma apropriada.
1. O Nome dos componentes da equipe dever ser exportados para o IFC no parâmetro apropriado, separados por ponto e vírgula. Opcionalmente pode-se exportar também os e-mails dos autores. também separados por ponto e vírgula.

1. Um endereço deve ser exportado como endereço do terreno.
2. Informações sobre o sistema de coordenadas geográficas utilizado devem ser exportadas.
3. As portas e paredes devem ser marcadas como internas e externas
4. Os ambientes devem ser exportados e agrupados em diferentes zonas (IfcZones) escolhidas pelo grupo.
5. As paredes devem ter camadas e estas devem ser exportadas de forma adequada, conforme especificação da Building smart.
6. As dimensões e valores das paredes devem ser exportados em um Qset com nome personalizado.
7. Quantitativos básicos das paredes devem ser exportados.

#### BilCollab project
1. Devem apresentar as informações exportadas

1. Deve ter SmartViews salvas para visualizar:
   1. Paredes externas e internas com cores diferentes
   2. Portas internas e externas com cores diferetnes
   3. Diferentes materias das paredes.
   4. As diferentes Zonas separadas por cor.

#### Produtos a serem entregues:

Em uma pasta compartilhada no serviço de armazenamento em núvem, configurado pelo professor, devem constar os seguintes arquivos.

  1. Os arquivos originais do editor
  2. Os arquivos IFC exportados
  3. O arquivo de projeto do BimCollab 
  4. Opcionalmente pode-se enviar um arquivo de texto com explicações sobre as informações criadas e exportadas


#### A data de entrega deve ser consultada no cronograma da disciplina
