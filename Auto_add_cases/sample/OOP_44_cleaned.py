class SS:
    def __init__(self):
        pass
    def Split_String(self, s):
        def is_palindrome(string):
            return string == string[::-1]
        def partition_helper(string, start, path, result):
            if start == len(string):
                result.append(path[:])
                return
            for end in range(start + 1, len(string) + 1):
                if is_palindrome(string[start:end]):
                    path.append(string[start:end])
                    partition_helper(string, end, path, result)
                    path.pop()
        result = []
        partition_helper(s, 0, [], result)
        return result
#--------------:
print(SS().Split_String("level") == [['l', 'e', 'v', 'e', 'l'], ['l', 'eve', 'l'], ['level']])
print(SS().Split_String("abcd") == [['a', 'b', 'c', 'd']])
print(SS().Split_String("aaa") == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
