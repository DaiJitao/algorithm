from typing import List, Optional


class Solution:
    def word2dict(self, word):

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == None or len(strs) == 0:
            return None
        if len(strs) == 1 or strs[0] == '':
            return [[""]]

        for word in strs:
