"""
class를 2개 만든다
계산을 하는 클래스
입력을 받는 클래스
2개의 클래스를 상속받는 계산기 클래스를 만들어서 계산기가 작동하게 만든다.
GUI 필요없음
입력예시)
1.1번째 숫자입력
2.계산부호 입력
3.2번째 숫자입력
4.1번째 숫자와 2번째 숫자를 계산부호로 계산한 결과를 출력
"""
"""class vari:
    def insrt(self):
    a=int(input('1st?'))
    b=int(input('2nd?'))
class cal:
    def add(self):
        result=a+b
        return result
    def min(self):
        result=a+b
        return result
    def mul(self):
        result=a+b
        return result
    def sub(self):
        result=a+b
        return result
class kim(vari,cal):
    pass
h=kim()"""
class calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b 
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b   
    def div(self,a,b):
         if b != 0:
            return a / b
         else:
            return "error"
class vari:
    def __init__(self):
        pass
    def qu_num(self,text):
        return int(input(text))
    def qu_booho(self):
        return input('what bohoo')



    
class fin(calculator,vari):
    def run(self):
        first=self.qu_num('첫번째?')
        bohoo=self.qu_booho()
        second=self.qu_num('두번째?')
        if bohoo=='+':
            result=self.add(first,second)
        elif bohoo=='-':
            result=self.sub(first,second)
        elif bohoo=='*':
            result=self.mul(first,second)
        elif bohoo=='/':
            result=self.div(first,second)
        print(result)
a=fin()   
a.run()      