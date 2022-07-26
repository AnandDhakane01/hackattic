from struct import unpack
import requests
import base64
import json

access_token = ""
base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def get_data():
    return requests.get(f"https://hackattic.com/challenges/help_me_unpack/problem?access_token={access_token}").json()


def main(data):
    bytes = data["bytes"]
    _decode = base64.b64decode(bytes)
    return json.dumps({
        "int": unpack("<i", _decode[:4])[0],
        "uint":  unpack("<I", _decode[4:8])[0],
        "short":  unpack("<h", _decode[8:10])[0],
        "float":  unpack("<f", _decode[12:16])[0],
        "double":  unpack("<d", _decode[16:24])[0],
        "big_endian_double":  unpack(">d", _decode[24:32])[0],
    })


def submit(res):
    response = requests.post(
        f"https://hackattic.com/challenges/help_me_unpack/solve?access_token={access_token}", data=res)
    return response.text


if __name__ == '__main__':
    res = main(get_data())
    print(submit(res))