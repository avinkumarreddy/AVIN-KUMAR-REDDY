def test(strl):
    return strl[len(strl)-2] in strl[len(strl)-1] and strl[len(strl)-2] != strl[len(strl)-1]

strll = ["a","abb","sfs","oo","de","sfde"]

print(test(strll))