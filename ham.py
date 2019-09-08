def square(lst) :
    #return phai dung list
    #     sq_lst = []
    #     for num in lst :
    #         sq_lst.append(num**2)
    # return sq_lst
   for num in lst : 
       yield num**2

       
kteam_ret =square([1,2,3])
for value in kteam_ret: 
    print(value)