#!/bin/env python
# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------------------------
# Name:         anag/bilmas.py
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

import awc.layout.gestanag as ga
import anag.bilcon_wdr as wdr

from Env import Azienda
bt = Azienda.BaseTab


import anag.dbtables as dba
adb = dba.adb

import report as rpt

import wx.grid as gl
import awc.controls.dbgrid as dbglib


FRAME_TITLE = "Conti di Bilancio"


class BilConSearchResultsGrid(ga.SearchResultsGrid):
    
    def GetDbColumns(self):
        _NUM = gl.GRID_VALUE_NUMBER
        _STR = gl.GRID_VALUE_STRING
        _DAT = gl.GRID_VALUE_DATETIME
        cn = lambda x: self.db._GetFieldIndex(x)
        tab = self.tabalias
        return (( 35, (cn('bilmas_codice'),  "Cod.",   _STR, True)),
                (240, (cn('bilmas_descriz'), "Mastro", _STR, True)),
                ( 35, (cn('bilcon_codice'),  "Cod.",   _STR, True)),
                (240, (cn('bilcon_descriz'), "Conto",  _STR, True)),
                (  1, (cn('bilmas_id'),      "#mas",   _STR, True )),
                (  1, (cn('bilcon_id'),      "#con",   _STR, True )),
            )
    
    def SetColumn2Fit(self):
        self.SetFitColumn(3)


# ------------------------------------------------------------------------------


class BilConPanel(ga.AnagPanel):
    """
    Gestione tabella Conti di bilancio.
    """
    def __init__(self, *args, **kwargs):
        ga.AnagPanel.__init__( self, *args, **kwargs)
        self.SetDbSetup( Azienda.BaseTab.tabelle[
                         Azienda.BaseTab.TABSETUP_TABLE_BILCON ] )
        self.SetDbOrderColumns((
            #ordinamento bilancio: sezione,cod.mastro,cod.conto,sottoconto
            #sottoconto x descrizione se cli/for, altrimenti codice
            ("Bilancio",    ('IF(bilmas.tipo="P",0,IF(bilmas.tipo="E",1,IF(bilmas.tipo="O",2,3)))', 
                             'bilmas.codice',
                             'bilcon.codice')),
            ("Codice",      ('bilcon.codice',)),
            ("Descrizione", ('bilcon.descriz',)),
        ))
        self._sqlrelcol = ", bilmas.tipo, bilmas.id, bilmas.codice, bilmas.descriz"
        self._sqlrelfrm =\
            " INNER JOIN %s AS bilmas ON %s.id_bilmas=bilmas.id"\
            % ( bt.TABNAME_BILMAS, bt.TABNAME_BILCON )
        self.db_tabprefix = "%s." % bt.TABNAME_BILCON
        
        self._valfilters['biltip'] = ['bilmas.tipo',   'T',  None]
        self._valfilters['bilmas'] = ['bilmas.codice', None, None]
        self._nulfilters['biltip'] = ['T']
        self._hasfilters = True
        
        self.db_report = "Conti di Bilancio"

    def InitAnagCard(self, parent):
        p = wx.Panel( parent, -1)
        wdr.BilConCardFunc( p, True )
        return p
    
    def GetSpecializedSearchPanel(self, parent):
        p = wx.Panel(parent, -1)
        wdr.BilConSpecSearchFunc(p)
        p.FindWindowById(wdr.ID_FILT_PEO).SetDataLink('biltip', 'TPEO')
        return p

    def OnTipBilChanged( self, event ):
        ctr = event.GetEventObject()
        n = ctr.GetSelection()
        if   n == 0: self._tipbil = "P"
        elif n == 1: self._tipbil = "E"
        else:        self._tipbil = "O"
        self.SetDataChanged()
        return self
    
    def GetSearchResultsGrid(self, parent):
        grid = BilConSearchResultsGrid(parent, ga.ID_SEARCHGRID, 
                                       self.db_tabname, self.GetSqlColumns())
        return grid
    
    def GetDbPrint(self):
        return dba.TabConti()


# ------------------------------------------------------------------------------


class BilConFrame(ga._AnagFrame):
    """
    Frame Gestione tabella Conti di bilancio.
    """
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key('title') and len(args) < 3:
            kwargs['title'] = FRAME_TITLE
        ga._AnagFrame.__init__(self, *args, **kwargs)
        self.LoadAnagPanel(BilConPanel(self, -1))


# ------------------------------------------------------------------------------


class BilConDialog(ga._AnagDialog):
    """
    Dialog Gestione tabella Conti di bilancio.
    """
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key('title') and len(args) < 3:
            kwargs['title'] = FRAME_TITLE
        ga._AnagDialog.__init__(self, *args, **kwargs)
        self.LoadAnagPanel(BilConPanel(self, -1))
