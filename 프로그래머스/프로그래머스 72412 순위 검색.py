"""
# 문제
2021 카카오 블라인드 테스트 3번 순위 검색
https://programmers.co.kr/learn/courses/30/lessons/72412

# 원인
binary search 를 잘못 짜서 시간이 오래걸렸다고 생각했으나
dictionary 에 원소를 넣는 과정에서 배열을 비효율적으로 사용해서 시간 지연이 발생함

# 내용
배열에 새로운 원소를 더할때 + 를 사용하지 않고 append 를 사용해야 한다
+ 를 사용할 경우, 새로운 배열을 생성하기 때문에 빅오가 O(n^2)이다.
append 를 사용할 경우, 기존 배열의 끝에 원소를 더하기 때문에 빅오가 O(1)이다.
Line 34 -> Line 35
Line 47 -> Line 48

참고자료 : https://www.geeksforgeeks.org/difference-between-and-append-in-python/


"""
import random, time


def solution(info, query):
    answer = []

    # info parse 하고 이것을 key, 코테 점수를 value 로 저장
    info_dic = {}
    parse_cases = [[0], [1], [2], [3], [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2, 3]]

    for i in info:
        # 지원서 parse
        data = i.split(' ')
        r_sentence = ''.join(data[:-1])
        if r_sentence in info_dic:
            # info_dic[r_sentence] = info_dic[r_sentence] + [int(data[-1])]
            info_dic[r_sentence].append(int(data[-1]))
        else:
            info_dic[r_sentence] = [int(data[-1])]

        for parse_case in parse_cases:
            t_data = i.split(' ')[:-1]
            for idx in parse_case:
                t_data[idx] = '-'
            r_sentence = ''.join(t_data)

            if info_dic.get(r_sentence) is not None:
                # info_dic[r_sentence] = info_dic[r_sentence] + [int(data[-1])]
                info_dic[r_sentence].append(int(data[-1]))
            else:
                info_dic[r_sentence] = [int(data[-1])]
    # print(info_dic)

    # info_dic value 오름차순으로 정렬하기
    for dic_key in info_dic.keys():
        info_dic[dic_key].sort()

    # print(info_dic)

    for q in query:
        # 질의 parse
        t_q = q.split(' and ')
        q = t_q[:-1] + t_q[-1].split(' ')

        q_value = int(q[-1])
        q_key = ''.join(q[:-1])

        # 질의를 만족하는 info가 있는지 확인
        if q_key in info_dic:
            value_list = info_dic.get(q_key)

            # 이분 탐색으로 value_list 보다 크거나 같은 최초의 value idx 찾기
            get_idx = binary_search(value_list, q_value)
            if get_idx == -1:
                answer.append(0)
            else:
                res = len(value_list) - get_idx
                answer.append(res)
        else:
            answer.append(0)

    return answer


def binary_search(value_list, value_want):
    check_idx = len(value_list) // 2

    low_idx = 0
    high_idx = len(value_list) - 1

    # 찾고자 하는 값이 모든 값보다 작거나 같을때
    if value_want <= value_list[low_idx]:
        check_idx = 0
    # 찾고자 하는 값이 모든 값보다 큰 경우
    elif value_want > value_list[high_idx]:
        check_idx = -1
    else:
        # 찾고자 하는 값이 중간에 있는 경우
        while True:
            if value_list[check_idx - 1] < value_want <= value_list[check_idx]:
                break
            elif value_want <= value_list[check_idx]:
                high_idx = check_idx
            else:
                low_idx = check_idx + 1
            check_idx = (low_idx + high_idx) // 2
    # print("check_idx:", check_idx)
    return check_idx


def make_case(info, query):
    language = ['cpp', 'java', 'python', '-']
    work = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    soul_food = ['chicken', 'pizza', '-']
    score = [1, 100000]
    # info_size = random.randint(1, 50000)
    # query_size = random.randint(1, 100000)
    info_size = 50000
    query_size = 50000

    for _ in range(info_size):
        sentence = language[random.randint(0, 2)] + " " + work[random.randint(0, 1)] + " " + career[random.randint(0, 1)]\
                   + " " + soul_food[random.randint(0, 1)] + " " + str(random.randint(score[0], score[1]))
        info.append(sentence)

    for _ in range(query_size):
        sentence = language[random.randint(0, 3)] + " and " + work[random.randint(0, 2)] + " and " + career[
            random.randint(0, 2)] \
                   + " and " + soul_food[random.randint(0, 2)] + " " + str(random.randint(score[0], score[1]))
        query.append(sentence)


info = []
query = []
make_case(info, query)

st = time.time()
ans = solution(info, query)
print(time.time() - st)