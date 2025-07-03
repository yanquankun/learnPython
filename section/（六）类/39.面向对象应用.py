"""
@Desc: 本讲解如何使用面向对象编程（OOP）中的面向对象和面向过程的编程方法
@Author: Mint.Yan
@Date: 2025-07-183 13:40:47
"""


# 注意点：
# 1. 类名通常使用驼峰命名法（首字母大写）
# 2. 类的属性和方法通常使用小写字母和下划线分隔
# 3. 类的属性可以是类属性（所有实例共享）或实例属性（每个实例独有）
# 4. 类的方法通常以self作为第一个参数，表示实例本身
# 5. 类的文档字符串（docstring）用于描述类的功能和用法
# 6. 通过super()函数可以调用父类的方法，方便实现继承和多态
# 7. 通过双下划线前缀定义的是私有属性和方法，不能在类外部直接访问

# 创建类：
# class Coffee(object):
# • class 定义类的关键字
# • Coffee 类的名称，一般首字母大写
# • object 父类，可不写，默认继承自 object，如传值X class，则表示 Coffee 类继承自 x class
# • 还可以使用 type() 函数创建类（一般用于动态创建类）
# • 类的初始化方法通常命名为 __init__，用于初始化实例的属性

class Dog:
    """
    狗类，表示一只狗
    """

    # 类的属性（所有实例共享）
    desc = "this is dog class"

    def __init__(self, name, age):
        """
        初始化方法，创建一个狗的实例
        :param name: str, 狗的名字
        :param age: int, 狗的年龄
        """
        print(f"{self.__class__.__name__} Class Init:{name}")
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    # 类的方法
    def bark(self):
        """
        狗叫方法
        :return: str, 狗叫声
        """
        return f"{self.name} says Woof!"

    def __str__(self):
        """
        返回类的字符串表示
        :return: str, 类的描述信息
        """
        return f"Dog(name={self.name}, age={self.age})"

    def get_description(self):
        """
        获取类的描述信息
        :return: str, 类的描述信息
        """
        return self.desc


# 类的实例化
dog1 = Dog("Buddy", 3)  # 创建一个名为 Buddy 的狗，年龄为 3 岁
dog2 = Dog("Max", 5)  # 创建一个名为 Max 的狗，年龄为 5 岁

# 调用类的方法
print(dog1.bark())  # 输出: Buddy says Woof!
print(dog2.bark())  # 输出: Max says Woof!

print("===" * 10)


# 类的继承
class Puppy(Dog):
    """
    小狗类，继承自 Dog 类
    """

    def __init__(self, name, age, breed):
        """
        初始化方法，创建一个小狗的实例
        :param name: str, 小狗的名字
        :param age: int, 小狗的年龄
        :param breed: str, 小狗的品种
        """
        print(f"{self.__class__.__name__} Class Init:{super().get_description()}:{name}")
        super().__init__(name, age)  # 调用父类的初始化方法
        self.breed = breed  # 实例属性

    def play(self):
        """
        小狗玩耍方法
        :return: str, 玩耍信息
        """
        return f"{self.name} is playing!"


# 创建小狗实例
puppy1 = Puppy("Charlie", 1, "Beagle")  # 创建一个名为 Charlie 的小狗，年龄为 1 岁，品种为 Beagle
puppy2 = Puppy("Bella", 2, "Labrador")  # 创建一个名为 Bella 的小狗，年龄为 2 岁，品种为 Labrador

# 调用父类的方法
print(puppy1.bark())  # 输出: Charlie says Woof!
print(puppy2.bark())  # 输出: Bella says Woof!
print(puppy1.__str__())  # 输出: Dog(name=Charlie, age=1)
print(puppy2.__str__())  # 输出: Dog(name=Bella, age=2)

# 调用小狗特有的方法
print(puppy1.play())  # 输出: Charlie is playing!
print(puppy2.play())  # 输出: Bella is playing!
