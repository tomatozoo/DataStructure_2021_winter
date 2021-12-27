# 키보드 입력을 통해 점수 계산

# 매 프레임마다 
#   입력 : 핀의 수
#   출력 : score board 점수 및 결과
        # 예외 : 필요한 값 입력될 때까지 출력 보류
            # 스트라이크
            # 스페어
            # 10 프레임에 스트라이크 / 스페어 치면 보너스 드로우 입력

# 스켈레톤 코드 이용함

def bowling():
    total = 0
    frame = []
    stack = []
    result = 'X'
    status = 'NONE'
    
    for i in range(10):
        
        print()
        first, second = input(f"{i+1} 프레임 : ").split(' ')
        f_total = int(first) + int(second)
        stack.append((int(first), int(second), result, f_total))

        
        if int(first) == 10:
            status = 'STRIKE'
            result = 'X'
            
            # 하나 더 받아서 계산
            """ 
            다음 거 첫번째 두번째를 모두 더해준다
            
            만약 다다음거도 스트라이크이면, 다음다음 첫번째 것도 더해준다
            
            """
            next_first, next_second = input(f"{i+2} 프레임 : ").split(' ')
            f_total += int(next_first)+ int(next_second)
            
        elif int(first) + int(second) == 10:
            status = 'SPARE'
            result = '/'
            
            # 하나 더 받아서 계산
            """ 
            다음 거 첫번째 거만 받아서 더한다
            
            """
            next_first, next_second = input(f"{i+2} 프레임 : ").split(' ')
            f_total += int(next_first)
            
        else:
            status = 'NONE'
            result = '-'
        
            total += f_total
            frame.append((int(first), int(second), result, f_total))
            print(frame)
            print("Total = ", total)
            print()

bowling()