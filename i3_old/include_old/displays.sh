# モニターの配置を行う
if [ -n "$(xrandr | grep 'DisplayPort-0 connected')" ] && [ -n "$(xrandr | grep 'HDMI-A-0 connected')" ]; then
  xrandr --output DisplayPort-0 --auto --primary --output HDMI-A-0 --auto --left-of DisplayPort-0
fi
