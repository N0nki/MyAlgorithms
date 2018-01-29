# coding: utf-8

"""
Base64
"""

from __future__ import print_function

class Base64:
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

    @classmethod
    def encode(cls, input):
        """
        バイナリデータをBase64でエンコードされた1行のASCII文字列に変換する
        """
        i = 0
        output = ''
        while i < len(input):
            input_buf = [0, 0, 0]
            output_buf = [0, 0, 0, 0]
            j = 0
            while j < 3 and i+j < len(input):
                input_buf[j] = ord(input[i+j])
                j += 1

            output_buf[0] = (input_buf[0] & 0xfc) >> 2
            output_buf[1] = ((input_buf[0] & 0x03) << 4) | ((input_buf[1]) >> 4)
            output_buf[2] = ((input_buf[1] & 0x0f) << 2) | ((input_buf[2]) >> 6)
            output_buf[3] = input_buf[2] & 0x3f
            for k in range(j, 3):
                output_buf[k+1] = 64
            for l in output_buf:
                output += cls.CHARS[l]
            i += 3
        return output

    @classmethod
    def decode(cls, input):
        """
        1行のASCII文字列をバイナリデータに変換する
        """
        i = 0
        output = ""
        while i < len(input):
            input_buf = [0, 0, 0, 0]
            output_buf = [0, 0, 0]
            j = 0
            while j < 4 and i+j < len(input):
                input_buf[j] = cls.CHARS.index(input[i+j])
                j += 1

            output_buf[0] = (input_buf[0] << 2) | ((input_buf[1] & 0x30) >> 4)
            output_buf[1] = ((input_buf[1] & 0x0f) << 4) | ((input_buf[2] & 0x3c) >> 2)
            output_buf[2] = ((input_buf[2] & 0x03) << 6) | input_buf[3]

            for k in output_buf:
                if k == 64:
                    break
                output += chr(k)
            i += 4
        return output

def write_binary(binary, filename):
    """
    バイナリデータをファイルに書き込む
    """
    with open(filename, "wb") as f:
        f.write(binary)


if __name__ == "__main__":

    img_binary = open("mygithubicon.png", "rb").read()
    enc = Base64.encode(img_binary)
    dec = Base64.decode(enc)

    write_binary(img_binary, "decoded.png")

    # print("input: {}".format(img_binary))
    print("encode: {}".format(enc))
    print("decode: {}".format(dec))
