# 凯撒密码加密程序

该程序实现了一个简单的凯撒密码加密功能。用户输入一段文本和偏移量（shift），程序将输出加密后的文本。

代码如下：

```
```

**使用说明**：

可以使用交互式运行或者编译运行，下面给出示例。

- 使用`ghci`进行交互式运行。

```
ghci Main.hs
GHCi, version 9.2.8: https://www.haskell.org/ghc/  :? for help
[1 of 1] Compiling Main             ( Main.hs, interpreted )
Ok, one module loaded.
ghci> encryptText alphabet "LOVE" 3
"ORYH"
```

- 使用cabal编译和运行。

```
cabal build
cabal run
```

运行效果如下：

```
Up to date
Input text:
ILOVEYOU
Input shift:
3
Encrypted text:
LORYHBRX
```

**功能**：

- `cleanText`：清理文本，只保留大写字母。
- `encryptText`：根据输入的偏移量加密文本。
- `main`：程序入口，处理用户输入和输出。

**依赖**：

- `Data.Char`：字符处理。
- `Data.List`：列表处理。
- `Data.Maybe`：处理可能的空值。
