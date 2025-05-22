x = [1, 3, 5, 12, 5, 1]
mid = 3

x[mid:]
print(x[mid:])

def merge(nums1, nums2):

    merged = []

    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <=nums2[j]:
            merged.append(nums1[i])
            i += 1
        
        else:
            merged.append(nums2[j])
            j +=1
    
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail

print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))


