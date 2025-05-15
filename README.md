# learnPython
自学习python的仓库

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