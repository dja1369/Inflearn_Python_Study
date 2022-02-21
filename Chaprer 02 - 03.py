# OOP(객체 지향 프로그래밍) -> 코드의 재사용, 코드 중복 방지 , 유지보수
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대함 -> 복잡함, 개선의 어려움
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Lee
    Date : 2022.02.20
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details

    def __str__(self):
        return f' stf : {self._company} - {self._details}'

    def __repr__(self):
        return f' repr : {self._company} - {self._details}'

    # Intance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f"Car detail Info : {self._company} {self._details.get('price')}")

    # Instance Method
    def get_price(self):
        return f"before car price -> company : {self._company } details : {self._details.get('price')}"
    # Instance Method
    def get_price_calc(self):
        return f"before car price -> company : {self._company} details : {self._details.get('price') * Car.price_per_raise}"

    # Class Method # 클래스 메소드는 self 대신 cls를 받음 cls = Class
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Plz enter 1 Or More")
            return
        cls.price_per_raise = per
        print("Succeed Price increased")

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return f'OK! this Car is {inst._company}'
        else:
            return f"No this car is not bmw"



#Self 의미 : 클래스를 기반으로 생성된 인스턴스 내부의 고유의 값을 저장하기 위한 예약어
car1 = Car('Ferrari', {'color': 'white', 'horsepower': '400', 'price': 8000})
car2 = Car('Bmw', {'color': 'black', 'horsepower': '270', 'price': 5000})

car1.detail_info()
# print 를 두번써서 none 이 출력됨
print(car2.detail_info())

# 가격정보(직접접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 변수 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격 인상(클래스 변수 메소드 사용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 스태틱 메소드는 인자를 받을필요가 없기에 굉장히 유연하다.
# 인스턴스로 호출(스태틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(스태틱)
print(Car.is_bmw(car2))
