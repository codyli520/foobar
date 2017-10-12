def answer(l):
    if len(l) < 3:
        return 0

    count = 0
    i_ls = []
    k_ls = []
    for j in range(1, len(l) - 1):
        for i in range(j):
            if l[j] % l[i] == 0:
                i_ls.append(l[i])
        for k in range(j+1,len(l)):
            if l[k] % l[j] == 0:
                k_ls.append(l[k])
        count += len(i_ls)*len(k_ls)
        i_ls = []
        k_ls = []
    return count

if __name__ == "__main__":
    print answer([1,1,1]) == 1