from src.subject import Subject
from src.knapsack import plan_studies
from src.priority import subject_priority


def print_dp_table(subjects, dp_table, available_time):
    print("\n" + "=" * 75)
    print("MATRIZ DE PROGRAMAÇÃO DINÂMICA (KNAPSACK)")
    print("=" * 75)

    header = " " * 22
    for t in range(available_time + 1):
        header += f"{t:>4}"
    print(header)
    print("-" * len(header))

    print(f"{'Nenhum':<22}" + "".join(f"{v:>4}" for v in dp_table[0]))

    for i, subject in enumerate(subjects, start=1):
        row = f"{subject.name:<22}"
        row += "".join(f"{v:>4}" for v in dp_table[i])
        print(row)

    print("-" * len(header))
    print(f"⭐ Melhor pontuação final: {dp_table[-1][-1]}")
    print("=" * 75)


def main():
    subjects = [
        Subject(
            name="Weighted Scheduling",
            time=4,
            importance=10,
            difficulty=9,
            mastery=3,
        ),
        Subject(
            name="Bellman-Ford",
            time=3,
            importance=9,
            difficulty=8,
            mastery=4,
        ),
        Subject(
            name="Alinhamento de Sequên.",
            time=5,
            importance=10,
            difficulty=10,
            mastery=2,
        ),
        Subject(
            name="Selos",
            time=2,
            importance=7,
            difficulty=5,
            mastery=5,
        ),
        Subject(
            name="Maior Sub. Crescente",
            time=2,
            importance=8,
            difficulty=6,
            mastery=4,
        ),
    ]

    available_time = 8

    print("=" * 75)
    print("PROVAMAX - PLANEJADOR INTELIGENTE DE ESTUDOS")
    print("=" * 75)

    print(f"\nTempo disponível para estudo: {available_time} horas\n")

    print("Conteúdos disponíveis:\n")

    print(
        f"{'Conteúdo':<25}"
        f"{'Tempo':<8}"
        f"{'Imp.':<8}"
        f"{'Dif.':<8}"
        f"{'Dom.':<8}"
        f"{'Prioridade'}"
    )

    print("-" * 75)

    for subject in subjects:
        print(
            f"{subject.name:<25}"
            f"{str(subject.time) + 'h':<8}"
            f"{subject.importance:<8}"
            f"{subject.difficulty:<8}"
            f"{subject.mastery:<8}"
            f"{subject_priority(subject)}"
        )

    result = plan_studies(subjects, available_time)

    print("\n" + "=" * 75)
    print("PLANO DE ESTUDOS ENCONTRADO")
    print("=" * 75)

    print(f"\n Tempo utilizado: {result.time_used} horas")
    print(f" Pontuação máxima: {result.max_score}\n")

    print(" Conteúdos escolhidos:")
    for subject in result.selected_subjects:
        print(
            f"• {subject.name} "
            f"({subject.time}h | prioridade = {subject_priority(subject)})"
        )

    print("\n Conteúdos não escolhidos:")
    for subject in result.rejected_subjects:
        print(
            f"• {subject.name} "
            f"({subject.time}h | prioridade = {subject_priority(subject)})"
        )

    print_dp_table(subjects, result.dp_table, available_time)


if __name__ == "__main__":
    main()