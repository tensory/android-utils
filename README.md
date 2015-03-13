# android-utils

Tiny scripts to help with Android day-to-day development.

### android_xml_converter.py
Use this script to convert blocks of XML properties. In the `res` directory, XML tags are supposed to be formatted as parameters, like `<item name="android:layout_width">match_parent</item>`. 

Within elements in `layout` files, they look like `android:layout_width="match_parent"`. 

If you paste a block of tags using either of those formats into this script's `input` variable, then run the script, you'll get back the block in the other format.