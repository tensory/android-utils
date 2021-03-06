# android-utils

Tiny scripts to help with Android day-to-day development.

### android_drawables
Two utilities for working with groups of drawables exported from Zeplin.

#### Usage notes for both tools

Files must be within this directory structure:

```
~/your/download/path/some_random_icon/
    drawable-mdpi/
        some_random_icon.png
    drawable-hdpi/
        some_random_icon.png
    drawable-xhdpi/
        some_random_icon.png
    drawable-xxhdpi/
        some_random_icon.png
      drawable-xxxhdpi/
        some_random_icon.png
```

You don't need to have a subdirectory for every density. Recognized densities are `[mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi]`. If any subdirectories are missing, they will be skipped.

The trailing slash after a source directory name is optional.

#### rename_drawables Usage

`./rename_drawables.py ~/Downloads/some_random_icon/ launch_icon`

Rename all drawables in `some_random_icon/` to the name `launch_icon`.

#### copy_image_to_drawables Usage

`./copy_image_to_drawables.py ~/Downloads/some_random_icon/  ~/path/to/project/android/app/res/drawable/`

Copy all images in the source directory to appropriate target drawable directories in your Android project.
