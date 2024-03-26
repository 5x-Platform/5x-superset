from superset.security import SupersetSecurityManager
import logging

class CustomSsoSecurityManager(SupersetSecurityManager):
    def oauth_user_info(self, provider, response=None):
        if provider == 'auth0':
            res = self.appbuilder.sm.oauth_remotes[provider].get('5xdev.us.auth0.com/userinfo')
            me = res.json()
            logging.info(" user_data: %s", me)

            prefix = 'Superset'
            return {
                'username' : me['email'],
                'name' : me['name'],
                'email' : me['email'],
                'first_name': me['email'],
                'last_name': me['name'],
            }
