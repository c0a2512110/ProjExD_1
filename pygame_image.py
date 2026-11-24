import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # 練習1 背景画像読み込み
    kk_img = pg.image.load("fig/3.png") # 練習3 こうかとん画像読み込み
    kk_img = pg.transform.flip(kk_img, True, False) # 練習3 左右を反転(flip) 第2引数:左右, 第3引数:上下
    bg_img2 = pg.transform.flip(bg_img, True, False) # 練習8 2枚目の背景画像を反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 # 練習5 背景画像を動かすための変数 # 練習9 背景画像をループ

        screen.blit(bg_img, [-x, 0]) # 練習2 背景画像を描画(blit) 練習5 背景画像を動かす
        screen.blit(bg_img2, [-x+1600, 0]) # 練習7 残像が残らないようにもう1回x=810の時にblit
        screen.blit(bg_img, [-x+3200, 0]) # 練習9 flipped1の右側にoriginal2をblit
        screen.blit(kk_img, [300, 200]) # 練習4 こうかとん描画
        pg.display.update()
        tmr += 1        
        clock.tick(200) # 練習6 FPSを200に変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()