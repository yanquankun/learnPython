# learnPython

自学习python的仓库

---

# 项目开始前

##### 安装python

``` bash
# macOS (我选择了最新的stable版本，实际我本机装了2.7、3.9和3.10的包，brew需要自行安装)
brew install python@3.10
# Windows
# 直接去官网下载安装包
```

##### 生成虚拟环境（使用虚拟环境，类似node项目中单个项目的node_modules，否则使用的是全局python的依赖包）

```bash
python -m venv venv
```

*安装的包会存储在虚拟环境的 site-packages 目录中，路径如下：  
macOS/Linux: venv/lib/pythonX.X/site-packages
Windows: venv\Lib\site-packages*

##### 激活虚拟环境

```bash
source venv/bin/activate
```

##### 使用pip安装依赖包（使用requirements.txt方便我们快速的安装所有的依赖包）

```bash
# 生成requirements.txt
pip freeze > requirements.txt
# 安装requirements.txt中的依赖包   
pip install -r requirements.txt
```

##### 安装依赖包示例

```bash
pip install <package_name>
or
python[your version] -m pip install requests
```

`如果总是提示安装超时，那你需要一个VPN了`

---

# 项目开始

##### 环境

- python3.10.7
- pip3 21.2.4
- macOS 13.4

##### 运行

- 所有学习代码均在section目录下
- 每个py文件为一个小节
- 可单独运行该py文件

---

# 学习内容

python基础

- 1.输入输出

---

# 参考资料

- [Python中文文档](https://docs.python.org/zh-cn/3/)
- [Python3.10.7中文文档](https://docs.python.org/zh-cn/3.10/)
- [Python标准库](https://docs.python.org/zh-cn/3/library/index.html)