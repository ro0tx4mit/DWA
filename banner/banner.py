
class Banner(object):
    def LoadDarkdumpBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''
     ____    __    _    __    ___ 
    |    \   \ \  / \  / /   /   \
    |  |  |   \ \/ _ \/ /   /  -  \
    |____/     \__/ \__/   /__/ \__\
                                        
        Developed By: RO0TX4MIT
        https://github.com/ro0tx4mit 
            ro0tx4mit.github.io
              Version: 1.0
              '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)