def same_string(s1, s2):
    '''(str, str) -> bool
    Return True iff s1 == s2
    REQ: len(s1) == len(s2)
    '''
    if s1 == "" and s2 == "":
        return True
    else:
        return s1[0] == s2[0] and same_string(s1[1:], s2[1:])


def almost_same_string(s1, s2):
    '''(str, str) -> bool
    Return True iff differ in at most one place
    REQ: len(s1) == len(s2)

    almost_same_string('aaa', 'aaa') => true
    almost_same_string('aaa', 'bbb') => false
    almost_same_string('aaa', 'aab') => true

    almost_same_string('aaaba', 'aaaaa')
        almost_same_string('aaba', 'aaaa')
            almost_same_string('aba', 'aaa')
                almost_same_string('ba', 'aa')
                    same_string('a', 'a')
                        same_string('','') => True
    '''

    # base case
    if s1 == "" and s2 == "":
        return True
    elif s1[0] != s2[0]:
        return same_string(s1[1:], s2[1:])
    else:
        return almost_same_string(s1[1:], s2[1:])


## solution using a helper function
def _almost_same_string_helper(s1, s2):
    '''(str, str) -> int
    Return the number of places where s1 and s2 differ
    REQ: len(s1) == len(s2)
    '''
    if s1 == '':
        return 0
    elif s1[0] != s2[0]:
        return 1 + _almost_same_string_helper(s1[1:], s2[1:])
    else:
        return _almost_same_string_helper(s1[1:], s2[1:])


def almost_same_string2(s1, s2):
    '''(str, str) -> bool
    Return True iff differ in at most one place
    REQ: len(s1) == len(s2)
    '''
    return _almost_same_string_helper(s1, s2) <= 1

def rsum(lst):
    pass

def rec_len(lst):
    if lst == []:
        return 0
    elif isinstance(lst[0], list):
        return rec_len(lst[0]) + rec_len(lst[1:])
    else:
        return 1 + rec_len(lst[1:])

def nest_level(lst):
    '''
    nest_level([1,	[[],	[[2]]],	’three’]) => 4
    :param lst:
    :return:
    '''
    # DO this yourself!
    pass

def is_elfish(word):
    ''' (str) -> bool
    Returns true if word is elfish, i.e. the word contains the letters
    'e', 'l', and 'f'.
    :param word:
    :return:
    '''
    pass

def _elfish_helper(word, elf_tracker):
    pass

if(__name__ == "__main__"):
    # true
    # print(same_string("ABCD", "ABCD"))
    # print(same_string("ABCD", "ABCf"))
    # print(same_string("", ""))

    # # true
    # print(almost_same_string("ABCD", "ABCD"))
    # # true
    # print(almost_same_string("ABXD", "ABCD"))
    # # false
    # print(almost_same_string("ABCD", "WXYZ"))

    # print(almost_same_string2("ABCD", "ABCD"))
    # print(almost_same_string2("ABXD", "ABCD"))
    # print(almost_same_string2("ABCD", "WXYZ"))

    print(rec_len([1,2,3,[1,2],1])) # should return 6

    # print(is_elfish("sdflkjsdf slkdfjlskdf"))
