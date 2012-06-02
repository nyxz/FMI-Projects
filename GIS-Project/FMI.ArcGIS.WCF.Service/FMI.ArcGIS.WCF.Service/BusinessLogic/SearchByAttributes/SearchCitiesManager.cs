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
    public class SearchCitiesManager
    {
        public List<CityDetails> FindCitiesByAttributes(string areaName, string state, string cityClass, string isCapital, string pop2000)
        {
            IFeatureCursor citiesCursor = null;
            List<CityDetails> resultCities = new List<CityDetails>();

            try
            {
                IFeatureClass citiesClass = MyHelper.GetLayer(Layers.CITIES);
                citiesCursor = getCityCursor(areaName, state, cityClass, isCapital, pop2000, citiesClass);
                IFeature city = citiesCursor.NextFeature();

                while (city != null)
                {
                    resultCities.Add(GetCityDetails(city, citiesClass));
                    city = citiesCursor.NextFeature();
                }

            }
            catch (Exception)
            {
                Console.WriteLine("Error searching cities.");
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

        private IFeatureCursor getCityCursor(string areaName, string state, string cityClass, string isCapital, string pop2000, IFeatureClass citiesClass)
        {
            IQueryFilter queryFilter = GetCitiesQueryFilter(areaName, state, cityClass, isCapital, pop2000);

            return citiesClass.Search(queryFilter, true); ;
        }

        private CityDetails GetCityDetails(IFeature city, IFeatureClass citiesClass)
        {
            int areaNameIdx = citiesClass.FindField(CityConst.AREA_NAME);
            int stateIdx = citiesClass.FindField(CityConst.STATE);
            int capitalIdx = citiesClass.FindField(CityConst.CAPITAL);
            int cityClassIdx = citiesClass.FindField(CityConst.CITY_CLASS);
            int pop2000Idx = citiesClass.FindField(CityConst.POP_2000);

            return new CityDetails()
            {
                AreaName = city.get_Value(areaNameIdx) as string,
                State = city.get_Value(stateIdx) as string,
                CityClass = city.get_Value(cityClassIdx) as string,
                IsCapital = city.get_Value(capitalIdx) as string,
                Pop2000 = (int)city.get_Value(pop2000Idx)
            };
        }

        private IQueryFilter GetCitiesQueryFilter(string areaName, string state, string cityClass, string isCapital, string pop2000)
        {
            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.WhereClause = CitiesWhereBuilder(areaName, state, cityClass, isCapital, pop2000);

            return (QueryFilter)spatialFilter;
        }

        private string CitiesWhereBuilder(string areaName, string state, string cityClass, string isCapital, string pop2000)
        {
            string where = "";
            bool isFirst = true;
            if (!MyHelper.isEmpty(areaName))
            {
                where += MyHelper.CreateEqualStatement(CityConst.AREA_NAME, areaName, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(state))
            {
                where += MyHelper.CreateEqualStatement(CityConst.STATE, state, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(cityClass))
            {
                where += MyHelper.CreateEqualStatement(CityConst.CITY_CLASS, cityClass, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(isCapital))
            {
                where += MyHelper.CreateEqualStatement(CityConst.CAPITAL, isCapital, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(pop2000))
            {
                Int32 pop2000Int32 = MyHelper.getInt32FromString(pop2000);
                where += MyHelper.CreateEqualStatementForNum(CityConst.POP_2000, pop2000Int32, isFirst);
                isFirst = false;
            }
            return where;
        }

        #endregion
    }
}