"""
@文件        :__init__.py
@说明        :This is an example
@时间        :2025/06/30 09:17:23
@作者        :xxx
@邮箱        :
@版本        :1.0.0
"""

import asyncio

from app.server import app
def register_server():
    params = {
            "port": "",  # 端口号，如果type为socket，则不需要
            "type": "socket",   # 服务类型，socket或者http
            "healthPath": "ping",  # 健康检查方法名
            "healthTimeout": 5,  # 健康检查超时时间
            "metaData": {
                "orgName": "official",  # 组织名
                "appName": "example",   # 应用名
                "version": "1.0.0"    # 应用版本
            }
        }
    rpc_path = os.path.join(Settings.TMP_PATH, "rpc.sock") # ga服务的socket路径
    if os.path.exists(rpc_path):
        req = Request(socket_path=rpc_path, sync=True)
        res = req.send_request("register_server", params) # 注册服务，register_server方法名固定
        if res.to_dict().get("code") == 200:
            print("The registration service was successful.")
        else:
            print("Registration service failed.")

if __name__ == "__main__":
    register_server()
    asyncio.run(app.run())