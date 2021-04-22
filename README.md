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

### DCGAN

- [x] 教師データの入り口を npy にして DCGAN を動かす
- [x] graphvis を使えるようにする
- [ ] 初回と二回目以降を if 文で切り分けられる様にする
- [ ] 入力画像サイズを変更できる様にする
- [ ] 水増しくんの吐き出し先を`npyPractice/data/`にする
- [ ] print 文（image shape のやつ）が大量に出るのでどうにかする
- [ ] Conv2DTranspose 調べる

### WGAN

- [ ] npy を入り口として動かす

## 参考

http://yusuke-ujitoko.hatenablog.com/entry/2017/05/20/145924<br>
https://sinyblog.com/deaplearning/dcgan-001/#i<br>
https://qiita.com/skyfish20ch/items/781407972c84de05af60
