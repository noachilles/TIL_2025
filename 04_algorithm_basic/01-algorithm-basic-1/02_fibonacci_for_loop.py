def fibonacci_for_loop(n):
    # 기본 룰은 동일하게 적용
    # n이 0이면 0을 반환
    if n == 0:
        return 0
    # n이 1이면 1을 반환
    elif n == 1:
        return 1
    else:
        # 이 else문에 올 수 있는 가장 적은 수 2를 기준으로
        first, second = 0, 1
        # 2부터 n까지도 위의 규칙과 동일한 규칙이 실행되어야 한다.
        # 2부터 n까지 모두 순회 할 건데...
            # 피보나치의 규칙상, 사실 그렇게 순회해서 얻어내는
            # 2, 3, 4, ... n 까지 있는 수는 필요 X
        # 그러므로, 임시변수는 _로 처리
        for _ in range(2, n+1):
            next_fib = first + second
            # 또한, 다음 피보나치 수가 이제 second가 되어야 한다.
            # first = second
            # second = next_fib
            first, second = second, next_fib
        return second
# 사용 예시
print(fibonacci_for_loop(10)) # 55