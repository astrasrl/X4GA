# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: report.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import awc.controls.windows as aw
from awc.controls.numctrl import NumCtrl

import awc.controls.images as images

from awc.controls.entries import PrintersComboBox

class TitlePanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour('white')
        TitlePanelFunc(self)


class PreviewPanel(wx.Panel):
    def __init__(self, parent, id, pos, size, style):
        wx.Panel.__init__(self, parent, id, pos, size, style)
        self.SetBackgroundColour('white')


class MultiReportStandardBottomPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        MultiReportStandardBottomPanelFunc(self)

class MultiReportLabelsBottomPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        MultiReportLabelsBottomPanelFunc(self)

MultiReportBottomPanel = MultiReportStandardBottomPanel


multicopia = None

class MultiCopiaPanel(wx.Panel):
    
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        s = wx.BoxSizer(wx.VERTICAL)
        for c, e in multicopia:
            v = wx.CheckBox(self, wx.NewId(), c, wx.DefaultPosition, wx.DefaultSize, 0)
            v.SetValue(e)
            s.Add(v, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5)
        self.SetSizer(s)
        s.SetSizeHints(self)
        self.Layout()
    
    def GetCopieSelez(self):
        copie = {}
        for c in self.GetChildren():
            if isinstance(c, wx.CheckBox):
                copie[c.GetLabel()] = c.IsChecked()
        return copie



# Window functions

ID_FOREIGN = 10000
ID_LINE = 10001
ID_TEXT = 10002
ID_REPORTDIRECTURL = 10003
ID_NUMCOPIE = 10004
ID_REPORTS = 10005
ID_PANEL = 10006
ID_PANELPREVIEW = 10007
ID_PANQUESTIONS = 10008
ID_PREVIEW = 10009
ID_PRINT = 10010

def MultiReportFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = TitlePanel(parent, ID_FOREIGN)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Stampa su:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = PrintersComboBox( parent, ID_REPORTDIRECTURL, "", wx.DefaultPosition, [100,-1], [], wx.CB_DROPDOWN|wx.CB_READONLY )
    item5.SetName( "printername" )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Copie:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item7 = NumCtrl(parent, ID_NUMCOPIE, integerWidth=3, allowNegative=False, groupDigits=False); item7.SetName("numcopie")
    item3.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3.AddGrowableCol( 1 )

    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item10 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item11 = wx.StaticText( parent, ID_TEXT, "Seleziona il report:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item11, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT, 5 )

    item12 = wx.ListBox( parent, ID_REPORTS, wx.DefaultPosition, [300,120], [], wx.LB_SINGLE )
    item12.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item12.SetName( "reports" )
    item10.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item13 = MultiReportBottomPanel( parent, ID_PANEL, wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item10.AddGrowableRow( 2 )

    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item14 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item15 = wx.StaticText( parent, ID_TEXT, "Anteprima stile", wx.DefaultPosition, [240,-1], wx.ST_NO_AUTORESIZE )
    item14.Add( item15, 0, wx.ALIGN_BOTTOM|wx.RIGHT, 5 )

    item16 = PreviewPanel( parent, ID_PANELPREVIEW, wx.DefaultPosition, [240,240], wx.SUNKEN_BORDER )
    item16.SetBackgroundColour( wx.WHITE )
    item14.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item9.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9.AddGrowableCol( 1 )

    item9.AddGrowableRow( 1 )

    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item17 = aw.Panel( parent, ID_PANQUESTIONS, wx.DefaultPosition, [-1,20], 0 )
    item17.SetName( "otherquestionspanel" )
    item0.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.BoxSizer( wx.HORIZONTAL )
    
    item19 = wx.Button( parent, ID_PREVIEW, "&Visualizza anteprima", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetName( "btnpreview" )
    item18.Add( item19, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = wx.Button( parent, ID_PRINT, "&Stampa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item20.SetName( "btnprint" )
    item18.Add( item20, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICONWAIT = 10011
ID_REPORTNAME = 10012

def TitlePanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.BoxSizer( wx.HORIZONTAL )
    
    item2 = wx.StaticBitmap(parent, ID_ICONWAIT, images.getPrinter32Bitmap())
    item1.Add( item2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3 = wx.StaticText( parent, ID_REPORTNAME, "Nome standard report", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetFont( wx.Font( 12, wx.DEFAULT, wx.NORMAL, wx.BOLD ) )
    item1.Add( item3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item1, 0, 0, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_NOTE = 10013

def MultiReportStandardBottomPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Note", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.TextCtrl( parent, ID_NOTE, "", wx.DefaultPosition, [200,90], wx.TE_MULTILINE )
    item2.SetForegroundColour( wx.BLACK )
    item2.SetBackgroundColour( wx.LIGHT_GREY )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ROW0 = 10014
ID_COL0 = 10015

def MultiReportLabelsBottomPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Offset di stampa" )
    item1 = wx.StaticBoxSizer( item2, wx.HORIZONTAL )
    
    item3 = wx.BoxSizer( wx.VERTICAL )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Posizione della prima", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "etichetta da stampare", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item5, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item3.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = wx.StaticText( parent, ID_TEXT, "Riga:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item9 = NumCtrl(parent, ID_ROW0, integerWidth=3); item9.SetName('row0')
    item7.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Colonna:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item11 = NumCtrl(parent, ID_COL0, integerWidth=3); item11.SetName('col0')
    item7.Add( item11, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item13 = wx.StaticText( parent, ID_TEXT, "Note", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item14 = wx.TextCtrl( parent, ID_NOTE, "", wx.DefaultPosition, [200,90], wx.TE_MULTILINE )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item12.AddGrowableCol( 0 )

    item12.AddGrowableRow( 1 )

    item0.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_BUTOK = 10016

def MultiCopiaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Selezionare le copie desiderate:", wx.DefaultPosition, [200,-1], 0 )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = MultiCopiaPanel( parent, ID_PANEL, wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetName( "copiepanel" )
    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.Button( parent, ID_BUTOK, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetDefault()
    item5.SetName( "butok" )
    item0.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
