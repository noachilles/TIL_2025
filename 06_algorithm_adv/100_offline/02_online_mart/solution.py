#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

'''
    c++ 풀이를 번역해보자
    자주 출제되던 데이터 추가, 삭제, 변경, 조회 형태 문제
    PQ, SET으로 풀이한다 - 여기서 SET이

    특이점: 품목과 회사로 분류되어 있음
        & 이후에 추가되는 물건들: 이전 discount만큼 더해서 저장해야 함

    0.
    sell에서 data base와 PQ에 품목 추가하고
    close sell에서 data base와 PQ에서 삭제하고
    discount에서 data base와 PQ 수정하고
    show에서 pq에서 뽑아서 보여줌

    1.
    discount에서 data base와 PQ를 하나하나 수정할 경우
    하나의 품목, 분류에 모든 데이터 50000개가 모두 들어있다면 50000이 걸림
    호출횟수 10000 * 데이터 50000 = 5억.. 시간초과

    2.
    품목, 분류별로 discount를 관리하고 show할 때 discount만큼 빼서 보여준다면,
    discount 이후에 들어온 상품들은 관리가 안 됨 - 세일에 포함이 안 되는데, 포함되는 것처럼 연산돼서

    3.
    => discount 이후에 들어온 상품들은 이전 누적 discount만큼 더해서 추가
    show 실행 시 discount만큼 빼서 보여준다면 가능 (정상 값으로 보임)

    품목, 분류별 discount에 접근해 더해주기만 하면 되기 때문에
    discount 시간복잡도는 1

    품목 추가할 때 discount 더해서 추가하고, 품목 고를 때 discount 빼면서 하면
    시간복잡도 추가되는 부분은 X

    4. 구현
'''

#####solution.py

import bisect

# --- 상수 정의 ---
MAX_CATE = 6
MAX_COMP = 6

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

class GoodsGroup:
    """카테고리와 회사별 상품 그룹 정보를 관리하는 클래스"""

    def __init__(self):
        # (가격, 상품 ID) 튜플을 담는 정렬된 리스트
        # C++의 set<pair<int, int>> 역할을 합니다.
        self.goods_set = []
        self.discount_num = 0
        self.goods_cnt = 0  # 판매 중인 (마감되지 않은) 상품의 개수


class GoodsInfo:
    """개별 상품 정보를 관리하는 클래스"""

    def __init__(self, mID, mCategory, mCompany, mPrice, mClosed=False):
        self.mID = mID
        self.mCategory = mCategory
        self.mCompany = mCompany
        # mPrice는 등록 시점의 할인액이 반영된 가격입니다.
        self.mPrice = mPrice
        self.mClosed = mClosed  # 판매 마감 여부 (Lazy Deletion을 위함)


# --- 전역 변수 선언 ---

# 카테고리/회사별 상품 그룹을 저장하는 2차원 리스트
cate_comp_goods = None
# 상품 ID를 key로, GoodsInfo 객체를 value로 갖는 딕셔너리
# C++의 mID_to_idx와 goods_list 역할을 동시에 수행합니다.
goods_list = None


# --- 함수 구현 ---

def init():
    """
    모든 데이터를 초기화합니다.
    """
    global cate_comp_goods, goods_list
    goods_list = {}
    cate_comp_goods = [[GoodsGroup() for _ in range(MAX_COMP)] for _ in range(MAX_CATE)]


def sell(mID: int, mCategory: int, mCompany: int, mPrice: int) -> int:
    """
    새로운 상품을 등록합니다.
    """
    group = cate_comp_goods[mCategory][mCompany]

    # C++ 코드와 동일하게, 등록 시점의 누적 할인액을 가격에 더해 저장합니다.
    # 나중에 실제 가격이 필요할 경우 이 할인액을 다시 빼줍니다.
    temp_price = mPrice + group.discount_num

    # 상품 정보를 딕셔너리에 저장하여 ID로 쉽게 찾을 수 있도록 합니다.
    goods_list[mID] = GoodsInfo(mID, mCategory, mCompany, temp_price, False)

    # 가격순으로 정렬된 리스트에 새 상품을 추가합니다.
    # bisect.insort는 정렬 순서를 유지하며 O(N) 시간 복잡도로 삽입합니다.
    bisect.insort(group.goods_set, (temp_price, mID))
    group.goods_cnt += 1

    return group.goods_cnt


def closeSale(mID: int) -> int:
    """
    특정 상품의 판매를 마감합니다.
    """
    # 상품이 존재하지 않거나 이미 마감된 경우 -1을 반환합니다.
    if mID not in goods_list or goods_list[mID].mClosed:
        return -1

    info = goods_list[mID]
    info.mClosed = True

    group = cate_comp_goods[info.mCategory][info.mCompany]
    # 판매 중인 상품 개수만 1 감소시켜 'Lazy Deletion'을 구현합니다.
    group.goods_cnt -= 1

    # 마감 시점의 실제 가격을 반환합니다.
    # (저장된 가격 - 현재까지의 누적 할인액)
    return info.mPrice - group.discount_num


def discount(mCategory: int, mCompany: int, mAmount: int) -> int:
    """
    특정 그룹의 상품들에 할인액을 적용합니다.
    """
    group = cate_comp_goods[mCategory][mCompany]
    group.discount_num += mAmount

    # 총 할인액보다 가격이 낮거나 같은 상품들을 찾아 마감 처리합니다.
    # (group.discount_num, float('inf')) 튜플을 사용하여
    # 가격이 discount_num 이하인 모든 상품의 경계를 찾습니다.
    cutoff_idx = bisect.bisect_right(group.goods_set, (group.discount_num, float('inf')))

    items_to_remove = group.goods_set[:cutoff_idx]

    for _, temp_mID in items_to_remove:
        info = goods_list[temp_mID]
        # 아직 마감되지 않은 상품만 마감 처리하고 개수를 줄입니다.
        if not info.mClosed:
            info.mClosed = True
            group.goods_cnt -= 1

    # 실제로 마감된 상품들을 리스트에서 제거합니다.
    group.goods_set = group.goods_set[cutoff_idx:]

    return group.goods_cnt


def show(mHow: int, mCode: int) -> RESULT:
    """
    조건에 맞는 상품 중 가격이 가장 저렴한 5개를 반환합니다.
    """
    res = RESULT()
    temp_sort_goods = []

    # mHow 값에 따라 조회할 카테고리와 회사의 범위를 설정합니다.
    category_range = range(1, MAX_CATE) if mHow != 1 else [mCode]
    company_range = range(1, MAX_COMP) if mHow != 2 else [mCode]

    for i in category_range:
        for j in company_range:
            group = cate_comp_goods[i][j]
            push_cnt = 0

            # 각 그룹에서 가격이 가장 저렴한 상품부터 순회합니다.
            for temp_price, temp_mID in group.goods_set:
                if push_cnt >= 5:
                    break

                info = goods_list[temp_mID]
                if not info.mClosed:
                    # 현재 실제 가격을 계산하여 (저장된 가격 - 누적 할인액) 임시 리스트에 추가합니다.
                    actual_price = temp_price - group.discount_num
                    temp_sort_goods.append((actual_price, temp_mID))
                    push_cnt += 1

    # 수집된 모든 상품들을 가격순으로 정렬합니다. (가격이 같으면 ID순)
    temp_sort_goods.sort()

    res.cnt = min(len(temp_sort_goods), 5)
    for i in range(res.cnt):
        res.IDs[i] = temp_sort_goods[i][1]  # 상품 ID만 결과에 저장

    return res

# def show(mHow : int, mCode : int) -> RESULT:
#     '''
#     mHow: 조건
#     조건 만족하는 상품 중 가격이 낮은 순서로 최대 5개 상품을 RESULT 구조체에 저장 및 반환
#     가격이 같은 경우, 상품 ID가 더 적은 값을 가진 상품이 우선
#     1. mHow = 0인 경우 모든 상품에 대해서
#     2. mHow = 1인 경우 품목이 mCode
#     3. mHow = 2인 경우 제조사가 mCode
#     '''
#     return RESULT(-1, [0, 0, 0, 0, 0])
