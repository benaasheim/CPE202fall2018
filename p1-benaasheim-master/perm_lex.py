def perm_gen_lex(s):
    perms = []
    if len(s) == 1:
        perms.append(s)
    else:
        for n in range(len(s)):
            x = s[n]
            y = s[:n] + s[n+1:]
            porms = perm_gen_lex(y)
            for i in porms:
                z = i
                z = x + z
                perms.append(z)
    return perms
