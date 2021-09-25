"""画像処理モジュール"""
import cv2
import numpy as np

class WaterDown():
    """画像処理クラス"""

    @classmethod
    def process(cls, target_image_list: list, is_black: bool, is_rotate: bool, square_size: int) -> list:
        """水増しを行う関数

            Args:
                target_image_list (list): 処理対象の画像のリスト
            
            Return:
                result_image_list (list): 処理後の画像のリスト
        """
        # 処理後の画像のリスト
        result_image_list = []
        # 処理
        for target_image in target_image_list:
            #塗り潰し
            if is_black:
                filled_image = cls._fill(target_image, [0, 0, 0])
            else:
                filled_image = cls._fill(target_image, [255, 255, 255])
            #サイズ変更
            resize_image = cls._resize(filled_image, square_size)
            # 回転
            rotate_image_list = cls._rotate(resize_image, is_rotate)
            # リストの生成
            for rotate_image in rotate_image_list:
                result_image_list.append(rotate_image)

        return result_image_list

    @staticmethod
    def _fill(target_image: np.ndarray, fill_color: list) -> np.ndarray:
        """アスペクト比が1:1となるよう入力画像を指定した色で塗りつぶした画像を生成する

            Args:
                image (np.ndarray)：入力画像
                fill_color (list): 塗りつぶす

            Return:
                res_image(np.ndarray): アスペクト比になるよう隙間を指定した色で塗りつぶした画像
        """
        #パラメータ設定
        height, width, dim = target_image.shape
        target_len = max((height, width))
        size = (target_len, target_len, dim)
        #空の配列
        base_image = np.zeros(size, dtype=np.uint8)
        #矩形塗りつぶし
        res_image = cv2.rectangle(base_image, (0,0), (target_len, target_len), fill_color, cv2.FILLED)
        #入力画像を上書き
        res_image[:height, :width] = target_image

        return res_image

    @staticmethod
    def _rotate(target_image: np.ndarray, is_rotate: bool) -> list:
        """入力画像を左に0°, 90°, 180°, 270°回転と、0°の画像を左右反転させて同様に回転させた画像を生成する

            Args:
                image (np.ndarray):対象画像
            
            Return:
                image_list (list<np.ndarray>): 回転や反転を行った画像のリスト(画像8枚分)
        """

        if is_rotate:
            #回転
            image_r0 = target_image
            image_r90 = np.rot90(target_image, 1)
            image_r180 = np.rot90(target_image, 2) 
            image_r270 = np.rot90(target_image, 3)
            #反転した物を回転
            image_flip_r0 = np.fliplr(target_image)
            image_flip_r90 = np.rot90(image_flip_r0, 1)
            image_flip_r180 = np.rot90(image_flip_r0, 2)
            image_flip_r270 = np.rot90(image_flip_r0, 3)
            #生成した画像をリスト化
            images_list = [
                image_r0, image_r90, image_r180, image_r270,
                image_flip_r0, image_flip_r90, image_flip_r180, image_flip_r270]
        else:
            #反転のみ
            image_r0 = target_image
            image_flip_r0 = np.fliplr(target_image)
            #生成した画像をリスト化
            images_list = [image_r0, image_flip_r0]

        return images_list

    @staticmethod
    def _resize(target_image: np.ndarray, square_size: int) -> np.ndarray:
        """指定された画像になるようにアスペクト比が1:1の画像を拡大縮小する

            Args:
                image (np.ndarray): 入力画像
                square_size (int): 出力画像の一辺の長さ(px)

            Return:
                res_image (np.ndarray): サイズを合わせた画像
        """
        #サイズ変更
        res_image = cv2.resize(target_image, dsize=(square_size, square_size))

        return res_image