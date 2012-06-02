using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace FMI.ArcGIS.WCF.Service
{
	[ServiceContract]
	public interface IUSAService
	{
        /* Search city in state */
        [OperationContract]
        List<City> SearchCitiesInState(string stateAbbr);

        /* City buffered search*/
		[OperationContract]
		List<City> SearchCities(string userName, string password, double centerX, double centerY, double distance);

        /* Search in layers by attributes */
        [OperationContract]
        List<CityDetails> FindCitiesByAttributes(string areaName, string state, string cityClass, string isCapital, string pop2000);

        [OperationContract]
        List<HighwayDetails> FindHighwaysByAttributes(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route);

        [OperationContract]
        List<StateDetails> FindStatesByAttributes(string stateName, string subRegion, string stateAbbr);

        [OperationContract]
        List<CountyDetails> FindCountiesByAttributes(string name, string stateName, string areaBottom, string areaTop);
	}
}
