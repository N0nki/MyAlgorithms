# coding: utf-8

"""
Base64
"""

from __future__ import print_function

class Base64:
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

    @classmethod
    def encode(cls, input_data):
        """
        バイナリデータをBase64でエンコードされた1行のASCII文字列に変換する
        """
        i = 0
        output_data = ''
        while i < len(input_data):
            input_data_buf = [0, 0, 0]
            output_data_buf = [0, 0, 0, 0]
            j = 0
            while j < 3 and i+j < len(input_data):
                input_data_buf[j] = ord(input_data[i+j])
                j += 1

            output_data_buf[0] = (input_data_buf[0] & 0xfc) >> 2
            output_data_buf[1] = ((input_data_buf[0] & 0x03) << 4) | ((input_data_buf[1]) >> 4)
            output_data_buf[2] = ((input_data_buf[1] & 0x0f) << 2) | ((input_data_buf[2]) >> 6)
            output_data_buf[3] = input_data_buf[2] & 0x3f
            for k in range(j, 3):
                output_data_buf[k+1] = 64
            for l in output_data_buf:
                output_data += cls.CHARS[l]
            i += 3
        return output_data

    @classmethod
    def decode(cls, input_data):
        """
        1行のASCII文字列をバイナリデータに変換する
        """
        i = 0
        output_data = ""
        while i < len(input_data):
            input_data_buf = [0, 0, 0, 0]
            output_data_buf = [0, 0, 0]
            j = 0
            while j < 4 and i+j < len(input_data):
                input_data_buf[j] = cls.CHARS.index(input_data[i+j])
                j += 1

            output_data_buf[0] = (input_data_buf[0] << 2) | ((input_data_buf[1] & 0x30) >> 4)
            output_data_buf[1] = ((input_data_buf[1] & 0x0f) << 4) | ((input_data_buf[2] & 0x3c) >> 2)
            output_data_buf[2] = ((input_data_buf[2] & 0x03) << 6) | input_data_buf[3]

            for k in output_data_buf:
                if k == 64:
                    break
                output_data += chr(k)
            i += 4
        return output_data

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

    # print("input_data: {}".format(img_binary))
    print("encode: {}".format(enc))
    print("decode: {}".format(dec))
