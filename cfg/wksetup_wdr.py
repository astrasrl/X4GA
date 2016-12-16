# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: wksetup.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.textctrl import TextCtrl, TextCtrl_LC
from awc.controls.numctrl import NumCtrl
from awc.controls.checkbox import CheckBox
from awc.controls.radiobox import RadioBox
from awc.controls.notebook import Notebook
from awc.controls.entries import FolderEntryCtrl, FullPathFileEntryCtrl, PrintersComboBox

from anag.basetab import UnoZeroStringCheckBox

from Env import Azienda
bt = Azienda.BaseTab

import csv

class CSVFormatPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        CSVFormatFunc(self)

class CSVQuoting(wx.ComboBox):
    values = map(str, [csv.QUOTE_MINIMAL,    #testo
                       csv.QUOTE_NONNUMERIC, #testo con spazi
                       csv.QUOTE_ALL,        #ovunque
                       csv.QUOTE_NONE,       #nessuno
                   ])
    def SetValue(self, v):
        if v in self.values:
            self.SetSelection(int(self.values.index(v)))
    def GetValue(self):
        out = None
        v = self.GetSelection()
        if v < len(self.values):
            out = self.values[v]
        return out

class DDECheckBox(CheckBox):
    def __init__(self, *args, **kwargs):
        CheckBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values={True: '1', False: '0'})

class CmdPrintCheckBox(CheckBox):
    def __init__(self, *args, **kwargs):
        CheckBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values={True: '1', False: '0'})

class PrintPreviewRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values='view print'.split())

class IconTypeRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=['Vista', 'Pastel', 'Spheric'])



# Window functions

ID_NOTEBOOK = 15000
ID_NOTEBOOK_MYSQL = 15001
ID_SQLSPY = 15002
ID_ADDSERVER = 15003
ID_SITEINETAO = 15004
ID_CSVASGRID = 15005
ID_CSVSPEC = 15006
ID_THEME = 15007
ID_TABGRID = 15008
ID_BTNQUIT = 15009
ID_BTNOK = 15010

def _OLD_WorkstationSetup( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.BoxSizer( wx.VERTICAL )
    
    item4 = wx.StaticBox( parent, -1, "Sito installazione" )
    item3 = wx.StaticBoxSizer( item4, wx.VERTICAL )
    
    item6 = Notebook( parent, ID_NOTEBOOK, wx.DefaultPosition, [200,160], 0 )
    item5 = item6
    
    item7 = wx.Panel( item6, -1 )
    SiteConfig(item7, False)
    item6.AddPage( item7, "Identificativo" )

    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = wx.StaticBox( parent, -1, "Database" )
    item8 = wx.StaticBoxSizer( item9, wx.VERTICAL )
    
    item11 = Notebook( parent, ID_NOTEBOOK_MYSQL, wx.DefaultPosition, [200,160], 0 )
    item10 = item11
    
    item12 = wx.Panel( item11, -1 )
    DbMySql(item12, False)
    item11.AddPage( item12, "Server" )

    item8.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item14 = CheckBox( parent, ID_SQLSPY, "SQL spy", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "Database_sqlspy" )
    item13.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15 = wx.Button( parent, ID_ADDSERVER, "Aggiungi Server", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item13.AddGrowableCol( 1 )

    item8.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item17 = wx.StaticBox( parent, -1, "Collegamento ad Internet" )
    item16 = wx.StaticBoxSizer( item17, wx.VERTICAL )
    
    item18 = CheckBox( parent, ID_SITEINETAO, "Questa workstation dispone di un accesso permanente", wx.DefaultPosition, [360,-1], 0 )
    item18.SetName( "Site_inetao" )
    item16.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.Add( item16, 0, wx.GROW|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item1.Add( item2, 0, wx.GROW, 5 )

    item19 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item21 = wx.StaticBox( parent, -1, "Cartelle" )
    item20 = wx.StaticBoxSizer( item21, wx.VERTICAL )
    
    item23 = Notebook( parent, ID_NOTEBOOK, wx.DefaultPosition, [200,160], 0 )
    item22 = item23
    
    item24 = wx.Panel( item23, -1 )
    Report(item24, False)
    item23.AddPage( item24, "Report" )

    item20.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item26 = wx.StaticBox( parent, -1, "Esportazione dati: Formato file .CSV" )
    item25 = wx.StaticBoxSizer( item26, wx.VERTICAL )
    
    item27 = CheckBox( parent, ID_CSVASGRID, "Esporta i valori come presentati nelle griglie", wx.DefaultPosition, [360,-1], 0 )
    item27.SetName( "DataExport_csvasgrid" )
    item25.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item28 = CSVFormatPanel(parent, ID_CSVSPEC)
    item25.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19.Add( item25, 0, wx.GROW|wx.LEFT|wx.BOTTOM, 5 )

    item19.AddGrowableRow( 1 )

    item1.Add( item19, 0, wx.GROW, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item29 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item30 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item31 = IconTypeRadioBox( parent, ID_THEME, "Tema", wx.DefaultPosition, wx.DefaultSize, 
        ["Vista","Pastel","Spheric"] , 1, wx.RA_SPECIFY_COLS )
    item31.SetName( "Controls_iconstype" )
    item30.Add( item31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item32 = RadioBox( parent, ID_TABGRID, "Sulle griglie, il tasto TAB naviga su:", wx.DefaultPosition, wx.DefaultSize, 
        ["le celle della griglia","i controlli adiacenti alla griglia"] , 1, wx.RA_SPECIFY_COLS )
    item32.SetName( "Controls_tabgrid" )
    item30.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item29.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item33 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item34 = wx.Button( parent, ID_BTNQUIT, "Abbandona", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item34, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item35 = wx.Button( parent, ID_BTNOK, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item35.SetDefault()
    item33.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item33, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 15011
ID_MYSQLDESC = 15012
ID_MYSQLHOST = 15013
ID_MYSQLPORT = 15014
ID_MYSQLUSER = 15015
ID_MYSQLPSW = 15016
ID_CONNTEST = 15017

def DbMySql( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Descrizione:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item0.Add( item1, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item2 = TextCtrl_LC( parent, ID_MYSQLDESC, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.SetName( "MySQL_desc" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.StaticText( parent, ID_TEXT, "Server URL:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item4 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item5 = TextCtrl_LC( parent, ID_MYSQLHOST, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "MySQL_host" )
    item4.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Porta:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item7 = NumCtrl( parent, integerWidth=5, allowNegative=False, groupDigits=False); item7.SetName("MySQL_port")
    item4.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item4.AddGrowableCol( 0 )

    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Utente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item9 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item10 = TextCtrl_LC( parent, ID_MYSQLUSER, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "MySQL_user" )
    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item11, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item12 = TextCtrl_LC( parent, ID_MYSQLPSW, "", wx.DefaultPosition, [80,-1], wx.TE_PASSWORD )
    item12.SetName( "MySQL_pswd" )
    item9.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.Button( parent, ID_CONNTEST, "Test", wx.DefaultPosition, [40,-1], 0 )
    item9.Add( item13, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.BOTTOM, 5 )

    item9.AddGrowableCol( 0 )

    item9.AddGrowableCol( 2 )

    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item14 = wx.StaticText( parent, ID_TEXT, "Database:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "version" )
    item0.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_SITEATTDIR = 15018
ID_LINE = 15019
ID_PDFDEF = 15020
ID_PDFIMG = 15021
ID_PDFGEN = 15022
ID_PDFDPERS = 15023
ID_PDFCMD = 15024
ID_PRTDEF = 15025
ID_LABELER = 15026
ID_RPTACTION = 15027
ID_RPTDDE = 15028
ID_RPTCMDPRINT = 15029

def Report( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "File per allegati:", wx.DefaultPosition, [120,-1], wx.ALIGN_RIGHT )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = FolderEntryCtrl( parent, ID_SITEATTDIR, "", wx.DefaultPosition, [280,-1], 0 )
    item3.SetName( "Site_attdir" )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Definizioni report:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item7 = FolderEntryCtrl( parent, ID_PDFDEF, "", wx.DefaultPosition, [280,-1], 0 )
    item7.SetName( "Report_defin" )
    item5.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Immagini:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item9 = FolderEntryCtrl( parent, ID_PDFIMG, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "Report_images" )
    item5.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Pdf generati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item11 = FolderEntryCtrl( parent, ID_PDFGEN, "", wx.DefaultPosition, [220,-1], 0 )
    item11.SetName( "Report_output" )
    item5.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Report personalizzati:", wx.DefaultPosition, [120,-1], wx.ALIGN_RIGHT )
    item5.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item13 = FolderEntryCtrl( parent, ID_PDFDPERS, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetName( "Report_dpers" )
    item5.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Programma apertura:", wx.DefaultPosition, [120,-1], wx.ALIGN_RIGHT )
    item5.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item15 = FullPathFileEntryCtrl( parent, ID_PDFCMD, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "Report_pdfcmd" )
    item5.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 1 )

    item0.Add( item5, 0, wx.GROW, 5 )

    item16 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item17 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item18 = wx.StaticText( parent, ID_TEXT, "Stampante predefinita:", wx.DefaultPosition, [120,-1], wx.ALIGN_RIGHT )
    item17.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item19 = PrintersComboBox( parent, ID_PRTDEF, "", wx.DefaultPosition, [100,-1], [], wx.CB_DROPDOWN|wx.CB_READONLY )
    item19.SetName( "Report_prtdef" )
    item17.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item20 = wx.StaticText( parent, ID_TEXT, "Etichettatrice:", wx.DefaultPosition, [120,-1], wx.ALIGN_RIGHT )
    item17.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item21 = PrintersComboBox( parent, ID_LABELER, "", wx.DefaultPosition, [100,-1], [], wx.CB_DROPDOWN|wx.CB_READONLY )
    item21.SetName( "Report_labeler" )
    item17.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item17.AddGrowableCol( 1 )

    item0.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item22 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item23 = PrintPreviewRadioBox( parent, ID_RPTACTION, "Di default proponi:", wx.DefaultPosition, wx.DefaultSize, 
        ["Anteprima di stampa","Stampa diretta"] , 1, wx.RA_SPECIFY_COLS )
    item23.SetName( "Report_action" )
    item22.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item24 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item26 = wx.StaticBox( parent, -1, "Modo di stampa diretta" )
    item25 = wx.StaticBoxSizer( item26, wx.VERTICAL )
    
    item27 = DDECheckBox( parent, ID_RPTDDE, "Attiva DDE (richiede Adobe Reader - deprecato)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item27.SetName( "Report_dde" )
    item25.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item28 = CmdPrintCheckBox( parent, ID_RPTCMDPRINT, "Usa programma apertura con /t per stampare direttamente", wx.DefaultPosition, wx.DefaultSize, 0 )
    item28.SetName( "Report_cmdprint" )
    item25.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item24.Add( item25, 0, wx.GROW|wx.ALL, 5 )

    item24.AddGrowableCol( 0 )

    item24.AddGrowableRow( 0 )

    item22.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item22.AddGrowableCol( 1 )

    item0.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_SITENAME = 15030
ID_SITEFOLDER = 15031
ID_SITEREMOTE = 15032

def SiteConfig( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Cod.Identificativo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = TextCtrl_LC( parent, ID_SITENAME, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetName( "Site_name" )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "Cartella comune:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5 = FolderEntryCtrl( parent, ID_SITEFOLDER, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "Site_folder" )
    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW, 5 )

    item6 = CheckBox( parent, ID_SITEREMOTE, "Postazione remota", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetName( "Site_remote" )
    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CSVSEPARATOR = 15033
ID_CSVDELIMITER = 15034
ID_CSVEXCELZERO = 15035
ID_CSVQUOTING = 15036

def CSVFormatFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item2 = wx.StaticText( parent, ID_TEXT, "Adotta i seguenti criteri:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Separatore colonne:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = wx.TextCtrl( parent, ID_CSVSEPARATOR, "", wx.DefaultPosition, [20,-1], 0 )
    item6.SetName( "DataExport_csvdelimiter" )
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Delimitatore colonna:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item8 = wx.TextCtrl( parent, ID_CSVDELIMITER, "", wx.DefaultPosition, [20,-1], 0 )
    item8.SetName( "DataExport_csvquotechar" )
    item5.Add( item8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item9 = UnoZeroStringCheckBox( parent, ID_CSVEXCELZERO, "Excel workaround testi con numeri", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "DataExport_csvexcelzero" )
    item5.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Impiego dei delimitatori:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item11 = CSVQuoting( parent, ID_CSVQUOTING, "", wx.DefaultPosition, [100,-1], 
        ["Testo ambiguo","Testo","Sempre","Mai"] , wx.CB_DROPDOWN|wx.CB_READONLY )
    item11.SetName( "DataExport_csvquoting" )
    item3.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3.AddGrowableCol( 1 )

    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def WorkstationSetup( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.Notebook( parent, ID_NOTEBOOK, wx.DefaultPosition, wx.DefaultSize, 0 )
    item1 = item2
    
    item3 = wx.Panel( item2, -1 )
    SetupSiteFunc(item3, False)
    item2.AddPage( item3, "Sito installazione" )

    item4 = wx.Panel( item2, -1 )
    SetupAspettoFunc(item4, False)
    item2.AddPage( item4, "Aspetto" )

    item5 = wx.Panel( item2, -1 )
    SetupDatabaseFunc(item5, False)
    item2.AddPage( item5, "Database" )

    item6 = wx.Panel( item2, -1 )
    SetupReportFunc(item6, False)
    item2.AddPage( item6, "Report" )

    item7 = wx.Panel( item2, -1 )
    SetupCSVFunc(item7, False)
    item2.AddPage( item7, "CSV" )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = wx.Button( parent, ID_BTNOK, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetDefault()
    item0.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_FUNCKEY = 15037

def SetupAspettoFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = IconTypeRadioBox( parent, ID_THEME, "Tema", wx.DefaultPosition, wx.DefaultSize, 
        ["Vista","Pastel","Spheric"] , 1, wx.RA_SPECIFY_COLS )
    item3.SetName( "Controls_iconstype" )
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = RadioBox( parent, ID_TABGRID, "Sulle griglie, il tasto TAB naviga su:", wx.DefaultPosition, wx.DefaultSize, 
        ["le celle della griglia","i controlli adiacenti alla griglia"] , 1, wx.RA_SPECIFY_COLS )
    item4.SetName( "Controls_tabgrid" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = RadioBox( parent, ID_FUNCKEY, "Tasti funzione su doc.magazzino:", wx.DefaultPosition, wx.DefaultSize, 
        ["abilitati","disabilitati"] , 1, wx.RA_SPECIFY_COLS )
    item5.SetName( "Controls_funckey" )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def SetupSiteFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Sito installazione" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Cod.Identificativo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = TextCtrl_LC( parent, ID_SITENAME, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "Site_name" )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Cartella comune:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item7 = FolderEntryCtrl( parent, ID_SITEFOLDER, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetName( "Site_folder" )
    item3.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3.AddGrowableCol( 1 )

    item1.Add( item3, 0, wx.GROW, 5 )

    item8 = CheckBox( parent, ID_SITEREMOTE, "Postazione remota", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "Site_remote" )
    item1.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.StaticBox( parent, -1, "Collegamento ad Internet" )
    item9 = wx.StaticBoxSizer( item10, wx.VERTICAL )
    
    item11 = CheckBox( parent, ID_SITEINETAO, "Questa workstation dispone di un accesso permanente", wx.DefaultPosition, [360,-1], 0 )
    item11.SetName( "Site_inetao" )
    item9.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item9, 0, wx.GROW|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def SetupDatabaseFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Database" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item4 = Notebook( parent, ID_NOTEBOOK_MYSQL, wx.DefaultPosition, [200,160], 0 )
    item3 = item4
    
    item5 = wx.Panel( item4, -1 )
    DbMySql(item5, False)
    item4.AddPage( item5, "Server" )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item6 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item7 = CheckBox( parent, ID_SQLSPY, "SQL spy", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetName( "Database_sqlspy" )
    item6.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = wx.Button( parent, ID_ADDSERVER, "Aggiungi Server", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item6.AddGrowableCol( 1 )

    item1.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXTCTRL = 15038

def SetupReportFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "File per allegati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = FolderEntryCtrl( parent, ID_SITEATTDIR, "", wx.DefaultPosition, [280,-1], 0 )
    item4.SetName( "Site_attdir" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "Definizioni report:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item6 = FolderEntryCtrl( parent, ID_PDFDEF, "", wx.DefaultPosition, [280,-1], 0 )
    item6.SetName( "Report_defin" )
    item2.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Immagini:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item8 = FolderEntryCtrl( parent, ID_PDFIMG, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "Report_images" )
    item2.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Pdf generati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item10 = FolderEntryCtrl( parent, ID_PDFGEN, "", wx.DefaultPosition, [220,-1], 0 )
    item10.SetName( "Report_output" )
    item2.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Report personalizzati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item12 = FolderEntryCtrl( parent, ID_PDFDPERS, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.SetName( "Report_dpers" )
    item2.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "Programma apertura:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item14 = FullPathFileEntryCtrl( parent, ID_PDFCMD, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "Report_pdfcmd" )
    item2.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Stampante predefinita:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item16 = PrintersComboBox( parent, ID_PRTDEF, "", wx.DefaultPosition, [100,-1], [], wx.CB_DROPDOWN|wx.CB_READONLY )
    item16.SetName( "Report_prtdef" )
    item2.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item17 = wx.StaticText( parent, ID_TEXT, "Etichettatrice:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item18 = PrintersComboBox( parent, ID_LABELER, "", wx.DefaultPosition, [100,-1], [], wx.CB_DROPDOWN|wx.CB_READONLY )
    item18.SetName( "Report_labeler" )
    item2.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 1 )

    item1.Add( item2, 0, wx.GROW, 5 )

    item19 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item20 = PrintPreviewRadioBox( parent, ID_RPTACTION, "Di default proponi:", wx.DefaultPosition, wx.DefaultSize, 
        ["Anteprima di stampa","Stampa diretta"] , 1, wx.RA_SPECIFY_COLS )
    item20.SetName( "Report_action" )
    item19.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item21 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item23 = wx.StaticBox( parent, -1, "Modo di stampa diretta" )
    item22 = wx.StaticBoxSizer( item23, wx.VERTICAL )
    
    item24 = DDECheckBox( parent, ID_RPTDDE, "Attiva DDE (richiede Adobe Reader - deprecato)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetName( "Report_dde" )
    item22.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item25 = CmdPrintCheckBox( parent, ID_RPTCMDPRINT, "Usa programma apertura con /t per stampare direttamente", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetName( "Report_cmdprint" )
    item22.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item26 = wx.StaticText( parent, ID_TEXT, "Paramertri per stampa diretta (in funzione del lettore pdf in uso)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item27 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item27.SetToolTip( wx.ToolTip("<pgm_pdf> -nome programma pdf <file_pdf>-file pdf da stampare") )
    item27.SetName( "Report_cmd2print" )
    item22.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21.Add( item22, 0, wx.GROW|wx.ALL, 5 )

    item21.AddGrowableCol( 0 )

    item21.AddGrowableRow( 0 )

    item19.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19.AddGrowableCol( 1 )

    item1.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def SetupCSVFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Esportazione dati: Formato file .CSV" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = CheckBox( parent, ID_CSVASGRID, "Esporta i valori come presentati nelle griglie", wx.DefaultPosition, [360,-1], 0 )
    item3.SetName( "DataExport_csvasgrid" )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = CSVFormatPanel(parent, ID_CSVSPEC)
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.LEFT|wx.BOTTOM, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
