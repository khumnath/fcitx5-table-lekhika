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
    "फ": ["ph", "P"],
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
    "त्र": ["tr"],
    "ज्ञ": ["jnj"]
}

vowel_transliteration = {
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
    "ौ": "au",
    "ं": "M",
    "ँ": "MM",
    "ः": "H",
    
}

output = {}

print("## Half Consonants")
# Add the half form of each consonant to the output
for k_key, k_values in consonant_transliteration.items():
    for k_value in k_values:
        output[k_value] = k_key + "्"
        print(f"{k_value} {k_key}्")

print("\n## Full Consonants")
for k_key, k_values in consonant_transliteration.items():
    for k_value in k_values:
        # Print the full form of the consonant
        print(f"{k_value + 'a'} {k_key}")

print("\n## Devanagari Tables")
for k_key, k_values in consonant_transliteration.items():
    for k_value in k_values:
        for g_key, g_value in vowel_transliteration.items():
            # Add the combination of the consonant and vowel sign to the output
            if g_key != "":
                output[k_value + g_value] = k_key + g_key
                print(f"{k_value + g_value} {k_key + g_key}")
