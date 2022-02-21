# OOP(객체 지향 프로그래밍) -> 코드의 재사용, 코드 중복 방지 , 유지보수
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대함 -> 복잡함, 개선의 어려움
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Lee
    Date : 2022.02.20
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
       #self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return f' stf : {self._company} - {self._details}'

    def __repr__(self):
        return f' repr : {self._company} - {self._details}'

    def __del__(self):
        #print('삭제 완료')
        Car.car_count -= 1

    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f"Car detail Info : {self._company} {self._details.get('price')}")


#Self 의미 : 클래스를 기반으로 생성된 인스턴스 내부의 고유의 값을 저장하기 위한 예약어
car1 = Car('Ferrari', {'color': 'white', 'horsepower': '400', 'price': 8000})
car2 = Car('BMW', {'color': 'black', 'horsespower': '270', 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': '300', 'price': 6000})

#ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

# ID값이 다르기에 당연히 False가 뜬다
print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print(car1.__dict__)
print(car2.__dict__)

# Doctring 클래스의 주석 출력
print(Car.__doc__)

#실행
car1.detail_info()
car2.detail_info()

# 비교 Car클래스의 ID를 비교한것이기에 같은걸로 출력된다
print(car1.__class__ is car2.__class__)
print(id(car1.__class__),id(car2.__class__),id(car3.__class__))

# 에러 # 인자를 넘겨주지 않아 오류가뜸
#Car.detail_info()
# 하지만 값을 넘겨준다면 정상적으로 출력됨
Car.detail_info(car1)

# 공유확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))


# 접근 방식은 편한대로 하면 된다.
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임 스페이스에 없으면 상위에서 검색
# 즉 동일한 이름으로 변수 생성가능 ( 인스턴스 검색후 -> 상위(클래스변수, 부모 클래스 변수)