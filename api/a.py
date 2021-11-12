import pytest

class TestA:
    a = 1
    def test_01(self):
        print("--1",self.a,TestA.a)
        TestA.a = 3
        self.a = 4

        print("===",TestA.a,self.a)

    def test_02(self):
        raise 99
        print("-->2",self.a)

    def teardown(self):
        print("-->>>>>3",TestA.a)
if __name__ == '__main__':
    pytest.main(['-s', 'a.py'])
