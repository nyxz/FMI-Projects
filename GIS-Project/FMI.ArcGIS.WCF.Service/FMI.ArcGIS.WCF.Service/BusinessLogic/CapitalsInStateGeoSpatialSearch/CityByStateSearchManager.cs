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
    public class CityByStateSearchManager
    {

        public List<City> SearchCitiesByState(string stateAbbr)
		{
            IFeatureCursor citiesCursor = null;
            List<City> resultCities = new List<City>();

            try
            {
                IFeatureClass citiesClass = MyHelper.GetLayer(Layers.CITIES);
                citiesCursor = GetCityCursor(stateAbbr, citiesClass);
                IFeature city = citiesCursor.NextFeature();

                while (city != null)
                {
                    resultCities.Add(GetCity(city, citiesClass));
                    city = citiesCursor.NextFeature();
                }

            }
            catch (Exception)
            {
                Console.WriteLine("Error searching city by state.");
            }
            finally
            {
                if (null != citiesCursor)
                {
                    Marshal.ReleaseComObject(citiesCursor);  
                }
            }

			return resultCities;
		}

        #region Private Methods

        private IFeatureCursor GetCityCursor(string stateAbbr, IFeatureClass citiesClass)
        {
            IQueryFilter queryFilter = GetQueryFilter(stateAbbr);

            return citiesClass.Search(queryFilter, true);
        }

        private City GetCity(IFeature city, IFeatureClass cityClass)
        {
            IPoint capitalShape = city.Shape as IPoint;
            int areaNameIndex = cityClass.FindField(CityConst.AREA_NAME);

            return new City()
            {
                AreaName = city.get_Value(areaNameIndex) as string,
                X = capitalShape.X,
                Y = capitalShape.Y
            };
        }

        private IQueryFilter GetQueryFilter(string stateAbbr)
        {
            IGeometry stateGeometry = getGeometry(stateAbbr);

            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.Geometry = stateGeometry;
            spatialFilter.SpatialRel = esriSpatialRelEnum.esriSpatialRelIntersects;

            return (QueryFilter)spatialFilter;
        }

        private IGeometry getGeometry(string stateAbbr)
        {
            IFeature state = GetStateByAbbr(stateAbbr);
            IPolygon statePolygon = state.Shape as IPolygon;

            return (statePolygon as ITopologicalOperator).Buffer(0);
        }

        private IFeature GetStateByAbbr(string stateAbbr)
        {
            IFeatureClass statesClass = MyHelper.GetLayer(Layers.STATES);
            IQueryFilter queryFilter = GetStateQueryFilter(stateAbbr);
            IFeatureCursor stateCursor = statesClass.Search(queryFilter, false);

            return stateCursor.NextFeature();
        }

        private IQueryFilter GetStateQueryFilter(string stateAbbr)
        {
            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.WhereClause = StatesWhereBuilder(stateAbbr);
            
            return (QueryFilter)spatialFilter;
        }

        private string StatesWhereBuilder(string stateAbbr)
        {
            return (MyHelper.isEmpty(stateAbbr)) ? "" : MyHelper.CreateEqualStatement(StateConst.STATE_ABBR, stateAbbr, true);
        }

        #endregion
    }
}