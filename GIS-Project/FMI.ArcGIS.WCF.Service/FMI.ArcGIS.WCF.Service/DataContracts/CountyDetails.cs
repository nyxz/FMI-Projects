using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Runtime.Serialization;

namespace FMI.ArcGIS.WCF.Service
{
    [DataContract]
    public class CountyDetails
    {
        private string name;
        private string stateName;
        private double area;
        private int pop2000;
        private double pop00_sqmi;

        public CountyDetails()
        { 
        }

        [DataMember]
        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
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
        public double Pop00_SQMI
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