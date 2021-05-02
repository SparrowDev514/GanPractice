"""メインウィンドウ"""
import pathlib
import sys

from PySide2 import QtWidgets, QtCore

from io_stream import IOStream, PathLineWidget
from water_down import WaterDown


class MainWindow(QtWidgets.QMainWindow):
    """メインウィンドウ"""

    def __init__(self, parent=None):
        """コンストラクタ"""
        super().__init__(parent)

        # 設定
        self.setWindowTitle('水増し君ver2')
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)

        #　変数
        self.input_folder_path = ''
        self.output_folder_path = ''

        # レイアウト
        main_layout = QtWidgets.QVBoxLayout()
        central_widget = QtWidgets.QWidget()
        inout_layout = QtWidgets.QVBoxLayout()
        setting_layout = QtWidgets.QHBoxLayout()
        bw_button_layout = QtWidgets.QVBoxLayout()
        npy_button_layout = QtWidgets.QVBoxLayout()

        # 入力先フォルダパス取得
        self.input_line = PathLineWidget('入力先フォルダ')
        self.input_line.get_path_signal.connect(self.set_input_path)

        # 出力先フォルダパス取得
        self.output_line = PathLineWidget('出力先フォルダ')
        self.output_line.get_path_signal.connect(self.set_output_path)

        # デフォルトパス入力ボタン
        def_path_btn = QtWidgets.QPushButton('デフォルト')
        def_path_btn.clicked.connect(self.on_def_path_btn)

        #白黒ラジオボタン
        bw_button_b = QtWidgets.QRadioButton('塗りつぶし：白')
        bw_button_w = QtWidgets.QRadioButton('塗りつぶし：黒')

        #白黒ラジオボタングループ
        self.bw_group = QtWidgets.QButtonGroup()
        self.bw_group.addButton(bw_button_b,1)
        self.bw_group.addButton(bw_button_w,0)
        self.bw_group.button(1).setChecked(True)

        #npyラジオボタン
        npy_button_t = QtWidgets.QRadioButton('保存形式:npy')
        npy_button_f = QtWidgets.QRadioButton('保存形式:png')

        #npyラジオボタングループ
        self.npy_group = QtWidgets.QButtonGroup()
        self.npy_group.addButton(npy_button_t, 1)
        self.npy_group.addButton(npy_button_f, 0)
        self.npy_group.button(1).setChecked(True)

        #画像サイズフォームタイトル
        target_size_title = QtWidgets.QLabel('画像のサイズ:')

        #画像サイズフォーム
        self.target_size_form = QtWidgets.QLineEdit()
        self.target_size_form.setText('200')
        self.target_size_form.setFixedWidth(50)

        #開始ボタン
        start_btn = QtWidgets.QPushButton('開始')
        start_btn.clicked.connect(self.on_start_btn)

        #入出力部分レイアウト
        inout_layout.setSpacing(0)
        inout_layout.addStretch()
        inout_layout.addWidget(self.input_line)
        inout_layout.addWidget(self.output_line)
        inout_layout.addStretch()

        #白黒ボタンレイアウト
        bw_button_layout.addStretch()
        bw_button_layout.addWidget(bw_button_b)
        bw_button_layout.addWidget(bw_button_w)
        bw_button_layout.addStretch()

        #npyボタンレイアウト
        npy_button_layout.addStretch()
        npy_button_layout.addWidget(npy_button_t)
        npy_button_layout.addWidget(npy_button_f)
        npy_button_layout.addStretch()

        #設定レイアウト
        setting_layout.addLayout(bw_button_layout)
        setting_layout.addLayout(npy_button_layout)
        setting_layout.addWidget(target_size_title)
        setting_layout.addWidget(self.target_size_form)
        setting_layout.addStretch()
        setting_layout.addWidget(def_path_btn)

        #レイアウト設定
        main_layout.addLayout(inout_layout)
        main_layout.addLayout(setting_layout)
        main_layout.addStretch()
        main_layout.addWidget(start_btn)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_start_btn(self):
        """開始ボタンを押したときの処理
        """
        if(self.input_folder_path != '') and (self.output_folder_path != ''):
            # 入力画像の読み込み
            input_image_list = IOStream.load_image(self.input_folder_path)
            # 水増し処理の実行
            is_black = bool(self.bw_group.checkedId())
            try:
                target_size = int(self.target_size_form.text())
            except ValueError:
                print('画像のサイズは正の整数にしてください')
            result_image_list = WaterDown.process(input_image_list, is_black, target_size)
            # 処理した画像の保存
            is_npy = bool(self.npy_group.checkedId())
            IOStream.save_image(self.output_folder_path, result_image_list, is_npy)

    def on_def_path_btn(self):
        """デフォルトパスボタンを押下した時の処理
        """
        project_path = pathlib.Path(__file__).parent.parent
        self.input_line.set_text(str(project_path.joinpath('input')) + '//')
        self.output_line.set_text(str(project_path.joinpath('output')) + '//')

    def set_input_path(self, input_path):
        """入力先フォルダパスをセットする

            Args:
                input_path(str):入力先フォルダパス
        """
        self.input_folder_path = input_path
    
    def set_output_path(self, output_path):
        """出力先フォルダパスをセットする

            Args:
                output_path(str):出力先フォルダパス
        """
        self.output_folder_path = output_path


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())