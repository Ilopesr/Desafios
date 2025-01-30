karnaugh_table = [
    # A  B  C  S
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]


def check_list(list):
    final_list = []
    for i in list:
        if i in list:
            pass
        else:
            final_list.append(i)
    return final_list


def get_karnaugth_combinations(table):
    combinations = []
    combinations_in_dict = {}
    for i in table:
        for j in i[3:]:
            combinations.append("%s%s" % (i[j], i[j + 1]))
    clean_combinations = sorted(list(set(combinations)))

    for i in clean_combinations:
        combinations_in_dict[str(i)] = []

    return combinations_in_dict


def create_karnaugth_table_combinations(table):
    new_table = [x[:3] for x in table if x[-1] != 0]
    true_table = [[] for i in range(len(new_table))]
    for index, i in enumerate(new_table):
        for i_index, j in enumerate(i):
            if j == 0 and i_index == 0:
                true_table[index].append("!A")
            elif j == 1 and i_index == 0:
                true_table[index].append("A")
            elif j == 0 and i_index == 1:
                true_table[index].append("!B")
            elif j == 1 and i_index == 1:
                true_table[index].append("B")
            elif j == 0 and i_index == 2:
                true_table[index].append("!C")
            elif j == 1 and i_index == 2:
                true_table[index].append("C")

    return list(set(tuple(sublist) for sublist in true_table))


true_table = create_karnaugth_table_combinations(karnaugh_table)


def simplify_table(true_table):
    to_list = [list(sub) for sub in true_table]


print(simplify_table(true_table))
