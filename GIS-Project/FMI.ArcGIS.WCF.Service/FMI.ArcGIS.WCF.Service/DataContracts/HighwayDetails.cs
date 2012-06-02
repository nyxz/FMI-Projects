using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Runtime.Serialization;

namespace FMI.ArcGIS.WCF.Service
{
    [DataContract]
    public class HighwayDetails
    {
        private double length;
        private string type;
        private string admnClass;
        private string tollRd;
        private string rteNum;
        private string rteNum2;
        private string route;

        public HighwayDetails()
        { 
        }

        [DataMember]
        public double Length
        {
            get
            {
                return length;
            }
            set
            {
                length = value;
            }
        }

        [DataMember]
        public string Type
        {
            get
            {
                return type;
            }
            set
            {
                type = value;
            }
        }

        [DataMember]
        public string AdmnClass
        {
            get
            {
                return admnClass;
            }
            set
            {
                admnClass = value;
            }
        }

        [DataMember]
        public string TollRd
        {
            get
            {
                return tollRd;
            }
            set
            {
                tollRd = value;
            }
        }

        [DataMember]
        public string RteNum
        {
            get
            {
                return rteNum;
            }
            set
            {
                rteNum = value;
            }
        }

        [DataMember]
        public string RteNum2
        {
            get
            {
                return rteNum2;
            }
            set
            {
                rteNum2 = value;
            }
        }

        [DataMember]
        public string Route
        {
            get
            {
                return route;
            }
            set
            {
                route = value;
            }
        }
    }
}