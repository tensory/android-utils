# android-utils

Tiny scripts to help with Android day-to-day development.

### android_xml_converter.py
`android:layout_width="match_parent"` <-> `<item name="android:layout_width">match_parent</item>`

If you paste a block of tags using either of those formats into this script's `input` variable, then run the script, you'll get back the block of the same tags in the other format.
