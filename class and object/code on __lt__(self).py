
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


n1 = Number(10)
n2 = Number(20)
n3 = Number(5)

print(n1 < n2)
print(n2 < n1)
print(n3 < n1)
