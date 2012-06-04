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
    public class SearchCountriesManager
    {
        public List<CountyDetails> FindCountiesByAttributes(string name, string stateName, string areaBottom, string areaTop)
        {
            IFeatureCursor countyCursor = null;
            List<CountyDetails> resultCounties = new List<CountyDetails>();

            try
            {
                IFeatureClass countyClass = MyHelper.GetLayer(Layers.COUNTIES);
                countyCursor = getCountyCursor(name, stateName, areaBottom, areaTop, countyClass);
                IFeature county = countyCursor.NextFeature();

                while (county != null)
                {
                    resultCounties.Add(GetCountyDetails(county, countyClass));
                    county = countyCursor.NextFeature();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Error searching county");
            }
            finally
            {
                if (null != countyCursor)
                {
                    Marshal.ReleaseComObject(countyCursor); 
                }
            }


            return resultCounties;
        }

        private IFeatureCursor getCountyCursor(string name, string stateName, string areaBottom, string areaTop, IFeatureClass countyClass)
        {
            IQueryFilter queryFilter = GetCountyQueryFilter(name, stateName, areaBottom, areaTop);

            return countyClass.Search(queryFilter, true);
        }

        private CountyDetails GetCountyDetails(IFeature county, IFeatureClass countyClass)
        {
            int nameIdx = countyClass.FindField(CountyConst.NAME);
            int stateNameIdx = countyClass.FindField(CountyConst.STATE_NAME);
            int areaIdx = countyClass.FindField(CountyConst.AREA);
            int pop2000Idx = countyClass.FindField(CountyConst.POP2000);
            int pop00sqmiIdx = countyClass.FindField(CountyConst.POP00_SQMI);

            return new CountyDetails()
            {
                Name = county.get_Value(nameIdx) as string,
                StateName = county.get_Value(stateNameIdx) as string,
                Area = (double)county.get_Value(areaIdx),
                Pop2000 = (int)county.get_Value(pop2000Idx),
                Pop00_SQMI = (double)county.get_Value(pop00sqmiIdx)
            };
        }

        private IQueryFilter GetCountyQueryFilter(string name, string stateName, string areaBottom, string areaTop)
        {
            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.WhereClause = CountyWhereBuilder(name, stateName, areaBottom, areaTop);

            return (QueryFilter)spatialFilter;
        }

        private string CountyWhereBuilder(string name, string stateName, string areaBottom, string areaTop)
        {
            string where = "";
            bool isFirst = true;
            if (!MyHelper.isEmpty(name))
            {
                where += MyHelper.CreateEqualStatement(CountyConst.NAME, name, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(stateName))
            {
                where += MyHelper.CreateEqualStatement(CountyConst.STATE_NAME, stateName, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(areaBottom))
            {
                double areaBottomDouble = MyHelper.getDoubleFromString(areaBottom);
                where += MyHelper.CreateGreaterThanStmntForDouble(CountyConst.AREA, areaBottomDouble, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(areaTop))
            {
                double areaTopDouble = MyHelper.getDoubleFromString(areaTop);
                where += MyHelper.CreateLessThanStmntForDouble(CountyConst.AREA, areaTopDouble, isFirst);
                isFirst = false;
            }

            return where;
        }
    }
}