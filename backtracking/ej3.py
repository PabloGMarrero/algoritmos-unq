def head(a, i):
    return a[:i]

def tail(a, i):
    return a[i:]

def permutation(list):
    if len(list) == 1:
        return [list]
  
    all_perm = []
 
    for i in range(len(list)):
       current_element = list[i]
 
       remain_list = head(list, i) + tail(list, i+1)
 
       for p in permutation(remain_list):
           all_perm.append([current_element] + p)
    return all_perm

if __name__ == '__main__':
    a = list('ABC')
    print(permutation(a))