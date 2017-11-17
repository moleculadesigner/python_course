import math
import conditions_and_cycles as cas

_example_list = sorted([2,3,3,45,4,23,43,54,34,5,32,423,4,23542354,3422,243,4,3,3,254,5643,3233,3,3,4,43,2,423,3,3,45,5,43,2,1,4,34234,34,3,342,23,4543,534,32423,23,4,4,4,3,423,3245,23,3,34254,235,234,5,235,4,345,235,23,5523,5,234,52,67,756,76,57,345,23,31,7,8,56,346,345,756,4343,754,674,8,568,9,65,34,3,5474,5687,56,2,3])
_estring = 'rewlkdfsklgjdflkjglkdsfjgkldfsjgliiiiiiiiiierwtsj;kldfjg;lksdfjgl;ksdjfl;gj;lsdfjg;lk'

dict_1 = {'A' : "12",
          'B' : 54,
          'C' : 'C',
          'D' : ["-", "2"],
          1   : 0   }

dict_2 = {'A' : 100,
          'E' : 4,
          '0' : 'h',
          0   : [],
          1   : 1   }

dict_3 = {'A' : 100,
          56  : 56,
          '"' : {},
          0   : "o/",
          1   : 1   }

def main():
    """
    """
    print("\n1. list of some numbers:")
    print(cas.list_to_str(_example_list))
    print("\n   Unique elements:")
    print(cas.list_to_str(sorted(list(set(_example_list)))))
    print("______\n")

    set_A = set("THIS IS A USUAL STRING")
    set_B = set("THE ANOTHER ONE")
    set_C = set("FINAL STRING")
    
    print("2. Set Theory operations:\nSet A = " + str(set_A))
    print("Set B = " + str(set_B))
    print("Set C = " + str(set_C) + '\n')
    print("A ∪ B = " + str(union(set_A, set_B)))
    print("A ∩ B = " + str(intersection(set_A, set_B)))
    print("A \\ B = " + str(difference(set_A, set_B)))
    print("A △ B = " + str(delta(set_A, set_B)))
    print("______\n\n3. Extensions:")
    print("∪(A, B, C) = " + str(union_milti([set_A, set_B, set_C])))
    print("∩(A, B, C) = " + str(intersection_multi([set_A, set_B, set_C])))
    print("______\n")

    print("4. Unique symbols in string '" + _estring + "':\n")
    u = ''
    for c in set(_estring):
        u += c
    print(u)
    print("______\n")

    print("5. Print some text:")
    s = set(cas.get_str())
    l = len(s)
    u = ''
    for c in s:
        u += c
    print("You typed " + str(l) + " unique chars: {" + u + "}")
    print("______\n")
    print("6. Dictionary 1:\n" + dict_to_str(dict_1))
    print("\n   Dictionary 2:\n" + dict_to_str(dict_2))
    print("\n   Dictionary 3:\n" + dict_to_str(dict_3))
    #cat(dict_1, dict_2)
    print("\n   Dictionaries concatenation:")
    print(dict_to_str(merge([dict_1, dict_2, dict_3])))


# Set theory binary operators
def union(set1, set2):
    u_set = set()
    for i in set1:
        u_set.add(i)
    for i in set2:
        u_set.add(i)
    return u_set

    
def intersection(set1, set2):
    i_set = set()
    for a in union(set1, set2):
        if (a in set1) and (a in set2):
            i_set.add(a)
    return i_set


def difference(set1, set2):
    d_set = set()
    for a in set1:
        if not (a in set2):
            d_set.add(a)
    return d_set


def delta(set1, set2):
    return(union(difference(set1, set2), difference(set2, set1)))

# Set theory operators extensions
def union_milti(list_of_sets):
    um_set = list_of_sets[0]
    for s in list_of_sets[1:]:
        um_set = union(um_set, s)
    return um_set    

def intersection_multi(list_of_sets):
    im_set = list_of_sets[0]
    for s in list_of_sets[1:]:
        im_set = intersection(im_set, s)
    return im_set 


def cat(dict1, dict2):
    full_dict = dict()
    dicts = list()
    dicts.append(dict1)
    dicts.append(dict2)
    
    keys = list()
    keys.append(set(dict1.keys()))
    keys.append(set(dict2.keys()))
    uni_ks = (difference(keys[0], keys[1]), difference(keys[1], keys[0]))
    com_ks = intersection(keys[0], keys[1])
    print(str(uni_ks))
    print(str(com_ks))
    for i in range(2):
        for index in uni_ks[i]:
            full_dict[index] = dicts[i][index]
    if len(com_ks) != 0:
        for index in com_ks:
            value_list = []
            for i in range(2):
                value_list.append(dicts[i][index])
            full_dict[index] = value_list
    print(dict_to_str(full_dict))
    return full_dict
        

def dict_to_str(dict_):
    s = "{ "
    for index in dict_.keys():
        s += str(index) + ": " + str(dict_[index]) + "\n  "
    s += "\b\b}"
    return s


def merge(dict_list):
    keys_ = set()
    full_dict = {}
    for dict_ in dict_list:
        for key in dict_.keys():
            keys_.add(key)

    for key in keys_:
        val_list = []
        for dict_ in dict_list:
            try:
                val_list.append(dict_[key])
            except KeyError:
                continue
        if len(val_list) == 1:
            full_dict[key] = val_list[0]
        else:
            full_dict[key] = val_list

    return full_dict
    


if __name__ == '__main__':
    main()