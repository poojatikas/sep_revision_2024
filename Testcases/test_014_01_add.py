class Test_014_01_addition():

    def test_01_add(self):

        a=25
        b=50
        add=a+b
        if(add==75):
            print("\n********ADDITION SUCESSFULLY********")
            print("ADDITION:",add)
            assert True
        else:
            print("\n*********SORRY,INVALID OPERATION*********")
            assert False