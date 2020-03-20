def isOneToOne(s1, s2):
    if len(s1) is not len(s2):
        return False
    mappings = {}
    #abb, aba
    #for i in range(len(s1)): #iterate through first str
    #    if mappings[s1[i]] is None:
    s2_used = [-1]*256
    unique_s1 = [];
    unique_s2 = [];
    """for i in range(len(s1)):
        #if mappings.get(s1[i]) is None: #current char not in mapping
        if s2_used[ord(s1[i])] is -1: # mapping available
            mappings[s1[i]] = s2[i]
            s2_used[ord(s1[i])] = s2[i]
        else: # mapping unavailable
                return False
        if mappings.get(s1[i]) is not s2_used[ord(s1[i])]:
            #if a mapping in s1 is mapped to two places
            print("pottery")
            return False """
    for c in s1[::]:
        if c not in unique_s1:
            unique_s1.append(c)
    for c in s2[::]:
        if c not in unique_s2:
            unique_s2.append(c)
    print(len(unique_s1))
    print(len(unique_s2))
    if len(unique_s1) < len(unique_s2):
        return False;
    return True;
    #return True
