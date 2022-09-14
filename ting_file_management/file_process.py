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

    file_name = dequeue_file["nome_do_arquivo"]

    return print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance_item_to_str = str(instance.search(position))

        return sys.stdout.write(instance_item_to_str)
    except IndexError:
        return sys.stderr.write("Posição inválida")


"""
5.1 - Será validado que ao executar a função file_metadata com sucesso deverá exibir a mensagem correta via stdout e;

5.2 - Será validado que ao executar a função file_metadata com posição inválida deverá exibir a mensagem correta via stderr
"""
