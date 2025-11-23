# IFLOW.md - rat-trig 项目指南

## 项目概述

**rat-trig** 是一个名为 "Rational Trigonometry"（有理三角学）的 Python 项目。该项目采用了一种新的方法来处理经典三角学，由 Norman Wildberger 开发，旨在通过仅使用有理数和运算，而不是无理数和极限，来简化和澄清三角学。

传统三角学中，角度的正弦、余弦和正切等概念通常使用圆和单位圆来定义，这些定义涉及无理数和极限，这使得该主题更难理解和处理。有理三角学用基于线和线段的定义替换了这些圆形定义，从而提供了更直接和直观的方法。有理三角学的基本概念是"quadaverage"（四次平均）和"dilated directed angle"（扩张有向角），它们是根据线和线段定义的，而不是圆。

## 项目结构

```
rat-trig/
├── _config.yml
├── .coveragerc
├── .gitignore
├── .pre-commit-config.yaml
├── .readthedocs.yml
├── AUTHORS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── GEMINI.md
├── LICENSE
├── LICENSE.txt
├── mypy.ini
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
├── tox.ini
├── .benchmarks/
├── .github/
├── .pytest_cache/
├── .ruff_cache/
├── docs/
├── requirements/
├── src/
│   └── rat_trig/
│       ├── __init__.py
│       ├── skeleton.py
│       └── trigonom.py
└── tests/
    ├── conftest.py
    ├── test_cross.py
    ├── test_dot.py
    ├── test_quad.py
    ├── test_skeleton.py
    ├── test_spread_law.py
    ├── test_spread.py
    ├── test_trigonom.py
    └── test_triple_quad_formula.py
```

## 核心模块

### trigonom.py
这是项目的核心模块，包含有理三角学的基本函数：

- `archimedes(q_1, q_2, q_3)`: 使用阿基米德公式计算三角形的四次面积，也可用于检查四边形是否在圆上
- `cross(v_1, v_2)`: 计算两个向量的叉积
- `dot(v_1, v_2)`: 计算两个向量的点积
- `quad(v)`: 计算向量的方差（quadrance）

### skeleton.py
提供了一个示例 Python 脚本骨架，包含一个斐波那契数列函数和命令行接口。

## 技术特性

- **类型支持**: 使用 Python 泛型类型变量 (TypeVar) 支持 int, Fraction, float 类型
- **依赖管理**: 使用 setuptools 和 pyproject.toml 管理依赖
- **测试框架**: 使用 pytest 进行测试
- **文档**: 使用 Sphinx 生成文档
- **版本控制**: 使用 setuptools_scm 进行版本管理

## 构建和运行

### 安装依赖
```bash
pip install -r requirements/default.txt
pip install -r requirements/test.txt
```

### 安装项目
```bash
pip install -e .
```

### 运行测试
```bash
pytest
# 或使用 tox
tox
```

### 构建文档
```bash
tox -e docs
```

### 运行特定测试
```bash
pytest tests/test_trigonom.py
```

## 开发约定

- 项目使用 PyScaffold 4.5 创建
- 代码遵循 PEP 8 标准
- 使用 doctest 进行文档测试
- 使用 mypy 进行类型检查
- 使用 pre-commit 钩子进行代码格式化和检查

## 项目配置

- **setup.cfg**: 包含项目元数据、依赖关系和测试配置
- **pyproject.toml**: 定义构建系统要求
- **tox.ini**: 定义 tox 环境用于测试和构建
- **mypy.ini**: 类型检查配置

## 测试结构

项目包含多个测试文件，测试不同的功能模块：
- `test_trigonom.py`: 测试 trigonom.py 中的函数
- `test_cross.py`, `test_dot.py`, `test_quad.py`: 测试相应的向量操作函数
- `test_skeleton.py`: 测试 skeleton.py 中的函数

## 作者信息

- 作者: Wai-Shing Luk
- 邮箱: luk036@gmail.com
- 许可证: MIT