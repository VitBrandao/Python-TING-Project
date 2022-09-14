from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    imported_file = txt_importer(path_file)
    instance_len = len(instance)

    for item in range(instance_len):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    final_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": imported_file.__len__(),
        "linhas_do_arquivo": imported_file
    }

    instance.enqueue(final_content)

    return sys.stdout.write(str(final_content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
