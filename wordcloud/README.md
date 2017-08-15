
使用wordcloud做词云
-----------------------

安装Anaconda
----------
###
请到https://www.continuum.io/downloads下载anaconda套装。下拉网页找到下载位置。根据你的操作系统类型选择合适的版本，选择python3.6。
###
安装过程中一定要选择加入到path

安装wordcloud
----------
###
好了，下面请进入命令行模式。如果是Windows，请打开“开始”-“附件”-“命令提示符”。键入以下命令：
###
    mkdir demo
    cd demo
###
先在命令行下，先执行：
###
    pip install wheel
###
然后，再执行：
###
    pip install wordcloud-1.3.1-cp36-cp36m-win_amd64.whl
###
好了，我们需要的全部Python运行环境终于装好了。请务必按照上述步骤执行，确保每一步都已经顺利完成。否则一旦遗漏，后面运行程序会报错。

运行
---
###
将py和原始文件放到demo目录下，运行以下命令即可得到词云。
###
    python ccs-bigdata-wordcloud.py

