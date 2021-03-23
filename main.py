# -*- coding: utf-8 -*-

# @File    : main.py
# @Date    : 2021-03-17
# @Author  : yuruhao

from fastapi import FastAPI
import os
# from fastapi.openapi.docs import (
#     get_redoc_html,
#     get_swagger_ui_html,
#     get_swagger_ui_oauth2_redirect_html,
# )
# from fastapi.staticfiles import StaticFiles

from base.index import router as index_router
from base.exchange import router as exchange_router
from base.usercenter import router as usercenter_router

app = FastAPI(title='书籍互换', version='1.0.0',
              description='你是否有很多看过的旧书？你是否想得到没看过的新书？何不在这里进行交换？')
#
# app = FastAPI(docs_url=None, redoc_url=None, title='书籍互换', version='1.0.0',
#               description='你是否有很多看过的旧书？你是否想得到没看过的新书？何不在这里进行交换？')

# static_path = os.path.join(os.path.basename(__file__), "../..")
# root = os.path.abspath(static_path)
#
# app.mount("/static", StaticFiles(directory=f"{root}/books/static"), name="static")


# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,
#         title=app.title + " - Swagger UI",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url="/static/js/swagger-ui-bundle.js",
#         swagger_css_url="/static/css/swagger-ui.css",
#     )


app.include_router(usercenter_router)
