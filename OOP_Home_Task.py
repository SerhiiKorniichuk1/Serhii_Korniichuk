
class A:
    def test(self):
        print('A')
        return 'A'


class B(A):
    def test(self):
        print('B')
        return 'B' + super().test()


class C(A):
    def test(self):
        print('C')
        return 'C' + super().test()


class D(B):
    def test(self):
        print('D')
        return 'D' + super().test()

class E(C):
    def test(self):
        print('E')
        return 'E' + super().test()


def test_method(cls):
    print(cls)
    print(cls().test())


if __name__ == '__main__':
    test_method(A)
    test_method(B)
    test_method(C)
    test_method(D)
    test_method(E)