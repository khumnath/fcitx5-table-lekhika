consonant_transliteration = {
    "क": ["k"],
    "ख": ["K", "kh"],
    "ग": ["g"],
    "घ": ["G", "gh"],
    "ङ": ["ng"],
    "च": ["c", "ch"],
    "छ": ["chh", "Ch"],
    "ज": ["j"],
    "झ": ["jh", "J"],
    "ञ": ["jn"],
    "ट": ["T"],
    "ठ": ["Th"],
    "ड": ["D"],
    "ढ": ["Dh"],
    "ण": ["N"],
    "त": ["t"],
    "थ": ["th"],
    "द": ["d"],
    "ध": ["dh"],
    "न": ["n"],
    "प": ["p"],
    "फ": ["ph", "f"],
    "ब": ["b"],
    "भ": ["bh", "B"],
    "म": ["m"],
    "य": ["y"],
    "र": ["r"],
    "ल": ["l"],
    "व": ["w", "v"],
    "श": ["sh"],
    "ष": ["Sh"],
    "स": ["s"],
    "ह": ["h"],
    "क्ष": ["ksh"],
    "क्स": ["ks"],
    "त्र": ["tr"],
    "ज्ञ": ["jnj"]
}

vowel_sign_transliteration = {
    "ा": "aa", 
    "ि": "i",
    "ी": "ee",
    "ु": "u",
    "ू": "oo",
    "ृ": "Ri",
    "ॄ": "Ree",
    "े": "e",
    "ै": "ai",
    "ो": "o",
    "ौ": "au"
}

vowel_transliteration = {
    "a": ["अ", "आ", "ए"],
    "aa": "आ",
    "A": ["आ", "ए"],
    "i": ["इ", "ई", "ऐ"],
    "ii": "ई",
    "I": ["ई", "ऐ"],
    "ee": "ई",
    "u": ["उ", "ऊ", "यु"],
    "uu": "ऊ",
    "oo": "ऊ",
    "U": "ऊ",
    "Ri": "ऋ",
    "Lri": "ऌ",
    "lri": "ऌ",
    "lree": "ॡ",
    "e": ["ए", "इ"],
    "E": ["ए", "इ"],
    "ai": "ऐ",
    "o": "ओ",
    "au": "औ"
}

output = {}

def handle_multi_value_transliteration(k_value, item):
    for alt_value in item:
        output[k_value + alt_value] = k_key + g_key
        f.write(f"{k_value + alt_value} {k_key + g_key}\n")

with open('table.txt', 'w') as f:
    # Write the contents of headers.txt into table.txt
    with open('header.txt', 'r') as header:
        for line in header:
            f.write(line)
    with open('symbols.txt', 'r') as symbol:
        for line in symbol:
            f.write(line)
    with open('numbers.txt', 'r') as symbol:
        for line in symbol:
            f.write(line)        
    f.write("\n## Vowels\n")

    for v_key, v_values in vowel_transliteration.items():
        for v_value in v_values:
            f.write(f"{v_key} {v_value}\n")
    f.write("\nam अं\naM अं\naH अः\naum ॐ\n")

    f.write("\n## Half Consonants\n")

    for k_key, k_values in consonant_transliteration.items():
        for k_value in k_values:
            output[k_value] = k_key + "्"
            f.write(f"{k_value} {k_key}्\n")

    f.write("\n## Full Consonants\n")

    for k_key, k_values in consonant_transliteration.items():
        for k_value in k_values:
            if k_value + "a" not in output:
                output[k_value + "a"] = k_key
                f.write(f"{k_value + 'a'} {k_key}\n")

    f.write("\n## Devanagari Tables\nRi ऋ\n")

    for k_key, k_values in consonant_transliteration.items():
        for k_value in k_values:
            for g_key, g_value in vowel_sign_transliteration.items():
                if g_key != "":
                    if isinstance(g_value, list):
                        handle_multi_value_transliteration(k_value, g_value)
                    else:
                        output[k_value + g_key] = k_key + g_key
                        f.write(f"{k_value + g_value} {k_key + g_key}\n")
            if k_value.endswith("a"):
                f.write(f"{k_value}\\ {k_key}्\n")
