# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: ftdif.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from anag.basetab import AnagCardPanel

from awc.controls.numctrl import NumCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.radiobox import RadioBox
from awc.controls.linktable import LinkTable

from anag.mag import MagazzDialog
from anag.pdc import PdcDialog
from anag.agenti import AgentiDialog
from anag.zone import ZoneDialog
from anag.modpag import ModPagDialog
from anag.catcli import CatCliDialog

from anag.basetab import WorkZoneNotebook

import Env
bt=Env.Azienda.BaseTab

class TipoEmailRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=("T","C","A","S"))



# Window functions

ID_WORKZONE = 15000

def FtdSelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = WorkZoneNotebook( parent, ID_WORKZONE, wx.DefaultPosition, wx.DefaultSize, 0 )
    item1 = item2
    
    item3 = wx.Panel( item2, -1 )
    SelFunc(item3, False)
    item2.AddPage( item3, "Selezioni" )

    item4 = wx.Panel( item2, -1 )
    DocRagFunc(item4, False)
    item2.AddPage( item4, "Documenti estratti" )

    item5 = wx.Panel( item2, -1 )
    DocGenFunc(item5, False)
    item2.AddPage( item5, "Documenti generati" )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_DESDOC = 15001
ID_TEXT = 15002
ID_DATLAST = 15003
ID_NUMLAST = 15004
ID_DATDOC = 15005
ID_NUMDOC = 15006
ID_SEPDEST = 15007
ID_SEPMP = 15008
ID_SEPALL = 15009
ID_DATMIN = 15010
ID_NUMMIN = 15011
ID_DATMAX = 15012
ID_NUMMAX = 15013
ID_DOCS = 15014
ID_CAUTRA = 15015
ID_ESCLACQ = 15016
ID_ESCLANN = 15017
ID_SOLOSTA = 15018
ID_SOLOMAG = 15019
ID_SOLOPDC = 15020
ID_SOLOAGE = 15021
ID_SOLOZONA = 15022
ID_SOLOCATEG = 15023
ID_SOLOMP = 15024
ID_STORY = 15025
ID_BUTEST = 15026

def SelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBox( parent, -1, "Documenti da generare" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.StaticText( parent, ID_DESDOC, "Documento", wx.DefaultPosition, [160,-1], 0 )
    item4.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Data", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Num.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Ultimo documento presente:", wx.DefaultPosition, [215,-1], wx.ALIGN_RIGHT )
    item5.Add( item9, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_DATLAST, "", wx.DefaultPosition, [80,-1], 0 )
    item5.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = NumCtrl(parent, ID_NUMLAST, integerWidth=6, allowNegative=False, groupDigits=False)
    item5.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Primo documento da generare:", wx.DefaultPosition, [215,-1], wx.ALIGN_RIGHT )
    item5.Add( item12, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item13 = DateCtrl( parent, ID_DATDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item5.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = NumCtrl(parent, ID_NUMDOC, integerWidth=6, allowNegative=False, groupDigits=False)
    item5.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

    item16 = wx.StaticBox( parent, -1, "Genera un diverso documento a fronte di:" )
    item15 = wx.StaticBoxSizer( item16, wx.VERTICAL )
    
    item17 = wx.CheckBox( parent, ID_SEPDEST, "Ogni diverso destinatario riscontrato", wx.DefaultPosition, [420,-1], 0 )
    item15.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.CheckBox( parent, ID_SEPMP, "Ogni diversa mod.pagamento riscontrata", wx.DefaultPosition, [280,-1], 0 )
    item15.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = wx.CheckBox( parent, ID_SEPALL, "Ogni documento esaminato", wx.DefaultPosition, [280,-1], 0 )
    item15.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item20 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item22 = wx.StaticBox( parent, -1, "Documenti da raggruppare" )
    item21 = wx.StaticBoxSizer( item22, wx.VERTICAL )
    
    item23 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item24 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item25 = wx.StaticText( parent, ID_TEXT, "Data", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.Add( item25, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item26 = wx.StaticText( parent, ID_TEXT, "Num.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.Add( item26, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item27 = wx.StaticText( parent, ID_TEXT, "Esamina documenti da:", wx.DefaultPosition, [215,-1], wx.ALIGN_RIGHT )
    item23.Add( item27, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item28 = DateCtrl( parent, ID_DATMIN, "", wx.DefaultPosition, [80,-1], 0 )
    item23.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item29 = NumCtrl(parent, ID_NUMMIN, integerWidth=6, allowNegative=False, groupDigits=False); 
    item23.Add( item29, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item30 = wx.StaticText( parent, ID_TEXT, "a:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.Add( item30, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item31 = DateCtrl( parent, ID_DATMAX, "", wx.DefaultPosition, [80,-1], 0 )
    item23.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item32 = NumCtrl(parent, ID_NUMMAX, integerWidth=6, allowNegative=False, groupDigits=False)
    item23.Add( item32, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item33 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item34 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item35 = wx.StaticText( parent, ID_TEXT, "Considera i documenti:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item34.Add( item35, 0, wx.GROW|wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT, 5 )

    item36 = wx.StaticText( parent, ID_TEXT, "Solo con queste causali di trasporto:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item34.Add( item36, 0, wx.ALIGN_BOTTOM|wx.RIGHT, 5 )

    item37 = wx.CheckListBox( parent, ID_DOCS, wx.DefaultPosition, wx.DefaultSize, [], wx.LB_SINGLE )
    item34.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item38 = wx.CheckListBox( parent, ID_CAUTRA, wx.DefaultPosition, wx.DefaultSize, [], wx.LB_SINGLE )
    item34.Add( item38, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item34.AddGrowableCol( 0 )

    item34.AddGrowableCol( 1 )

    item34.AddGrowableRow( 1 )

    item33.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item33.AddGrowableCol( 0 )

    item33.AddGrowableRow( 0 )

    item21.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item39 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item40 = wx.CheckBox( parent, ID_ESCLACQ, "Escludi se acquisiti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item40.SetValue( True )
    item39.Add( item40, 0, wx.GROW|wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item41 = wx.CheckBox( parent, ID_ESCLANN, "Escludi se annullati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item41.SetValue( True )
    item39.Add( item41, 0, wx.GROW|wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item42 = wx.CheckBox( parent, ID_SOLOSTA, "Estrai solo se stampati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item42, 0, wx.GROW|wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item39.AddGrowableCol( 0 )

    item39.AddGrowableCol( 1 )

    item39.AddGrowableCol( 2 )

    item21.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item20.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item43 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item45 = wx.StaticBox( parent, -1, "Selezioni:" )
    item44 = wx.StaticBoxSizer( item45, wx.VERTICAL )
    
    item46 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item47 = wx.StaticText( parent, ID_TEXT, "Solo del magazzino:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item47, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item48 = LinkTable(parent, ID_SOLOMAG ); item48.SetDataLink( bt.TABNAME_MAGAZZ, "magazz", MagazzDialog, canins=False, canedit=False)
    item46.Add( item48, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item49 = wx.StaticText( parent, ID_TEXT, "Solo del cliente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item49, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item50 = LinkTable(parent, ID_SOLOPDC ); item50.SetDataLink( bt.TABNAME_PDC, "pdc", PdcDialog, canins=False, canedit=False)
    item46.Add( item50, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item51 = wx.StaticText( parent, ID_TEXT, "Solo clienti dell'agente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item51, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item52 = LinkTable(parent, ID_SOLOAGE ); item52.SetDataLink( bt.TABNAME_AGENTI, "agente", AgentiDialog, canins=False, canedit=False)
    item46.Add( item52, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item53 = wx.StaticText( parent, ID_TEXT, "Solo clienti della zona:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item53, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item54 = LinkTable(parent, ID_SOLOZONA ); item54.SetDataLink( bt.TABNAME_ZONE, "zona", ZoneDialog, canins=False, canedit=False)
    item46.Add( item54, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item55 = wx.StaticText( parent, ID_TEXT, "Solo clienti della categoria:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item55, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item56 = LinkTable(parent, ID_SOLOCATEG); item56.SetDataLink(bt.TABNAME_CATCLI, "catcli", CatCliDialog, canins=False, canedit=False)
    item46.Add( item56, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item57 = wx.StaticText( parent, ID_TEXT, "Solo con mod.pagamento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item57, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item58 = LinkTable(parent, ID_SOLOMP ); item58.SetDataLink( bt.TABNAME_MODPAG, "modpag", ModPagDialog, canins=False, canedit=False)
    item46.Add( item58, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item46.AddGrowableCol( 1 )

    item44.Add( item46, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item43.Add( item44, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item43.AddGrowableCol( 0 )

    item20.Add( item43, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item20.AddGrowableCol( 1 )

    item0.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item59 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item60 = wx.Button( parent, ID_STORY, "Elaborazioni precedenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item59.Add( item60, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item61 = wx.Button( parent, ID_BUTEST, "Avvia estrazione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item59.Add( item61, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item0.Add( item59, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( [ 20, 160 ] , 0, wx.ALIGN_CENTER, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_DOCINCLNUM = 15027
ID_DOCINCLTOT = 15028
ID_DOCESCLNUM = 15029
ID_DOCESCLTOT = 15030
ID_DOCRAGZONE = 15031
ID_LINE = 15032
ID_LISTRAG = 15033
ID_BUTRAG = 15034

def DocRagFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Documenti da raggruppare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = NumCtrl(parent, ID_DOCINCLNUM, integerWidth=6, allowNegative=False, groupDigits=False); item3.SetEditable(False)
    item1.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "Totale imponibile:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = NumCtrl(parent, ID_DOCINCLTOT, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item5.SetEditable(False)
    item1.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Documenti esclusi da raggruppamento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = NumCtrl(parent, ID_DOCESCLNUM, integerWidth=6, allowNegative=False, groupDigits=False); item7.SetEditable(False)
    item1.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Totale imponibile:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = NumCtrl(parent, ID_DOCESCLTOT, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item9.SetEditable(False)
    item1.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 2 )

    item1.AddGrowableCol( 6 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.SplitterWindow( parent, ID_DOCRAGZONE, wx.DefaultPosition, wx.DefaultSize, wx.SP_BORDER|wx.SP_3D|wx.CLIP_CHILDREN )
    item10.SetMinimumPaneSize( 100 )
    item11 = wx.Panel( item10, -1 )
    DocRagDocFunc( item11, False, True )
    item12 = wx.Panel( item10, -1 )
    DocRagMovFunc( item12, False, True )
    item10.SplitHorizontally( item11, item12 )
    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item14 = wx.BoxSizer( wx.HORIZONTAL )
    
    item15 = wx.Button( parent, ID_LISTRAG, "Lista documenti estratti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item16 = wx.Button( parent, ID_BUTRAG, "Avvia raggruppamento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.Add( item16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PGEDOC = 15035

def DocRagDocFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Documenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.Panel( parent, ID_PGEDOC, wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PGEMOV = 15036

def DocRagMovFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Dettaglio documento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.Panel( parent, ID_PGEMOV, wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_DOCGENNUM = 15037
ID_DOCGENMIN = 15038
ID_DOCGENMAX = 15039
ID_DOCGENZONE = 15040
ID_LISTGEN = 15041
ID_BUTCONF = 15042

def DocGenFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Documenti generati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = NumCtrl(parent, ID_DOCGENNUM, integerWidth=6, allowNegative=False, groupDigits=False); item3.SetEditable(False)
    item1.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "dal num:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = NumCtrl(parent, ID_DOCGENMIN, integerWidth=6, allowNegative=False, groupDigits=False); item5.SetEditable(False)
    item1.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "al num:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item7 = NumCtrl(parent, ID_DOCGENMAX, integerWidth=6, allowNegative=False, groupDigits=False); item7.SetEditable(False)
    item1.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = wx.SplitterWindow( parent, ID_DOCGENZONE, wx.DefaultPosition, wx.DefaultSize, wx.SP_BORDER|wx.SP_3D|wx.CLIP_CHILDREN )
    item8.SetMinimumPaneSize( 100 )
    item9 = wx.Panel( item8, -1 )
    DocGenDocFunc( item9, False, True )
    item10 = wx.Panel( item8, -1 )
    DocGenMovFunc( item10, False, True )
    item8.SplitHorizontally( item9, item10 )
    item0.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.BoxSizer( wx.HORIZONTAL )
    
    item13 = wx.Button( parent, ID_LISTGEN, "Lista documenti generati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.Button( parent, ID_BUTCONF, "Conferma generazione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PGGDOC = 15043

def DocGenDocFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Documenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.Panel( parent, ID_PGGDOC, wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PGGMOV = 15044

def DocGenMovFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Dettaglio documento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.Panel( parent, ID_PGGMOV, wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TIPDOC = 15045
ID_MAGAZZ = 15046
ID_YEAR = 15047
ID_NUMDOC1 = 15048
ID_NUMDOC2 = 15049
ID_TIPEMAIL = 15050
ID_UPDATE = 15051
ID_PANGRID = 15052
ID_EMAIL = 15053
ID_LISTA = 15054
ID_STAMPA = 15055

def StaDifFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBox( parent, -1, "Selezioni" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item5 = wx.StaticText( parent, ID_TEXT, "Tipo documento da stampare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item6 = LinkTable(parent, ID_TIPDOC ); item6.SetDataLink( bt.TABNAME_CFGMAGDOC, "id_tipdoc", None, canins=False, canedit=False)
    item4.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Documenti del magazzino:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item8 = LinkTable(parent, ID_MAGAZZ ); item8.SetDataLink( bt.TABNAME_MAGAZZ, "id_magazz", MagazzDialog, canins=False, canedit=False)
    item4.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Registrati nell'anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item11 = NumCtrl(parent, ID_YEAR, integerWidth=4, allowNegative=False, groupDigits=False)
    item10.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "dal num.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item12, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item13 = NumCtrl(parent, ID_NUMDOC1, integerWidth=5, allowNegative=False, groupDigits=False); item13.SetName('numdoc1')
    item10.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "al num.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item14, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item15 = NumCtrl(parent, ID_NUMDOC2, integerWidth=5, allowNegative=False, groupDigits=False); item15.SetName('numdoc2')
    item10.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item4.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4.AddGrowableCol( 1 )

    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = TipoEmailRadioBox( parent, ID_TIPEMAIL, "Seleziona la stampa dei documenti di:", wx.DefaultPosition, wx.DefaultSize, 
        ["Tutti i clienti","Solo clienti con email da spedire","Solo clienti con email, anche già spedite","Solo clienti senza email"] , 1, wx.RA_SPECIFY_COLS )
    item16.SetName( "tipemail" )
    item1.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item17 = wx.Button( parent, ID_UPDATE, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.RIGHT|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item18 = wx.StaticText( parent, ID_TEXT, "Documenti presenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetForegroundColour( wx.BLUE )
    item0.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item19 = wx.Panel( parent, ID_PANGRID, wx.DefaultPosition, [660,300], wx.SUNKEN_BORDER )
    item0.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item21 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item22 = wx.Button( parent, ID_EMAIL, "Spedisci email", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetName( "butemail" )
    item22.Enable(False)
    item21.Add( item22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item23 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item24 = wx.Button( parent, ID_LISTA, "Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetName( "butlist" )
    item23.Add( item24, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item25 = wx.Button( parent, ID_STAMPA, "Stampa documenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetName( "butprint" )
    item23.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20.Add( item23, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item20.AddGrowableCol( 1 )

    item0.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_STORYDAT1 = 15056
ID_STORYDAT2 = 15057
ID_STORYORDER = 15058
ID_STORYUPD = 15059
ID_STORYPANGRID = 15060

def FtDifHistoryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Periodo da analizzare dal:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item4 = DateCtrl( parent, ID_STORYDAT1, "", wx.DefaultPosition, [80,-1], 0 )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "al:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item6 = DateCtrl( parent, ID_STORYDAT2, "", wx.DefaultPosition, [80,-1], 0 )
    item2.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item2, 0, wx.ALIGN_BOTTOM, 5 )

    item7 = wx.RadioBox( parent, ID_STORYORDER, "Ordina per documento:", wx.DefaultPosition, wx.DefaultSize, 
        ["Raggruppato","Generato"] , 1, wx.RA_SPECIFY_ROWS )
    item1.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.Button( parent, ID_STORYUPD, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetDefault()
    item1.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item10 = wx.StaticText( parent, ID_TEXT, "Documenti estratti e generati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetForegroundColour( wx.BLUE )
    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = wx.Panel( parent, ID_STORYPANGRID, wx.DefaultPosition, [600,400], wx.SUNKEN_BORDER )
    item9.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item9.AddGrowableCol( 0 )

    item9.AddGrowableRow( 1 )

    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
