# 소수 구하기

a = 8
b = 16

# a ~ b 범위의 숫자 중에서 소수가 아닌 것들을 지워나가는 방식 이용
# 1단계: 방문 리스트 준비하기.
# ** 리스트 인덱스와 실제 정수 값을 같게 해주기위해 0부터 넣을 것이기 때문에 갯수는 b+1로 해주자.
# visited = [0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
visited = [0] * (b+1)

for i in range(2, b+1):          # 정수 리스트: 2부터 16까지.
    if visited[i] == 0:          # 배수에 해당 하는 녀석들을 지워주자.
        for j in range(i*2, b+1, i):    # range설명: i가 2일때: j는 4,6,8,10,12,14,16
            visited[j] = 1       # 배수에 1표시 해주기
# print(visited)
# visited에 배수인 녀석들을 1로 표시 해줬으니, 0인 녀석들의 값을 뽑자.
# 어떻게? visited 인덱스 자리와 실제 정수 자리 값을 같게 해주자. visited[2] = 정수2
for i in range(b+1):        # i의 범위는 0 ~ 16까지   ** 정수의 범위를 지정해서 그 안에 속한 소수를 뽑고 싶으면 range를 조절하자.
    if i > 1 and visited[i] == 0:     # visited에 0이라고 돼있는 녀석들을 정수로 뽑아내자.
        print(i)            # 하지만 숫자 0과 1은 정수가 될 수 없으니 제외 시켜야 해.



