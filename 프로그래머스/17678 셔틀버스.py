"""
# 문제
2018 KAKAO BLIND RECRUITMENT [1차] 셔틀버스
https://programmers.co.kr/learn/courses/30/lessons/17678

# 원인
1. 시간을 "시:분"으로 저장하고, 비교할때만 분으로 치환해서 비교하다보니 코드가 길어지고 실행 시간도 늘어남
> 애초에 시간을 분으로 저장해두고 마지막에 "시:분"으로 치환하기만 하면 간단해졌음

2. 앞 배차에 사람이 많아 못타는 사람이 있고 뒤 배차를 계산할 때, 앞 배차에 못타고 기다리고 있는 사람 중 가장 먼저 도착한 사람보다 1분 빨리 도착하면 된다고 생각함
> 앞 배차에 못타고 기다리고 있는 사람의 시간을 고려할 필요는 없음. 무조건 이번 배차에 타는 마지막 사람보다 1분 빨리 도착하면 됨

참고
"마지막버스에 자리가 없으면 남은 인원중 가장 "먼저"가 아닌 가장"마지막에" 도착한 한명보다만 빨리 도착하면됨."
https://programmers.co.kr/questions/20374
"""


def solution(n, t, m, timetable):
    answer = ''

    for idx, time in enumerate(timetable):
        hour, minute = time.split(':')
        timetable[idx] = int(hour) * 60 + int(minute)
    timetable.sort()

    now_time = 9 * 60  # 시각을 분으로 치환한 값
    now_men = 0  # 지금 배차 셔틀에 탑승한 사람 수
    bus_repeat_count = 0  # 셔틀 배차 번호

    idx = 0
    while idx < len(timetable):
        if timetable[idx] <= now_time:
            if now_men < m:
                now_men += 1
                idx += 1
            else:
                now_time += t
                bus_repeat_count += 1
                now_men = 0

                if bus_repeat_count >= n:
                    answer = timetable[idx - 1] - 1
                    break
        else:
            if now_men == m:
                answer = timetable[idx - 1] - 1
            else:
                answer = now_time

            now_time += t
            bus_repeat_count += 1
            now_men = 0

            if bus_repeat_count >= n:
                break

    if idx == len(timetable):
        if now_men < m:
            answer = 9 * 60 + (n - 1) * t
        else:
            answer = timetable[idx - 1] - 1

    hour, minute = divmod(answer, 60)
    answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
    return answer


if __name__ == '__main__':
    n = 2
    t = 10
    m = 2
    timetable = ["09:00", "09:00", "09:00", "09:08", "09:09"]
    ans = solution(n, t, m, timetable)
    print(ans)
