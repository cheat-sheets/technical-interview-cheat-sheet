import collections


def Trie():
    return collections.defaultdict(Trie)


def build_trie(words):
    trie = Trie()

    for word in words:
        cur = trie
        for l in word:
            cur = cur[l]
    return trie


def print_trie(trie, level):
    for key, val in trie.items():
        print((' ' * level) + key)
        print_trie(val, level + 4)


words = ['abc', 'abb', 'test', 'aba', 'tesla', 'abba']
trie = build_trie(words)
print_trie(trie, 0)
