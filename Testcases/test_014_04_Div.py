class Test_014_04_Division:

    def test_04_division(self):

        g=100
        h=25
        div=g/h
        if(div==4):
            print("\n************DIVISION SUCSSFULLY***********")
            print("DIVISION:",div)
            assert True

        else:
            print("***********SORRY,INVALID OPERATION********")
            assert False

