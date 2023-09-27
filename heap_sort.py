from random import *

# root부터 자식 노드로 내려가면서 heapify
def heapify(root, size):
    global array

    # 왼쪽 자식
    left_ch = root * 2 + 1
    # 왼쪽 자식이 배열의 크기보다 크면 종료
    if left_ch >= size:
        return
    # 부모 노드와 바꿔야하는 자식 노드 저장
    change_ch = left_ch

    # 오른쪽 자식
    right_ch = root * 2 + 2
    # 만약 오른쪽 자식이 있다면
    if right_ch < size:
        # 더 큰 자식으로 바꿈
        if array[left_ch] < array[right_ch]:
            change_ch = right_ch

    # 부모 노드보다 자식 노드가 더 크면 바꿈
    if array[root] < array[change_ch]:
        array[root], array[change_ch] = array[change_ch], array[root]
        heapify(change_ch, size)

def heap_sort(array):
    count = len(array)

    # 마지막 부모 노드
    last_parent_idx = count // 2 - 1
    # heapify
    for i in range(last_parent_idx, 0 - 1, -1):
        heapify(i, count)

    last_parent_idx = count - 1
    while last_parent_idx > 0:
        # swap
        array[last_parent_idx], array[0] = array[0], array[last_parent_idx]
        # 바꿔준 배열을 0부터 다시 heapify
        heapify(0, last_parent_idx)
        last_parent_idx -= 1


# 랜덤 array 생성
array = [randint(0, 1000) for i in range(50)]
print('before heap sort : ', array)
heap_sort(array)
print('after heap sort : ', array)
