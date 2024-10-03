import pytest

class Test_015_MKcreation():

    @pytest.mark.skip
    def test_01_addition(self):
        a=100
        b=25
        add=a+b
        if(add==125):
            print("\n********ADDITION SUCESFULLY*******")
            print("ADDITIO:",add)
            assert True
        else:
            print("********INVALID OPERATION")
            assert False

    @pytest.mark.xfail
    def test_02_substraction(self):
        a=10
        b=5
        sub=a-b
        if(sub==5):
            print("\n**********SUBSTRACTION SUCESSFULLY*******")
            print("SUBSTRACTION:",sub)
            assert True
        else:
            print("************INVALID OPERATION**********")
            assert False

    @pytest.mark.skipif
    def test_03_Multiplication(self):
        a=10
        b=5
        mul=a*b
        if(mul==50):
            print("\n***********MULTIPLICATION SUCESSFULLY********")
            print("MULTIPLICATION:",mul)
            assert True
        else:
            print("*************INVALID OPERATION***********")
            assert False

    def test_04_division(self):
        a=10
        b=2
        div=a/b
        if int(div==5):
            print("\n**************DIVISION SUCESSFULLY***********")
            print("DIVISION:",div)
            assert True
        else:
            print("**************INVALID OPERATON***********")
            assert False