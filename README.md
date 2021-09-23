# drum_separation

librosaをラップしてCLI的に手軽に音源分離出来ます。

オーディオファイルを読み込み、ドラムを抽出したオーディオファイルを出力、またはドラムの音を除去したオーディオファイルを出力します。

※完全に除去するものではありません。

## 動作確認環境

### OS
- Ubuntu 20.04（WSL2）
- macOS Big Sur

### Pythonバージョン
- Python 3.8.5

## 使い方

### Ubuntuの場合
```
$ ./setup_ubuntu.sh
$ python3 drum_separation/main.py -i [読み込むファイル] -o [出力ファイル]
```

### Macの場合
```
$ ./setup_mac.sh
$ python3 drum_separation/main.py -i [読み込むファイル] -o [出力ファイル]
```
