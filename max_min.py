def find_max_min(num_list):
  
    results =[]
    
    if type(num_list)!=list:
        raise TypeError
    elif min(num_list) == max(num_list):
        return [len(num_list)]
    else:
        results.append(min(num_list)) 
        results.append(max(num_list)) 
        return results
    