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

import sys, Ice, os
from PySide2 import QtWidgets, QtCore

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except KeyError:
	print '$ROBOCOMP environment variable not set, using the default value /opt/robocomp'
	ROBOCOMP = '/opt/robocomp'

preStr = "-I/opt/robocomp/interfaces/ -I"+ROBOCOMP+"/interfaces/ --all /opt/robocomp/interfaces/"
Ice.loadSlice(preStr+"CommonBehavior.ice")
import RoboCompCommonBehavior

additionalPathStr = ''
icePaths = [ '/opt/robocomp/interfaces' ]
try:
	SLICE_PATH = os.environ['SLICE_PATH'].split(':')
	for p in SLICE_PATH:
		icePaths.append(p)
		additionalPathStr += ' -I' + p + ' '
	icePaths.append('/opt/robocomp/interfaces')
except:
	print 'SLICE_PATH environment variable was not exported. Using only the default paths'
	pass





class GenericWorker(QtCore.QObject):

	kill = QtCore.Signal()
#Signals for State Machine
	inittolambscan = QtCore.Signal()
	lambscantoend = QtCore.Signal()
	lambscantosend_message = QtCore.Signal()
	send_messagetoend = QtCore.Signal()
	start_framestoget_frames = QtCore.Signal()
	start_framestono_camera = QtCore.Signal()
	get_framestoprocessing_and_filter = QtCore.Signal()
	get_framestono_camera = QtCore.Signal()
	get_framestoget_frames = QtCore.Signal()
	processing_and_filtertoget_frames = QtCore.Signal()
	processing_and_filtertosave = QtCore.Signal()
	savetoget_frames = QtCore.Signal()
	savetono_memory = QtCore.Signal()
	no_cameratostart_frames = QtCore.Signal()
	no_cameratoend_ls = QtCore.Signal()
	no_memorytosave = QtCore.Signal()
	no_memorytoend_ls = QtCore.Signal()

#-------------------------

	def __init__(self, mprx):
		super(GenericWorker, self).__init__()



		
		self.mutex = QtCore.QMutex(QtCore.QMutex.Recursive)
		self.Period = 30
		self.timer = QtCore.QTimer(self)

#State Machine
		self.Application= QtCore.QStateMachine()
		self.lambscan_state = QtCore.QState(self.Application)
		self.send_message_state = QtCore.QState(self.Application)
		self.init_state = QtCore.QState(self.Application)

		self.end_state = QtCore.QFinalState(self.Application)



		self.get_frames_state = QtCore.QState(self.lambscan_state)
		self.processing_and_filter_state = QtCore.QState(self.lambscan_state)
		self.save_state = QtCore.QState(self.lambscan_state)
		self.no_camera_state = QtCore.QState(self.lambscan_state)
		self.no_memory_state = QtCore.QState(self.lambscan_state)
		self.start_streams_state = QtCore.QState(self.lambscan_state)

		self.end_ls_state = QtCore.QFinalState(self.lambscan_state)


#------------------
#Initialization State machine
		self.init_state.addTransition(self.inittolambscan, self.lambscan_state)
		self.lambscan_state.addTransition(self.lambscantoend, self.end_state)
		self.lambscan_state.addTransition(self.lambscantosend_message, self.send_message_state)
		self.send_message_state.addTransition(self.send_messagetoend, self.end_state)
		self.start_frames_state.addTransition(self.start_framestoget_frames, self.get_frames_state)
		self.start_frames_state.addTransition(self.start_framestono_camera, self.no_camera_state)
		self.get_frames_state.addTransition(self.get_framestoprocessing_and_filter, self.processing_and_filter_state)
		self.get_frames_state.addTransition(self.get_framestono_camera, self.no_camera_state)
		self.get_frames_state.addTransition(self.get_framestoget_frames, self.get_frames_state)
		self.processing_and_filter_state.addTransition(self.processing_and_filtertoget_frames, self.get_frames_state)
		self.processing_and_filter_state.addTransition(self.processing_and_filtertosave, self.save_state)
		self.save_state.addTransition(self.savetoget_frames, self.get_frames_state)
		self.save_state.addTransition(self.savetono_memory, self.no_memory_state)
		self.no_camera_state.addTransition(self.no_cameratostart_frames, self.start_frames_state)
		self.no_camera_state.addTransition(self.no_cameratoend_ls, self.end_ls_state)
		self.no_memory_state.addTransition(self.no_memorytosave, self.save_state)
		self.no_memory_state.addTransition(self.no_memorytoend_ls, self.end_ls_state)


		self.lambscan_state.entered.connect(self.sm_lambscan)
		self.send_message_state.entered.connect(self.sm_send_message)
		self.init_state.entered.connect(self.sm_init)
		self.end_state.entered.connect(self.sm_end)
		self.start_streams_state.entered.connect(self.sm_start_streams)
		self.end_ls_state.entered.connect(self.sm_end_ls)
		self.get_frames_state.entered.connect(self.sm_get_frames)
		self.processing_and_filter_state.entered.connect(self.sm_processing_and_filter)
		self.save_state.entered.connect(self.sm_save)
		self.no_camera_state.entered.connect(self.sm_no_camera)
		self.no_memory_state.entered.connect(self.sm_no_memory)

		self.Application.setInitialState(self.init_state)
		self.lambscan_state.setInitialState(self.start_streams_state)

#------------------

#Slots funtion State Machine
	@QtCore.Slot()
	def sm_lambscan(self):
		print "Error: lack sm_lambscan in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_send_message(self):
		print "Error: lack sm_send_message in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_init(self):
		print "Error: lack sm_init in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_end(self):
		print "Error: lack sm_end in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_get_frames(self):
		print "Error: lack sm_get_frames in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_processing_and_filter(self):
		print "Error: lack sm_processing_and_filter in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_save(self):
		print "Error: lack sm_save in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_no_camera(self):
		print "Error: lack sm_no_camera in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_no_memory(self):
		print "Error: lack sm_no_memory in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_start_streams(self):
		print "Error: lack sm_start_streams in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_end_ls(self):
		print "Error: lack sm_end_ls in Specificworker"
		sys.exit(-1)


#-------------------------
	@QtCore.Slot()
	def killYourSelf(self):
		rDebug("Killing myself")
		self.kill.emit()

	# \brief Change compute period
	# @param per Period in ms
	@QtCore.Slot(int)
	def setPeriod(self, p):
		print "Period changed", p
		Period = p
		timer.start(Period)
