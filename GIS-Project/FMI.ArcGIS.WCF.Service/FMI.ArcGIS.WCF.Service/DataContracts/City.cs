using System.Runtime.Serialization;

namespace FMI.ArcGIS.WCF.Service
{
	[DataContract]
	public class City
	{
		private string areaName;
		private double x;
		private double y;

		public City()
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
		public double X
		{
			get
			{
				return x;
			}
			set
			{
				x = value;
			}
		}

		[DataMember]
		public double Y
		{
			get
			{
				return y;
			}
			set
			{
				y = value;
			}
		}
	}
}