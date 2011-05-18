# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: gestanag.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import sys

import awc.layout.images as images
import awc.controls.images as awcimg

from awc.controls.textctrl import TextCtrl
from awc.controls.button import FlatBitmapButton as BitmapButton
from awc.controls.button import FlatButton
from awc.controls.radiobox import RadioBox
from awc.controls.linktable import LinkTable
import awc.controls.windows as aw

ID_SEARCHGRID = wx.NewId()

class SearchPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        AnagToolbarSearchFunc(self)

class SSVToggleButton(wx.ToggleButton):

    def __init__(self, *args, **kwargs):
        wx.ToggleButton.__init__(self, *args, **kwargs)
        self.SetValue(True)

class CopyFromRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=('U', 'S'))



# Window functions

ID_TEXT = 12000
ID_SEARCHVAL = 12001
ID_SSV = 12002
ID_SEARCHBTN = 12003
ID_SEARCHORD = 12004
ID_BTNFILTERS = 12005
ID_BTNVALSRC = 12006
ID_BTN_RECNEW = 12007
ID_BTN_COPYFROM = 12008
ID_NUMRECFIRST = 12009
ID_BTN_RECFIRST = 12010
ID_BTN_RECPREVIOUS = 12011
ID_BTN_RECNEXT = 12012
ID_BTN_RECLAST = 12013
ID_NUMRECLAST = 12014
ID_BTN_RECSAVE = 12015
ID_BTN_RECDELETE = 12016
ID_RECORDSTATUS = 12017
ID_BTN_RECUNDO = 12018

def AnagToolbarFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 3, 0, 0, 0 )
    parent.schedaSizer = item0
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    parent.bottoniSizer = item1
    
    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Cerca:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 10 )

    item4 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item4.Add( [ 20, 2 ] , 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item5 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item6 = TextCtrl( parent, ID_SEARCHVAL, "", wx.DefaultPosition, [120,-1], 0 )
    item6.SetToolTip( wx.ToolTip("Digitare il valore da cercare come iniziali\\nSe preceduto da .. cerca per contenuto") )
    item6.SetName( "_searchval" )
    item5.Add( item6, 0, wx.GROW|wx.ALL, 5 )

    item5.AddGrowableCol( 0 )

    item4.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4.AddGrowableCol( 0 )

    item4.AddGrowableRow( 0 )

    item2.Add( item4, 0, wx.GROW|wx.ALIGN_BOTTOM, 5 )

    item7 = SSVToggleButton( parent, ID_SSV, "SSV", wx.DefaultPosition, [40,30], 0 )
    item7.SetToolTip( wx.ToolTip("Se premuto, non visualizza gli elementi con status nascosto") )
    item7.SetName( "_ssv" )
    item2.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item8 = wx.Button( parent, ID_SEARCHBTN, "Cerca", wx.DefaultPosition, [50,-1], 0 )
    item8.SetDefault()
    item8.SetToolTip( wx.ToolTip("Cerca il valore digitato") )
    item2.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item9 = FlatButton( parent, ID_SEARCHORD, "v", wx.DefaultPosition, [20,-1], 0 )
    item9.SetToolTip( wx.ToolTip("Imposta l'ordinamento della ricerca") )
    item2.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item10 = wx.BitmapButton(parent, ID_BTNFILTERS, images.getSearch20Bitmap()); item10.SetToolTipString("Visualizza la maschera dei filtri di ricerca"); item10.SetLabel("&F")
    item2.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item11 = wx.BitmapButton(parent, ID_BTNVALSRC, awcimg.getFilter20Bitmap())
    item2.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 1 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item12 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item12.Add( [ 10, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item13 = wx.BitmapButton(parent, ID_BTN_RECNEW, images.getNew20Bitmap()); item13.SetToolTipString("Predispone l'inserimento di una nuova voce")
    item12.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item14 = FlatButton( parent, ID_BTN_COPYFROM, "v", wx.DefaultPosition, [20,-1], 0 )
    item14.SetToolTip( wx.ToolTip("Consente di inizializzare i dati in inserimento a partire dall'ultimo elemento inserito o da un elemento presente a scelta") )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item12.Add( [ 10, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item15 = wx.StaticText( parent, ID_NUMRECFIRST, "", wx.DefaultPosition, [35,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item12.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = wx.BitmapButton(parent, ID_BTN_RECFIRST, images.getLeftmost20Bitmap()); item16.SetToolTipString("Sposta alla prima voce trovata")
    item12.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item17 = wx.BitmapButton(parent, ID_BTN_RECPREVIOUS, images.getLeft20Bitmap()); item17.SetToolTipString("Sposta alla voce precedente")
    item12.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item18 = wx.BitmapButton(parent, ID_BTN_RECNEXT, images.getRight20Bitmap()); item18.SetToolTipString("Sposta alla voce successiva")
    item12.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item19 = wx.BitmapButton(parent, ID_BTN_RECLAST, images.getRightmost20Bitmap()); item19.SetToolTipString("Sposta all'ultima voce trovata")
    item12.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item20 = wx.StaticText( parent, ID_NUMRECLAST, "", wx.DefaultPosition, [35,-1], wx.ST_NO_AUTORESIZE )
    item12.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12.Add( [ 10, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item21 = wx.BitmapButton(parent, ID_BTN_RECSAVE, images.getSave20Bitmap()); item21.SetToolTipString("Memorizza i cambiamenti apportati")
    item12.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item12.Add( [ 10, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item22 = wx.BitmapButton(parent, ID_BTN_RECDELETE, images.getDelete20Bitmap()); item22.SetToolTipString("Elimina la voce corrente")
    item12.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item23 = wx.StaticText( parent, ID_RECORDSTATUS, "INS", wx.DefaultPosition, [40,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_CENTRE )
    item23.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item12.Add( item23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item24 = wx.BitmapButton(parent, ID_BTN_RECUNDO, images.getUndo20Bitmap()); item24.SetToolTipString("Annulla le modifiche effettuate sulla voce")
    item12.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

    item1.Add( item12, 0, wx.ALIGN_CENTER, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXTCTRL = 12019
ID_TXT_DESCRIZ = 12020
ID_TXT_RAGSOC = 12021

def AnagCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item1 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Codice:", wx.DefaultPosition, [60,-1], 0 )
    item2.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

    item4 = wx.StaticText( parent, ID_TEXT, "ID:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item2.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item5 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item5.SetName( "codice" )
    item2.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

    item6 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item6.SetBackgroundColour( wx.LIGHT_GREY )
    item6.SetName( "ID" )
    item2.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0 )

    item2.AddGrowableCol( 0 )

    item2.AddGrowableCol( 1 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.BoxSizer( wx.VERTICAL )
    
    item8 = wx.StaticText( parent, ID_TXT_DESCRIZ, "Descrizione:", wx.DefaultPosition, [90,-1], 0 )
    item7.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.TextCtrl( parent, ID_TXT_RAGSOC, "", wx.DefaultPosition, [220,26], 0 )
    item9.SetFont( wx.Font( 14, wx.ROMAN, wx.NORMAL, wx.NORMAL ) )
    item9.SetName( "descriz" )
    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( [ 2, 80 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableCol( 1 )

    item0.AddGrowableCol( 2 )

    item0.AddGrowableRow( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_BITMAPCARD = 12022
ID_TITLECARD = 12023

def TitlePanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = wx.StaticBitmap(parent, ID_BITMAPCARD, wx.EmptyBitmap(16,16))
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item2 = wx.StaticText( parent, ID_TITLECARD, "Titolo", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.SetFont( wx.Font( 12, wx.DEFAULT, wx.NORMAL, wx.BOLD ) )
    item2.SetName( "_titlecard" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 10 )

    item0.AddGrowableCol( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def AnagToolbarSearchFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = wx.TextCtrl( parent, ID_SEARCHVAL, "", wx.DefaultPosition, [120,-1], 0 )
    item1.SetName( "TextCtrl" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_SEARCHPANGRID = 12024
ID_BTNPRINT = 12025

def SearchResultsFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.Panel( parent, ID_SEARCHPANGRID, wx.DefaultPosition, [200,160], wx.SUNKEN_BORDER )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.BoxSizer( wx.HORIZONTAL )
    
    item3 = wx.Button( parent, ID_BTNPRINT, "&Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_SEARCHNUM = 12026
ID_ORDERDOWN = 12027
ID_BTNORDER = 12028

def SeachOrderFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = parent.FindWindowById( ID_SEARCHNUM )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2 = wx.CheckBox( parent, ID_ORDERDOWN, "Decrescente", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3 = wx.Button( parent, ID_BTNORDER, "Imposta", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetDefault()
    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_COPYFROM = 12029
ID_LINKTAB1 = 12030
ID_LINKTAB2 = 12031
ID_BUTCOPY = 12032

def CopyFromFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item3 = CopyFromRadioBox( parent, ID_COPYFROM, "Seleziona da dove copiare", wx.DefaultPosition, wx.DefaultSize, 
        ["Copia dall'ultimo elemento inserito","Seleziona elemento da cui copiare"] , 1, wx.RA_SPECIFY_COLS )
    item3.SetName( "copyfrom" )
    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.AddGrowableCol( 0 )

    item2.AddGrowableRow( 0 )

    item1.Add( item2, 0, wx.GROW, 5 )

    item5 = wx.StaticBox( parent, -1, "Copia da..." )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    
    item6 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item7 = wx.StaticText( parent, ID_TEXT, "Ultimo elemento inserito:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item8 = parent.FindWindowById( ID_LINKTAB1 ); item8.Disable()
    item6.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Elemento da copiare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item10 = parent.FindWindowById( ID_LINKTAB2 )
    item6.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item6.AddGrowableCol( 1 )

    item4.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 1 )

    item1.AddGrowableRow( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( [ 700, 2 ] , 0, wx.ALIGN_CENTER, 5 )

    item11 = wx.Button( parent, ID_BUTCOPY, "Copia", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.SetDefault()
    item11.SetName( "butcopy" )
    item0.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
