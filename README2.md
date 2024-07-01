下载checkpoint: [rvm_resnet50](https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_resnet50.pth)

```bash
# python >= 3.10
pip install git+https://github.com/sword4869/RobustVideoMatting.git
```

原本
```
python inference.py \
--variant resnet50 \
--checkpoint D:\git\RobustVideoMatting\model\rvm_resnet50.pth \
--device cuda \
--input-source "input.mp4" \
--output-type video \
--output-composition "composition.mp4" \
--output-alpha "alpha.mp4" \
--output-foreground "foreground.mp4" \
--output-video-mbps 4 \
--seq-chunk 1
```
变成
```
# bash
$ rvm --variant resnet50 \
--checkpoint D:\git\RobustVideoMatting\model\rvm_resnet50.pth \
--device cuda \
--input-source D:\DataSet\Talk\Obama.mp4 \
--output-type video \
--output-composition "composition.mp4" \
--output-alpha "alpha.mp4" \
--output-foreground "foreground.mp4" \
--output-video-mbps 4 \
--seq-chunk 1

# powershell
$ rvm --variant resnet50 `
--checkpoint D:\git\RobustVideoMatting\model\rvm_resnet50.pth `
--device cuda `
--input-source D:\DataSet\Talk\Obama.mp4 `
--output-type video `
--output-composition "composition.mp4" `
--output-alpha "alpha.mp4" `
--output-foreground "foreground.mp4" `
--output-video-mbps 4 `
--seq-chunk 1
```

---

为什么前景出现问题？

![image-20240701212634709](https://cdn.jsdelivr.net/gh/sword4869/pic1@main/images/202407012126742.png)

![image-20240701212616493](https://cdn.jsdelivr.net/gh/sword4869/pic1@main/images/202407012126550.png)

![image-20240701212539823](https://cdn.jsdelivr.net/gh/sword4869/pic1@main/images/202407012125922.png)