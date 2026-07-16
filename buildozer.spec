[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# CAUTION: Add any extra python packages your app needs below (e.g., kivymd, requests)
requirements = python3,kivy

# (str) Supported orientations (valid options are: landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


# =============================================================================
# Android specific variables (AUTOMATION & STABILITY OVERRIDES)
# =============================================================================

# (bool) Automatically accept SDK license agreements in CI/headless environments
android.accept_sdk_license = True

# (num) Android API to use (Target Android 14 / API 34)
android.api = 34

# (num) Minimum API required (Supports Android 5.0 and up)
android.minapi = 21

# (str) Android NDK version to use (Matches python-for-android core recommendations)
android.ndk = 28c

# (str) Android SDK Build Tools version (Locks version to bypass v37 error bugs)
android.sdk_build_tools_version = 34.0.0

# (bool) Use gradle instead of ant
android.gradle_dependencies =

# (str) Format used to package the app for debug
android.debug_artifact = apk

# (str) Format used to package the app for the Google Play Store (apk or aab)
android.release_artifact = apk


# =============================================================================
# Buildozer global configuration
# =============================================================================
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
