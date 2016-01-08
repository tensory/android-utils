#! /usr/bin/env python
# Ari Lacenski 20151218

import sys, os
import shutil
from densities import for_all_densities

def error_no_destination():
	print("Destination directory does not exist.")

def error_usage():
	print("Usage: " + __file__ + " [source_path] [destination_path]")
	print("Example: " + __file__ + " /Users/ari/Downloads/ic_launcher /Users/ari/workspace/android/android-mango/app/res/drawable")

# source_dir should contain drawable- subdirectories with the image at different densities
# drawable-mdpi, drawable-hdpi, drawable-xhdpi, and so on
try: 
	source_dir = sys.argv[1]
except:
	error_usage()
	exit()

try:
	dest_dir = sys.argv[2]
except:
	error_usage()
	exit()

if not dest_dir:
	error_usage()
	exit()

if not os.path.exists(dest_dir):
	error_no_destination()
	exit()

# the unique filename of the asset: 
# ic_launcher.png
asset_filename = os.path.basename(source_dir) + ".png"

def copy_file(density_prefix, source_dir, dest_dir, asset_filename):
	
	# confirm that the file exists at the expected density
	source_asset_path = os.path.join(source_dir, "drawable-" + density_prefix, asset_filename)

	file = open(source_asset_path, "r")
	
	if not file:
		print(source_asset_path + " does not exist. Skipping.")

	else:
		# prune "drawable" off the destination, if provided
		if "drawable" in dest_dir:
			dest_dir = os.path.dirname(dest_dir)

		drawable_dir = "drawable-" + density_prefix
		dest_drawable_dir = os.path.join(dest_dir, drawable_dir)
		if not os.path.exists(dest_drawable_dir):
			os.makedirs(dest_drawable_dir)

		dest_asset_path = os.path.join(dest_dir, drawable_dir, asset_filename) 
		shutil.copyfile(source_asset_path, dest_asset_path)
		
		if not open(dest_asset_path, "r"):
			print("Copying " + source_asset_path + " failed.")
			exit()
		else:
			print(dest_asset_path + " created.")


for_all_densities(copy_file, source_dir=source_dir, dest_dir=dest_dir, asset_filename=asset_filename)
