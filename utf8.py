#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
[Function]
【整理】Python中用encoding声明的文件编码和文件的实际编码之间的关系
http://www.crifan.com/python_string_encoding_declare_encoding_vs_file_real_encoding

[Date]
2013-07-19 

[Author]
Crifan Li

[Contact]
http://www.crifan.com/about/me/
-------------------------------------------------------------------------------
"""


# ---------------------------------import---------------------------------------

# ------------------------------------------------------------------------------
def declare_encoding_vs_real_encoding_declareUtf8RealUtf8():
    """
        Demo Python declare encoding vs. real file encoding
    """
    helpInfo = """在当前Python文件的第一行，用
    # -*- coding: utf-8 -*-
    去声明当前文件编码是utf-8
    所以，当前文件，也必须的确是UTF编码的。
    如此：
    1. Python解析器解析当前文件，才会去按照UTF-8解析
    2. 后面的，当前文件内的，直接写出的中文字符，自然也的确就是UTF-8
    3. 然后在用decode("utf-8")去解码，才能正确，详见后面代码的演示
    """;

    realUtf8Char = "我是UTF-8的中文字符串";
    decodedUnicodeStr = realUtf8Char.decode("utf-8");
    print
    "decodedUnicodeStr=", decodedUnicodeStr;  # 在windows的cmd中，此处Unicode字符串，才能正常输出：decodedUnicodeStr= 我是UTF-8的中文字符串


###############################################################################
if __name__ == "__main__":
    declare_encoding_vs_real_encoding_declareUtf8RealUtf8();