#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from genericworker import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.Period = 2000
		self.timer.start(self.Period)

		self.Application.start()

	def __del__(self):
		print 'SpecificWorker destructor'

	def setParams(self, params):
		#try:
		#	self.innermodel = InnerModel(params["InnerModelPath"])
		#except:
		#	traceback.print_exc()
		#	print "Error reading config params"
		return True


# =============== Slots methods for State Machine ===================
# ===================================================================
	#
	# sm_init
	#
	@QtCore.Slot()
	def sm_init(self):
		print("Entered state init")
		pass

	#
	# sm_lambscan
	#
	@QtCore.Slot()
	def sm_lambscan(self):
		print("Entered state lambscan")
		pass

	#
	# sm_send_message
	#
	@QtCore.Slot()
	def sm_send_message(self):
		print("Entered state send_message")
		pass

	#
	# sm_end
	#
	@QtCore.Slot()
	def sm_end(self):
		print("Entered state end")
		pass

	#
	# sm_start_streams
	#
	@QtCore.Slot()
	def sm_start_streams(self):
		print("Entered state start_streams")
		pass

	#
	# sm_get_frames
	#
	@QtCore.Slot()
	def sm_get_frames(self):
		print("Entered state get_frames")
		pass

	#
	# sm_no_camera
	#
	@QtCore.Slot()
	def sm_no_camera(self):
		print("Entered state no_camera")
		pass

	#
	# sm_no_memory
	#
	@QtCore.Slot()
	def sm_no_memory(self):
		print("Entered state no_memory")
		pass

	#
	# sm_processing_and_filter
	#
	@QtCore.Slot()
	def sm_processing_and_filter(self):
		print("Entered state processing_and_filter")
		pass

	#
	# sm_save
	#
	@QtCore.Slot()
	def sm_save(self):
		print("Entered state save")
		pass

	#
	# sm_end_ls
	#
	@QtCore.Slot()
	def sm_end_ls(self):
		print("Entered state end_ls")
		pass


# =================================================================
# =================================================================

