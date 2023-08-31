import pandas as pd

csv_path = './2023.2/CIMATEC/Represetacao_digital_da_construcao/RDC_Calendario_de_Aulas_2023.2.csv'
mk_path = './2023.2/CIMATEC/Represetacao_digital_da_construcao/plano_rdc.md'
encoding = ''
df = pd.read_csv(csv_path, encoding= encoding  )
with open("my_markdown.md", 'w') as md:
  df.to_markdown(buf=md, tablefmt="grid")