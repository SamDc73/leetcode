def groupAnagrams(strs):
    d = {}
    for w in strs:
        key = tuple(sorted(w))  # sort each word in tuple
        d[key] = d.get(key, []) + [w]
    return d.values()


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
