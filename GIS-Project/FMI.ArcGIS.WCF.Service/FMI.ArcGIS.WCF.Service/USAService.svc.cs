using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.ServiceModel.Activation;

using ESRI.ArcGIS;
using ESRI.ArcGIS.DataSourcesGDB;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.Geometry;

namespace FMI.ArcGIS.WCF.Service
{
	[AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
	public class USAService : IUSAService
	{
		static USAService()
		{
			RuntimeManager.Bind(ProductCode.Desktop);

			IAoInitialize aoInitialize = new AoInitialize();

			aoInitialize.Initialize(esriLicenseProductCode.esriLicenseProductCodeArcInfo);
		}


        /* City buffered search*/

		public List<City> SearchCities(string userName, string password, double centerX, double centerY, double distance)
		{
            return new CityBufferedSearchManager().SearchCities(userName, password, centerX, centerY, distance);
		}

        /* Search in layers by attributes */

        public List<CityDetails> FindCitiesByAttributes(string areaName, string state, string cityClass, string isCapital, string pop2000)
        {
            return new SearchCitiesManager().FindCitiesByAttributes(areaName, state, cityClass, isCapital, pop2000);
        }

        public List<HighwayDetails> FindHighwaysByAttributes(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route)
        {
            return new SearchHighwaysManager().FindHighwaysByAttributes(lenBottomBound, lenUpperBound, admClass, rtNum, route);
        }

        public List<StateDetails> FindStatesByAttributes(string stateName, string subRegion, string stateAbbr)
        {
            return new SearchStatesManager().FindStatesByAttributes(stateName, subRegion, stateAbbr);
        }

        public List<CountyDetails> FindCountiesByAttributes(string name, string stateName, string areaBottom, string areaTop)
        {
            return new SearchCountriesManager().FindCountiesByAttributes(name, stateName, areaBottom, areaTop);
        }

        /* Search city in state (geospatial search)*/

        public List<City> SearchCitiesInState(string stateAbbr)
        {
            return new CityByStateSearchManager().SearchCitiesByState(stateAbbr);
        }
    }
}
