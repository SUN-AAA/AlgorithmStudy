from typing import Any

class FixedStack:
    #스택이 비어있을 때 pop 또는 peak 할 경우 내보내는 예외처리
    class Empty(Exception):
        pass

    #스택이 가득 차 있을 때 push 할 경우 내보내는 예외처리
    class Full(Exception):
        pass

    #스택 초기화
    def __init__(self, capacity: int = 256):
        self.stk = [None] * capacity    #스택 배열
        self.capacity = capacity        #스택 크기
        self.ptr = 0                    #스택 포인터
    
    #쌓여있는 데이터의 개수를 알아내는 __len__() 함수
    def __len__(self):
        return self.ptr                 #스택 포인터 값 그대로 반환
    
    #스택이 비어 있는지 판단하는 is_empty() 함수
    def is_empty(self):
        return self.ptr <= 0
    
    #스택이 가득 차 있는지 판단하는 is_full() 함수
    def is_full(self):
        return self.ptr >= self.capacity
    
    #push() 함수
    def push(self, value: Any):
        if self.is_full():              #스택이 가득 차 있으면 예외처리 발생
            raise FixedStack.Full
        self.stk[self.ptr] = value      #스택에 값 추가
        self.ptr += 1                   #스택 포인터 값 증가
    
    #pop() 함수
    def pop(self):
        if self.is_empty():             #스택이 비어 있으면 예외처리 발생
            raise FixedStack.Empty
        self.ptr -= 1                   #스택 포인터 값 감소
        return self.stk[self.ptr]       #pop 된 값 반환
    
    #스택의 꼭대기 데이터를 들여다보는 peek() 함수
    def peek(self):
        if self.is_empty():             #스택이 비어 있으면 예외처리 발생
            raise FixedStack.Empty
        return self.stk[self.ptr-1]     #꼭대기 값 반환
    
    #스택의 모든 데이터를 삭제하는 clear() 함수
    def clear(self):
        self.ptr = 0

    #데이터를 검색하는 find() 함수 -> 발견한 원소의 인덱스를 반환, 실패하면 -1 반환
    def find(self,value: Any):
        for i in range(self.ptr-1, -1, -1):     #꼭대기 값부터탐색
            if self.stk[i] == value:            #발견하면 인덱스 값 반환
                return i
        return -1                               #없으면 -1 반환
    
    #데이터 개수를 세는 count() 함수
    def count(self,value:Any):
        c = 0
        for i in range(self.ptr):           
            if self.stk[i] == value:
                c += 1
        return c
    
    #데이터가 포함되어 있는지 판단하는 __contains()__ 함수
    def __contains__(self,value: Any):
        return self.count(value) > 0
    
    #스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력하는 dump() 함수
    def dump(self):
        print(self.stk[:self.ptr])

s1 = FixedStack()
for i in range(10):
    s1.push(i)

s1.dump()
print(s1.peek())

s1.pop()
print(s1.peek())

print(s1.find(3))
print(s1.count(1))
print(s1.__contains__(8))

s1.clear()
s1.dump()