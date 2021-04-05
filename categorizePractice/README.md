# 機械学習による画像分類

## 想定しているフォルダの構成

```
pracCategorize/
     ├myDatasets
     │    ├inputfile
     │    │    ├0
     │    │    ├1
     │    │    └2
     │    └martial
     │         ├0
     │         ├1
     │         └2
     ├src
     │ ├FaceDetect.py
     │ ├Features.py
     │ ├MakeDataset.py
     │ └Train.py
     └README.md
```

## 各フォルダの説明

- inputFile -> 各フォルダにカテゴリごとの画像を入れる
- MakeDataset.py -> martial フォルダ内の画像をまとめて.npz ファイルにする
- Train.py -> 学習を実行する
- Features.py -> test.jpg を判定する
- FaceDetect.py -> は恐らく使わない
