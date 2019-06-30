

fp = open("input.txt")

first = True

s = []


def list_diff(a, b):
    diff = []
    for be in b:
        if be not in a:
            diff.append(be)
    return diff



def process(s):

    l = len(s)
    s1 = ""
    s2 = ""

    if l%2 == 0 :
        half = l/2
        s1 = s[0:half]
        s2 = s[half:l]

        s3 = list_diff(s1, s2)
        print s1, " ------ ", s3, "--------" , s2
        return len(s3)


    return -1




for line in fp:
    if first == True:
      num_test_cases = int(line.strip())
      first = False
      continue

    s.append(line.strip())

for ss in s:
  print "result = " + str(process(ss))
