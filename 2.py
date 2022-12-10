def get_phonetic_matches(word, file):
    word = word.strip().lower()
    with open(file, 'r') as f:
        vocab = f.readlines()
    vocab = [v.strip().lower() for v in vocab]
    
    ph = phonetics.dmetaphone(word)
    sim = list()
    for w, e in zip(vocab, phonet_file_list):
        if e[0] == ph[0]:
            sim.append(w)
            
    return sim