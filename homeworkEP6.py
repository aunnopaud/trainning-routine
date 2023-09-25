#daily_weight trainning

#getup7-8 eat8-9 hobby11-12 hobby13-16  (trainning16-19 cooldown17.40 rest19.45) , back to home20 and sleep21-6

check_time = float(input('what is times? : '))
healthy_food = {'a':'Salmon salad','b':'Tuna Sandwich+Salad and Fried rice','c':'Banana and Sandwich','d':'Whey protien'} #dictionary use {} 
hobby = ['drawing','play game','play football','read python text'] #list
trainning_type = {'a':'Plank','b':'Clinch','c':'Sit up','d':'Push ups','e':'Dumbell curls','cool':'Cool Down','rest':'Rest'} #dictionary
t_type = ('Plank','Clinch','Sit up','Push ups','Dumbell curls')
if 7<= check_time <8 :
    print('get up', check_time)
    check_time = float(input('after you get up , what is times? : '))
    print('Select food (type number a-d) \n a.Salmon salad \n b.Tuna Sandwich+Salad and Fried rice \n c.Banana and Sandwich \n d.Whey protien')
    food_want = str((input('Type code of food you want to eat : ')))
    if 8<= check_time < 9 and food_want == 'a' or 'b' or 'c' or 'd' :
        print(check_time, 'is times to eat , you can eat ', (healthy_food[food_want]))
        check_time = float(input('after you eat some food , what is times? : '))
        print('This is my hobby : \n drawing \n play game \n play football \n read python text')
        hobby_todo = input('i want to do : ')
        if 11<= check_time <16 :
            print('let is do hobbyyyyy... let is do  ', hobby_todo )
            print('completed')
            check_time = float(input('Fininshed your hobby?, what is times? : '))
            if check_time >= 16 : 
                print('let is Trainning .. Now is ', check_time )
                print('Go to gym')
                print('Your trainning \n a.Plank \n b.Clinch \n c.Sit up \n d. Push ups \n e.Dumbell curls \n cool - Cool Down \n rest - Rest') 
                while check_time <= 20 : #ทำใน loop จนกว่าจะตรงเงื่อนไข หากตรงเงื่อนไข จะหลุดจาก loop
                    print('now is', check_time )
                    print('Your trainning \n a.Plank 30 min \n b.Clinch 30 min \n c.Sit up 100 times \n d. Push ups 150 times \n e.Dumbell curls 80 times \n cool - Cool Down \n rest - Rest')
                   #t_type = input('Type your trainning : ') 
                    '''while t_type in trainning_type :
                        print('You do', t_type ,'30 minutes')
                        print('Now, time is ', check_time+0.50)'''
                    check_time = check_time + 0.5
                print('This time is more than 20.00, You must rest \n And now You can Back to home ')
                for i in range(5):
                    print('Car Driving Now ....')
                print('Here is your home , take a bath and sleep in 21 ')
            else :
                print('GO TO SLEEP AND START THE PROGRAM NEXT DAY!!!')
        else :
            print('GO TO SLEEP AND START THE PROGRAM NEXT DAY!!!')
    else :
        print('GO TO SLEEP AND START THE PROGRAM NEXT DAY!!!')
else :
    print('GO TO SLEEP AND START THE PROGRAM NEXT DAY!!!')


                











