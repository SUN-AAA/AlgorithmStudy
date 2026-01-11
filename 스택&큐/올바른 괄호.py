#올바른 괄호의 조건을...찾아야되는디..
#첫번째 괄호가 ')'이거나 마지막 괄호가 '('이면 False
#여는 괄호'('가 나오면 cnt++, 닫는 괄호')'가 나오면 cnt-- -> 마지막까지 문자열 순회를 마쳤을 때 cnt == 0이면 올바른 괄호
#또, 여는 괄호는 앞에 많이 나와도 뒤에 닫는 괄호가 나오고 최종적으로 cnt==0이 되면 true이지만
#닫는 괄호가 앞에 많이 나오면(cnt < 0이 되면) 뒤에 여는 괄호가 나와고 cnt == 0이 되어도 false이므로 cnt < 0이 되면 반복 종료 및 false 반환

def solution(s):
    cnt = 0
    answer = True
    if s[0] == ')' or s[len(s) - 1] == '(':
        answer = False
    else:
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    answer = False
                    return answer

    if cnt != 0:
        answer = False 

    return answer

print(solution("()()((((()))))(())(())))"))