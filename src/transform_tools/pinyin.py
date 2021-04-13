from pypinyin import pinyin, lazy_pinyin, Style

def str_to_pinyin(string):  #输入中文字符串，返回每个字的拼音首字母（大写）
    return_str = ""  
    lst = pinyin(string, style=Style.FIRST_LETTER)  #获得每个字的开头的字母
    for char in lst:
        return_str += char[0]

    return_str = return_str.upper()
    return return_str

