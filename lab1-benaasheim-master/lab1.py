def max_list_iter(int_list):
    if int_list == None:
        raise(ValueError)
    elif len(int_list) == 0:
        return None
    else:
        maxx = int_list[0]
        for i in int_list:
            if i > maxx:
                maxx = i
    return maxx

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError()
    else:
        rev_list = []
        rev_list.append(int_list[-1])
        if len(int_list) > 1:
            rvr_list = reverse_rec(int_list[:-1])
            for i in rvr_list:
                rev_list.append(i)
        return rev_list
        
def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError()
    elif len(int_list) == 0:
        return None
    else:
        x = int((high - low)/2 + low)
        if int_list[x] == target:
            return x
        elif int_list[x] > target:
            return bin_search(target, low, x, int_list)
        else:
            return bin_search(target, x, high, int_list)
