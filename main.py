my_math_lib/
    ├── my_math/
    │   ├── __init__.py
    │   └── operations.py
    ├── setup.py
    └── README.md
# my_math/operations.py

def add(a, b):
    """Возвращает сумму a и b."""
    return a + b

def subtract(a, b):
    """Возвращает разность a и b."""
    return a - b

def multiply(a, b):
    """Возвращает произведение a и b."""
    return a * b

def divide(a, b):
    """Возвращает частное от деления a на b."""
    if b == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return a / b
# my_math/__init__.py

from .operations import add, subtract, multiply, divide

# setup.py

from setuptools import setup, find_packages

setup(
    name='my_math_lib',
    version='0.1',
    packages=find_packages(),
    description='Простая библиотека для базовых математических операций',
    author='Ваше имя',
    author_email='ваша_почта@example.com',
    url='https://github.com/ваш_пользователь/my_math_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# My Math Library



## Установка


## Использование
from my_math import add, subtract, multiply, divide

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
print(multiply(3, 4))   # 12
print(divide(10, 2))     # 5.0


### Шаг 3: Установка библиотеки и тестирование

