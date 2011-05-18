#!/bin/env python
# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------------------------
# Name:         anag/statpdc.py
# Author:       Fabio Cassini <fabio.cassini@gmail.com>
# Copyright:    (C) 2011 Astra S.r.l. C.so Cavallotti, 122 18038 Sanremo (IM)
# ------------------------------------------------------------------------------
# This file is part of X4GA
# 
# X4GA is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# X4GA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with X4GA.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

import wx

import MySQLdb

import awc.layout.gestanag as ga
import anag.statpdc_wdr as wdr

import awc.util as util

from Env import Azienda
bt = Azienda.BaseTab


FRAME_TITLE = "Status Piano dei Conti"


class StatPdcPanel(ga.AnagPanel):
    def __init__(self, *args, **kwargs):
        ga.AnagPanel.__init__(self, *args, **kwargs)
        self.SetDbSetup( bt.tabelle[ bt.TABSETUP_TABLE_STATPDC] )
        self.db_report = "Status Piano dei Conti"
    
    def InitAnagCard(self, parent):
        p = wx.Panel( parent, -1)
        wdr.StatPdcCardFunc( p, True )
        return p
    

# ------------------------------------------------------------------------------


class StatPdcFrame(ga._AnagFrame):
    """
    Frame Gestione tabella Status Piano dei Conti.
    """
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key('title') and len(args) < 3:
            kwargs['title'] = FRAME_TITLE
        ga._AnagFrame.__init__(self, *args, **kwargs)
        self.LoadAnagPanel(StatPdcPanel(self, -1))


# ------------------------------------------------------------------------------


class StatPdcDialog(ga._AnagDialog):
    """
    Dialog Gestione tabella Status Piano dei Conti.
    """
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key('title') and len(args) < 3:
            kwargs['title'] = FRAME_TITLE
        ga._AnagDialog.__init__(self, *args, **kwargs)
        self.LoadAnagPanel(StatPdcPanel(self, -1))
