def find(text, pattern):

    def build_dfa(text, pattern):
        dfa = [{}] * len(pattern)
        characters = set(text + pattern)
        dfa[0] = {character: 0 for character in characters}
        dfa[0][pattern[0]] = 1

        simulation_state = 0
        for i in range(1, len(pattern)):
            dfa[i] = {character: dfa[simulation_state][character] for character in characters}
            dfa[i][pattern[i]] = i + 1
            simulation_state = dfa[simulation_state][pattern[i]]

        return dfa

    if pattern == "":
        return 0

    dfa = build_dfa(text, pattern)
    i, state = 0, 0
    pattern_length, text_length = len(pattern), len(text)

    while i < text_length and state < pattern_length:
        state = dfa[state][text[i]]
        i += 1

    return i - pattern_length if state == pattern_length else -1
