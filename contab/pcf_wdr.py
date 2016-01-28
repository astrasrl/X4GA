# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: pcf.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from wx import Panel as wxPanel

from awc.controls.linktable import LinkTable
from awc.controls.textctrl import TextCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.checkbox import CheckBox, CheckListBox
from awc.controls.radiobox import RadioBox

from anag.lib import LinkTableCliFor, LinkTableBanca, LinkTableEffetto

from Env import Azienda
bt = Azienda.BaseTab

from anag.pdc import PdcDialog
from anag.pdctip import PdcTipDialog
from anag.modpag import ModPagDialog


class ClientiListBox(CheckListBox):
    pass

import stormdb as adb

def GetTipanaId(tipo):
    out = None
    tipana = adb.DbTable(bt.TABNAME_PDCTIP, writable=False)
    if tipana.Retrieve('codice=%s', tipo) and tipana.OneRow():
        out = tipana.id
    return out



# Window functions

ID_TEXT = 10000
ID_PDC = 10001
ID_PCF = 10002
ID_LINE = 10003
ID_CAUSALE = 10004
ID_DATDOC = 10005
ID_NUMDOC = 10006
ID_MODPAG = 10007
ID_DATSCAD = 10008
ID_CHKRIBA = 10009
ID_CONTRASS = 10010
ID_CHKINSOL = 10011
ID_TEXTCTRL = 10012
ID_IMPTOT = 10013
ID_IMPPAR = 10014
ID_SALDO = 10015
ID_IMPEFF = 10016
ID_EFFEMESS = 10017
ID_EFFCONT = 10018
ID_BANEMI = 10019
ID_EFFPDC = 10020
ID_BANAPP = 10021
ID_PANELHIST = 10022
ID_BTNDEL = 10023
ID_BTNOK = 10024

def PcfPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Sottoconto:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = LinkTableCliFor(parent, ID_PDC); item3.SetDataLink(bt.TABNAME_PDC, "id_pdc", None); item3.SetObligatory(True)
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "ID Partita:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item5 = NumCtrl( parent, integerWidth=12, fractionWidth=0, allowNegative=False, groupDigits=False); item5.SetName("id_pcf"); item5.SetEditable(False)
    item1.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item6 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = wx.StaticText( parent, ID_TEXT, "Causale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item10 = LinkTable(parent, ID_CAUSALE ); item10.SetDataLink( bt.TABNAME_CFGCONTAB, "id_caus", None ); item10.SetObligatory(True)
    item7.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item12 = wx.StaticText( parent, ID_TEXT, "Data:", wx.DefaultPosition, [30,-1], wx.ALIGN_RIGHT )
    item11.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item13 = DateCtrl( parent, ID_DATDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item13.SetName( "datdoc" )
    item11.Add( item13, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Num.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item11.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item15 = TextCtrl( parent, ID_NUMDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item15.SetName( "numdoc" )
    item11.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item16 = wx.StaticText( parent, ID_TEXT, "Mod. Pagamento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item17 = wx.StaticText( parent, ID_TEXT, "Scadenza:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item18 = LinkTable(parent, ID_MODPAG ); item18.SetDataLink( bt.TABNAME_MODPAG, "id_modpag", ModPagDialog ); item18.SetObligatory(True)
    item7.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item20 = wx.StaticText( parent, ID_TEXT, "Data:", wx.DefaultPosition, [30,-1], wx.ALIGN_RIGHT )
    item19.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item21 = DateCtrl( parent, ID_DATSCAD, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "datscad" )
    item19.Add( item21, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item22 = CheckBox( parent, ID_CHKRIBA, "RIBA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetToolTip( wx.ToolTip("Barrare se la scadenza è una Ricevuta Bancaria") )
    item22.SetName( "riba" )
    item19.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item23 = CheckBox( parent, ID_CONTRASS, "Contrassegno", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.SetToolTip( wx.ToolTip("Barrare se la scadenza è un Contrassegno") )
    item23.SetName( "contrass" )
    item19.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item24 = CheckBox( parent, ID_CHKINSOL, "Insoluto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetToolTip( wx.ToolTip("Barrare se la scadenza è una Ricevuta Bancaria") )
    item24.SetName( "insoluto" )
    item19.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19.AddGrowableCol( 2 )

    item19.AddGrowableCol( 3 )

    item7.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7.AddGrowableCol( 0 )

    item7.AddGrowableCol( 1 )

    item0.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item25 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item26 = wx.StaticText( parent, ID_TEXT, "Note:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item27 = TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [627,-1], 0 )
    item27.SetName( "note" )
    item25.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item25.AddGrowableCol( 1 )

    item0.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item28 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item29 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item30 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item31 = wx.StaticText( parent, ID_TEXT, "Valori", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item31.SetForegroundColour( wx.BLUE )
    item30.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item32 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item33 = wx.StaticText( parent, ID_TEXT, "Importo:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item32.Add( item33, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item34 = NumCtrl( parent, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=True, groupDigits=True); item34.SetName("imptot")
    item32.Add( item34, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item35 = wx.StaticText( parent, ID_TEXT, "Pareggiamento:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item32.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item36 = NumCtrl( parent, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=True, groupDigits=True); item36.SetName("imppar")
    item32.Add( item36, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item32.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER, 5 )

    item37 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item32.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item38 = wx.StaticText( parent, ID_TEXT, "Saldo:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item32.Add( item38, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item39 = NumCtrl( parent, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=True, groupDigits=True); item39.SetName("saldo"); item39.SetEditable(False)
    item32.Add( item39, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item30.Add( item32, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item29.Add( item30, 0, wx.ALIGN_RIGHT, 5 )

    item40 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [-1,20], wx.LI_VERTICAL )
    item29.Add( item40, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

    item41 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item42 = wx.StaticText( parent, ID_TEXT, "Dati Effetto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.SetForegroundColour( wx.BLUE )
    item41.Add( item42, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item43 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item44 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item45 = wx.StaticText( parent, ID_TEXT, "Importo:", wx.DefaultPosition, [100,-1], wx.ALIGN_RIGHT )
    item44.Add( item45, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item46 = NumCtrl( parent, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=True, groupDigits=True); item46.SetName("impeff")
    item44.Add( item46, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item47 = CheckBox( parent, ID_EFFEMESS, "Emesso", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.SetName( "f_effemes" )
    item44.Add( item47, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item48 = CheckBox( parent, ID_EFFCONT, "Contabilizzato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item48.SetName( "f_effcont" )
    item44.Add( item48, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item43.Add( item44, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item49 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item50 = wx.StaticText( parent, ID_TEXT, "Data di emissione:", wx.DefaultPosition, [100,-1], wx.ALIGN_RIGHT )
    item49.Add( item50, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item51 = DateCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item51.SetName( "effdate" )
    item49.Add( item51, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item43.Add( item49, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item41.Add( item43, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item52 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item53 = wx.StaticText( parent, ID_TEXT, "Banca emittente:", wx.DefaultPosition, [100,-1], wx.ALIGN_RIGHT )
    item52.Add( item53, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item54 = LinkTableBanca(parent, ID_BANEMI ); item54.SetDataLink( bt.TABNAME_PDC, "id_effban", None); item54.SetObligatory(True)
    item52.Add( item54, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item55 = wx.StaticText( parent, ID_TEXT, "Conto effetti:", wx.DefaultPosition, [100,-1], wx.ALIGN_RIGHT )
    item52.Add( item55, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item56 = LinkTableEffetto(parent, ID_EFFPDC, "id_effpdc")
    item52.Add( item56, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item57 = wx.StaticText( parent, ID_TEXT, "Banca d'appoggio:", wx.DefaultPosition, [100,-1], wx.ALIGN_RIGHT )
    item52.Add( item57, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item58 = LinkTable(parent, ID_BANAPP ); item58.SetDataLink(bt.TABNAME_BANCF, "id_effbap", None)
    item52.Add( item58, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item52.AddGrowableCol( 1 )

    item41.Add( item52, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item41.AddGrowableCol( 0 )

    item29.Add( item41, 0, wx.GROW, 5 )

    item29.AddGrowableCol( 2 )

    item0.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item59 = wx.StaticText( parent, ID_TEXT, "Storia della partita", wx.DefaultPosition, wx.DefaultSize, 0 )
    item59.SetForegroundColour( wx.BLUE )
    item0.Add( item59, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item60 = wx.Panel( parent, ID_PANELHIST, wx.DefaultPosition, [-1,160], wx.SUNKEN_BORDER )
    item0.Add( item60, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item61 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item62 = wx.Button( parent, ID_BTNDEL, "Elimina", wx.DefaultPosition, wx.DefaultSize, 0 )
    item62.SetDefault()
    item62.SetName( "btndel" )
    item61.Add( item62, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item63 = wx.BoxSizer( wx.HORIZONTAL )
    
    item64 = wx.Button( parent, ID_BTNOK, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item64.SetDefault()
    item64.SetName( "btnok" )
    item63.Add( item64, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item61.Add( item63, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item61.AddGrowableCol( 1 )

    item0.Add( item61, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 7 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CLIFOR = 10025
ID_RIBA = 10026
ID_DATA1 = 10027
ID_DATA2 = 10028
ID_NOPCFSALD = 10029
ID_SCADMULTI = 10030
ID_UPDATE = 10031
ID_ACCORPA = 10032
ID_WRITE = 10033
ID_CLIENTI = 10034
ID_PANGRIDPCF = 10035

def AccorpaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = RadioBox( parent, ID_CLIFOR, "Tipo", wx.DefaultPosition, wx.DefaultSize, 
        ["Clienti","Fornitori"] , 1, wx.RA_SPECIFY_COLS )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = RadioBox( parent, ID_RIBA, "RIBA", wx.DefaultPosition, wx.DefaultSize, 
        ["Si","No","Tutto"] , 1, wx.RA_SPECIFY_COLS )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item5 = wx.StaticBox( parent, -1, "Periodo da analizzare" )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    
    item6 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item7 = wx.StaticText( parent, ID_TEXT, "Da data:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = DateCtrl( parent, ID_DATA1, "", wx.DefaultPosition, [80,-1], 0 )
    item6.Add( item8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "a data:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = DateCtrl( parent, ID_DATA2, "", wx.DefaultPosition, [80,-1], 0 )
    item6.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item4.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item12 = wx.StaticBox( parent, -1, "Partite" )
    item11 = wx.StaticBoxSizer( item12, wx.VERTICAL )
    
    item13 = CheckBox( parent, ID_NOPCFSALD, "Escludi le partite saldate", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetValue( True )
    item11.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item14 = CheckBox( parent, ID_SCADMULTI, "Mostra solo le partite che hanno la stessa data di scadenza", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetValue( True )
    item11.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

    item15 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item16 = wx.Button( parent, ID_UPDATE, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.SetDefault()
    item15.Add( item16, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item17 = wx.Button( parent, ID_ACCORPA, "Accorpa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item17, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item18 = wx.Button( parent, ID_WRITE, "Scrivi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item15.AddGrowableCol( 1 )

    item15.AddGrowableRow( 0 )

    item1.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 4 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item20 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item21 = wx.StaticText( parent, ID_TEXT, "Clienti con partite multiple nel periodo", wx.DefaultPosition, [300,-1], 0 )
    item21.SetBackgroundColour( wx.LIGHT_GREY )
    item20.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item22 = ClientiListBox(parent, ID_CLIENTI)
    item20.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item20.AddGrowableCol( 0 )

    item20.AddGrowableRow( 1 )

    item19.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item23 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item24 = wx.StaticText( parent, ID_TEXT, "Partite del cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetBackgroundColour( wx.LIGHT_GREY )
    item23.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item25 = wx.Panel( parent, ID_PANGRIDPCF, wx.DefaultPosition, [600,300], wx.SUNKEN_BORDER )
    item23.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item23.AddGrowableCol( 0 )

    item23.AddGrowableRow( 1 )

    item19.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19.AddGrowableCol( 0 )

    item19.AddGrowableCol( 1 )

    item19.AddGrowableRow( 0 )

    item0.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
