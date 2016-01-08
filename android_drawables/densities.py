#! /usr/bin/env python
# Ari Lacenski 20151218

def for_all_densities(func, **kwargs):
	for density_prefix in ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']:
		func(density_prefix=density_prefix, **kwargs)