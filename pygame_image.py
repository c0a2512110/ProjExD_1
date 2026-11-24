import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # 練習1:背景画像読み込み
    kk_img = pg.image.load("fig/3.png") # 練習3:こうかとん画像読み込み
    kk_img = pg.transform.flip(kk_img, True, False) # 練習3:左右を反転(flip) 第2引数:左右, 第3引数:上下
    bg_img2 = pg.transform.flip(bg_img, True, False) # 練習8:2枚目の背景画像を反転
    kk_rct = kk_img.get_rect() # 練習10-1:こうかとんRectの取得
    kk_rct.center = 300, 200 # 練習10-2:こうかとん初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() # 練習10-3:全キー状態の取得
        if key_lst[pg.K_UP]: # 練習10-4 押下キーに応じた移動量でmove_ip((横, 縦))する
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((2, 0)) #演習1-2:右矢印キーを押している場合は右に進む
        kk_rct.move_ip((-1, 0)) # 演習1-1:何も押していない場合背景画像と同じ速度で左に流れる

        x = tmr%3200 # 練習5:背景画像を動かすための変数 # 練習9:背景画像をループ

        screen.blit(bg_img, [-x, 0]) # 練習2:背景画像を描画(blit) 練習5:背景画像を動かす
        screen.blit(bg_img2, [-x+1600, 0]) # 練習7:残像が残らないようにもう1回x=810の時にblit
        screen.blit(bg_img, [-x+3200, 0]) # 練習9:flipped1の右側にoriginal2をblit
        screen.blit(kk_img, kk_rct) # 練習4:こうかとん描画 # 練習10-5 Rectを使ってblit
        pg.display.update()
        tmr += 1        
        clock.tick(200) # 練習6:FPSを200に変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()