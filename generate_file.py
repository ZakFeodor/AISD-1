import random


def generate_file(file_name):
    with open(f'{file_name}.txt', 'w') as f:
        for i in range(100, 10_001, 100):
            sublist = [str(random.randint(-100_000, 100_000)) for _ in range(i)]
            f.write(' '.join(sublist) + '\n')
            