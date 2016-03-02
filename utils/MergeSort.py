def MergeSort(arr, sIndex, eIndex):
    if eIndex - sIndex < 2:
        if arr[eIndex] < arr[sIndex]:
            return [arr[eIndex], arr[sIndex]] # reverse array
        return [arr[sIndex], arr[eIndex]]
    
    mIndex = int((eIndex + sIndex) / 2) # mid point
    sortedArr1 = MergeSort(arr, sIndex, mIndex)
    sortedArr2 = MergeSort(arr, mIndex + 1, eIndex)
    return Merge(sortedArr1, sortedArr2)
    
def Merge(arr1, arr2):
    mergedArr = []
    i = 0 # tracker for arr1
    j = 0 # tracker for arr2
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergedArr.append(arr1[i])
            i += 1
        else:
            mergedArr.append(arr2[j])
            j += 1
    while i < len(arr1): 
        mergedArr.append(arr1[i])
        i += 1
    while j < len(arr2):
        mergedArr.append(arr2[j])
        j += 1
    return mergedArr
