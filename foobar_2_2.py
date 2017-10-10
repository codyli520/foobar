def answer(h, q):
    output = []

    for node in q:
        size = 2**h - 1
        before = 0
        if node == size:
            output.append(-1)
            continue

        while True:
            size /= 2
            left = before + size
            right = left + size
            parent = right + 1

            if left == node or right == node:
                output.append(parent)
                break
            if node > left:
                before = left
                
    return output



if __name__ == "__main__":

    print answer(5,[19,14,28])
    print answer(3,[7,3,5,1])
