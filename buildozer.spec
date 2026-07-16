[app]
title = USB HID Controller
package.name = usbhidcontroller
package.domain = org.hidlink
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

# Target portrait mode for mobile screens
orientation = portrait
fullscreen = 1

# Standard modern Android compilation architectures
android.archs = arm64-v8a, armeabi-v7a

# Essential security and storage clearance
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Forces the compiler to allow root-level execution parameters
android.manifest.attributes = android:sharedUserId="android.uid.system"

[buildozer]
log_level = 2
warn_on_root = 0
