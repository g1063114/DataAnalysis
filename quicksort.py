def quick_sort(items):
    quick_recur(items,0,len(items)-1)

def quick_recur(items,left,right):
    if left >= right:
        return
    
    pivot = partition(items,left,right)

    quick_recur(items,left,pivot-1)
    quick_recur(items,pivot+1,right)

def swap(items,a,b):
    items[a],items[b] = items[b],items[a]

def partition(items,left,right):
    pivot = items[right]

    cur = left - 1
    for i in range(left,right):
        if items[i] < pivot:
            cur=cur+1
            swap(items,cur,i)
    pos = cur + 1
    swap(items,cur+1,right)

    return pos
    


def main():
    item = [7,2,5,1,3,8,7,4,9,6]
    quick_sort(item)
    print(item)

main()
