from PDF_OCR_Reader.String_compare import String_Compare


def is_sublist(a, b):
    if not a: return True
    if not b: return False
    return b[:len(a)] == a or is_sublist(a, b[1:])

def is_substring(str1, str2):
    sc = String_Compare()
    str1 = sc.strip_punctuations(str1)
    w1 = sc.prepare_phrase(str1,0)
    str2 = sc.strip_punctuations(str2)
    w2 = sc.prepare_phrase(str2,0)
    print(w1)
    print(w2)
    if is_sublist(w2, w1):
        return True
    else: return False


if __name__ == "__main__":
    str1 = 'hs Light Trucks\n(0 - 10,000 Lbs.\n\nG.V.W.)'
    str2 = 'Light Trucks (0 - 10,000 Lbs. G.V.W.)'
    print(str_compare_with_tokenize(str1, str2))
