def calcular_media(nota1, nota2):
    """Calcula a média de duas notas."""
    return (nota1 + nota2) / 2


def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado."""
    if media >= 7:
        return "Aprovado"
    return "Reprovado"


def calcular_frequencia(presencas, total_aulas):
    """Calcula o percentual de frequência do aluno."""
    if total_aulas <= 0:
        raise ValueError("O total de aulas deve ser maior que zero")

    return (presencas / total_aulas) * 100


def realizar_matricula(nome, idade):
    """Realiza a matrícula de um aluno."""
    if not nome or idade < 5:
        return "Matrícula inválida"

    return "Matrícula realizada com sucesso"
