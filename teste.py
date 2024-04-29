import re

# String fornecida
string = """
Mais vendidoem Celulares e Smartphones

Smartphone Poco X3 PRO 256gb 8gb RAM – Phantom Black - Preto

4,8 de 5 estrelas
320

R$ 1.975,00R$1.975,00
R$ 2.075,00R$2.075,00

Receba Quinta-feira, 29 de jul - Terça-feira, 3 de ago Frete GRÁTIS

Mais opções de compraR$ 1.969,00(48 ofertas de novos)
"""

# Expressão regular para extrair classificação
classificacao_regex = r'(\d\.\d)\sde\s5\sestrelas'

# Procurar correspondência da classificação
match_classificacao = re.search(classificacao_regex, string)

# Verificar se a correspondência foi encontrada
if match_classificacao:
    classificacao = match_classificacao.group(1)
else:
    classificacao = None

# Imprimir classificação
print("Classificação:", classificacao)
