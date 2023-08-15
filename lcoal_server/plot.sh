#!/bin/bash
set terminal png size 720,1600 lw 2
#建立空白图片,设置字体
#注明标题
set output "2.png"
#设置文件名
set ydata time
set timefmt '%H:%M:%S'
set format y "%H:%M"
# set yrange [:] reverse
set yrange ["23:59":"7:00"] reverse
# set yrange ["7:00":"23:59"] 
set ytics "0:30"
set ytics mirror
set mytics 3
#设置X轴名称
#设置y轴名称
set xrange [-0.1:1.1]
#设置y轴范围
set xtics 0.5
set grid x y my
#设置网格线
plot "/root/temp.log" every 2:1:0:0:1440:0 using 3:2 w lp pt 10 title "test"
#分别取数据表1和7列作为x，y变量绘制曲线
quit
#退出软件
