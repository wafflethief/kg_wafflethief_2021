def isOneToOne(s1, s2):
    if len(s1) is not len(s2):
        return False
    mappings = {}
    #for i in range(len(s1)): #iterate through first str
    #    if mappings[s1[i]] is None:
    s2_used = [-1]*256
    for i in range(len(s1)):
        if mappings.get(s1[i]) is None: #current char not in mapping
            if s2_used[ord(s1[i])] is -1: # mapping available
                mappings[s1[i]] = s2[i]
                s2_used[ord(s1[i])] = s2[i]
            else: # mapping unavailable
                return False
        else: # found a mapping
            if mappings.get(s1[i]) is not s2_used[ord(s1[i])]:
                #if a mapping in s1 is mapped to two places
                return False
    return True
