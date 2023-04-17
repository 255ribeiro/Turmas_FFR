# Modelagem da Informação da Construção

## Edital da AV2


### Atividade em equipe ( 4 ou 5 membros)

Podendo ser a mesma equipe do trabalho anterior

#### Descrição geral do trabalho

1. A equipe deve elaborar um projeto simplificado no Revit e exportar para IFC
2. Para verificar a exportação **recomenda-se** a utilização do Software BimCollad na versão gratúita.

#### Descrição do projeto

Um projeto de dois pavimentos desenvolvido em 3 arquivos do Revit:

##### Arquivos do projeto
1. Um arquivo base para georreferenciar os demais
1. Um para o modelo arquitetônico
2. Um para o modelo de estrutura
   
##### O projeto deve apresentar por pavimento:
1. Pav. térreo: Algumas lojas faceadas com o lote e uma portaria de acesso ao pavimento superior
2. Pav. Superior: Uma circulação geral e um conjunto de salas comerciais. Cada sala deve ter um espaço de trabalho e um sanitário.

#### Simplificações:
1. O terreno deve ser modelado como um plano
2. A cobertura pode ser representada por uma laje (ou cobertura) simples com camada única
3. As lajes podem ser modeladas no projeto de arquitetura e ignoradas no projeto de estruturas
4. O projeto de estrutura deve conter pilares e vigas de sustentação do primeiro pavimento e da cobertura. Todos os elementos de fundação podem ser desconsiderados.

#### Especificações de exportação dos arquivos IFC
1. O grupo deve representar uma empresa de projeto e construção. A organização deve ter um nome e este nome deve ser exportado para o IFC de forma apropriada.
1. O Nome dos componentes da equipe dever ser exportados para o IFC no parâmetro apropriado, separados por ponto e vírgula. Opcionalmentepode-se exportar também os e-mails dos autores. também separados por ponto e vírgula.
1. O projeto não tem nenhuma obrigação de encaixar em um terreno no mundo real, mas devemos usar coordenadas de georreferenciaento naexportação. Elas podem ser definidas pela equipe.
1. Um endereço deve ser exportado como endereço do terreno.
2. Informações sobre o sistema de coordenadas utilizado devem ser exportadas
3. As portas e paredes devem ser marcadas como internas e externas
4. Os ambientes devem ser exportados e agrupados em diferentes zonas (IfcZones) escolhidas pelo grupo
5. As paredes devem ter camadas e estas devem ser exportadas de forma adequada.
6. Parâmetros especiais definidos pelo grupo devem ser exportados em um Pset criado pelo grupo.
7. Quantitativos básicos das paredes devem ser exportados.

#### BilCollab project
1. Devem apresentar as informações eportadas

1. Deve ter SmartViews salvas para visualizar:
   1. Paredes externas e internas
   2. Portas internas e extarnas
   3. Diferentes materias das paredes.
   4. As diferentes Zonas

    

#### Produtos a serem entregues:

Um arquivo .ZIP contendo:

  1. Os arquivos originais do Revit
  2. Os arquivos IFC exportados
  3. O arquivo de projeto do BimCollab (ou do programa de verificação do IFC utilizado)
  4. Opcionalmente pode-se enviar um arquivo de texto com explicações sobre as informações craidas e exportadas
  5. Os arquivos devem ter uma organização de pastas definida pelo grupo.

#### A data de entrega deve ser consultada no cronograma da disciplina
