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
    public class SearchHighwaysManager
    {
        public List<HighwayDetails> FindHighwaysByAttributes(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route)
        {
            IFeatureCursor highwayCursor = null;
            List<HighwayDetails> resultHighways = new List<HighwayDetails>();

            try
            {
                IFeatureClass highwaysClass = MyHelper.GetLayer(Layers.HIGHWAYS);
                highwayCursor = GetHighwayCursor(lenBottomBound, lenUpperBound, admClass, rtNum, route, highwaysClass);
                IFeature highway = highwayCursor.NextFeature();

                while (highway != null)
                {
                    resultHighways.Add(GetHighwayDetails(highway, highwaysClass));
                    highway = highwayCursor.NextFeature();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Error searching highways.");
            }
            finally
            {
                if (null != highwayCursor)
                {
                    Marshal.ReleaseComObject(highwayCursor); 
                }
            }

            return resultHighways;
        }

        #region Private methods

        private IFeatureCursor GetHighwayCursor(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route, IFeatureClass highwaysClass)
        {
            IQueryFilter queryFilter = GetHighwaysQueryFilter(lenBottomBound, lenUpperBound, admClass, rtNum, route);

            return highwaysClass.Search(queryFilter, true);
        }

        private IQueryFilter GetHighwaysQueryFilter(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route)
        {
            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.WhereClause = HighwaysWhereBuilder(lenBottomBound, lenUpperBound, admClass, rtNum, route);

            return (QueryFilter)spatialFilter;
        }

        private string HighwaysWhereBuilder(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route)
        {
            string where = "";
            bool isFirst = true;
            if (!MyHelper.isEmpty(lenBottomBound))
            {
                double lenBBound = MyHelper.getDoubleFromString(lenBottomBound);
                where += MyHelper.CreateGreaterThanStmntForDouble(HighwayConst.LENGTH, lenBBound, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(lenUpperBound))
            {
                double lenUBound = MyHelper.getDoubleFromString(lenUpperBound);
                where += MyHelper.CreateLessThanStmntForDouble(HighwayConst.LENGTH, lenUBound, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(admClass))
            {
                where += MyHelper.CreateEqualStatement(HighwayConst.ADMN_CLASS, admClass, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(rtNum))
            {
                where += MyHelper.CreateEqualStatement(HighwayConst.RTE_NUM1, rtNum, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(route))
            {
                where += MyHelper.CreateEqualStatement(HighwayConst.ROUTE, route, isFirst);
                isFirst = false;
            }
            return where;
        }

        private HighwayDetails GetHighwayDetails(IFeature highway, IFeatureClass highwaysClass)
        {
            int lengthIdx = highwaysClass.FindField(HighwayConst.LENGTH);
            int typeIdx = highwaysClass.FindField(HighwayConst.TYPE);
            int admnClassIdx = highwaysClass.FindField(HighwayConst.ADMN_CLASS);
            int tollRdIdx = highwaysClass.FindField(HighwayConst.TOLL_RD);
            int rt1NumIdx = highwaysClass.FindField(HighwayConst.RTE_NUM1);
            int rt2NumIdx = highwaysClass.FindField(HighwayConst.RTE_NUM2);
            int routeIdx = highwaysClass.FindField(HighwayConst.ROUTE);
            
            return new HighwayDetails()
            {
                Length = (double)highway.get_Value(lengthIdx),
                Type = highway.get_Value(typeIdx) as string,
                AdmnClass = highway.get_Value(admnClassIdx) as string,
                TollRd = highway.get_Value(tollRdIdx) as string,
                RteNum = highway.get_Value(rt1NumIdx) as string,
                RteNum2 = highway.get_Value(rt2NumIdx) as string,
                Route = highway.get_Value(routeIdx) as string
            };
        }

        #endregion
    }
}