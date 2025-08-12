import threading
import websocket
import sys
import logging
import os
import time
import urllib.parse

def start_websocket(config_name):

    # 日志配置部分保持不变...
    log_dir = rf".\log"
    config_name = urllib.parse.quote(config_name)
    # 配置日志：通过 handlers 实现文件+控制台输出
    file_handler = logging.FileHandler(os.path.join(log_dir, f"log_{config_name}.log"))
    stream_handler = logging.StreamHandler(sys.stdout)  # 输出到控制台

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[file_handler, stream_handler]
    )
    logging.info("日志配置成功！")

    logging.info("开始启动websocket")
    ws = websocket.WebSocketApp(f"ws://127.0.0.1:22288/ws/{config_name}")
    logging.info("连接成功")
    ws.on_open = lambda ws: ws.send("start")
    logging.info("发送start")

    # 设置超时退出
    def exit_timer():
        logging.info("超时关闭连接...")
        ws.close()
        sys.exit(0)

    timer = threading.Timer(5, exit_timer)  # 30秒后自动关闭
    timer.start()

    ws.run_forever()
    timer.cancel()  # 如果连接正常关闭，取消定时器


if __name__ == "__main__":
    # 保证通过命令行运行时传入参数，例如：python script.py MI

    config_name = sys.argv[1]
    # config_name = "du"
    print(f'[{config_name}]启动...')
    start_websocket(config_name)

