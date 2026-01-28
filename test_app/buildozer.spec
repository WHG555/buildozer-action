### # # # # # # # # # # # # # # # # # # # # # ###  
# 说明：
# 时间：
# 作者：ROrange
# 版本：  
# - 0.1 -> : 
#    SHA256: 
# 备注：
### # # # # # # # # # # # # # # # # # # # # # ###
[app]

title = kivy模板
package.name = demo
package.domain = org.rorange.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false


[buildozer]
log_level = 2
warn_on_root = 1

