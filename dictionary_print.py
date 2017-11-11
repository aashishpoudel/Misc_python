
d = {"1234": { "catfish": 30, "123456789012345": 12345},
  "dog": {"collie": 0, "poodle": 45, "doberman": 20, "test": {"test1": 1, "test2": 2}}}




def gen_space(level):
    mystr = "    "
    for i in range(level):
        mystr += "    "
    return mystr


def myprint(d, level):
    lvl = level
    num_of_keys=1
    mystr = gen_space(lvl)
    for k, v in d.items():
        if isinstance(v, dict):
            lbl = lvl
            lbl += 1
            num_of_keys += 1
            mystr = gen_space(lvl)
            #print(mystr, str(k), ": ", "levelstr", str(lvl))
            print(mystr, str(k), ": ")
            myprint(v, lbl)
        else:
            lbl = lvl
            mystr = gen_space(lbl)
            #print(mystr, str(k), ":", v, "level", str(lbl))
            print(mystr, str(k), ":", v)


myprint(d, 1)

print("\n\n\n")
