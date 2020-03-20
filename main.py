from testMapping import isOneToOne
def main():
    print(isOneToOne("abb", "aba"))
    print(isOneToOne("aab", "foo")) # True
    print(isOneToOne("bar", "foo")) # True
    print(isOneToOne("foo", "bar")) # False
main()
