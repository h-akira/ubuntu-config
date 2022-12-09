# Ubuntu用のconfig
[linux-mint用のもの](https://github.com/h-akira/linux-config)がベースとしている．

# 条件・仕様
- Deskmini X300
- Ubuntu
- タイル型ウィンドウマネージャのi3を利用する．
- xkeysnailでキーマップを設定する．
- ターミナルは`xfce4-terminal`を利用することにして，ショートカットの一部も変更する．

## 環境構築
以下は一例．
```
cd ~/.config
git init
git remote add origin git@github.com:h-akira/ubuntu-config.git
git pull origin main
git submodule update --init
```
必要ものをインストールする．  
```
# i3関係
sudo apt install i3
sudo apt install i3blocks
# 背景用に
sudo apt install feh
# CPUの温度を表示するために
sudo apt install lm-sensors
# ドル円の相場を表示するために
pip3 install pandas-datareade

# 背景
sudo apt install feh

# xfce4
sudo apt install xfce4-terminal
sudo apt install xfce4-screenshooter

# xkeysnail
sudo apt install python-pip python3-pip
sudo pip3 install xkeysnail
```
デフォルトのターミナルを変更する．
```
sudo update-alternatives --config x-terminal-emulator
```
[xkeysnail](https://github.com/h-akira/xkeysnail)をどこかに`git clone`して`src`のパスを通し，
[これらのスクリプト内でsudoをパスワード無しで利用するために，
`sudo visudo`でファイルを開いて以下を追記する．
```
${ユーザーネーム} ALL=(ALL) NOPASSWD: /usr/local/bin/xkeysnail
```
このとき，`visudo`のエディターを変更したければ以下を実行する．
```
sudo update-alternatives --config editor
```



