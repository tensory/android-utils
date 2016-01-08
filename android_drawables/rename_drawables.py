#! /usr/bin/env python
# Ari Lacenski 20151218

import sys, os
from densities import for_all_densities

def error_no_rename():
	print("No new filename was provided.")

def error_usage():
	print("Usage: " + __file__ + " [source_path] [new_name]")
	print("Example: " + __file__ + " /Users/ari/Downloads/ic_launcher launcher_icon")

# source_dir should contain drawable- subdirectories with the image at different densities
# drawable-mdpi, drawable-hdpi, drawable-xhdpi, and so on
try: 
	source_dir = sys.argv[1]
except:
	error_usage()
	exit()

# new_name should be the renamed asset name
# do not include a file extension
try:
	new_name = sys.argv[2]
except:
	error_usage()
	exit()

if not new_name:
	error_no_rename()
	exit()

# the unique filename of the asset: 
# ic_launcher.png
asset_filename = os.path.basename(source_dir) + ".png"

def move_file(density_prefix, source_dir, asset_filename, new_name):
	drawable_dir = "drawable-" + density_prefix

	# confirm that the file exists at the expected density
	source_asset_path = os.path.join(source_dir, drawable_dir, asset_filename)
	new_asset_path = os.path.join(source_dir, drawable_dir, new_name + ".png")

	file = open(source_asset_path, "r")
	
	if not file:
		print(source_asset_path + " does not exist. Skipping.")

	else:
		# move (destructively) the old path to the new path
		os.rename(source_asset_path, new_asset_path)

		if not open(new_asset_path, "r"):
			print("Moving " + source_asset_path + " failed.")
			exit()
		else:
			print(new_asset_path + " created.")


for_all_densities(move_file, source_dir=source_dir, asset_filename=asset_filename, new_name=new_name)
