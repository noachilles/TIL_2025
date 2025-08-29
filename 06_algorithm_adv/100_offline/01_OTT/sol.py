# 각 함수만 구현하면 된다.
# 함수 input, output만 신경쓰면 됨
# 별도 class를 만드는 것도 안 될 것 같음 - user 코드만 건들 수 있어서

# RESULT
RESULT = {
    'cnt': 0,
    'IDs': []
}

def init(N):
    '''
    :param N: 각 tc에 대한 초기화 함수
    :return:
    '''
    # 1부터 N까지의 고유 번호로 구분된다
    # 초기에 시스템에 등록된 영화는 없고 어떤 사용자도 영화 본 적 X
    movies_list = dict() # {viewers: set, genre: x, total: y}
    users_list = {i: dict() for i in range(N)} # uID: {mID: rating}

def add(mID, mGenre, mTotal):
    nonlocal movies_list
    nonlocal users_list
    '''
    영화를 등록하는 함수 - 삭제된 영화의 ID로 다시 등록하는 경우는 X
    :param mID: 영화 ID
    :param mGenre: 장르
    :param mTotal: 총점
    :return:
    '''
    if movies_list.get(mID): return 0
    movies_list[mID] = {'viewers': set(),
                        'genre': mGenre,
                        'total_rating': mTotal
                        }
    return 1

def erase(mID):
    nonlocal movies_list
    nonlocal users_list
    '''
    ID가 mID인 영화를 삭제한다.
    이미 삭제되었거나 등록된 적이 없으면(movies_list에 없으면: 0 반환)
    :param mID: 삭제할 영화의 ID
    :return:
    '''
    if movies_list.get(mID) is None: return 0
    movies_list.pop(mID)
    return 1

def watch(uID, mID, mRating):
    nonlocal movies_list
    nonlocal users_list
    '''
    uID 사용자가 mID 영화를 시청하고 그 영화에 대한 평점을 mRating으로 준다.
    :param uID: 사용자 ID
    :param mID: 영화 ID
    :param mRating: 사용자가 남긴 영화 평점
    :return: 
    '''
    # 영화가 등록된 적이 없으면 실패
    if movies_list.get(mID) is None: return 0
    # 영화를 이미 시청했어도 실패
    elif users_list[uID].get(mID) is not None: return 0

    # 위의 실패 경우가 아니면 영화 평점을 반영
    movies_list[mID]['total_rating'] += mRating
    users_list[uID][mID] = mRating
    return 1

def suggest(uID):
    global RESULT
    nonlocal movies_list
    nonlocal users_list
    '''
    사용자에게 '최대' 5개의 영화를 추천
    :param uID: 사용자 고유 번호 uID
    :return:
    '''
    # 1. 사용자가 이미 시청했거나 삭제된 영화는 제외 - OK

