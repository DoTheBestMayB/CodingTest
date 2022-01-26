"""
# 문제
2018 카카오 블라인드 1차 추석 트래픽
https://programmers.co.kr/learn/courses/30/lessons/17676

# 원인
처리 시간이 0.001초 여서 처리 요청을 받자마자 끝나는 로그를 고려 하지 않았다.(26-27번 라인이 없었음)
왜 안되는지 여러 로그를 테스트 해보다가 잘못된 값이 출력되는 것을 보고 원인을 찾았다.
만약 실제 시험이였다면 찾지 못했을 것 같다.
처음에 작성할때부터 꼼꼼히하는 습관을 가져야겠다.

# 내용
left cursor, right cursor를 이용해 1초 구간 범위를 이동하며 품
"""


def solution(lines):
    answer = 0
    start_and_end_time_list = []

    for idx, line in enumerate(lines):
        end_time, process_time = get_end_time_and_process_time(line)
        start_and_end_time_list.append([end_time, idx])
        if process_time > 1:
            start_and_end_time_list.append([end_time - process_time + 1, idx])
        else:
            start_and_end_time_list.append([end_time, idx])


    start_and_end_time_list.sort()

    # left_cur 는 1초가 시작되는 지점
    left_cur = right_cur = 0

    count = 1
    right_cur = 1
    process_time_set = {start_and_end_time_list[0][1]: 2}

    for time_item, idx in start_and_end_time_list[1:]:
        if idx not in process_time_set:
            # 시작 시간과 현재 탐색하는 시간이 1초보다 많이 차이가 나면 left cursor를 이동시켜 차이를 1초 이하로 변경시킨다
            if time_item - start_and_end_time_list[left_cur][0] + 1 > 1000:
                if count > answer:
                    answer = count
                while time_item - start_and_end_time_list[left_cur][0] + 1 > 1000 and left_cur < right_cur:
                    if start_and_end_time_list[left_cur][1] in process_time_set:
                        process_time_set[start_and_end_time_list[left_cur][1]] -= 1
                        if process_time_set[start_and_end_time_list[left_cur][1]] == 0:
                            count -= 1
                            process_time_set.pop(start_and_end_time_list[left_cur][1])
                    left_cur += 1

            process_time_set[idx] = 2
            count += 1
        right_cur += 1

    if count > answer:
        answer = count

    return answer


def get_end_time_and_process_time(input_str: str):
    input_list = input_str.split(' ')
    time_list = input_list[1].split(':')
    end_time = 0
    for idx, i in enumerate(time_list):
        end_time += int(float(i)*1000 * (60**(2-idx)))

    process_time = int(float(input_list[2][:-1]) * 1000)

    return [end_time, process_time]


if __name__ == '__main__':
    input_lines = [
        "2016-09-15 00:00:00.001 0.001s",
        "2016-09-15 00:00:01.000 0.001s",
        "2016-09-15 01:00:07.000 2s"
    ]
    ans = solution(input_lines)
    print(ans)