# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: trasp.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.textctrl import TextCtrl, TextCtrl_LC, NotEditableTextCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.checkbox import CheckBox, RCheckBox, UnoZeroCheckBox
from awc.controls.radiobox import RadioBox
from awc.controls.button import FlatButton
from awc.controls.linktable import LinkTable
from awc.controls.entries import PartitaIvaEntryCtrl, CodiceFiscaleEntryCtrl, PhoneEntryCtrl, MailEntryCtrl, FolderEntryCtrl, HttpEntryCtrl

import awc.controls.windows as aw

from anag.basetab import AnagCardPanel, UnoZeroCheckBox, WorkZoneNotebook

import anag.lib as alib

import Env
bt = Env.Azienda.BaseTab


class LinkTableStatiSoloCodice(alib.LinkTableStati):

    _codewidth = 60
    _descwidth = 0
    
    def __init__(self, *args, **kwargs):
        alib.LinkTableStati.__init__(self, *args, **kwargs)
        s = self.GetSize()
        self.SetSize((60, s[1]))


class ExtraVetDataPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        if bt.MAGEXTRAVET:
            ExtraVetFunc(self)
        else:
            self.Hide()



# Window functions

ID_ANAGMAIN = 16000
ID_ESCLFTD = 16001

def TraCauCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.StaticBox( parent, -1, "" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = CheckBox( parent, ID_ESCLFTD, "Escludi il DDT dalla Fatturazione Differita", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "esclftd" )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( [ 20, 120 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ASKVET = 16002

def TraCurCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.StaticBox( parent, -1, "" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = CheckBox( parent, ID_ASKVET, "Gestione vettore", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "askvet" )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( [ 20, 120 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def TraAspCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 160 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def TraPorCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 160 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def TraConCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 160 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_WORKZONE = 16003

def TraVetCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = WorkZoneNotebook( parent, ID_WORKZONE, wx.DefaultPosition, [200,160], 0 )
    item2 = item3
    
    item4 = aw.Panel( item3, -1 ); item4.SetName('ClientiCommPage')
    TraVetCardAnagFunc(item4, False)
    item3.AddPage( item4, "Dati anagrafici" )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 16004
ID_TXT_INDIRIZZO = 16005
ID_TXT_CAP = 16006
ID_TXT_CITTA = 16007
ID_TXT_PROVINCIA = 16008
ID_STATO = 16009
ID_LINE = 16010
ID_TXT_CODFISC = 16011
ID_TXT_NAZIONE = 16012
ID_TXT_PIVA = 16013
ID_TXT_NUMTEL = 16014
ID_TXT_NUMTEL2 = 16015
ID_TXT_NUMFAX = 16016
ID_TXT_NUMFAX2 = 16017
ID_TXT_EMAIL = 16018
ID_TXT_SITEURL = 16019
ID_PANEXTRAVET = 16020

def TraVetCardAnagFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBox( parent, -1, "Sede legale" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.FlexGridSizer( 4, 0, 0, 0 )
    
    item5 = wx.FlexGridSizer( 0, 1, 0, 0 )
    parent.sizersede = item5
    
    item6 = wx.StaticText( parent, ID_TEXT, "Indirizzo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = TextCtrl( parent, ID_TXT_INDIRIZZO, "", wx.DefaultPosition, [400,-1], 0 )
    item7.SetName( "indirizzo" )
    item5.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item8 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "CAP", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Città", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Prov.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Stato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = TextCtrl( parent, ID_TXT_CAP, "", wx.DefaultPosition, [50,-1], 0 )
    item13.SetName( "cap" )
    item8.Add( item13, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = TextCtrl( parent, ID_TXT_CITTA, "", wx.DefaultPosition, [80,-1], 0 )
    item14.SetName( "citta" )
    item8.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item15 = TextCtrl( parent, ID_TXT_PROVINCIA, "", wx.DefaultPosition, [30,-1], 0 )
    item15.SetName( "prov" )
    item8.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item16 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item17 = LinkTableStatiSoloCodice(parent, ID_STATO, "id_stato")
    item16.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item16.Add( [ 60, 1 ] , 0, wx.ALIGN_CENTER, 5 )

    item16.AddGrowableCol( 0 )

    item8.Add( item16, 0, wx.ALIGN_CENTER, 5 )

    item8.AddGrowableCol( 1 )

    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 0 )

    item5.AddGrowableCol( 0 )

    item4.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4.AddGrowableCol( 0 )

    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item18 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item2.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item19 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item20 = wx.StaticText( parent, ID_TEXT, "Cod. Fiscale:", wx.DefaultPosition, [90,-1], 0 )
    item19.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.StaticText( parent, ID_TEXT, "P.IVA:", wx.DefaultPosition, [40,-1], 0 )
    item19.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item22 = CodiceFiscaleEntryCtrl( parent, ID_TXT_CODFISC, "", wx.DefaultPosition, [140,-1], 0 )
    item22.SetName( "codfisc" )
    item19.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item23 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item24 = NotEditableTextCtrl( parent, ID_TXT_NAZIONE, "", wx.DefaultPosition, [40,-1], 0 )
    item24.SetName( "nazione" )
    item23.Add( item24, 0, wx.GROW|wx.BOTTOM, 5 )

    item25 = PartitaIvaEntryCtrl( parent, ID_TXT_PIVA, "", wx.DefaultPosition, [100,-1], 0 )
    item25.SetFont( wx.Font( 10, wx.MODERN, wx.NORMAL, wx.NORMAL ) )
    item25.SetName( "piva" )
    item23.Add( item25, 0, wx.GROW|wx.RIGHT|wx.BOTTOM, 5 )

    item19.Add( item23, 0, wx.ALIGN_CENTER, 5 )

    item2.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item27 = wx.StaticBox( parent, -1, "Recapiti" )
    item26 = wx.StaticBoxSizer( item27, wx.VERTICAL )
    
    item28 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item29 = wx.StaticText( parent, ID_TEXT, "Telefono #1:", wx.DefaultPosition, [50,-1], 0 )
    item28.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item30 = wx.StaticText( parent, ID_TEXT, "Telefono #2:", wx.DefaultPosition, [50,-1], 0 )
    item28.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item31 = PhoneEntryCtrl( parent, ID_TXT_NUMTEL, "", wx.DefaultPosition, [120,-1], 0 )
    item31.SetName( "numtel" )
    item28.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item32 = PhoneEntryCtrl( parent, ID_TXT_NUMTEL2, "", wx.DefaultPosition, [120,-1], 0 )
    item32.SetName( "numtel2" )
    item28.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item33 = wx.StaticText( parent, ID_TEXT, "FAX #1:", wx.DefaultPosition, [40,-1], 0 )
    item28.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item34 = wx.StaticText( parent, ID_TEXT, "FAX #2:", wx.DefaultPosition, [40,-1], 0 )
    item28.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item35 = PhoneEntryCtrl( parent, ID_TXT_NUMFAX, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item35.SetName( "numfax" )
    item28.Add( item35, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item36 = PhoneEntryCtrl( parent, ID_TXT_NUMFAX2, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item36.SetName( "numfax2" )
    item28.Add( item36, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item28.AddGrowableCol( 0 )

    item28.AddGrowableCol( 1 )

    item26.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item37 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item38 = wx.StaticText( parent, ID_TEXT, "E-Mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item37.Add( item38, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item39 = MailEntryCtrl( parent, ID_TXT_EMAIL, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.SetName( "email" )
    item37.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item37.AddGrowableCol( 0 )

    item26.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item40 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item41 = wx.StaticText( parent, ID_TEXT, "Url Sito Internet:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item40.Add( item41, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item42 = HttpEntryCtrl( parent, ID_TXT_SITEURL, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.SetName( "siteurl" )
    item40.Add( item42, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item40.AddGrowableCol( 0 )

    item26.Add( item40, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW, 5 )

    item43 = ExtraVetDataPanel( parent, ID_PANEXTRAVET, wx.DefaultPosition, wx.DefaultSize, 0 )
    item43.SetName( "panextravet" )
    item0.Add( item43, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 100 ] , 0, wx.ALIGN_CENTER, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TIPDOC = 16021
ID_DATA1 = 16022
ID_DATA2 = 16023
ID_BUTUPDATE = 16024
ID_PANGRIDOC = 16025
ID_NUMDOCS = 16026
ID_TOTCOLLI = 16027
ID_TOTPESO = 16028
ID_BUTPRINT = 16029

def TraVetCardInterFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Estrai documenti di tipo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = alib.LinkTableDocMagazz(parent, ID_TIPDOC, 'id_tipdoc')
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "dal:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = DateCtrl( parent, ID_DATA1, "", wx.DefaultPosition, [80,-1], 0 )
    item5.SetName( "data1" )
    item1.Add( item5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "al:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item7 = DateCtrl( parent, ID_DATA2, "", wx.DefaultPosition, [80,-1], 0 )
    item7.SetName( "data2" )
    item1.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = wx.Button( parent, ID_BUTUPDATE, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetDefault()
    item8.SetName( "butupdate" )
    item1.Add( item8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Documenti trovati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetForegroundColour( wx.BLUE )
    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = wx.Panel( parent, ID_PANGRIDOC, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
    item11.SetName( "pangridoc" )
    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item13 = wx.StaticText( parent, ID_TEXT, "Totale spedizioni:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item14 = NumCtrl(parent, ID_NUMDOCS, integerWidth=5, groupDigits=False); item14.SetName("numdocs")
    item12.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Totale colli:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item15, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item16 = NumCtrl(parent, ID_TOTCOLLI, integerWidth=6, groupDigits=False); item16.SetName("totcolli")
    item12.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = wx.StaticText( parent, ID_TEXT, "Totale peso KG:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item17, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item18 = NumCtrl(parent, ID_TOTPESO, integerWidth=8, fractionWidth=3, groupDigits=True); item18.SetName("totpeso")
    item12.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19 = wx.Button( parent, ID_BUTPRINT, "Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetName( "butprint" )
    item12.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 3 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_DICHIAR = 16030
ID_TARGA = 16031
ID_AUTISTA = 16032

def ExtraVetFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Dichiarazione del vettore:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item4 = TextCtrl_LC( parent, ID_DICHIAR, "", wx.DefaultPosition, [-1,80], wx.TE_MULTILINE )
    item4.SetName( "dichiar" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 0 )

    item2.AddGrowableRow( 1 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item5 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Targa:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Autista:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item8 = TextCtrl( parent, ID_TARGA, "", wx.DefaultPosition, [80,-1], 0 )
    item8.SetName( "targa" )
    item5.Add( item8, 0, wx.ALIGN_CENTER|wx.BOTTOM, 5 )

    item9 = TextCtrl( parent, ID_AUTISTA, "", wx.DefaultPosition, [200,-1], 0 )
    item9.SetName( "autista" )
    item5.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 1 )

    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableRow( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

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
