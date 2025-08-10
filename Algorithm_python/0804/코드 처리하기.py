def solution(code):
    mode = 0
    ret = []
    for idx, ch in enumerate(code):
        if ch == '1':
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(ch)
            elif mode == 1 and idx % 2 == 1:
                ret.append(ch)

    if len(ret) == 0:
        return "EMPTY"
    else:
        return ''.join(ret)