# -*- encoding=utf8 -*-
__author__ = "@旅行者_五年高考"
'''
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
'''
from airtest.core.api import *
from airtest.aircv import *
from airtest.report.report import simple_report
import random
import datetime
import time
auto_setup(__file__,devices=["Windows:///"])

# for device 
gen = device()
def write_exp_time(wjm,x):
    t = datetime.datetime.now()
    t = t + datetime.timedelta(hours = x)
    t = datetime.datetime.strftime(t,'%Y-%m-%d %H:%M:%S')
    lj = "C:\\Users\\admin\\Desktop\\new file\\test_ys.air\\"
    xt = open(lj + wjm + '.ini','w+')
    xt.write(t)
    xt.close()
    
def read_exp_time(wjm):
    lj = "C:\\Users\\admin\\Desktop\\new file\\test_ys.air\\"
    xt = open(lj + wjm + '.ini','r+')
    t = xt.readline()
    t1 = datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S')
    xt.close()
    return t1

def write_collected_time(wjm):
    
    t = datetime.datetime.now()
    t = t - datetime.timedelta(days = 1)
    t = datetime.datetime.strftime(t,'%Y-%m-%d %H:%M:%S')
    lj = "C:\\Users\\admin\\Desktop\\new file\\test_ys.air\\"
    xt = open(lj + wjm + '.ini','w+')
    xt.write(t)
    xt.close()

def read_collected_time(n,wjm):
    lj = "C:\\Users\\admin\\Desktop\\new file\\test_ys.air\\"
    xt = open(lj + wjm + '.ini','r+')
    t = xt.readline()
    t1 = datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S')
    t2 = t1 + datetime.timedelta(days = n)
    xt.close()
    return t2

time_NOW = datetime.datetime.now()
def touch_plus(t,x1,y1,x2,y2):
   
    screen = G.DEVICE.snapshot()
    local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))

    # 将我们的目标截图设置为一个Template对象

    # 在局部截图里面查找指定的图片对象
    pos = t.match_in(local_screen)
    while not(pos):
        screen = G.DEVICE.snapshot()
        local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))

        # 将我们的目标截图设置为一个Template对象

        # 在局部截图里面查找指定的图片对象
        pos = t.match_in(local_screen)

    touch((x1 + pos[0],y1 + pos[1]))
def wait_plus(t,x1,y1,x2,y2):

    screen = G.DEVICE.snapshot()
    local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))
    pil_image = cv2_2_pil(local_screen)
    pil_image.save("wait.png", quality=99, optimize=True)
    # 将我们的目标截图设置为一个Template对象

    # 在局部截图里面查找指定的图片对象
    pos = t.match_in(local_screen)
    while not(pos):
        screen = G.DEVICE.snapshot()
        local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))
        pil_image = cv2_2_pil(local_screen)
        pil_image.save("wait.png", quality=99, optimize=True)
        # 将我们的目标截图设置为一个Template对象

        # 在局部截图里面查找指定的图片对象
        pos = t.match_in(local_screen)
    return
def cmp_limit_touch(t1,t2,x1,y1,x2,y2):
    
    screen = G.DEVICE.snapshot()
    local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))

    # 将我们的目标截图设置为一个Template对象

    # 在局部截图里面查找指定的图片对象
    pos1 = t1.match_in(local_screen)
    pos2 = t2.match_in(local_screen)
    
    while(1):
        screen = G.DEVICE.snapshot()
        local_screen = aircv.crop_image(screen,(x1,y1,x2,y2))

        # 将我们的目标截图设置为一个Template对象

        # 在局部截图里面查找指定的图片对象
        pos1 = t1.match_in(local_screen)
        pos2 = t2.match_in(local_screen)
        if(pos1):
            touch((x1 + pos1[0],y1 + pos1[1]))
            return
        elif(pos2):
            touch((x1 + pos2[0],y1 + pos2[1]))
            return
#---------配置区↓↓↓

skip_cgh = 0


skip_ts = 0
time = 0

skip_sz = 0
sz = 0

skip_sleep = 0
sleep_time = 0

skip_close = 0
flag_sz = 0
flag_yueka = 0
skip_init = 0
#---------配置区↑↑↑

print("\t\t\t原神每日自动化即将启动……")
skip_init = int(input("\t\t\t是否跳过“初始化”"))
skip_cgh = int(input("\t\t\t是否跳过“去尘歌壶”"))

skip_ts = int(input("\t\t\t是否跳过“探索”"))
time = 0
if(skip_ts == 0):
    time = int(input("\t\t\t时间？(h)"))

skip_sz = int(input("\t\t\t是否跳过“合成树脂”"))
sz = 0
if(skip_sz == 0):
    sz = int(input("\t\t\t个数？"))

#延时Select模块
skip_sleep = int(input("\t\t\t是否跳过“延时执行”"))
sleep_time = 0
if(skip_sleep == 0):
    sleep_time = int(input("\t\t\t时间？(s)"))

skip_close =int(input("\t\t\t是否跳过“关闭游戏”"))

print("\t\t\t配置完成！冲")
zw = 0
zw = input("\t\t\t按回车键开始")

#延时Execute模块
if(skip_sleep == 0):
    print("\t\t\tETA:")
    count = sleep_time / 10
    while count > 0:
        print("\t\t\t" + str(int(count * 10)))
        sleep(10)
        count = count - 1
print("\t\t\tStart!")

def init_start():
    touch_plus(Template(r"tpl1661268961479.png"),0,850,1400,900)
    #connect_device("Windows:///?title_re=原神")

    touch_plus(Template(r"dianjijinru.png"),730,828,895,862)
    
    while(1):
        if(exists(Template(r"yueka.png"))):
            touch((288,388))
            touch(Template(r"yueka_2.png"))
            return 1
            break
        if(exists(Template(r"paimeng.png"))):
            return 0
            break
    

def cgh():
    sleep(2)
    #1 find position
    gen.key_press('m')
    sleep(0.2)
    gen.key_release('m')
    sleep(2.5)
    touch(Template(r"bb5.png", threshold=0.85))
    touch(Template(r"cgh_name.png", threshold=0.9000000000000001))
    touch(Template(r"cgh_icon.png", threshold=0.8))
    sleep(1)
    cmp_limit_touch(Template(r"dq_dq.png", threshold=0.6999999999999999),Template(r"dq.png", threshold=0.6999999999999998),1205,200,1320,380)
    '''
    已淘汰，改用CMP_LIMIT_TOUCH函数解决“双图检测+点击”问题
    if(exists(Template(r"dq_dq.png", threshold=0.9000000000000001))):
        touch(Template(r"dq_dq.png", threshold=0.9000000000000001))
    elif(exists(Template(r"dq.png", threshold=0.8500000000000001))):
        touch(Template(r"dq.png", threshold=0.8500000000000001))
    '''
    sleep(1)
    touch((800,450))
    touch(Template(r"csmd.png", threshold=0.8))
    touch(Template(r"cs.png", threshold=0.8))
    
    #2 enter hu
    sleep(2)
    wait_plus(Template(r"paimeng.png"),0,0,150,150)
    sleep(1.5)
    gen.key_press('b')
    sleep(0.2)
    gen.key_release('b')
    sleep(1.5)
    screen = G.DEVICE.snapshot()
    local_screen = aircv.crop_image(screen,(835,0,918,80))

    # 将我们的目标截图设置为一个Template对象
    tempalte1 = Template(r"xdj_jh.png", threshold=0.8500000000000001)
    template2 = Template(r"xdj.png", threshold=0.8500000000000001)
    # 在局部截图里面查找指定的图片对象
    pos_1 = tempalte1.match_in(local_screen)
    pos_2 = template2.match_in(local_screen)
    if(pos_1):
        print("jh")
        touch(Template(r"fz.png", threshold=0.83))
    if(pos_2):
        print("wjh")
        touch((835 + pos_2[0],pos_2[1]))
        touch(Template(r"fz.png", threshold=0.83))
    sleep(1)
    gen.key_press('f')
    sleep(0.2)
    gen.key_release('f')
    
    #3 receive gift
    wait_plus(Template(r"wifes.png"),0,0,260,220)
    sleep(2)
    gen.key_press('d')
    sleep(0.2)
    gen.key_release('d')
    sleep(0.1)
    gen.key_press('f')
    sleep(0.2)
    gen.key_release('f')
    sleep(1.3)
    touch((500,600))
    touch(Template(r"xrdj.png"))
    sleep(1)
    touch((876,777))
    touch((1508,593))
    gen.key_press('ESCAPE')
    sleep(0.1)
    gen.key_release('ESCAPE')
    
    sleep(2.5)
    touch((1183,673))
    sleep(1)
    touch((700,450))
    sleep(2)
    
def go_dq():
    gen.key_press('m')
    sleep(0.2)
    gen.key_release('m')
    sleep(2.5)
    '''
    已淘汰，改用CMP_LIMIT_TOUCH函数解决“双图检测+点击”问题
    if(exists(Template(r"bb5.png"))):
        touch(Template(r"bb5.png", threshold=0.8))
    else:
        touch(Template(r"cgh_icon.png"))
     '''
    cmp_limit_touch(Template(r"bb5.png"),Template(r"cgh_icon.png"),1433,786,1599,899)
    if(skip_cgh != 0):
        touch(Template(r"cgh_name.png", threshold=0.9000000000000001))
        touch(Template(r"cgh_icon.png", threshold=0.8))
    sleep(1)
    '''
    已淘汰，改用CMP_LIMIT_TOUCH函数解决“双图检测+点击”问题
    if(exists(Template(r"dq_dq.png", threshold=0.9000000000000001))):
        touch(Template(r"dq_dq.png", threshold=0.9000000000000001))
    elif(exists(Template(r"dq.png", threshold=0.8500000000000001))):
        touch(Template(r"dq.png", threshold=0.8500000000000001))
    '''
    cmp_limit_touch(Template(r"dq_dq.png", threshold=0.7499999999999999),Template(r"dq.png", threshold=0.6999999999999998),1205,274,1289,353)
    sleep(1)
    touch((800,450))
    touch(Template(r"csmd.png", threshold=0.8))
    touch(Template(r"cs.png", threshold=0.8))
    wait(Template(r"paimeng.png"),timeout = 50)
    sleep(1)

def hc_shuzhi(n):
    gen.key_press('F')
    sleep(0.1)
    gen.key_release('F')
    sleep(1)
    touch((400,500))
    sleep(1.5)
    if(exists(Template(r"shuzhi.png"))):
        touch((1300,553),times = n-1)
        touch((1452,854))
        touch((1000,663))
        sleep(1.5)

        gen.key_press('ESCAPE')
        sleep(0.1)
        gen.key_release('ESCAPE')
        sleep(0.5)
        gen.key_press('ESCAPE')
        sleep(0.1)
        gen.key_release('ESCAPE')
        return 1
    else:
        sleep(0.5)
        gen.key_press('ESCAPE')
        sleep(0.1)
        gen.key_release('ESCAPE')
        return 0
    
def go_to_ksl():
    gen.key_press('W')
    sleep(9)
    gen.key_release('W')
    
    sleep(0.5)
    gen.key_press('D')
    sleep(1)
    gen.key_release('D')
    
def go_to_hc():
    gen.key_press('A')
    sleep(1.5)
    gen.key_release('A')
    sleep(0.5)

    gen.key_press('W')
    sleep(2.5)
    gen.key_release('W')
    
def explorer(hours):
    #start at ksl
    #hours == [3 6 9 15]
    
    #dian 对话进探索
    gen.key_press('F')
    sleep(0.1)
    gen.key_release('F')

    sleep(1)
    touch((200,200))
    sleep(1)
    touch((1158,486))
    sleep(2)

    #mengde 1
    touch((138,141))
    touch((871,271))

    #ling jiang
    touch((1441,853))
    sleep(random.uniform(0,0.5))
    touch((100,100))
    

    #ren list 1
    if(hours == 15):
        touch((1528,560))
    elif(hours == 9):
        touch((1438,560))
    elif(hours == 6):
        touch((1337,560))
    elif(hours == 3):
        touch((1248,560))
    touch((1441,853))
    touch((422,138))

    #mengde 2
    touch((472,335))

    #ling jiang
    touch((1441,853))
    sleep(random.uniform(0,0.5))
    touch((100,100))

    #ren list 2
    if(hours == 15):
        touch((1528,560))
    elif(hours == 9):
        touch((1438,560))
    elif(hours == 6):
        touch((1337,560))
    elif(hours == 3):
        touch((1248,560))
    touch((1441,853))
    touch((422,234))
    
    # liyue 1
    touch((132,196))
    touch((683,470))
    
    #ling jiang
    touch((1441,853))
    sleep(random.uniform(0,0.5))
    touch((100,100))
    
    #ren list 1
    if(hours == 15):
        touch((1528,560))
    elif(hours == 9):
        touch((1438,560))
    elif(hours == 6):
        touch((1337,560))
    elif(hours == 3):
        touch((1248,560))
    touch((1441,853))
    touch((422,138))
    
    # liyue 2
    touch((461,468))
    
    #ling jiang
    touch((1441,853))
    sleep(random.uniform(0,0.5))
    touch((100,100))
    
    #ren list 1
    if(hours == 15):
        touch((1528,560))
    elif(hours == 9):
        touch((1438,560))
    elif(hours == 6):
        touch((1337,560))
    elif(hours == 3):
        touch((1248,560))
    touch((1441,853))
    touch((422,234))
    
     # daoqi 1
    touch((114,252))
    touch((919,238))
    
    #ling jiang
    touch((1441,853))
    sleep(random.uniform(0,0.5))
    touch((100,100))
    
    #ren list 1
    if(hours == 15):
        touch((1528,560))
    elif(hours == 9):
        touch((1438,560))
    elif(hours == 6):
        touch((1337,560))
    elif(hours == 3):
        touch((1248,560))
    touch((1441,853))
    touch((422,138))
    sleep(1)
    # exit
    
    gen.key_press('ESCAPE')
    sleep(0.5)
    gen.key_release('ESCAPE')
    sleep(1)
    wait(Template(r"paimeng.png"),timeout = 30)
    

def dida_ts(h,m,w):
    touch_plus(Template(r"tpl1661487317932.png"),900,861,1580,899)
    sleep(1)
    if not(exists(Template(r"tpl1662600176582.png", record_pos=(-0.31, -0.104), resolution=(1600, 900)))):
        touch(Template(r"tpl1661830579919.png", threshold=0.75, record_pos=(0.035, 0.269), resolution=(1600, 900)))
    sleep(5)
    find = exists(Template(r"tpl1661487731797.png", record_pos=(-0.221, 0.059), resolution=(1600, 900)))
    while not(find):
        find = exists(Template(r"tpl1661487731797.png", record_pos=(-0.221, 0.059), resolution=(1600, 900)))
        if(find):
            break
        
    find_x = find[0]
    find_y = find[1]
    touch((find_x + 250,find_y))
    sleep(3)
    wait(Template(r"qr_qc.png"))
    if(h >= 24):
        tmr = 1
        h = h - 24
    else:
        tmr = 0
    if(h < 10):
        h = '0' + str(h)
    else:
        h = str(h)
    sleep(1)
    keyevent(h + str(m))
    if(tmr == 1):
        if(w != 5):
            #点明天
            find = exists(Template(r"tomorrow.png"))
            while not(find):
                find = exists(Template(r"tomorrow.png"))
                if(find):
                    break
            find_x = find[0]
            find_y = find[1]
            touch((find_x + 34,find_y))
        else:
            find = exists(Template(r"tomorrow.png"))
            while not(find):
                find = exists(Template(r"tomorrow.png"))
                if(find):
                    break
            find_x = find[0]
            find_y = find[1]
            touch((find_x - 205,find_y + 40))
    touch(Template(r"dida_qr.png"))
    
    
if(skip_init == 0):
    flag_yueka = init_start()
sleep(1)
if(skip_cgh == 0):
    cgh()
sleep(1)
go_dq()
go_to_ksl()


if(skip_ts == 0):
    explorer(time)
    time_now = datetime.datetime.now()

if(skip_sz == 0):
    go_to_hc()
    sleep(0.5)
    flag_sz = hc_shuzhi(sz)

if(skip_close == 0):
    sleep(2)
    gen.key_press('LALT')
    gen.key_press('F4')
    sleep(0.1)
    gen.key_release('F4')
    gen.key_release('LALT')




print("\t\t\tGenShin Auto test——V2.0")
print("\t\t\t本次执行项目：")
if(flag_yueka == 1):
    print("\t\t\t~点月卡")
if(skip_cgh == 0):
    print("\t\t\t~尘歌壶领银币，好感度")
if(skip_ts == 0):
    print("\t\t\t~探索： " + str(time) + "h")
    if(time_now.hour + time < 24):
        print("\t\t\t~~~探索完成ETA：" + str(time_now.hour + time) + ":" + str(time_now.minute))
    else:
        print("\t\t\t~~~探索完成ETA：（次日）" + str(time_now.hour + time - 24) + ":" + str(time_now.minute))
if(skip_sz == 0 and flag_sz == 1):
    print("\t\t\t~合成树脂：" + str(sz) + "个")
elif(flag_sz == 0 and skip_sz == 0):
    print("\t\t\t~树脂不够，合成失败！")
if(skip_close == 0):
    print("\t\t\t~关闭原神")

print("\t\t\t【mission compeleted,已生成报告! 】")


#-------------------【48h采集物】
tyl = read_collected_time(2,'xt')

if(time_NOW < tyl):
    yuelian_flag = 0
else:
    yuelian_flag = 1
if(yuelian_flag == 1):
    print("\t\t\t~~【纳西妲】的 莲花 刷新了哦！！")
    '''
    yuelian_colt = input()
    if(yuelian_colt == 'y'):
        write_collected_time('xt')
    '''
else:
    print("\t\t\t~~【纳西妲】的 莲花 还没好")
    tyl = datetime.datetime.strftime(tyl,'%Y-%m-%d %H:%M:%S')
    print("\t\t\t~~~~预计生成时间：" + tyl)
    
#-------------------【72h矿石】水晶
shuijin = read_collected_time(3,'shuijin')

if(time_NOW < shuijin):
    shuijin_flag = 0
else:
    shuijin_flag = 1
if(shuijin_flag == 1):
    print("\t\t\t~~层岩的【水晶矿】刷新了哦！！")
    '''
    shuijin_colt = input()
    if(shuijin_colt == 'y'):
        write_collected_time('shuijin')
    '''
else:
    print("\t\t\t~~层岩的水晶矿还没好")
    shuijin = datetime.datetime.strftime(shuijin,'%Y-%m-%d %H:%M:%S')
    print("\t\t\t~~~~预计生成时间：" + shuijin)
    


if(skip_ts == 0):
    dd = input("\t\t\t~需要在【滴答清单】帮忙设置【探索提醒】日程吗？")
    touch((1599,899))
    dida_ts(time_now.hour + time,time_now.minute,time_now.weekday())
    dd = input("\t\t\t日程提醒已调整，按回车结束~")
else:
    dd = input("\t\t\t未进行探索，无需设置日程提醒，按回车结束~")




m