class Test_014_03_multiplication():

    def test_03_mul(self):

        e=10
        f=20
        mul=e*f
        if(mul==200):
            print("\n*********MULTIPLICATION SUCESSFULLY*********")
            print("MULTIPLICATION:",mul)
            assert True
        else:
            print("\n*********Sorry,INVALID OPERATION**********")
            assert False
