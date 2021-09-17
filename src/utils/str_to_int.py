def str_to_int(chs: str) -> int:
    """
    将Excel英文列名转为数值
    """
    if chs[0].isdigit():
        return int(chs)
    else:
        num = 0
        for ch in chs:
            num *= 26
            if ord('A') <= ord(ch) <= ord('Z'):
                num += ord(ch) - ord('A') + 1
            elif ord('a') <= ord(ch) <= ord('z'):
                num += ord(ch) - ord('a') + 1
    return num
