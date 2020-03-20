def isOneToOne(s1, s2):
    if len(s1) is not len(s2):
        return False
    mappings = {}
    s2_used = [-1]*256
    unique_s1 = [];
    unique_s2 = [];
    for c in s1[::]:
        if c not in unique_s1:
            unique_s1.append(c)
    for c in s2[::]:
        if c not in unique_s2:
            unique_s2.append(c)
    if len(unique_s1) < len(unique_s2):
        return False;
    return True;
    #return True
