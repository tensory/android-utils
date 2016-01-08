#! /usr/bin/env python
# Ari Lacenski 20151218

import sys, os
import shutil
from string import rstrip
from densities import for_all_densities

def error_no_rename():
	print("No new filename was provided.")

def error_usage():
	print("Usage: " + __file__ + " [source_path] [new_name]")
	print("Example: " + __file__ + " /Users/ari/Downloads/ic_launcher/ launcher_icon")

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
asset_filename = os.path.basename(source_dir.rstrip(os.sep)) if source_dir.endswith(os.sep) else os.path.basename(source_dir)
asset_filename = asset_filename + ".png"

def move_file(density_prefix, source_dir, asset_filename, new_name):

	# confirm that the file exists at the expected density
	if not os.path.exists(source_dir):
		print(source_dir + " does not exist.")

	drawable_dir = "drawable-" + density_prefix
	source_asset_path = os.path.join(source_dir, drawable_dir, asset_filename)
	new_asset_path = os.path.join(source_dir, drawable_dir, new_name + ".png")

	file = open(source_asset_path, "r")
	
	if not file:
		print(source_asset_path + " does not exist. Skipping.")

	else:
		# copy the old path to the new path
		shutil.copy(source_asset_path, new_asset_path)

		if not open(new_asset_path, "r"):
			print("Moving " + source_asset_path + " failed.")
			exit()
		else:
			# clean up the old file
			os.remove(source_asset_path)
			print(new_asset_path + " created.")
		
	
# prune trailing slashes to prepare dirname
source_dir = source_dir.rstrip(os.sep)

# os.path.abspath(os.path.join(source_dir, os.path.pardir)) if source_dir.endswith(os.sep) else 
parent_name = os.path.dirname(source_dir)
new_asset_dir = os.path.join(parent_name, new_name)
shutil.copytree(source_dir, new_asset_dir)

for_all_densities(move_file, source_dir=new_asset_dir, asset_filename=asset_filename, new_name=new_name)

if not os.path.exists(new_asset_dir):
	print("Could not rename directory to %s." % new_name)
else:
	shutil.rmtree(source_dir)
	print("Done renaming %s to %s." % (os.path.basename(source_dir), new_name))
