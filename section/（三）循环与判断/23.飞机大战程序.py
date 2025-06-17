"""
@Desc: 本讲解Python内置数据类型的飞机大战程序
@Author: Mint.Yan
@Date: 2025-06-168 13:38:00
"""
from pynput.keyboard import Listener, KeyCode


# 核心功能：飞机大战游戏的基本实现
# 1. 对象：我方飞机、低机
# 2. 属性：坐标、生命值
# 3. 方法：移动、命中飞机（敌我双方）

# 生成地图：
def create_map(_width, _height):
    return [[0 for _ in range(_width)] for _ in range(_height)]


width = 3  # 地图宽度
height = 3  # 地图高度
background = create_map(width, height)
# 在地图上放置飞机
background[1][1] = '飞机'
print("地图生成成功！", background)
print("按下 'c' 键，结束游戏")


# 监听wasd键按下
def on_press(key):
    # 飞机移动完成，则跳出最外层循环，防止重复调用
    moved = False
    try:
        if key.char == 'w':
            print("向上移动")
            for i in range(width):
                for j in range(height):
                    if background[i][j] == '飞机' and i > 0:
                        background[i][j] = 0
                        background[i - 1][j] = '飞机'
                        break
                if moved:
                    break

        elif key == KeyCode.from_char('s'):
            print("向下移动")
            for i in range(width):
                for j in range(height):
                    if background[i][j] == "飞机" and i < 2:
                        background[i][j] = 0
                        background[i + 1][j] = "飞机"
                        moved = True
                        break
                if moved:
                    break

        elif key.char == 'a':
            print("向左移动")
            for i in range(width):
                for j in range(height):
                    if background[i][j] == '飞机' and j > 0:
                        background[i][j] = 0
                        background[i][j - 1] = '飞机'
                        break
                if moved:
                    break

        elif key.char == 'd':
            print("向右移动")
            for i in range(width):
                for j in range(height):
                    if background[i][j] == '飞机' and j < width - 1:
                        background[i][j] = 0
                        background[i][j + 1] = '飞机'
                        break
                if moved:
                    break
        elif key.char == 'c':
            print("Game Over!")
            listener.stop()

        print()
        print("当前地图状态：", background)
    except AttributeError:
        pass  # 忽略非字符键


with Listener(on_release=on_press) as listener:
    print("按下 'w', 'a', 's', 'd' 键来控制飞机移动")
    listener.join()  # 等待监听器结束
