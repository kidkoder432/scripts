import multiprocessing
l = list(range(1001))
def x(n):
    return n*n
if __name__ == '__main__':
    with multiprocessing.Pool() as p:
        print(p.map(x, l))