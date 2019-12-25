import yaml, os, sys
import pytest

# sys.path.append(os.getcwd())

from Base.get_data import Data


def huoqu_data():
    ss = []
    r = Data().ss("xx.yml")
    for aa in r.values():
        ss.append(tuple(aa.values()))
    print(ss)
    return ss


class Test_01:
    @pytest.mark.parametrize("a,b,c", huoqu_data())
    def test_01(self, a, b, c):
        print('{}+{}={}'.format(a, b, c))
        assert a + b == c
