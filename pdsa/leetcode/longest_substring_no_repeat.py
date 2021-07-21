
class LongestSubstringNoRepeat(object):
    def lengthOfLongestSubstring(self, s):
        """
            Given a string s, find the length of the longest substring without repeating characters.

            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3.
        """
        working_string = ""
        hash_table = {}
        longest = 0
        floor_index = 0
        for i in range(len(s)):
            if s[i] not in working_string:
                working_string += s[i]
                hash_table[s[i]] = i
                if len(working_string) > longest:
                    longest = len(working_string)
                else:
                    floor_index = hash_table[s[i]] + 1
                    working_string = s[floor_index:i + 1]
                    hash_table[s[i]] = i
                    
        return longest