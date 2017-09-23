# -*- coding: utf-8 -*-
from .models import * #初始化model
'''
通过 python manage.py shell
>>>import app.models.*
>>>from werkzeug.security import generate_password_hash
>>>role = Role(
         name="超级管理员",
         auths=""
     )
>>>admin = Admin(
         name="imoocmovie",
         pwd=generate_password_hash("imoocmovie"),
         is_super=0,
         role_id=1
     )
>>>db.session.add(role,admin)
>>>db.session.commit()
'''