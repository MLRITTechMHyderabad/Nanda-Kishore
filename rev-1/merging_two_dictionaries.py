def merge_dictionaries(dict1,dict2):
    for key in dict2.keys():
        if key in dict1:
            try:
                if type(dict1[key]) == str and type(dict2[key]) == str:
                    dict1[key] = [dict1[key], dict2[key]]
                else:
                    dict1[key] = dict1[key] + dict2[key]
            except:
                dict1[key] = [dict1[key], dict2[key]]
        else:
            dict1[key] = dict2[key]
    return dict1

dict1 = {"name":"Nanda ","Technology":"Core java ","fee":5000}
dict2 = {"name":"Kishore ","Technology":"Core Python","fee":2500}
print(merge_dictionaries(dict1,dict2))
