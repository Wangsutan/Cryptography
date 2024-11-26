# Python：凯撒密码、多表加密和恩尼格玛的面向对象实现

## 项目简介

本项目使用Python语言实现了凯撒密码、多表加密和恩尼格玛的面向对象实现。凯撒密码是一种简单的移位加密技术，通过将字母表中的每个字母替换为字母表中固定位置后的字母来实现加密。多表加密是一种更复杂的加密技术，通过使用多个凯撒密码来实现加密。恩尼格玛是一种特别复杂的加密技术，但它的基础仍然是移位加密。

本项目将移位加密的基础方法做成了一个基类`Cipher`的方法。凯撒密码、多表加密和恩尼格玛都使用了这个方法，并实现了自己的加密和解密方法。由此可以看出，这三种加密方法确实都基于一种同样的思想，即移位加密。不过，它们的上层结构却存在着巨大的差异。

## 项目结构

本项目主要包含以下程序：

- `cipher.py`：关于替换加密的基础库文件。其中包含移位加密等的基础功能，以及关于凯撒密码的一种实现。
- `polyalphabetic_cipher.py`：多表加密的实现文件。它继承了`cipher.py`模块中相应的类和变量。
- `Enigma.py`：恩尼格玛的实现文件。它继承了`cipher.py`模块中相应的类和变量。

项目文件夹下的文件的情况大致如下（可能一些文件名是不同的），供参考：

```
ls -tlr
总计 92
drwxr-xr-x 2 wst wst  4096 Sep 8日 09:28 Enigma_py
-rw-r--r-- 1 wst wst    55 Sep 9日 16:46 input.txt
-rw-r--r-- 1 wst wst  2718 Sep10日 15:54 cipher.py
-rw-r--r-- 1 wst wst    13 Sep10日 15:56 input_file.txt
-rw-r--r-- 1 wst wst    10 Sep10日 15:58 plain_file.txt
drwxr-xr-x 2 wst wst  4096 Sep10日 16:00 __pycache__
-rw-r--r-- 1 wst wst    10 Sep10日 16:02 output_file.txt
-rw-r--r-- 1 wst wst    10 Sep10日 16:10 plain_file_poly.txt
-rw-r--r-- 1 wst wst  2126 Sep10日 16:11 polyalphabetic_cipher.py
-rw-r--r-- 1 wst wst    40 Sep10日 16:23 plugboard.txt
-rw-r--r-- 1 wst wst 15126 Sep10日 16:28 Enigma.py
-rw-r--r-- 1 wst wst     9 Sep10日 16:31 rotors_cursor.txt
-rw-r--r-- 1 wst wst   260 Sep10日 16:31 reflector.txt
-rw-r--r-- 1 wst wst   368 Sep10日 16:31 passwords.txt
-rw-r--r-- 1 wst wst    48 Sep10日 16:34 output.txt
-rw-r--r-- 1 wst wst    48 Sep10日 16:36 test.txt
-rw-r--r-- 1 wst wst  4853 Sep10日 16:41 Readme.md
```

## 准备工作

1. 确保已经安装了必要的Python环境。
2. 将项目文件放置在一个文件夹中。有些文件可以由程序生成，有些需要自己准备。不过项目已经提前配置好了。

## 具体介绍

### 凯撒密码

本项目在`cipher.py`中实现了凯撒密码。代码如下：

```
```

该程序要求文件夹下存放有一个输入文本文件，文件名比如为`input_file.txt`。

`input_file.txt`的内容如下：

```
Hello, World!
```

查看命令行程序的帮助的方式如下：

```
python cipher.py -h
```

加密的命令如下：

```
python cipher.py -m 3 -i input_file.txt -o output_file.txt
```

加密后的文件内容如下：

```
KHOORZRUOG
```

解密的命令如下：

```
python cipher.py -m -3 -i output_file.txt -o plain_file.txt
```

解密后的文件内容如下：

```
HELLOWORLD
```

### 多表加密

本项目在`polyalphabetic_cipher.py`中实现了多表加密。代码如下：

```
```

该程序要求文件夹下存放有一个输入文本文件，文件名比如为`input_file.txt`。

`input_file.txt`的内容如下：

```
Hello, World!
```

查看命令行程序的帮助的方式如下：

```
python polyalphabetic_cipher.py -h
```

加密的命令如下：

```
python polyalphabetic_cipher.py -k CAT -i input_file.txt -o output_file.txt
```

加密后的文件内容如下：

```
KFFOPQRSFG
```

解密的命令如下：

```
python polyalphabetic_cipher.py -k CAT -i output_file.txt -o plain_file_poly.txt -d
```

注意观察，解密的命令中多了一个参数`-d`，表示解密。

解密后的文件内容如下：

```
HELLOWORLD
```

### 恩尼格玛

本项目在`Enigma.py`中实现了恩尼格玛。代码如下：

```
```

该程序文件夹下应该存在的文件如下：

- `input.txt`： 输入文件。文件内容如下：

```
Deutsch Vertrauen sollte stets begleiten ihre Soldaten!
```

- `output.txt`： 输出文件
- `reflector.txt`： 反射器配置文件。文件内容如下：

```
{'N': 'W', 'U': 'M', 'G': 'S', 'Z': 'D', 'Q': 'L', 'E': 'A', 'B': 'V', 'C': 'R', 'X': 'H', 'O': 'T', 'J': 'K', 'Y': 'P', 'F': 'I', 'W': 'N', 'M': 'U', 'S': 'G', 'D': 'Z', 'L': 'Q', 'A': 'E', 'V': 'B', 'R': 'C', 'H': 'X', 'T': 'O', 'K': 'J', 'P': 'Y', 'I': 'F'}
```

- `passwords.txt`：密码本。文件内容如下：

```
[4, 16, 5, 19, 22, 14, 10, 9, 23, 2, 12, 6, 17, 8, 20, 1, 15, 18, 25, 13, 11, 24, 3, 21, 7]
[9, 20, 10, 4, 8, 7, 14, 25, 6, 13, 11, 2, 23, 24, 21, 18, 1, 3, 16, 12, 15, 19, 5, 17, 22]
[1, 4, 6, 5, 18, 14, 12, 25, 9, 2, 19, 22, 23, 11, 13, 20, 10, 24, 16, 15, 3, 8, 17, 21, 7]

```

- `rotors_cursor.txt`：转子游标设置文件，用于确定转子起始位置。文件内容如下：

```
4
10
16

```

- `plugboard.txt`：插线板配置文件。文件内容如下。通常，恩尼格玛存在比如10对插线。

```
A-C
D-Z
E-Y
F-W
G-R
H-Q
I-P
J-O
K-N
L-M

```

查看命令行程序的帮助的方式如下：

```
python Enigma.py -h
```

加密的命令如下：

```
python Enigma.py -i input.txt -o output.txt -n 4 --reflector_from m --passwords_from m --rotors_cursor_from m
```

该命令使用了4个转子，自动更新了反射器、密码本和转子游标的配置文件，并加密`input.txt`的内容，输出到`output.txt`中。如果想使用既有的相关配置文件，可以使用以下命令：

```
python Enigma.py -i input.txt -o output.txt -n 4
```

注意，转子的数量与游标数量以及密码本中的密码条数应该匹配，否则会报错。

加密后的文件内容如下：

```
XWVFHEXSWZVTPSBHCGYOEFIVYBIZRDOTSMWHJETVVBILWHZS
```

解密的命令如下：

```
python Enigma.py -i output.txt -o test.txt -n 4
```

解密后的文件内容如下：

```
DEUTSCHVERTRAUENSOLLTESTETSBEGLEITENIHRESOLDATEN
```

注意，默认情况下，该程序使用3转子版本，并且不需要显式地设置转子数量。
