# Ubuntu用のconfig
[linux-mint用のもの](https://github.com/h-akira/linux-config)をベースとしている．

# 条件・仕様
- Ubuntu 22.04.1 LTS
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
git submodule update --init --recursive
```
必要ものをインストールする．  
```
# i3関係
sudo apt install i3
sudo apt install i3blocks
## 背景用に
sudo apt install feh

# i3blocks関係
## CPUの温度を表示するために
sudo apt install lm-sensors
## ドル円の相場を表示するために
sudo apt install python3-selenium

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
[xkeysnail/bin](https://github.com/h-akira/xkeysnail/bin)の
スクリプト内でsudoをパスワード無しで利用するために，
`sudo visudo`でファイルを開いて以下を追記する．
```
${ユーザーネーム} ALL=(ALL) NOPASSWD: /usr/local/bin/xkeysnail
```
このとき，`visudo`のエディターを変更したければ以下を実行する．
```
sudo update-alternatives --config editor
```
起動時にDropBoxを開始するため，`service/dropbox_start.service`を
```
/etc/systemd/system/
```
に配置した上で`${USER}`をユーザーネームに書き換える．
`vi`や`rsync`を用いる場合は`sudo`が必要．
```
sudo rsync dropbox_start.service /etc/systemd/system/
sudo vi /etc/systemd/system/dropbox_start
```
その後，以下のコマンドを実行する．
```
sudo systemctl enable dropbox_start
sudo systemctl start dropbox_start
```
`dropbox_start.service`を編集した場合は
```
sudo systemctl daemon-reload
sudo systemctl restart dropbox_start
```
動作を確認する場合は
```
sudo systemctl status dropbox_start
```


