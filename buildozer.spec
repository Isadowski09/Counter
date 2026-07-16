[app]
title = USB HID Controller
package.name = usbhidcontroller
package.domain = org.hidlink
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

# Granting core Android storage capabilities
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
