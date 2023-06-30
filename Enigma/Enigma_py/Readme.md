一、主要构件：

恩尼格玛机：Enigma.py
密码本：passwords.txt
插线板：plugboard.txt
明文文件：plainText.txt
密文文件：cipherText.txt

二、基本用法

（一）使用说明

默认转子数`3`，默认密码本`passwords.txt`，默认插线板`plugboard.txt`，默认明文文件`plainText.txt`，默认密文文件`cipherText.txt`。

帮助信息如下：

```
python Enigma -h
python Enigma.py
    [-n 3]
    [--password passwords.txt]
    [--plugboard plugboard.txt]
    [-i plainText.txt]
    [-o cipherText.txt]
```

（二）示例用法

比如，初始加密的步骤如下：

1. 准备好一份明文文件`plainText.txt`；
2. 在终端运行代码`python Enigma.py`
3. 代码开始运行后，恩尼格玛机`Enigma.py`会自动生成密码本`passwords.txt`和插线板`plugboard.txt`；
3. 恩尼格玛机还会用上述的密码本和插线板，根据明文生成密文。

默认加密：

```
python Enigma.py
```

选择明文文件进行加密：

```
python Enigma.py -i plainText.txt
```

客制化加密：

```
python Enigma -n 3 --password my_passwords.txt --plugboard my_plugboard.txt -i myText.txt
```

解密：

```
python Enigma -n 3 --password my_passwords.txt --plugboard my_plugboard.txt -i myCipherText.txt -o myPlainText.txt
```

（三）错误提示

自选的密码本所对应的转子数与恩尼格玛实际所用的转子数应该对应。如不对应，就会出现错误运行。目前已修复该缺陷。

```
python Enigma.py -n 4 --password passwords.txt --plugboard plugboard.txt -i cipherText.txt
The numbers of passwords and rotors are not equal.
An exception has occurred, use %tb to see the full traceback.
```
