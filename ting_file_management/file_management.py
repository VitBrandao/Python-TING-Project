import csv
import sys


def txt_importer(path_file):
    try:
        is_txt = path_file.endswith('.txt')

        if not is_txt:
            return print("Formato inválido", file=sys.stderr)

        else:
            file_lines_list = []

            with open(path_file) as file:
                read_file = csv.reader(file, delimiter="\n")

                for line in read_file:
                    file_lines_list.append(line[0])

                return file_lines_list

    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
