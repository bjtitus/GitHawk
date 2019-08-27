import lldb

# Import: command script import /Users/bjtitus/Source/GitHawk/commands.py

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f commands.username GH-Username')
    debugger.HandleCommand('command script add -f commands.clearCookies GH-ClearCookies')
    debugger.HandleCommand('command script add -f commands.clearCache GH-ClearCache')
    debugger.HandleCommand('command script add -f commands.changeBadge GH-ChangeBadge ')

def username(debugger, command, result, internal_dict):
    debugger.HandleCommand("e -l swift -- import UIKit; import Freetime;") 
    debugger.HandleCommand("e -l swift -- (UIApplication.shared.delegate as! AppDelegate).appController.appClient!.userSession!.username")

def clearCookies(debugger, command, result, internal_dict):
    debugger.HandleCommand("e -l swift -- import UIKit; import Freetime;") 
    debugger.HandleCommand("e -l swift -- ((UIApplication.shared.delegate as! AppDelegate).appController.appClient!.client.apollo.networkTransport as! HTTPNetworkTransport).session.configuration.httpCookieStorage.cookies?.forEach(HTTPCookieStorage.shared.deleteCookie)")

def clearCache(debugger, command, result, internal_dict):
    debugger.HandleCommand("e -l swift -- import UIKit; import Freetime; import FlatCache;") 
    debugger.HandleCommand("e -l swift -- ((UIApplication.shared.delegate as! AppDelegate).appController.appClient!.cache as! FlatCache).clear()")

def changeBadge(debugger, command, result, internal_dict):
    debugger.HandleCommand("e -l swift -- import UIKit; import Freetime; import FlatCache;") 
    debugger.HandleCommand("e -l swift -- BadgeNotifications.isBadgeEnabled = true")
    debugger.HandleCommand("e -l swift -- BadgeNotifications.updateBadge(count: 2)")
