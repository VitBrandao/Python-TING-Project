def exists_word(word, instance):
    data = instance.data

    final_object = []
    count_lines = []

    for file in data:
        indexed_list = enumerate(file["linhas_do_arquivo"])
        # print(indexed_list)
        for index, line in indexed_list:
            if word.lower() in line.lower():
                count_lines.append({"linha": index + 1})

        # print(count_lines)

        final_object.append({
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": count_lines,
            "palavra": word,
        })

    if count_lines.__len__() == 0:
        return count_lines

    return final_object


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
