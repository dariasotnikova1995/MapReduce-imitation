import os
import threading

def letter_counter_in_one_thread(directory, letter_to_find):
    count = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            count += content.count(letter_to_find)
    return count

def letter_counter_in_group(file_group, letter_to_find, result, index):
    count = 0
    for file_path in file_group:
        with open(file_path, 'r') as file:
            content = file.read()
            count += content.count(letter_to_find)
    result[index] = count

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]
    total_files = len(file_paths)
    files_per_thread = total_files // number_of_threads
    threads = []
    results = [0] * number_of_threads

    for i in range(number_of_threads):
        start_index = i * files_per_thread
        end_index = (i + 1) * files_per_thread if i != number_of_threads - 1 else total_files
        file_group = file_paths[start_index:end_index]
        thread = threading.Thread(target=letter_counter_in_group, args=(file_group, letter_to_find, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)