# tinify-image

TinyPNG画像一括圧縮プログラム

## はじめに

TinyPNGの開発アカウントに登録してAPI KEYを取得

https://tinypng.com/developers

## Installation

```
# install  API client
$ pip install tinify
```

## Usage

```shell
api_key='YOUR_API_KEY'
input_dir="INPUT IMAGE DIRECTORY"
output_dir="OUTPUT IMAGE DIRECTORY"
$ python compress.py --input ${input_dir} --output ${output_dir} --key ${api_key}
```
