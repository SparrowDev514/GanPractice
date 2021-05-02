"""入出力モジュール"""
import os
import pathlib

import cv2
import numpy as np
from PySide2 import QtWidgets, QtCore


class IOStream():
    """入出力クラス"""

    @staticmethod
    def load_image(input_dir_path: str) -> np.ndarray:
        """画像を読み込む

            Args:
                input_dir_path(str): 入出力フォルダパス
            
            Return:
                input_image_list(list[np.ndarray]): 入力画像のリスト
        """
        #入力画像リスト
        input_image_list = []

        if os.path.exists(input_dir_path) is True: #指定フォルダが存在している場合
            #指定されたフォルダから画像の絶対パスの一覧を取得
            input_paths = list(pathlib.Path(input_dir_path).glob('*.png'))

            #入力画像を読み込みリストを生成
            for input_path in input_paths:
                input_image = cv2.imread(str(input_path))
                input_image_list.append(input_image)

        return input_image_list
    
    @staticmethod
    def save_image(output_dir_path: str, output_image_list: list, is_npy: bool):
        """画像を読み込む

            Args:
                output_dir_path(str): 出力先フォルダパス
                output_image_list (list[np.ndarray]):出力画像のリスト
        """
        if is_npy: # npyで保存
            output_image_array = np.array(output_image_list)
            np.save(output_dir_path + 'result.npy', output_image_array)
        else: # pngで保存
            for index, image in enumerate(output_image_list):
                extension = '.png'
                _, image_buf = cv2.imencode(extension, image)
                with open(output_dir_path + str(index) + '.png', mode='w+b') as i_f:
                    image_buf.tofile(i_f)
                # cv2.imwrite(output_dir_path + str(index) + '.png', image)



class PathLineWidget(QtWidgets.QWidget):
    """フォルダパス取得ウィジェット"""

    # パス入力時シグナル
    get_path_signal = QtCore.Signal(str)

    def __init__(self, dir_title='', parent=None):
        """コンストラクタ"""
        super(PathLineWidget, self).__init__(parent)

        # 全体レイアウト
        layout = QtWidgets.QVBoxLayout()
        dir_layout = QtWidgets.QHBoxLayout()

        # ラベル
        title_label = QtWidgets.QLabel(dir_title)

        # パス指定用ライン
        self.path_line = QtWidgets.QLineEdit()
        self.path_line.setPlaceholderText('パスを入力してください')
        self.path_line.setMinimumWidth(300)
        self.path_line.textChanged.connect(self.get_path_signal) 

        #ディレクトリ選択ボタン
        dir_btn = QtWidgets.QPushButton('選択')
        dir_btn.clicked.connect(self._select_directory)

        #全体レイアウト設定
        dir_layout.addWidget(self.path_line)
        dir_layout.addWidget(dir_btn)

        #全体レイアウト
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addLayout(dir_layout)
        layout.addStretch()
        self.setLayout(layout)

    def _select_directory(self):
        """ディレクトリ選択ダイアログを表示する"""
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Directory', '../' + os.path.dirname(os.path.abspath(__file__)))
        if dir_name != "":
            self.path_line.setText(dir_name + '/')

    def set_text(self, text: str):
        """テキストを入力する

            Args:
                text(str):入力する文字
        """
        self.path_line.setText(text)  