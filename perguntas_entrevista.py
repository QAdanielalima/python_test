# Função para verificar palíndromo
def is_palindrome(word):
    # Inverta a string usando reversed() e join().
    reversed_str = ''.join(reversed(word))
    return word == reversed_str


# Teste. Verificação da função is_palindrome
def test_is_palindrome():
    # Defina a string de entrada
    input_str = "osso"

    # Execute a verificação do palíndromo
    result = is_palindrome(input_str)

    # Verifique se o resultado é True (verdadeiro) para um palíndromo
    assert result == True

    print("Teste aprovado! '" + input_str + "' é um palíndromo.")

# Importe o módulo matemático para acessar funções matemáticas
import math
# Calcule o fatorial de 5 usando a função fatorial do módulo matemático
print(math.factorial(5))