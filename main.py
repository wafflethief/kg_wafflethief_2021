from testMapping import isOneToOne

MAX_CHARS = 256
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False
    marked = [False] * MAX_CHARS
    map = [-1] * MAX_CHARS
    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True

def main():
    """print(areIsomorphic("abb", "aba"))
    print(areIsomorphic("aab", "foo")) # True
    print(areIsomorphic("bar", "foo")) # True
    print(areIsomorphic("foo", "bar")) # False
    print(areIsomorphic("fff", "bar")) # False
    print(areIsomorphic("f", "bar")) # False
    """
    print(isOneToOne("abb", "aba")) # True
    print(isOneToOne("aab", "foo")) # True
    print(isOneToOne("bar", "foo")) # True
    print(isOneToOne("foo", "bar")) # False
    print(isOneToOne("fff", "bar")) # False
    print(isOneToOne("f", "bar")) # False
main()
