
with open('name.txt', 'r+') as name_files:
    names = name_files.readlines()
    for name in names:
        filterd_name = name.strip().splitlines()

        for len_name in filterd_name:
            polished_name = len_name.replace(' ', '')
            final_length = f'{str(len(polished_name))} \n'

        with open('numerology.txt', 'a+') as f:
            f.write(final_length)
