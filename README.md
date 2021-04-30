#機械学習練習用リポジトリ

## DCGAN

- Deep Convolutional GAN
- https://arxiv.org/abs/1511.06434

## Wasserstein GAN

- Wasserstein GAN
- https://arxiv.org/abs/1701.07875

## 環境構築

1. 環境をまとめた yaml ファイル(EnvName.yaml とする)を作る
2. `conda env create --file EnvName.yaml`を実行すれば仮想環境が出来上がり、コードを走らせることができるはず

## TODO

### 全体

- [ ] スネークケースにする

1. categorizePractice/myDataSets
2. categorizePractice/myDataSets/inputFile
3. categorizePractice/myDataSets/outputFile
4. categorizePractice/src/FaceDetect.py
5. categorizePractice/src/Features.py
6. categorizePractice/src/MakeDataset.py
7. categorizePractice/src/Train.py
8. imageToNpy
9. npyPractice/notebook/DCGAN.ipynb

### DCGAN

- [x] 教師データの入り口を npy にして DCGAN を動かす
- [x] graphvis を使えるようにする
- [x] 初回と二回目以降を if 文で切り分けられる様にする
- [ ] Conv2DTranspose 調べる

### WGAN

- [ ] npy を入り口として動かす

### 動画作るやつ

- [ ] 任意の区間で作れる様にする

## 参考

http://yusuke-ujitoko.hatenablog.com/entry/2017/05/20/145924<br>
https://sinyblog.com/deaplearning/dcgan-001/#i<br>
https://qiita.com/skyfish20ch/items/781407972c84de05af60
