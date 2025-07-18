"""
@Desc: 本讲解为python中设计模式的讲解，主要介绍了设计模式的概念、分类以及常用的设计模式。
@Author: Mint.Yan
@Date: 2025-07-197 14:13:13
"""


# 设计模式是软件开发中常用的解决方案，它们提供了一种通用的方式来解决特定类型的问题。以下是一些常见的设计模式：
# 1. 创建型模式（Creational Patterns）：这些模式涉及对象的创建方式。
#   - 单例模式（Singleton Pattern）
#   - 工厂模式（Factory Pattern）
#   - 抽象工厂模式（Abstract Factory Pattern）
#   - 建造者模式（Builder Pattern）
#   - 原型模式（Prototype Pattern）

# 创建型模式的典型设计模式：单例模式
#   单实例模式可以由import来实现
#       例如：from singleton import Singleton
#   可以借助类属性实现多实例共享(monostate)一个属性
class MonostateSingleton:
    # 类属性，所有实例共享
    _val = None

    def __init__(self, val):
        # 等于调用了get_var的setter方法，给_val进行了赋值
        self.get_var = val

    @property
    def get_var(self):
        return self._val

    # 描述器
    @get_var.setter
    def get_var(self, value):
        # 这里是核心，通过__class__._val来访问类属性
        # 而不是实例属性，从而修改了所有实例共享的类属性
        self.__class__._val = value

    def display(self):
        return self.get_var


monostate1 = MonostateSingleton(10)
monostate2 = MonostateSingleton(20)
# 由于monostate1和monostate2共享同一个类属性_val，所以修改其中一个实例的_val会影响到另一个实例
# 这里修改monostate2的_val
# 会导致monostate1的_val也被修改
monostate2.get_var = 30

print(monostate1.get_var)
print(monostate1.display())
print("===" * 10)


#   也可以借助__new__方法实现单例模式
class Singleton:
    _instance = None

    # **kwargs 允许传入任意关键字参数
    # *args 允许传入任意位置参数
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance
        else:
            print("Instance already exists, returning the existing instance.")
            return cls._instance


singleton = Singleton()
singleton2 = Singleton()
print("===" * 10)


# 2. 结构型模式（Structural Patterns）：这些模式涉及对象的组合方式。
#   - 适配器模式（Adapter Pattern）
#   - 桥接模式（Bridge Pattern）
#   - 组合模式（Composite Pattern）
#   - 装饰器模式（Decorator Pattern）
#   - 外观模式（Facade Pattern）

# 结构型模式的典型设计模式：适配器模式
#   通常用来解决不同接口之间的兼容问题

class OldSystem:
    def old_method(self):
        return "Old System Method"


class NewSystem:
    def new_method(self):
        return "New System Method"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.old_method()


#  使用适配器模式
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.new_method())  # 输出: Old System Method
new_system = NewSystem()
print(new_system.new_method())  # 输出: New System Method
# 可以看到，我们通过适配器模式将旧系统的接口适配为新系统的接口，使得它们可以互相兼容

print("===" * 10)


# 3. 行为型模式（Behavioral Patterns）：这些模式涉及对象之间的交互和职责分配。
#   - 观察者模式（Observer Pattern）
#   - 策略模式（Strategy Pattern）
#   - 命令模式（Command Pattern）

# 行为型模式的典型设计模式：观察者模式

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} Observer received message: {message}")


# 使用观察者模式
subject = Subject()
observer1 = Observer('obs1')
observer2 = Observer('obs2')
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello Observers!")
# 输出：
# obs1 Observer received message: Hello Observers!
# obs2 Observer received message: Hello Observers!
