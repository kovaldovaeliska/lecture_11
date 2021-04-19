import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seqs = json.load(json_file)

    return seqs[key]

def linear_search(sequence, number):
    positions = []
    count = 0
    while i < len(sequence):
        if sequence[i] == number:
            positions.append(i)
            count += 1
        i += 1

    return {'positions': positions,
            'count': count,
            }

def pattern_search(seq, pattern):
    position = set()
    pattern_size = len(pattern)

    left_idx, right_idx = 0, pattern_size
    while right_idx < len(seq):
        if pattern == seq [left_idx:right_idx]:
            position.add(left_idx + pattern_size // 2)
        left_idx += 1
        right_idx += 1
    return position



def main():
    seq = read_data(file_name='sequential.json', key='unordered_numbers')
    results = linear_search(seq, number=5)
    seq = read_data(file_name='sequential.json', key='dna_sequence')
    results = pattern_search(seq, pattern= 'ATA')


if __name__ == '__main__':
    main()