class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr1=["".join(sorted(word)) for word in strs]
        group=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            group[key].append(word)
        print(group)
        return list(group.values())