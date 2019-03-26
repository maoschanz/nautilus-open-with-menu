# -*- coding: utf-8 -*-
# "Nautilus Open With Menu" 0.5
# Copyright (C) 2018 Romain F. T.
#
# "Nautilus Open With Menu" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# "Nautilus Open With Menu" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with "Create .desktop file"; if not, see http://www.gnu.org/licenses
# for more information.

import os, gi, gettext, urllib
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, Gtk, GObject, Gio, GLib

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
LOCALE_PATH = os.path.join(BASE_PATH, 'locale')
try:
	import gettext
	gettext.bindtextdomain('open-with-menu', LOCALE_PATH)
	_ = lambda s: gettext.dgettext('open-with-menu', s)
except:
	_ = lambda s: s

class OpenWithMenu(GObject.GObject, Nautilus.MenuProvider):
	"""'Open With…' Menu"""
	def __init__(self):
		pass
	
	def get_file_items(self, window, file_items):
		"""Nautilus invoke this function in its startup > Then, create menu entry"""
		# Checks
		if not self._check_generate_menu(file_items):
			return
		
		# Return menu
		return self._generate_menu(file_items)
	
	def get_background_items(self, window, file_items):
		pass
	
	def _check_generate_menu(self, file_items):
		"""Show the menu?"""
		
		# No items selected
		if not len(file_items):
			return False
		
		return True
	
	def _generate_menu(self, file_items):
		"""Generate menu"""
		top_menuitem = Nautilus.MenuItem(name='OpenWithMenu', label=_("Open With…"), sensitive=True)
		menu = Nautilus.Menu()
		possible_apps = []
		self.uris = []
		
		for item in file_items:
			self.uris.append(item.get_uri())
			item_type = item.get_mime_type()
			if len(possible_apps) == 0:
				possible_apps = Gio.AppInfo.get_all_for_type(item_type)
			else:
				possible_apps_new = Gio.AppInfo.get_all_for_type(item_type)
				possible_apps_common = []
				for app in possible_apps:
					for app2 in possible_apps_new:
						if app.equal(app2):
							possible_apps_common.append(app)
				possible_apps = possible_apps_common
		
		for app in possible_apps:
			menu.append_item(self.add_app_item(app, possible_apps.index(app)))

		top_menuitem.set_submenu(menu)
		return top_menuitem, None
	
	def add_app_item(self, app, index):
		item_label = app.get_name()
		item_name = 'OpenWithMenu' + str(index)
		item = Nautilus.MenuItem(name=item_name, label=item_label, sensitive=True)
		item.connect('activate', self.open_with_app, app)
		return item
	
	def open_with_app(self, menuitem, app):
		print(app)
		if app.supports_uris():
			app.launch_uris(self.uris)




