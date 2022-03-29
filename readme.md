![coverage badge](https://raw.githubusercontent.com/percent4/unittest_example/master/coverage.svg)

本项目用于展示python中的unittest（单元测试）模块的使用以及coverage模块的使用。

文本用途说明如下:

- func_add.py: python代码
- test_func_add.py: 单元测试脚本
- test_coverage_api: 使用coverage api实现单元测试
- .coveragerc: coverage配置文件,具体使用可参考: [https://coverage.readthedocs.io/en/6.3.2/config.html](https://coverage.readthedocs.io/en/6.3.2/config.html)

添加coverage badge说明如下:

1. 安装coverage和coverage-badge模块
2. 使用coverage模块对python代码实现单元测试，运行后生成.coverage文件
3. 再运行`coverage-badge -o coverage.svg`即可生成coverage badge