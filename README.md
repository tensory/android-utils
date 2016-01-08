# android-utils

Tiny scripts to help with Android day-to-day development.

### android_xml_converter.py
`android:layout_width="match_parent"` <-> `<item name="android:layout_width">match_parent</item>`

If you paste a block of tags using either of those formats into this script's `input` variable, then run the script, you'll get back the block of the same tags in the other format.

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

`./copy_image_to_drawables.py ~/Downloads/some_random_icon/ ~/Users/alice/workspace/android/app/res/drawable/`

Copy all images in the source directory to appropriate target drawable directories in your Android project.
