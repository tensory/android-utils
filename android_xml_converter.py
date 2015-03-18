#! /usr/bin/env python

import re

def is_property_name(line):
    p = re.compile('[a-zA-Z]+:') # match anything in double quotes
    try:
        return p.search(line).group().strip('":') is not None
    except:
        return False

def get_layout_key(line):
    return line[:line.index('=')]

def get_quoted_value(line):
    p = re.compile('"(.*)"') # match anything in double quotes
    return p.search(line).group().strip('"')

def get_tag_value(line):
    p = re.compile('>(.*)<') # match anything inside a tag
    return p.search(line).group().strip('<>')

input = """
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_gravity="center"
    android:textColor="@color/white"
    android:clickable="true"
    android:hint="@string/txt_addmed_name_hint"
    android:inputType="textNoSuggestions"
    android:textColorHint="@color/white"
    android:textSize="26sp"
    android:paddingBottom="2dp"
"""

## to go the other way, try 
# input = """
# <item name="android:layout_width">match_parent</item>
# """

# you can also supply an input block of styles from styles.xml,
# e.g. <item name="android:layout_width">match_parent</item>

input_lines = input.strip().split('\n')

# clean_input includes all input text, stripped of any whitespace
clean_input = [line.strip() for line in input_lines]
clean_output = []

if is_property_name(clean_input[0]):
    # convert layout XML style to the format expected by styles.xml
    # android:layout_width="match_parent" -> <item name="android:layout_width">match_parent</item>
    for line in clean_input:
        key = get_layout_key(line)
        value = get_quoted_value(line)
        clean_output.append('<item name="%s">%s</item>' % (key, value))
else:
    for line in clean_input:
        key = get_quoted_value(line)
        value = get_tag_value(line)
        clean_output.append('%s="%s"' % (key, value))

for line in clean_output:
    print("\t%s" % line)
