import pytest
def removeG(string):
    return string.replace("g", " ")
pytest.mark.parametrize('input , result',
                        [
                              ("good","ood") , ("gun","un") , ("good girl","ood irl")
                        ])
def test_string(input , result):
    assert removeG(input) == result