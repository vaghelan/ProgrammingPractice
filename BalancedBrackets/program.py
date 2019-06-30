def balancedBrackets(string):
    # Write your code here.
    q = []
    brackets = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    print (brackets.values())
    print(brackets.keys())


    for c in string:
        if c in brackets.values():
            q.append(c)
        if c in brackets.keys():
            if len(q) == 0:
                return False
            b = q.pop()
            if brackets[c] != b:
                return False

    if len(q) > 0:
        return False

    return True

print (balancedBrackets("(([]()()){})"))
