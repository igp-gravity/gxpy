#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxapi as gxapi
import geosoft.gxpy.om as gxom


###############################################################################################

def test_get_user_input():

    gxom.pause('Testing pause')
    gxom.pause('Testing pause\nSome descriptive mumbo-gumbo.........')
    gxom.pause('Testing pause with cancel',cancel='Cancel')

    ret = gxom.get_user_input('Testing string input','String',default='test')
    if ret != 'test':
        gxom.pause('You should gave entered \'test\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    if ret != 1.5:
        gxom.pause('You should gave entered \'1.5\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing int', 'Int', kind='int', default=7)
    if ret != 7:
        gxom.pause('You should gave entered \'7\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    if ret != 'maki':
        gxom.pause('You should gave entered \'maki\', but you entered \'{}\''.format(ret))

def test_state():

    state = gxom.state()
    print(json.dumps(state, indent=4))

def test_menus():
    env = gxom.menus()
    print(json.dumps(env, indent=4))

def rungx():

    #test_get_user_input()
    test_state()
    test_menus()
    input("Press enter to exit...")