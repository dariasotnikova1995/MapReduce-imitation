import os
import random
import string

def file_generator(directory, number_of_files, size):
    if not os.path.exists(directory):
        os.makedirs(directory)

    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(number_of_files):
        file_size = random.randint(size // 2, size)
        content = ''.join(random.choice(characters) for _ in range(file_size))
        with open(os.path.join(directory, f"file_{i}.txt"), 'w') as file:
            file.write(content)