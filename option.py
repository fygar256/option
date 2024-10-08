def option(l,o):
    if o in l:
        idx=l.index(o)
        if idx+1<len(l):
            if idx+2<len(l):
                return l[0:idx]+l[idx+2:],l[idx+1]
            else:
                return l[0:idx],l[idx+1]
        else:
            return l[0:idx],''
    return l,''
