def isOneToOne(s1, s2):
    if len(s1) is not len(s2):
        return False
    mappings = {}
    #for i in range(len(s1)): #iterate through first str
    #    if mappings[s1[i]] is None:
    s2_used = [-1]*256
    for i in range(len(s1)):
        if mappings.get(s1[i]) is None: #current char not in mapping
            # check for available mappings in s2
            #if s2[i] is mapped to something else, False
            #if not, then map s1[i] to s2[i] and add s2[i] to list
            if s2_used[ord(s1[i])] is -1:
                # mapping available
                mappings[s1[i]] = s2[i]
                s2_used[ord(s1[i])] = s1[i]
            else:
                return False
        else: # found a mapping
            #check to see if
            if mappings.get(s1[i]) is not s2[i]:
                return False
