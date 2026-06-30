class Produto:
    def __init__(self, dados):
        # Usamos .get() para evitar erro se a chave não existir
        self.nome = dados.get('nome')
        self.validade = dados.get('validade')
        self.quantidade = dados.get('quantidade')
        self.preco = dados.get('preco')
        self.fornecedor = dados.get('fornecedor')
    
    def __str__(self):
        tratar = self.fornecedor if self.fornecedor else 'não encontrado'
        return f"Produto: {self.nome} | Validade: {self.validade} | Qtd: {self.quantidade} | Preço: R${self.preco} | fornecedor {tratar}" 

class ProdutoSeco(Produto):
    def __init__(self, dados, kg):
        super().__init__(dados) # Passa o dicionário para o Pai
        self.kg = kg            # Define o específico aqui
        
    def __str__(self):
        return f"{super().__str__()} | Kg: {self.kg}"    

class ProdutoLiquido(Produto):
    def __init__(self, dados, ml):
        super().__init__(dados)
        self.ml = ml
    
    def __str__(self):
        return f"{super().__str__()} | Ml: {self.ml}"

# --- COMO VOCÊ DEVE USAR NO SEU SISTEMA ---

# 1. Defina os dados fora da classe
dados_feijao = {'nome': 'Feijão', 'validade': '12/07/2026', 'quantidade': 2, 'preco': 5.6,'fornecedor': 'bruno'}
dados_leite = {'nome': 'Leite', 'validade': '12/07/2026', 'quantidade': 1, 'preco': 4.5,'fornecedor': 'bruno'}

# 2. Passe o dicionário para a classe
produtoseco = ProdutoSeco(dados_feijao, 2)
produtoliquido = ProdutoLiquido(dados_leite, 500)

print(produtoseco) 
print(produtoliquido)
