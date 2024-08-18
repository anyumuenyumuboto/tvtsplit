#!/bin/bash
# https://test.pypi.org/project/tvtsplit/0.0.1/

# pypiへのアップロードツールのtwineをインストール
pip install twine


twine upload --repository testpypi dist/*


# 動作確認
# testpypiの場合は依存パッケージはインストールしてくれないので、先にインストールしておく
pip install polars
pip install --index-url https://test.pypi.org/simple/ tvtsplit==0.0.1

# testpypiからダウンロードするとき、pypiに登録済みのパッケージの場合は以下も使えるかも
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ tvtsplit
