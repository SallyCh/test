import timeit
import sys
menu=0
todomenu=0
tasklimit=3
todo1=0
todo2=0
todo3=0
tasks=[]
timetodo1=[]
timetodo2=[]
timetodo3=[]

while menu != 9:
    print("-----------------------------------------------------")
    print("                    집중력 측정기                   ")
    print("     *오늘하루, 당신이 꼭 집중해야 할 일 3가지를 적어주세요!")
    print("한번 테스커를 실행하면 종료전까지 수정이 불가능합니다. 신중하게 적어주세요")
    print("-----------------------------------------------------")
    print('1. 할일 확인')
    print('2. 할일 추가')
    print('3. 할일 삭제')
    print('8. 테스커 실행')
    print('9. 프로그램 종료')
    while True:
        menu=int(input('메뉴를 선택하시오: '))
        if menu ==1:
            if len(tasks)==0:
                print("할일이 없습니다. 할일을 추가해주세요")
            else:
                print("할일:", tasks)
        elif menu==2:
            for i in range(tasklimit):
                createtodo=input('해야할 일을 적어주세요: ')
                tasks.append(createtodo)
        elif menu==3:
            del_name=input('삭제하고 싶은 일을 적어주세요: ')
            if del_name in tasks:
                tasks.remove(del_name)
                createtodo = input('해야할 일을 적어주세요: ')
                tasks.append(createtodo)
            else:
                print('일이 발견되지 않았음')
        elif menu==8:
            print("--------------")
            print('1. ', tasks[0], '집중해보기')
            print('2. ', tasks[1], '집중해보기')
            print('3. ', tasks[2], '집중해보기')
            print('4. 집중시간 확인하기')
            print('5. 총 집중시간')
            print('6. 종료하기')
            print("--------------")
            while True:
                todomenu=int(input('테스커 입력창: '))
                while True:
                    if todomenu==1:
                        start=timeit.default_timer()
                        todo1=int(input('집중을 종료하려면 1을 입력하시오:'))
                        if todo1==1:
                            stop=timeit.default_timer()
                            timetodo1.append(stop-start)
                            print(tasks[0],'을', stop-start,'초 동안 집중했습니다!')
                            print('총', tasks[0], '을', sum(timetodo1), '초 만큼 집중했습니다.')
                        break
                    elif todomenu==2:
                        start=timeit.default_timer()
                        todo2=int(input('집중을 종료하려면 1을 입력하시오:'))
                        if todo2==1:
                            stop=timeit.default_timer()
                            timetodo2.append(stop-start)
                            print(tasks[1],'을', stop-start,'초 동안 집중했습니다!')
                            print('총', tasks[1], '을', sum(timetodo2), '초 만큼 집중했습니다.')
                        break
                    elif todomenu==3:
                        start=timeit.default_timer()
                        todo3=int(input('집중을 종료하려면 1을 입력하시오:'))
                        if todo3==1:
                            stop=timeit.default_timer()
                            timetodo3.append(stop - start)
                            print(tasks[2],'을', stop-start,'초 동안 집중했습니다!')
                            print('총', tasks[2], '을', sum(timetodo3), '초 만큼 집중했습니다.')
                        break
                    elif todomenu==4:
                        print(tasks[0], '의 집중시간: ', sum(timetodo1), '초')
                        print(tasks[1], '의 집중시간: ', sum(timetodo2), '초')
                        print(tasks[2], '의 집중시간: ', sum(timetodo3), '초')
                        break
                    elif todomenu==5:
                        print('총 집중시간: ', sum(timetodo1+timetodo2+timetodo3),'초')
                        break
                    elif todomenu==6:
                        print('고생하셨습니다.')
                        sys.exit(1)
        elif menu==9:
            break