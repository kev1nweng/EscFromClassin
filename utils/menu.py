from utils.shortcuts import *
from utils.imports import *
from utils.func import *

stage = "Pre-Alpha"
version = "0.1.0"



def waitAndMenu():
    wait(2)
    menu()

def menu():
    
    funcChoice = ""
    run("mode con cols=50 lines=30")
    run("title>nul EscFromClassin")
    run("cls")
    time.sleep(0.5)

    if stage == "Release":
        workingStatus = "(Stable)"
    else:
        workingStatus = "(Work in progress)"

    nameStr = "EscFromClassin by kev1nweng"
    print(nameStr)
    print(stage, version, workingStatus)

    time.sleep(0.1)
    print("\n+菜单\n")
    print("1. 立即结束 Classin 主进程")
    print("2. 置顶操作 (可用于解除专注全屏)")
    print("+ 2.1 置顶窗口")
    print("+ 2.2 取消置顶")
    print("3. 对进程注入DLL文件")
    print("4. 立即蓝屏")
    print("0. 退出")
    print("\n114514. ?????")


    while True:
        try:
            funcChoice = float(input("\n请输入你要执行的功能序号：\n>> "))
            break
        except ValueError:
            print("\n[!] 非法输入值。")
            time.sleep(3)
            menu()

    if funcChoice == 0:
        print('\n[!] 正在退出程序...')
        time.sleep(1)
        cls()
        sys.exit(0)

    if funcChoice == 1:
        func1()
        waitAndMenu()

    if funcChoice == 2.1:
        func2_1()
        waitAndMenu()

    if funcChoice == 2.2:
        func2_2()
        waitAndMenu()

    if funcChoice == 3:
        func3()
        waitAndMenu()

    if funcChoice == 4:
        func4()
        waitAndMenu()

    if funcChoice == 114514:
        func114514()
        waitAndMenu()
    
    menu()
