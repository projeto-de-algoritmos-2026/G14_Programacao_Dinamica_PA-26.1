from src.knapsack import plan_studies
from src.subject import Subject


def main() -> None:
    subjects = [
        Subject("Knapsack", time=3, importance=10, difficulty=8, mastery=4),
        Subject("LIS", time=2, importance=7, difficulty=5, mastery=6),
        Subject("Bellman-Ford", time=4, importance=9, difficulty=9, mastery=3),
    ]

    result = plan_studies(subjects, available_time=7)

    print("Plano de estudos sugerido")
    print(f"Pontuacao maxima: {result.max_score}")
    print(f"Tempo utilizado: {result.time_used}h")
    print("Conteudos escolhidos:")
    for subject in result.selected_subjects:
        print(f"- {subject.name}")


if __name__ == "__main__":
    main()
