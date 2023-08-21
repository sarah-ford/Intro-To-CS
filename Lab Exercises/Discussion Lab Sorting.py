lst=raw_input("Please enter numbers separated by commas: ")
lst=lst.split(",")

def smallest(lst):
    if lst==[]:
        return None
    elif len(lst)==1:
        return lst[0]
    else:
        minimum=lst[0]
        for x in lst[1:]:
            if x<minimum:
                minimum = x
        return minimum
    
print smallest(lst)


def secondsmall(lst):
    small1=smallest(lst)
    new_lst=[]
    for i in lst:
        if i<>small1:
            new_lst.append(i)
    return new_lst

print
print secondsmall(lst)



# new_lst=[i for i in lst if i<>small1]
