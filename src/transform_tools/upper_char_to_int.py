def char_to_int(ch: str) -> int:
    if ord('A') <= ord(ch) <= ord('Z'):
        return ord(ch) - ord('A')
    elif ord('a') <= ord(ch) <= ord('z'):
        return ord(ch) - ord('a')
    else:
        return -1
