# Genshin-DTAE Bot
Genshin Daily Task Auto Execute bot
> 刷牙洗脸的时间让Bot帮你处理原神每日需要做的一些烦心事（4个每日任务除外，工作量太大X﹏X）

## Main Goals 主要目标
__桌面启动原神后甩手不管，自动执行以下操作：__
- 1.自动领取尘歌壶银币，好感度 _~~就因为这个，有的人老婆好感度10了还没和她在尘歌壶里说过一句话~~_
- 2.自动领取探索奖励，按需执行探索任务 _疯狂加班的小艾咪)_
- 3.自动按需合成树脂  _浪费可耻，节约为荣)_
- 4.自动设置下一次探索时间提醒到滴答清单 ([下载滴答清单](https://dida365.com)) _(个人使用习惯，不想用可以跳过)_
- 5.提醒区域特色采集物（恢复时间3天），水晶矿（恢复时间2天）是否就绪 _养~~老婆~~不再烦恼_

## Issues 待优化事项
- [ ] [多分辨率适配](https://github.com/kriswang6/Genshin-DTAE/issues/4)
- [ ] [多账号环境测试](https://github.com/kriswang6/Genshin-DTAE/issues/5)
- [x] [添加延时执行模块](https://github.com/kriswang6/Genshin-DTAE/issues/6)（探索还剩几分钟时，可以通过此模块延时后不管）
- [x] ["init_start" 模块中 "touch" 改为 "touch_plus"](https://github.com/kriswang6/Genshin-DTAE/issues/7)
- [ ] [优化尘歌壶定位](https://github.com/kriswang6/Genshin-DTAE/issues/8)（简化寻路过程）
- [ ] [开发自动收取、种植尘歌壶作物模块](https://github.com/kriswang6/Genshin-DTAE/issues/9)
- [ ] [探索未完成时跳过执行](https://github.com/kriswang6/Genshin-DTAE/issues/10)
- [ ] [活动结束时，背包道具到期的弹窗会影响尘歌壶的进入](https://github.com/kriswang6/Genshin-DTAE/issues/11)
- [ ] [克服“必须少女体型角色（影响移动速度）”的限定](https://github.com/kriswang6/Genshin-DTAE/issues/12)（主要影响尘歌壶、探索、合成树脂中走路的过程）
- [ ] [自动传送到每日任务地点？](https://github.com/kriswang6/Genshin-DTAE/issues/13)

## Instructions for Using Custom Functions 自定义函数使用说明
> 基于Airtest API定义

### Encapsalution Execute Module 封装执行模块
| 函数名 | 参数 | 用法 | 执行点 |
| --- | --- | --- | --- |
| __init_start__ | _void_ | 执行“点击开始”前的启动过程 | “开始游戏”后 |
| __cgh__ | _void_ | 执行进入尘歌壶过程 | 任意地点 | 
| __go_dq__ | _void_ | 到稻妻城传送点 | 任意地点 |
| __hc_shuzhi__ | n:合成个数 | 合成树脂 | 合成台旁 |
|__go_to_ksl()__| _void_ | 走到稻妻凯瑟琳旁 | 稻妻传送锚点 |
|__go_to_hc()__| _void_ | 走到合成台旁 | 稻妻凯瑟琳 |
|__explorer()__| hours:探索时间:3, 6, 9, 15(默认使用探索时间 - 20%的角色) | 领取探索奖励、执行探索 | 稻妻凯瑟琳 |
| __dida_ts__ | h:设置小时, m:设置分钟, w:今天周几 | 把探索完成时间设置到滴答清单提醒 | 启动滴答清单的桌面 |

### Wheel 轮子
| 函数名 | 参数 | 用法 |
| --- | --- | --- |
| __write_exp_time__ | (File, hours) | --not used-- |
| __read_exp_time__ | (File) | --not used-- |
| __write_collected_time__ | (File) | --not used-- | 
| __touch_plus__ | (t,x1,y1,x2,y2) | 屏幕范围内点击[t = Template(r"xx.png")] |
| __wait_plus__ | (t,x1,y2,x2,y2) | 屏幕范围内等待[t = Template(r"xx.png")] |
| __cmp_limit_touch__ | (t1,t2,x1,y1,x2,y2) | 范围内A or B点击[t1,t2同上] |
