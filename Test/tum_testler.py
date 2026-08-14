# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from eFatura import e_fatura

def test_false():
    assert e_fatura("7430531392") == False

def test_true():
    assert e_fatura("0080067509") == True
