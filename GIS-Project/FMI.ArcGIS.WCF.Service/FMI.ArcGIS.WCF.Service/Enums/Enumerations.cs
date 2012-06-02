using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace FMI.ArcGIS.WCF.Service
{
    public static class CityConst
    {
        public const string AREA_NAME = "AREANAME";
        public const string STATE = "ST";
        public const string CAPITAL = "CAPITAL";
        public const string CITY_CLASS = "CLASS";
        public const string POP_2000 = "POP2000";
    }

    public static class HighwayConst
    {
        public const string LENGTH = "LENGTH";
        public const string TYPE = "TYPE";
        public const string ADMN_CLASS = "ADMN_CLASS";
        public const string TOLL_RD = "TOLL_RD";
        public const string RTE_NUM1 = "RTE_NUM1";
        public const string RTE_NUM2 = "RTE_NUM2";
        public const string ROUTE = "ROUTE";
    }

    public static class StateConst
    {
        public const string AREA = "AREA";
        public const string STATE_NAME = "STATE_NAME";
        public const string SUB_REGION = "SUB_REGION";
        public const string STATE_ABBR = "STATE_ABBR";
        public const string POP2000 = "POP2000";
        public const string POP00_SQMI = "POP00_SQMI";
    }

    public static class CountyConst
    {
        public const string NAME = "NAME";
        public const string STATE_NAME = "STATE_NAME";
        public const string AREA = "AREA";
        public const string POP2000 = "POP2000";
        public const string POP00_SQMI = "POP00_SQMI";
    }

    public static class Layers
    {
        public const string CITIES = "Cities";
        public const string HIGHWAYS = "Highways";
        public const string STATES = "States";
        public const string COUNTIES = "Counties";
    }

    public static class Connection
    { 
        public const string DATABASE = "DATABASE";
        public const string DATABASE_PATH = @"C:\GisDB\USA\USA.gdb";
    }
}