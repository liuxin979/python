n = 1
def getPentagonalNumber(n):
    count = 0
    for n in range(1,101):
        n = n * (3 * n - 1) / 2
        print("%d" % n,end = '\t')
        count += 1
        if count % 10 == 0:
            print('\n')

if __name__ == '__main__':
    getPentagonalNumber(n)
    