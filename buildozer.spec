[app]

# (str) Title of your application
title = My Awesome App

# (str) Package name
package.name = myawesomeapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Ensure kivy or any required frameworks are listed here
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# ---------------------------------------------
# Android specific configurations
# ---------------------------------------------

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 26b

# (str) Android NDK directory (leave empty to let buildozer auto-download)
android.ndk_path =

# (str) Android SDK directory (leave empty to let buildozer auto-download)
android.sdk_path =

# (int) Android build-tools version
android.build_tools_ver = 34.0.0

# (bool) Use --private data directory (True) or public /sdcard (False)
android.private_storage = True

# (list) Android application skip architectures
android.skip_architectures = mips,arm64-v8a_legacy

# (str) Format used to package the app for android mode (aab or apk)
android.archs = armeabi-v7a, arm64-v8a

# (bool) Enable AndroidX support (required for modern libraries)
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
