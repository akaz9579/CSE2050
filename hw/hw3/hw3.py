import random
import time

def generate_lists(size):
    """Generates two random lists of unique integers with length equal to `size`."""
    list1 = random.sample(range(size * 2), size)
    list2 = random.sample(range(size * 2), size)
    return list1, list2

def find_common(list1, list2):
    """Finds the number of common items between list1 and list2 without using collections."""
    common_count = 0
    
    for i in range(len(list1)):           
        for j in range(len(list2)):       
            if list1[i] == list2[j]:      
                common_count += 1         
    
    return common_count                   


def find_common_efficient(list1, list2):
    """ """
    set1 = set(list1)                     
    set2 = set(list2)                    
    common_items = set1 & set2           
    
    return len(common_items)              
                                          
def measure_time():
    """ """
    sizes = [10, 100, 1000, 10000] 
    
    print(f"{'List Size':<12}{'find_common Time (s)':<30}{'find_common_efficient Time (s)':<30}")
    print("-" * 72)
    
    for size in sizes:
        list1, list2 = generate_lists(size)
        
        start_time = time.time()
        find_common(list1, list2)
        time_common = time.time() - start_time
        
        start_time = time.time()
        find_common_efficient(list1, list2)
        time_efficient = time.time() - start_time
        
        print(f"{size:<12}{time_common:<30}{time_efficient:<30}")
    
    larger_sizes = [100000, 1000000]
    for size in larger_sizes:
        list1, list2 = generate_lists(size)
        
        time_common = "N/A"
        
        start_time = time.time()
        find_common_efficient(list1, list2)
        time_efficient = time.time() - start_time
        
        print(f"{size:<12}{time_common:<30}{time_efficient:<30}")


if __name__ == "__main__":
    measure_time()
