consonant_transliteration = {
    "क": ["ka"],
    "ख": ["kha"],
    "ग": ["ga"],
    "घ": ["gha"],
    "ङ": ["nga"],
    "च": ["cha"],
    "छ": ["chha"],
    "ज": ["ja"],
    "झ": ["jha"],
    "ञ": ["jna"],
    "ट": ["ta"],
    "ठ": ["tha"],
    "ड": ["da"],
    "ढ": ["dha"],
    "ण": ["na"],
    "त": ["ta"],
    "थ": ["tha"],
    "द": ["da"],
    "ध": ["dha"],
    "न": ["na"],
    "प": ["pa"],
    "फ": ["pha"],
    "ब": ["ba"],
    "भ": ["bha"],
    "म": ["ma"],
    "य": ["ya"],
    "र": ["ra"],
    "ल": ["la"],
    "व": ["wa"],
    "श": ["sa"],
    "ष": ["sa"],
    "स": ["sa"],
    "ह": ["ha"],
    "क्ष": ["ksha"],
    "त्र": ["tra"],
    "ज्ञ": ["jnja"]
}

vowel_transliteration = {
    "आ": "a",
    "इ": "i",
    "ई": "i",
    "उ": "u",
    "ऊ": "u",
    "ऋ": "ri",
    "ॠ": "ri",
    "ए": "e",
    "ऐ": "ai",
    "ओ": "o",
    "औ": "au",
    "अं": "am",
    "अँ": "an",
    "अः": "ah",
    "अ": "a"  # Add 'अ' to vowel transliteration
}
diacritic_transliteration = {
    "ा": "a",
    "ि": "i",
    "ी": "i",
    "ु": "u",
    "ू": "u",
    "े": "e",
    "ै": "ai",
    "ो": "o",
    "ौ": "au",
    "ं": "m",
    "ँ": "n",
    "ः": "h",
}

def transliterate_nepal(nepal_word):
    transliterated_word = ""
    i = 0
    while i < len(nepal_word):
        char = nepal_word[i]
        if i < len(nepal_word) - 1 and nepal_word[i:i+2] in consonant_transliteration:
            # Handle combined characters
            transliterated_word += consonant_transliteration[nepal_word[i:i+2]][0]
            i += 2
        elif char in consonant_transliteration:
            # Check if the consonant is followed by a diacritic
            if i < len(nepal_word) - 1 and nepal_word[i+1] in diacritic_transliteration:
                # If so, remove the inherent "a"
                transliterated_word += consonant_transliteration[char][0][:-1]
            else:
                # Otherwise, add the consonant as is
                transliterated_word += consonant_transliteration[char][0]
            i += 1
        elif char in vowel_transliteration:
            transliterated_word += vowel_transliteration[char]
            i += 1
        elif char in diacritic_transliteration:
            # Handle diacritics
            transliterated_word += diacritic_transliteration[char]
            i += 1
        elif char == "्":
            # Handle half consonants
            transliterated_word = transliterated_word[:-1]  # Remove the inherent "a"
            i += 1
        else:
            i += 1
    return transliterated_word






with open('nepali.txt', 'r') as f_in, open('transliterated_words.txt', 'w') as f_out:
    for line in f_in:
        nepal_word = line.strip()
        transliterated_word = transliterate_nepal(nepal_word)
        f_out.write(f"{transliterated_word} {nepal_word}\n")