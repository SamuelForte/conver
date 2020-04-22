def main():
    # converte qualquer base de bin ate hex
    def base_qualquer_para_decimal(base, numero):
        lista = ['a', 'b', 'c', 'd', 'e', 'f']
        resultado = 0
        expoente = 0
        i = len(numero) - 1

        while i >= 0:
            if numero[i] == '-':
                break

            if numero[i].lower() in lista:
                resultado += (lista.index(numero[i].lower()) + 10) * pow(int(base), expoente)
            else:
                resultado += int(numero[i]) * pow(int(base), expoente)
            
            expoente += 1
            i -= 1

        print(resultado) if numero[0] != '-' else print('-' + str(resultado))

    base_qualquer_para_decimal(input('Digite a base: '), input('Digite o Numero: '))

main()