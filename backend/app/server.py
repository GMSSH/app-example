"""
@文件        :__init__.py
@说明        :This is an example
@时间        :2025/06/30 09:17:23
@作者        :xxx
@邮箱        :
@版本        :1.0.0
"""
import os

from simplejrpc.app import ServerApplication
from simplejrpc.response import jsonify
from simplejrpc.i18n import T as i18n

from app.services.example import Example
from app.schemas.example import ExampleForm
from app.middlewares.example import ExampleMiddleware

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "config.yaml")
socket_path = os.path.join(current_path, "app.sock")
i18n_path = os.path.join(current_path, "i18n")
app = ServerApplication(socket_path=socket_path, i18n_path=i18n_path, config_path=config_path)
app.middleware(ExampleMiddleware())


@app.route(name="hello", form=ExampleForm)
async def hello(**kwargs):
    """ """
    example = Example()
    data = await example.hello(kwargs)
    return jsonify(data=data, msg=i18n.translate("STATUS_OK"))

# 状态检查接口
@app.route(name="ping")
async def ping(**kwargs):
    """ """
    return jsonify(data="pong", msg=i18n.translate("STATUS_OK"))
