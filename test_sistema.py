from sistema import (
    calcular_media,
    verificar_aprovacao,
    calcular_frequencia,
    realizar_matricula
)


# Teste 1 - Calcular média
def test_calcular_media():
    resultado = calcular_media(8, 6)
    assert resultado == 10  # ERRO PROPOSITAL


# Teste 2 - Verificar aprovação
def test_verificar_aprovacao():
    resultado = verificar_aprovacao(8)
    assert resultado == "Aprovado"


# Teste 3 - Calcular frequência
def test_calcular_frequencia():
    resultado = calcular_frequencia(18, 20)
    assert resultado == 90


# Teste 4 - Realizar matrícula
def test_realizar_matricula():
    resultado = realizar_matricula("João", 18)
    assert resultado == "Matrícula realizada com sucesso"
