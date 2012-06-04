using System.Runtime.Serialization;

namespace FMI.ArcGIS.WCF.Service
{
    [DataContract]
    public class CityDetails
    {
        private string areaName;
        private string state;
        private string cityClass;
        private string isCapital;
        private int pop2000;

        public CityDetails()
		{
		}

        [DataMember]
        public string AreaName
        {
            get
            {
                return areaName;
            }
            set
            {
                areaName = value;
            }
        }

        [DataMember]
        public string State
        {
            get
            {
                return state;
            }
            set
            {
                state = value;
            }
        }

        [DataMember]
        public string CityClass
        {
            get
            {
                return cityClass;
            }
            set
            {
                cityClass = value;
            }
        }

        [DataMember]
        public string IsCapital
        {
            get
            {
                return isCapital;
            }
            set
            {
                isCapital = value;
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
    }
}