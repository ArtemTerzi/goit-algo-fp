import random
import matplotlib.pyplot as plt

def main():
    analytical_probs = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

    N = 100000

    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(N):
        cube_1 = random.randint(1, 6)
        cube_2 = random.randint(1, 6)
        s = cube_1 + cube_2
        sum_counts[s] += 1

    sum_probs = {s: count / N for s, count in sum_counts.items()}

    header = f"{'Сума':>4} | {'Монте-Карло':>13} | {'Аналітична':>13}"
    print(header)
    print('-' * len(header))

    for total in range(2, 13):
        mc_prob = sum_probs[total] * 100
        an_prob = analytical_probs[total] * 100
        print(f"{total:>4} | {mc_prob:11.2f}% | {an_prob:11.2f}%")


    plt.figure(figsize=(10, 6))
    plt.bar(sum_probs.keys(), [p * 100 for p in sum_probs.values()],
            alpha=0.6, color='purple', label='Монте-Карло')

    plt.plot(list(analytical_probs.keys()), [p * 100 for p in analytical_probs.values()],
            'o-', color='green', label='Аналітична')

    plt.title('Розподіл ймовірностей сум кубиків')
    plt.xlabel('Сума значень двох кубиків')
    plt.ylabel('Ймовірність (%)')
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()