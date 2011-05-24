# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: effetti.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc import util

from awc.controls.linktable import LinkTable
from anag.lib import LinkTablePdc, LinkTableEffetto

from awc.controls.radiobox import RadioBox
from awc.controls.checkbox import CheckBox
from awc.controls.textctrl import TextCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.entries import FolderEntryCtrl

from Env import Azienda
bt = Azienda.BaseTab

from anag.pdc import PdcDialog
from anag.clienti import ClientiDialog
from anag.banche import BancheDialog
from anag.modpag import ModPagDialog

class FilePathControl(FolderEntryCtrl):

    def __init__(self, *args, **kwargs):
        FolderEntryCtrl.__init__(self, *args, **kwargs)
        self.SetName('filepath')



# Window functions

ID_TIPEFF = 10000
ID_TEXT = 10001
ID_CAUS = 10002
ID_MODPAG = 10003
ID_PDC = 10004
ID_DATSCA1 = 10005
ID_DATSCA2 = 10006
ID_DATDOC1 = 10007
ID_DATDOC2 = 10008
ID_NUMDOC1 = 10009
ID_NUMDOC2 = 10010
ID_LINE = 10011
ID_INCLEMES = 10012
ID_INCLCONT = 10013
ID_INCLINSOL = 10014
ID_INCLCHIUS = 10015
ID_BUTSRC = 10016
ID_DATDIST = 10017
ID_BANCA = 10018
ID_CONTOEFF = 10019
ID_BUTDIST = 10020
ID_FILEPATH = 10021
ID_BUTFILE = 10022
ID_CAUCONT = 10023
ID_BUTCONT = 10024
ID_BUTSAVESEL = 10025
ID_PANGRID = 10026
ID_COLORSELEZ = 10027
ID_COLOREMESSO = 10028
ID_COLORERROR = 10029
ID_COLORINSATT = 10030
ID_COLORINSPAG = 10031
ID_NUMEFF = 10032
ID_TOTEFF = 10033
ID_NUMSEL = 10034
ID_TOTSEL = 10035
ID_BUTLISTALL = 10036
ID_BUTLISTSEL = 10037
ID_BUTSELEFF = 10038
ID_BUTDESELEFF = 10039
ID_BUTSELALL = 10040
ID_BUTDESELALL = 10041

def EffettiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item3 = RadioBox( parent, ID_TIPEFF, "Tipo effetti da emettere:", wx.DefaultPosition, wx.DefaultSize, 
        ["RIBA - Ricevute Bancarie","RID - Addebito sul conto"] , 1, wx.RA_SPECIFY_ROWS )
    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item5 = wx.StaticBox( parent, -1, "Selezioni" )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    
    item6 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item7 = wx.StaticText( parent, ID_TEXT, "Causale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = LinkTable(parent, ID_CAUS ); item8.SetDataLink(bt.TABNAME_CFGCONTAB, "caus", None)
    item6.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Mod. pagamento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = LinkTable(parent, ID_MODPAG ); item10.SetDataLink(bt.TABNAME_MODPAG, "modpag", ModPagDialog)
    item6.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Cliente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12 = LinkTablePdc(parent, ID_PDC ); item12.SetDataLink(bt.TABNAME_PDC, "pdc", ClientiDialog)
    item6.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6.AddGrowableCol( 1 )

    item4.Add( item6, 0, wx.GROW, 5 )

    item13 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item14 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item14, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Da:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item16 = wx.StaticText( parent, ID_TEXT, "A:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item17 = wx.StaticText( parent, ID_TEXT, "Data scadenza:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = DateCtrl( parent, ID_DATSCA1, "", wx.DefaultPosition, [80,-1], 0 )
    item18.SetName( "datsca1" )
    item13.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = DateCtrl( parent, ID_DATSCA2, "", wx.DefaultPosition, [80,-1], 0 )
    item19.SetName( "datsca2" )
    item13.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = wx.StaticText( parent, ID_TEXT, "Data documento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = DateCtrl( parent, ID_DATDOC1, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "datdoc1" )
    item13.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item22 = DateCtrl( parent, ID_DATDOC2, "", wx.DefaultPosition, [80,-1], 0 )
    item22.SetName( "datdoc2" )
    item13.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item23 = wx.StaticText( parent, ID_TEXT, "Num. documento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item23, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item24 = NumCtrl( parent, integerWidth=10, allowNegative=False, groupDigits=False); item24.SetName("numdoc1"); item24.SetId(ID_NUMDOC1)
    item13.Add( item24, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item25 = NumCtrl( parent, integerWidth=10, allowNegative=False, groupDigits=False); item25.SetName("numdoc2"); item25.SetId(ID_NUMDOC2)
    item13.Add( item25, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item4.Add( item13, 0, wx.GROW, 5 )

    item26 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item4.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item27 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item28 = wx.BoxSizer( wx.HORIZONTAL )
    
    item29 = wx.StaticText( parent, ID_TEXT, "Includi:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item28.Add( item29, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item30 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item31 = wx.CheckBox( parent, ID_INCLEMES, "Effetti Emessi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = wx.CheckBox( parent, ID_INCLCONT, "Contabilizzati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item33 = wx.CheckBox( parent, ID_INCLINSOL, "Insoluti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item34 = wx.CheckBox( parent, ID_INCLCHIUS, "Partite chiuse", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item28.Add( item30, 0, wx.ALIGN_CENTER, 5 )

    item27.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item35 = wx.Button( parent, ID_BUTSRC, "&Cerca", wx.DefaultPosition, wx.DefaultSize, 0 )
    item35.SetDefault()
    item27.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item27.AddGrowableCol( 1 )

    item4.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.AddGrowableCol( 0 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item36 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item38 = wx.StaticBox( parent, -1, "Emissione" )
    item37 = wx.StaticBoxSizer( item38, wx.VERTICAL )
    
    item39 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item40 = wx.StaticText( parent, ID_TEXT, "Data distinta:", wx.DefaultPosition, [80,-1], wx.ALIGN_RIGHT )
    item39.Add( item40, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item41 = DateCtrl( parent, ID_DATDIST, "", wx.DefaultPosition, [80,-1], 0 )
    item41.SetName( "datdist" )
    item39.Add( item41, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item42 = wx.StaticText( parent, ID_TEXT, "Banca:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item42, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item43 = LinkTablePdc(parent, ID_BANCA ); item43.SetDataLink(bt.TABNAME_PDC, "banca", BancheDialog)
    item39.Add( item43, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item44 = wx.StaticText( parent, ID_TEXT, "Conto effetti:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item44, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item45 = LinkTableEffetto(parent, ID_CONTOEFF, "contoeff")
    item39.Add( item45, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item39.AddGrowableCol( 1 )

    item37.Add( item39, 0, wx.GROW, 5 )

    item46 = wx.Button( parent, ID_BUTDIST, "Stampa &distinta", wx.DefaultPosition, wx.DefaultSize, 0 )
    item37.Add( item46, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item36.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item48 = wx.StaticBox( parent, -1, "Generazione file da trasmettere alla banca" )
    item47 = wx.StaticBoxSizer( item48, wx.VERTICAL )
    
    item49 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item50 = wx.StaticText( parent, ID_TEXT, "Percorso:", wx.DefaultPosition, [80,-1], wx.ALIGN_RIGHT )
    item49.Add( item50, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item51 = FilePathControl(parent, ID_FILEPATH)
    item49.Add( item51, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item49.AddGrowableCol( 1 )

    item47.Add( item49, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item52 = wx.Button( parent, ID_BUTFILE, "Genera &file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item52, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item36.Add( item47, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item54 = wx.StaticBox( parent, -1, "Contabilizzazione" )
    item53 = wx.StaticBoxSizer( item54, wx.VERTICAL )
    
    item55 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item56 = wx.StaticText( parent, ID_TEXT, "Causale:", wx.DefaultPosition, [80,-1], wx.ALIGN_RIGHT )
    item55.Add( item56, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item57 = LinkTable(parent, ID_CAUCONT ); item57.SetDataLink(bt.TABNAME_CFGCONTAB, "caucont", None)
    item55.Add( item57, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item55.AddGrowableCol( 1 )

    item53.Add( item55, 0, wx.GROW, 5 )

    item58 = wx.BoxSizer( wx.HORIZONTAL )
    
    item59 = wx.Button( parent, ID_BUTCONT, "Avvia contabilizzazione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item58.Add( item59, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item53.Add( item58, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item36.Add( item53, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item36.AddGrowableCol( 0 )

    item36.AddGrowableRow( 1 )

    item1.Add( item36, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item60 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item61 = wx.StaticText( parent, ID_TEXT, "Effetti estratti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item61.SetForegroundColour( wx.BLUE )
    item60.Add( item61, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item62 = wx.Button( parent, ID_BUTSAVESEL, "Salva selezioni", wx.DefaultPosition, [-1,10], wx.NO_BORDER )
    item60.Add( item62, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, 5 )

    item60.AddGrowableCol( 0 )

    item0.Add( item60, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item63 = wx.Panel( parent, ID_PANGRID, wx.DefaultPosition, [820,260], wx.SUNKEN_BORDER )
    item0.Add( item63, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item64 = wx.BoxSizer( wx.HORIZONTAL )
    
    item65 = wx.StaticText( parent, ID_TEXT, "Legenda:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item64.Add( item65, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item66 = wx.BoxSizer( wx.HORIZONTAL )
    
    item67 = wx.Panel( parent, ID_COLORSELEZ, wx.DefaultPosition, [20,20], wx.RAISED_BORDER )
    item66.Add( item67, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item68 = wx.StaticText( parent, ID_TEXT, "Selezionato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item66.Add( item68, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item64.Add( item66, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item69 = wx.BoxSizer( wx.HORIZONTAL )
    
    item70 = wx.Panel( parent, ID_COLOREMESSO, wx.DefaultPosition, [20,20], wx.RAISED_BORDER )
    item69.Add( item70, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item71 = wx.StaticText( parent, ID_TEXT, "Già emesso", wx.DefaultPosition, wx.DefaultSize, 0 )
    item69.Add( item71, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item64.Add( item69, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item72 = wx.BoxSizer( wx.HORIZONTAL )
    
    item73 = wx.Panel( parent, ID_COLORERROR, wx.DefaultPosition, [20,20], wx.RAISED_BORDER )
    item72.Add( item73, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item74 = wx.StaticText( parent, ID_TEXT, "Dati errati o mancanti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item72.Add( item74, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item64.Add( item72, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item75 = wx.BoxSizer( wx.HORIZONTAL )
    
    item76 = wx.Panel( parent, ID_COLORINSATT, wx.DefaultPosition, [20,20], wx.RAISED_BORDER )
    item75.Add( item76, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item77 = wx.StaticText( parent, ID_TEXT, "Insoluto aperto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item75.Add( item77, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item64.Add( item75, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item78 = wx.BoxSizer( wx.HORIZONTAL )
    
    item79 = wx.Panel( parent, ID_COLORINSPAG, wx.DefaultPosition, [20,20], wx.RAISED_BORDER )
    item78.Add( item79, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item80 = wx.StaticText( parent, ID_TEXT, "Insoluto pagato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item78.Add( item80, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item64.Add( item78, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item64, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item81 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item82 = wx.BoxSizer( wx.HORIZONTAL )
    
    item83 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item84 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item83.Add( item84, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item85 = wx.StaticText( parent, ID_TEXT, "Num.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item83.Add( item85, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item86 = wx.StaticText( parent, ID_TEXT, "Importo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item83.Add( item86, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item87 = wx.StaticText( parent, ID_TEXT, "Estratti:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item83.Add( item87, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item88 = NumCtrl(parent, ID_NUMEFF, integerWidth=4, allowNegative=False, groupDigits=True); item88.SetName("numeff")
    item83.Add( item88, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item89 = NumCtrl(parent, ID_TOTEFF, integerWidth=12, fractionWidth=2, groupDigits=True); item89.SetName("toteff")
    item83.Add( item89, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item90 = wx.StaticText( parent, ID_TEXT, "Selezionati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item83.Add( item90, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item91 = NumCtrl(parent, ID_NUMSEL, integerWidth=4, allowNegative=False, groupDigits=True); item91.SetName("numsel")
    item83.Add( item91, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item92 = NumCtrl(parent, ID_TOTSEL, integerWidth=12, fractionWidth=2, groupDigits=True); item92.SetName("totsel")
    item83.Add( item92, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item82.Add( item83, 0, wx.ALIGN_CENTER, 5 )

    item93 = wx.BoxSizer( wx.VERTICAL )
    
    item94 = wx.Button( parent, ID_BUTLISTALL, "&Lista effetti estratti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item93.Add( item94, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item95 = wx.Button( parent, ID_BUTLISTSEL, "&Lista effetti selezionati", wx.DefaultPosition, wx.DefaultSize, 0 )
    item93.Add( item95, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item82.Add( item93, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item81.Add( item82, 0, wx.ALIGN_CENTER, 5 )

    item96 = wx.BoxSizer( wx.HORIZONTAL )
    
    item97 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item98 = wx.Button( parent, ID_BUTSELEFF, "Seleziona", wx.DefaultPosition, wx.DefaultSize, 0 )
    item97.Add( item98, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item99 = wx.Button( parent, ID_BUTDESELEFF, "Deseleziona", wx.DefaultPosition, wx.DefaultSize, 0 )
    item97.Add( item99, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item100 = wx.Button( parent, ID_BUTSELALL, "Seleziona Tutto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item97.Add( item100, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item101 = wx.Button( parent, ID_BUTDESELALL, "Deseleziona Tutto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item97.Add( item101, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item97.AddGrowableCol( 0 )

    item97.AddGrowableCol( 1 )

    item96.Add( item97, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item81.Add( item96, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )

    item81.AddGrowableCol( 1 )

    item0.Add( item81, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
