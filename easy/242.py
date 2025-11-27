class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)
        t_set = set(t)
        if s_set == t_set and len(s) == len(t):
            s_dict = {}
            t_dict = {}
            for s_single, t_single in zip(s, t):
                if not (s_single in s_dict):
                    s_dict[s_single] = 1
                else:
                    s_dict[s_single] += 1

                if not (t_single in t_dict):
                    t_dict[t_single] = 1
                else:
                    t_dict[t_single] += 1

            if s_dict == t_dict:
                return True
        return False
