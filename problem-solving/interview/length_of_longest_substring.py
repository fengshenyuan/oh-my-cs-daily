# from leetcode
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    cur_dt = {}
    max_len = 0 # history max_len
    inn_len = 0 # current round max_len
    last_check_point = 0
    for seq, ch in enumerate(s):
        if ch not in cur_dt:
            cur_dt[ch] = seq
            inn_len += 1
        else:
            ch_begin = cur_dt[ch]
            if ch_begin < last_check_point:
                # fake repeat
                cur_dt[ch] = seq
                inn_len += 1
            else:
                # real repeat
                max_len = max(max_len, inn_len)
                inn_len = min(seq - ch_begin, inn_len)
                cur_dt[ch] = seq
                last_check_point = ch_begin + 1

    max_len = max(max_len, inn_len)
    return max_len