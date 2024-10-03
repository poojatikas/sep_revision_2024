class Test_014_02_substraction():

    def test_02_sub(self):

        c=100
        d=25
        sub=c-d
        if(sub==75):
            print("\n**********SUBSTRATION SUCESSFULLY*******")
            print("SUBSTARCTIO:",sub)
            assert True
        else:
            print("\n**********SORRY,INVALID OPERATION********")
            assert False