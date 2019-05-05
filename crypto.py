def _alphabet_index(t):
    return ord(t) - ord('a')

def shift_cypher(val, k):
    r = ''
    for c in val:
        new_pos = ord(c) + k
        if new_pos > ord('z'):
            new_pos = ord('a')
        r += chr(new_pos)
    return r

'''
perm = ZEBRASCDFGHIJKLMNOPQTUVWXY
'''
def sub_cypher(val, perm):
    r = ''
    for c in val:
        r += perm[_alphabet_index(c)]
    return r

def vigenere_cypher(val, k):
    ALPHABET = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    def _get_row(l):
        i_in_alph = _alphabet_index(l)
        return ALPHABET[i_in_alph:] + ALPHABET[:i_in_alph]

    r = ''
    for i, c in enumerate(val):
        generated_row = _get_row(k[i % len(k)])
        new_c = generated_row[_alphabet_index(c)]
        # or new_c = shift_cypher(c, _alphabet_index(k[i % len(k)]))
        r += new_c
    return r

if __name__ == '__main__':
    s = 'privacidadepublicatranparenciaprivada'

    s_cypher = shift_cypher(s, 3)
    print(s_cypher)

    s_cypher = sub_cypher(s, 'ZEBRASCDFGHIJKLMNOPQTUVWXY')
    print(s_cypher)

    s_cypher = vigenere_cypher(s, 'senha')
    print(s_cypher)
