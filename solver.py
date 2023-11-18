mutagen_file = "mutagens.txt"
exitus_file = "exitus.txt"

def load_mutagens(filename):
    """Loads the mutagens from the given file and returns a dictionnary [mutagen_name] = sequence.
    With sequence being list of atoms"""
    mutagens = {}
    with open(filename) as mutagen_data:
        for line in mutagen_data:
            name, sequence = line.split(":")
            name = name.replace(" ", "")
            sequence = sequence[:-1]
            sequence = sequence[1:]
            sequence = sequence.split(" ")
            mutagens[name] = sequence

    return mutagens

def combine_sequences(seq1, seq2):
    """Creates a new sequence by combining 2 sequences"""
    result_sequence = seq1.copy()

    for atom in seq2:
        if atom not in result_sequence:
            if atom[0] == '-':
                negative = atom[1:]
                if negative in result_sequence:
                    result_sequence.remove(negative)
            else:
                result_sequence.append(atom)

    return [atom for atom in result_sequence if atom[0] != "-"]

def get_negatives(mutagens):
    """Gets a list of all the negatives atoms available in the given mutagens dict"""
    negatives = []
    for seq in mutagens.values():
        for atoms in seq:
            if atoms[0] == '-':
                negatives.append(atoms)
    
    return negatives

def solve(mutagens, exitus_sequence, current_sequence = [], current_combinaison = []):
    if (current_sequence == exitus_sequence):
        return current_combinaison
    
    # Prune if current sequence is longer than target sequence
    # !! This is a false assumption but unlikely to break !!
    # eg : sequence RJ UT EU CC -MO -JT -M1 -AL -NI contains more negatives than positives therefore adding this sequence will shorten the current one
    if (len(current_sequence) > len(exitus_sequence)):
        return []

    # Prune if one of the sequence atom is not inside the target and there are no negative opposite available to cancel it
    if (current_sequence != [] and current_sequence[0] != exitus_sequence[0]):
        negatives = get_negatives(mutagens)
        for atoms in current_sequence:
            if atoms not in exitus_sequence and atoms not in negatives:
                return []
        

    for name, sequence in mutagens.items():
        sub_mutagens = mutagens.copy()
        del sub_mutagens[name]
        combinaison = solve(sub_mutagens, exitus_sequence, combine_sequences(current_sequence, sequence), current_combinaison + [name] )
        if combinaison != []:
            return combinaison


    return []


def main():
    print("Loading mutagens from files .....", end="")
    mutagens = load_mutagens(mutagen_file)
    exitus_sequence = load_mutagens(exitus_file)["Exitus"]
    print(" OK")

    print("Starting solver .....")
    result = solve(mutagens, exitus_sequence)
    if (result != []):
        print("Puzzle solved ! The orderer combinaison is :\n", result)
    else:
        print("Solver failed to find a solution. Make sure that the given mutagens sequences are correct")


main()
        