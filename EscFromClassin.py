from utils.shortcuts import *
from utils.imports import *
from utils.func import *
from utils.menu import *

ALT = False
Z = False
X = False
C = False


def listenKeyboard():  # 键盘监听函数
    def on_press(key):
        global ALT, Z, X, C, start_time, real_fps
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            ALT = True
        if key == keyboard.KeyCode(char="c") or key == keyboard.KeyCode(char="C"):
            C = True

        if ALT and C:
            ALT = C = False
            func2key()

    def on_release(key):
        global ALT, Z, X, C
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            ALT = False
        if key == keyboard.KeyCode(char="c") or key == keyboard.KeyCode(char="C"):
            C = False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


listenerThread = threading.Thread(target=listenKeyboard)
listenerThread.start()


# 防止 Ctrl+C Traceback 并退出
def signal_handler(signal, frame):
    print("\n\n[!] 你按下了Ctrl+C，正在退出程序...")
    time.sleep(1)
    cls()
    print("\n系统仍在监听关闭置顶快捷键。\n如果要停止，请直接关闭此窗口。")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

menu()
