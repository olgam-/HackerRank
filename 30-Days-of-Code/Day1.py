word = [5.35, 'a', False, 100, "I am a code monkey", True, 17.3, 'c', "derp"]

for i in word:
    word_type = type(i)

    if word_type == str:
        if len(i) == 1:
            print "Primitive : char"
        else:
            print "Referenced : String"
    elif word_type == int:
        print "Primitive : int"
    elif word_type == float:
        print "Primitive : double"
    elif word_type == bool:
        print "Primitive : boolean"
    else:
        print "Referenced : Array"
