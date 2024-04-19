from flask import redirect, flash, request
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import AuthDBView
from flask_appbuilder.security.views import expose
from flask_login import login_user
from flask_jwt_extended import decode_token
class CustomAuthDBView(AuthDBView):
    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        token = request.args.get('token')
        sm = self.appbuilder.sm
        session = sm.get_session
        if not token:
            return super(CustomAuthDBView,self).login()
        try:
            token = decode_token(token)
            id = token["sub"]
            user = session.query(sm.user_model).filter_by(id=id).first()
            login_user(user, remember=False, force=True)
            return redirect(self.appbuilder.get_url_for_index)
        except:
            flash('Unable to auto login', 'warning')
            return super(CustomAuthDBView,self).login()
class CustomSsoSecurityManager(SupersetSecurityManager):
    authdbview = CustomAuthDBView
    def __init__(self, appbuilder):
        super(CustomSsoSecurityManager, self).__init__(appbuilder)