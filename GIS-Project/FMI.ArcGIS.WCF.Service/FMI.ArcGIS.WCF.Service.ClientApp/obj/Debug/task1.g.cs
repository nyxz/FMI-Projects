﻿#pragma checksum "C:\Documents and Settings\maistora\Desktop\FMI.ArcGIS.WCF.Service\FMI.ArcGIS.WCF.Service.ClientApp\task1.xaml" "{406ea660-64cf-4c82-b6f0-42d48172a799}" "11218A0B2491E18E93FF6E832DBF82AD"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.269
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Automation.Peers;
using System.Windows.Automation.Provider;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Resources;
using System.Windows.Shapes;
using System.Windows.Threading;


namespace FMI.ArcGIS.WCF.Service.ClientApp {
    
    
    public partial class task1 : System.Windows.Controls.Page {
        
        internal System.Windows.Controls.Grid LayoutRoot;
        
        internal System.Windows.Controls.TextBox areaName;
        
        internal System.Windows.Controls.TextBox state;
        
        internal System.Windows.Controls.TextBox capital;
        
        internal System.Windows.Controls.TextBox cityClass;
        
        internal System.Windows.Controls.TextBox pop2000;
        
        internal System.Windows.Controls.Button searchCities;
        
        internal System.Windows.Controls.DataGrid foundCitiesGrid;
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Windows.Application.LoadComponent(this, new System.Uri("/FMI.ArcGIS.WCF.Service.ClientApp;component/task1.xaml", System.UriKind.Relative));
            this.LayoutRoot = ((System.Windows.Controls.Grid)(this.FindName("LayoutRoot")));
            this.areaName = ((System.Windows.Controls.TextBox)(this.FindName("areaName")));
            this.state = ((System.Windows.Controls.TextBox)(this.FindName("state")));
            this.capital = ((System.Windows.Controls.TextBox)(this.FindName("capital")));
            this.cityClass = ((System.Windows.Controls.TextBox)(this.FindName("cityClass")));
            this.pop2000 = ((System.Windows.Controls.TextBox)(this.FindName("pop2000")));
            this.searchCities = ((System.Windows.Controls.Button)(this.FindName("searchCities")));
            this.foundCitiesGrid = ((System.Windows.Controls.DataGrid)(this.FindName("foundCitiesGrid")));
        }
    }
}
