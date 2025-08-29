#####main.py
# import sys
# sys.stdin = open('input.txt')
from solution import init, sell, closeSale, discount, show

CMD_INIT = 100
CMD_SELL = 200
CMD_CLOSE_SALE = 300
CMD_DISCOUNT = 400
CMD_SHOW = 500

def run1():
    Q = int(input())
    okay = False
    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_SELL:
            mID = int(next(input_iter))
            mCategory = int(next(input_iter))
            mCompany = int(next(input_iter))
            mPrice = int(next(input_iter))
            ret = sell(mID, mCategory, mCompany, mPrice)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_CLOSE_SALE:
            mID = int(next(input_iter))
            ret = closeSale(mID)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_DISCOUNT:
            mCategory = int(next(input_iter))
            mCompany = int(next(input_iter))
            mAmount = int(next(input_iter))
            ret = discount(mCategory, mCompany, mAmount)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_SHOW:
            mHow = int(next(input_iter))
            mCode = int(next(input_iter))
            res = show(mHow, mCode)
            cnt = int(next(input_iter))
            if res.cnt != cnt:
                okay = False
            for i in range(cnt):
                ans = int(next(input_iter))
                if res.IDs[i] != ans:
                    okay = False
        else:
            okay = False
    return okay


#sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())
T = 1

for tc in range(1, T + 1):
    score = MARK if run1() else 0
    print("#%d %d" % (tc, score), flush = True)