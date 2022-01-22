Letter = '''
         Dear <|Name|>,
         You are Selected !!!!


         Date: <|Date|>
         
         '''
Name = input("Enter Your Name :\n")
Date = input("Enter Date \n")

Letter = Letter.replace("<|Name|>" , Name)
Letter = Letter.replace(" <|Date|>" , Date)
print(Letter)
