import pytest 

class Test_02:
    @pytest.mark.parametrize("a,b",[(1,6),(2,5),(3,4)])
    def test_002(self,a,b):
        c = a + b 
        assert c == 7

        
