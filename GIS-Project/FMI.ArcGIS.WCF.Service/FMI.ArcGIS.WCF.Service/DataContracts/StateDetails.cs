using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Runtime.Serialization;

namespace FMI.ArcGIS.WCF.Service
{
    [DataContract]
    public class StateDetails
    {
        private double area;
        private string stateName;
        private string subRegion;
        private string stateAbbr;
        private int pop2000;
        private int pop00_sqmi;

        public StateDetails()
        { }

        [DataMember]
        public double Area
        {
            get
            {
                return area;
            }
            set
            {
                area = value;
            }
        }

        [DataMember]
        public string StateName
        {
            get
            {
                return stateName;
            }
            set
            {
                stateName = value;
            }
        }

        [DataMember]
        public string SubRegion
        {
            get
            {
                return subRegion;
            }
            set
            {
                subRegion = value;
            }
        }

        [DataMember]
        public string StateAbbr
        {
            get
            {
                return stateAbbr;
            }
            set
            {
                stateAbbr = value;
            }
        }

        [DataMember]
        public int Pop2000
        {
            get
            {
                return pop2000;
            }
            set
            {
                pop2000 = value;
            }
        }

        [DataMember]
        public int Pop00_SQMI
        {
            get
            {
                return pop00_sqmi;
            }
            set
            {
                pop00_sqmi = value;
            }
        }
    }
}