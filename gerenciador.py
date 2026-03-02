from modelos import Receita, Despesa
import csv

class GerenciadorFinanceiro:
    def __init__(self):
        self.despesas = []
        self.receitas = [] 

  //funções básicas para agregar e manipular receitas e despesas
    def add_receita(self, receita):
        self.receitas.append(receita)

    def add_despesa(self, despesa):
        self.despesas.append(despesa)

    def sum_receita(self):
        total_receita = 0
        for r in self.receitas:
            total_receita += r.valor
        return total_receita

    def sum_despesas(self):
        total_despesa = 0
        for d in self.despesas:
            total_despesa += d.valor
        return total_despesa

    def calcular_saldo(self):
        return self.sum_receita() - self.sum_despesas()

  //função dque gera o relatório mensal
    def relatorio_mensal(self, mes, ano):
        receitas_data = []
        despesas_data = []
        total_receitas_data = 0
        total_despesas_data = 0

        for r in self.receitas:
            if r.data.month == mes and r.data.year == ano:
                receitas_data.append(r)

        for d in self.despesas:
            if d.data.month == mes and d.data.year == ano:
                despesas_data.append(d)

        for r in receitas_data:
            total_receitas_data += r.valor

        for d in despesas_data:
            total_despesas_data += d.valor

        return {
        "receitas": receitas_data,
        "despesas": despesas_data,
        "total_receitas": total_receitas_data,
        "total_despesas": total_despesas_data,
        "saldo": total_receitas_data - total_despesas_data
    }


  //função de criação do arquivo csv, podendo também, no caso do nome ser de um arquivo já criado, agregar essas informaçãoes nesse arquivo
    def exportar_csv(self, nome_arquivo):
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Tipo", "Valor", "Descrição", "Categoria", "Data"])

            for r in self.receitas:
                writer.writerow(["Receita", r.valor, r.descricao, "", r.data])

            for d in self.despesas:
                writer.writerow(["Despesa", d.valor, d.descricao, d.categoria, d.data])
