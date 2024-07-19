def sum_matrix(*args):
    args_size = len(args)

    if args_size == 0:
        return "No arguments"

    if args_size == 1:
        return "Only one argument"

    for arg in args:
        if not isinstance(arg, list):
            return "All arguments must be list type"

    args = sorted(args, key=lambda x: -len(x))

    matrix_sum = args[0]

    for index, matrices in enumerate(args[1::]):
        for j in range(len(matrices)):
            for i in range(len(matrices[j])):
                matrix_sum[j][i] += args[index + 1][j][i]

    return matrix_sum
