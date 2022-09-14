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
    instance_len = len(instance)

    if instance_len == 0:
        return print("Não há elementos")

    dequeue_file = instance.dequeue()
    # print(dequeue_file)
    file_name = dequeue_file["nome_do_arquivo"]
    # print(file_name)
    return print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
