# Python：破解恩尼格玛的一个重要环节：用crib（小抄）推测目标字符串

我此前曾实现过某种恩尼格玛加密算法。它的解密也极简单：保持原有的转子、插线板等设置，再直接把密文输入进去，直接就是一个解密过程。这也是恩尼格玛极为迷人的一个地方。

说到解密，凯撒加密和多表加密，其实只要令其移动**反向**即可解开。

但是破解不同于解密。解密是从已知的结果和确定的方式，来得到明文。而对破解而言，其中未知的东西太多了。

像破解恩尼格玛，其中要考虑的参数极多，我现在说实话无法破解，哪怕我能设计它的加解密算法。

不过，我根据已经获知的一些破解思路，设计了一段代码，能够模拟用小抄（crib）来推测哪些字符可能符合特定的明文。

代码如下：

```

```

开头有一些代码，用来生成随机的拉丁字母字符串，作为假设的密文。当然，大家也可用我分享出来的恩尼格玛算法，生成一些密文。

接下来就是确定咱们的小抄的字符串，并用这个小抄来逐个对比密文字符串。

对比的方式是：从密文字符串的开头位置，即索引为0的位置，将小抄中的诸字符一一对比密文中的相同数量的字符，确定诸字符分别是否有重复，一旦有重复，就说明所对照的密文片段绝不是小抄所确定的明文，否则可能是。无论是不是，对照的起始位置都后移一位。对这一密文片段，是就记录下来，不是就不记录。

其中，小抄和密文的长度是重要的参数。注意控制参数`i`的最大值，不能让小抄末端超出密文末端，否则会报错。

大家可以自己运行试试。我的一次运行结果如下：

```
CRIB:wetter
65 ['VLZESF', 'LZESFT', 'FTKMFO', 'TKMFOE', 'MFOENO', 'FOENOH', 'ENOHZT', 'NOHZTS', 'ZTSMQL', 'TSMQLW', 'SMQLWX', 'MQLWXD', 'QLWXDQ', 'LWXDQK', 'XDQKWU', 'DQKWUJ', 'QKWUJL', 'KWUJLT', 'LTAWIF', 'TAWIFQ', 'AWIFQV', 'IFQVGW', 'FQVGWX', 'QVGWXJ', 'GWXJRI', 'JRIEXQ', 'EXQRUO', 'XQRUOC', 'QRUOCS', 'RUOCSO', 'UOCSOE', 'CSOEPH', 'SOEPHG', 'PHGJRC', 'HGJRCH', 'GJRCHG', 'JRCHGH', 'RCHGHL', 'CHGHLC', 'HGHLCI', 'GHLCIC', 'HLCICT', 'LCICTZ', 'CTZLZA', 'ZLZARD', 'LZARDU', 'ZARDUW', 'ARDUWW', 'RDUWWC', 'DUWWCY', 'UWWCYV', 'CYVPOA', 'YVPOAB', 'VPOABQ', 'POABQF', 'OABQFS', 'ABQFSW', 'BQFSWL', 'QFSWLE', 'SWLEIL', 'EILVMH', 'ILVMHJ', 'LVMHJE', 'MHJEPD', 'HJEPDL']
```

