
## 百度搜索URL提取

### 环境要求

- Python2.7 如果想在Python3 环境使用，请修改print
- PhantonJS 将PhantonJS.exe 加入环境变量:[PhantonJS下载地址](http://phantomjs.org/)
- Selenium包安装 

```python

pip install selenium
#CMD 查看安装信息
pip show selenium

```

- 如果有问题，重启电脑，或者手动指定下PhantoJS.exe路径

```python
browser = webdriver.PhantomJS(executable_path="phantomjs.exe")
```

### 基本使用

- 由于比较懒，没有加入参数解析，也没将结果写入文件，有需要自己写一下，修改Keyword 直接运行即可
- 修改pages值指定搜索的页面数量
- 获取数度挺慢，不知道是不是我的电脑问题，使用Chrome挺快的


> 后期有时间会完善