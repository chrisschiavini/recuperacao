class Soma:
    @staticmethod
    def calcula_dados(dados):
        resultado = 0
        for numero in dados:
            resultado = resultado + numero
        return resultado
dados = [5,9,7]

resultado = Soma.calcula_dados(dados)
print("A soma dos valores é igual a: " + str(resultado))
