import copy

def r_unpack(x):
    ''' recursive unpacking of x '''
    unpacked = []

    try:
        for i in x:
            try:
                if len(i) == 1:
                    i = i[0] # unpack single element lists
                    unpacked.append(i)
                else:
                    unpacked.extend(r_unpack(i))
            except TypeError: # no length or can't unpack
                unpacked.append(i)
    except TypeError: # can't be iterated
        unpacked.append(x)
    
    return unpacked        

def substring(x, y):
    ''' return shortest substring of x from set y '''

    y = set( # turn any input into a set of single characters
        r_unpack(
            [str(s) for s in r_unpack(y)]
            )
        )
    y_confirm = copy.copy(y)
    x = str(x)
    i0 = len(x)
    i1 = 0
    
    for i in range(len(x)):
        if x[i] in y:
            if i < i0:
                i0 = i
            if i > i1:
                i1 = i
            y_confirm.discard(x[i])
            if len(y_confirm) == 0:
                break

    if len(y_confirm) == 0:
        low = substring(x[i0+1:], y) # test rest of string for shorter occurences
        if low != None and len(low) < (i1+1 - i0): # test matches against current
            return low
        else:
            return x[i0:i1+1]
    else:
        return None
