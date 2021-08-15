class Div:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def div_null(a, b):
        try:
            return (a / b)
        except:
            return (f"Деление на ноль недопустимо")


div = Div(10, 100)
print(Div.div_null(10, 0))
print(Div.div_null(10, 0.1))
print(div.div_null(100, 0))
