
def replace_string(s, words):

    new_string = ''
    index = 0
    state_open = True

    max_index = len(s) - 1

    i = 0
    while i <= max_index:

        if s[i] == '{':
            go_back = i
            i = i + 1
            if i > max_index:
                new_string = new_string + s[i - 1]
                break

            num = ''
            bad_format = False
            while s[i] != '}':
                if s[i] == ' ':
                    i = i + 1
                    if i > max_index:
                        bad_format = True
                        break
                    continue
                num = num + s[i]
                if not num.isdigit():
                    bad_format = True
                    break

                i = i + 1
                if i > max_index:
                    bad_format = True
                    break

            if bad_format or num == '':
                i = go_back
                new_string = new_string + s[i]
            else:
                index = int(num)
                if index > len(words) - 1:
                    i = go_back
                    new_string = new_string + s[i]
                else:
                    new_string = new_string + words[int(num)]
        else:
            new_string = new_string + s[i]

        i = i + 1

    return new_string

test_case_num = 1

def test_me(s, words):
    global  test_case_num
    o = open("result.txt", "w+")
    o.write ("======test case {}=======".format(test_case_num))
    o.write ("words = {}".format(words))
    o.write ("original = \"" +  s  + "\"")
    o.write ("new      = \"" +  replace_string(s, words) + "\"")
    o.write("======test case {}=======\n\n".format(test_case_num))
    test_case_num += 1
    o.close()


def test_all(words):
    s1 = 'In {0} science, the {1} numbers always include {2}. In {3}, some {{4} define them to include {2}} and some do not.'
    test_me(s1, words)

    # empty string
    s2 = ''
    test_me(s2, words)

    # empty string
    s3 = '{}'
    test_me(s3, words)

    # out of range of words
    s4 = '{-1}'
    test_me(s4, words)

    # out of range of words
    s5 = '{55}'
    test_me(s5, words)

    # surrounded by lot of other characters.
    s6 = '{{{{{   0   }}}}}'
    test_me(s6, words)

    s7 = 'In {0} science, the {  1   } numbers always include {2}. In {3}, some {{4} define them to include {2}} and some do not.'
    test_me(s7, words)

words = ['computer', 'natural', 'zero', 'mathematics', 'texts']

test_all(words)

words = ['computer']

test_all(words)

words = []

test_all(words)