import pandas as pd

C1_PATH = './gbk/char/GB2312_C1.txt'
C2_PATH = './gbk/char/GB2312_C2+.txt'
ALPH_PATH = './gbk/char/alphabets.txt'
# ASC_JP_PATH = './gbk/char/ASCII_JP_GBK_keys.txt'
SYMB_PATH = './gbk/char/symbols.txt'
AGRE_PATH = './gbk/char/agreement_char.txt'

def compose_key_txt(new_compose_name, *k_path):
  df = None
  for path in k_path:
    if df is None:
      df = pd.read_table(path, sep='\t', header=None, quoting=3)
    else:
      df = df.append(pd.read_table(path, sep='\t', header=None)).reset_index(drop=True)
  # pass
  df = pd.DataFrame({0: df[0].unique()})
  df.to_csv(new_compose_name, sep='\t', header=False, index=False, quoting=3)


compose_key_txt('./gbk/char/compose/c1.txt', C1_PATH)
compose_key_txt('./gbk/char/compose/c1_alph_symb_arge.txt', C1_PATH, ALPH_PATH, SYMB_PATH, AGRE_PATH)
compose_key_txt('./gbk/char/compose/c1_c2.txt', C1_PATH, C2_PATH)
compose_key_txt('./gbk/char/compose/c1_c2_alph_symb_arge.txt', C1_PATH, C2_PATH, ALPH_PATH, SYMB_PATH, AGRE_PATH)
