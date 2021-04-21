def compare_strings(string1,string2):
    str1=0
    str2=0
    for i in range(len(string1)):
        if string1[i]>="0" and string1[i]<="9":
            str1 +=1
    for i in range(len(string2)):
        if string2[i]>="0" and string2[i]<="9":
            str2 +=1
    if str1==str2:
        return "Same"
    return "not same"

