from flask import redirect, g, flash, request
    from flask_appbuilder.security.views import UserDBModelView, AuthDBView
    from superset.security import SupersetSecurityManager
    from flask_appbuilder.security.views import expose
    from flask_appbuilder.security.manager import BaseSecurityManager
    from flask_login import login_user, logout_user
    from datetime import datetime
    import cx_Oracle

    class SupersetAuth:
        def __init__(self, id, token, username, consumed, creationDate, expirationDate, consumedDate, userId):
            self.id = id
            self.token = token
            self.username = username
            self.consumed = consumed
            self.creationDate = creationDate
            self.expirationDate = expirationDate
            self.consumedDate = consumedDate
            self.userId = userId


    class CustomAuthDBView(AuthDBView):
        login_template = 'appbuilder/general/security/login_db.html'

        @expose('/login/', methods=['GET', 'POST'])
        def login(self):
            authsuccess = True
            if authsuccess:
                login_user(user, remember=False)
                return redirect(redirect_url)
            else:
                flash('Auto Login Failed', 'warning')
                return super().login()


    class CustomSsoSecurityManager(SupersetSecurityManager):
        authdbview = CustomAuthDBView

        def __init__(self, appbuilder):
            super().__init__(appbuilder)