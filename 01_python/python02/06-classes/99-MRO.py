O = object
class D(O):
    pass
class D(O): pass
class E(O): pass
class F(O): pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass

# A 클래스의 상속 탐색 순서 출력
print(A.__mro__)