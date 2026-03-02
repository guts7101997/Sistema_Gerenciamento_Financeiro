from modelos import Receita, Despesa
from gerenciador import GerenciadorFinanceiro //importando classes criadas

//criando objetos e testando as funcionalidade
gerenciador = GerenciadorFinanceiro()

gerenciador.add_receita(
    Receita(3000, "Salário")
)

gerenciador.add_despesa(
    Despesa(200, "Aluguel", "Moradia")
)

gerenciador.add_despesa(
    Despesa(150, "Mercado", "Alimentação")
) 

print("Saldo:", gerenciador.calcular_saldo())

//gernado arquivo csv 
gerenciador.exportar_csv("relatorio.csv")
