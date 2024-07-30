import time
from file_generator import file_generator
from letter_counter import letter_counter_in_one_thread, letter_counter_in_n_threads

def client_code(directory, number_of_files, size, letter_to_find, number_of_threads):
    print("Generating files...")
    file_generator(directory, number_of_files, size)

    print("Counting letters in one thread...")
    start_time = time.time()
    count_single_thread = letter_counter_in_one_thread(directory, letter_to_find)
    time_single_thread = time.time() - start_time
    print(f"Count (single thread): {count_single_thread}, Time: {time_single_thread} seconds")

    print("Counting letters in multiple threads...")
    start_time = time.time()
    count_multi_thread = letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
    time_multi_thread = time.time() - start_time
    print(f"Count (multi thread): {count_multi_thread}, Time: {time_multi_thread} seconds")

    print("Execution complete.")


if __name__ == "__main__":
    client_code('files', 200, 1000000, 'a', 4)