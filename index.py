class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        if produto in self.produtos:
            index = self.produtos.index(produto)
            self.produtos[index].estoque -= quantidade
        else:
            produto.estoque -= quantidade
            self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = CarrinhoDeCompras()

    def comprar(self, produto, quantidade):
        self.carrinho.adicionar_produto(produto, quantidade)

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        print(f"Total da compra: R${total:.2f}")
        print("Compra finalizada. Obrigado por comprar conosco!")

# Exemplo de uso
produto1 = Produto("Camiseta", 29.99, 50)
produto2 = Produto("Calça Jeans", 59.99, 30)

cliente1 = Cliente("João")
cliente2 = Cliente("Maria")

cliente1.comprar(produto1, 3)
cliente2.comprar(produto1, 2)
cliente2.comprar(produto2, 1)

cliente1.finalizar_compra()
cliente2.finalizar_compra()
