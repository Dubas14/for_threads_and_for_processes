import time
import multiprocessing

# Функція для пошуку дільників числа
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Синхронна версія факторизації
def factorize_sync(*numbers):
    result = []
    for number in numbers:
        result.append(find_factors(number))
    return result

# Паралельна версія факторизації з використанням multiprocessing
def factorize_parallel(*numbers):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(find_factors, numbers)
    return result

# Основна функція, яка запускає і вимірює час обох версій
if __name__ == '__main__':
    numbers_to_factorize = [128, 255, 99999, 10651060]

    # Вимірюємо час для синхронної версії
    start_time = time.time()
    sync_results = factorize_sync(*numbers_to_factorize)
    sync_end_time = time.time()

    # Вимірюємо час для паралельної версії
    parallel_start_time = time.time()
    parallel_results = factorize_parallel(*numbers_to_factorize)
    parallel_end_time = time.time()

    # Виводимо результати і час виконання
    print("Synchronous results:")
    for result in sync_results:
        print(result)

    print(f"Synchronous execution time: {sync_end_time - start_time} seconds\n")

    print("Parallel results:")
    for result in parallel_results:
        print(result)

    print(f"Parallel execution time: {parallel_end_time - parallel_start_time} seconds\n")

    # Перевірка коректності результатів
    a, b, c, d = sync_results
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


