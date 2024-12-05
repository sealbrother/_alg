def my_permutation(elements):
    """
    計算輸入元素的所有排列組合
    :param elements: 可排列的元素 (list, tuple, or string)
    :return: 所有排列組合的列表
    """
    #終止
    if len(elements) == 1:
        return [elements]
    #保存
    permutations = []
    #起始元素
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for p in my_permutation(remaining):
            permutations.append([current] + p)
    return permutations
#測試
if __name__ == "__main__":
    input_data = [1, 2, 3]
    result = my_permutation(input_data)
    print("所有排列組合:")
    for perm in result:
        print(perm)