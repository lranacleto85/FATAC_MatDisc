import math

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def combinacao(opcao, n, k):
    resultado = 0

    if opcao == 1:  # Permutacao de n
        resultado = fatorial(n)
    elif opcao == 2:  # Arranjo de n tomados de k em k
        if k > n:
            resultado = -1  # Arranjo não é possível quando k > n
        else:
            resultado = fatorial(n) // fatorial(n - k)
    elif opcao == 3:  # Combinacao de n tomados de k em k
        if k > n:
            resultado = -1  # Combinação não é possível quando k > n
        else:
            resultado = fatorial(n) // (fatorial(k) * fatorial(n - k))
    else:
        print("OPCAO", opcao, ": OPERACAO INEXISTENTE")
        resultado = -2

    return resultado

# NAO MODIFICAR O CODIGO TESTE ABAIXO///
if __name__ == "__main__":
    n = 5
    k = 2
    print("***********************************************************")
    print("ANALISE COMBINATORIA (SEM REPETICAO)")
    print("Considerando n =", n, "e k =", k, "em cada uma das opcoes")
    print("***********************************************************")

    for opcao in range(1, 4):
        if opcao == 1:
            print("OPCAO", opcao, ": P(", n, ") =", combinacao(opcao, n, k))
        elif opcao == 2:
            print("OPCAO", opcao, ": A(", n, ",", k, ") =", combinacao(opcao, n, k))
        elif opcao == 3:
            print("OPCAO", opcao, ": C(", n, ",", k, ") =", combinacao(opcao, n, k))
        else:
            print("OPCAO", opcao, ": OPERACAO INEXISTENTE")

    # TESTANDO ALGUNS CASOS
    print("\n***********************************************************")
    print("*** Analisando alguns casos validos e invalidos ***")
    print("***********************************************************")
    nota = 0.0
    soma = 0

    if combinacao(1, 0, 1) == 1:
        soma = 1 + soma
        print("P(0) =", combinacao(1, 0, 1), ", resposta correta")
    if combinacao(1, 0, 1) != 1:
        print("Sua resposta: P(0) =", combinacao(1, 0, 1))
        print("Mas P(0) = 1, resposta incorreta")

    if combinacao(1, 1, 1) == 1:
        soma = 1 + soma
        print("P(1) =", combinacao(1, 1, 1), ", resposta correta")
    if combinacao(1, 1, 1) != 1:
        print("Sua resposta: P(1) =", combinacao(1, 1, 1), end=" ")
        print("Mas P(1) = 1, resposta incorreta")

    if combinacao(1, 5, 2) == 120:
        soma = 1 + soma
        print("P(5) =", combinacao(1, 5, 2), ", resposta correta")
    if combinacao(1, 5, 2) != 120:
        print("Sua resposta: P(5) =", combinacao(1, 5, 2), end=" ")
        print("Mas P(5) = 120, resposta incorreta")

    if combinacao(1, -5, 2) == -2:
        soma = 1 + soma
        print("P(-5) nao existe pq n<0, resposta correta")
    if combinacao(1, -5, 2) != -2:
        print("Sua resposta: P(-5) =", combinacao(1, -5, 2), end=" ")
        print("Mas P(-5) nao existe pq n<0, resposta incorreta")

    if combinacao(2, 5, 2) == 20:
        soma = 1 + soma
        print("A(5,2) =", combinacao(2, 5, 2), ", resposta correta")
    if combinacao(2, 5, 2) != 20:
        print("Sua resposta: A(5,2) =", combinacao(2, 5, 2), end=" ")
        print("Mas A(5,2) = 20, resposta incorreta")

    if combinacao(2, 2, 5) == -2:
        soma = 1 + soma
        print("A(2,5) nao existe pq n<k, resposta correta")
    if combinacao(2, 2, 5) != -2:
        print("Sua resposta: A(2,5) =", combinacao(2, 2, 5), end=" ")
        print("Mas A(2,5) nao existe pq n<k, resposta incorreta")

    if combinacao(3, 5, 2) == 10:
        soma = 1 + soma
        print("C(5,2) =", combinacao(3, 5, 2), ", resposta correta")
    if combinacao(3, 5, 2) != 10:
        print("Sua resposta: C(5,2) =", combinacao(3, 5, 2), end=" ")
        print("Mas C(5,2) = 10, resposta incorreta")

    if combinacao(3, 2, 5) == -2:
        soma = 1 + soma
        print("C(2,5) nao existe pq n<k, resposta correta")
    if combinacao(3, 2, 5) != -2:
        print("Sua resposta: C(2,5) =", combinacao(3, 2, 5), end=" ")
        print("Mas C(2,5) nao existe pq n<k, resposta incorreta")

    nota = soma

    print("\n***************************")
    print("Nota da atividade = %.2f" % (10 * nota / 8))
    print("*****************************")
