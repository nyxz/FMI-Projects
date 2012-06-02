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
    public class SearchStatesManager
    {
        public List<StateDetails> FindStatesByAttributes(string stateName, string subRegion, string stateAbbr)
        {
            List<StateDetails> resultStates = new List<StateDetails>();
            IFeatureCursor statesCursor = null;

            try
            {
                IFeatureClass statesClass = MyHelper.GetLayer(Layers.STATES);
                statesCursor = getStateCursor(stateName, subRegion, stateAbbr, statesClass);
                IFeature state = statesCursor.NextFeature();
                while (null != state)
                {
                    resultStates.Add(GetStateDetails(state, statesClass));
                    state = statesCursor.NextFeature();
                }
                throw new Exception();
            }
            catch (Exception)
            {
                Console.WriteLine("Error while searching states.");
            }
            finally
            {
                if (null != statesCursor)
                {
                    Marshal.ReleaseComObject(statesCursor);
                }
            }

            return resultStates;
        }

        #region Private Methods

        private IFeatureCursor getStateCursor(string stateName, string subRegion, string stateAbbr, IFeatureClass statesClass)
        {
            IQueryFilter queryFilter = GetStateQueryFilter(stateName, subRegion, stateAbbr);

            return statesClass.Search(queryFilter, true);
        }

        private IQueryFilter GetStateQueryFilter(string stateName, string subRegion, string stateAbbr)
        {
            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.WhereClause = StatesWhereBuilder(stateName, subRegion, stateAbbr);
            
            return (QueryFilter)spatialFilter;
        }

        private string StatesWhereBuilder(string stateName, string subRegion, string stateAbbr)
        {
            string where = "";
            bool isFirst = true;
            if (!MyHelper.isEmpty(stateName))
            {
                where += MyHelper.CreateEqualStatement(StateConst.STATE_NAME, stateName, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(subRegion))
            {
                where += MyHelper.CreateEqualStatement(StateConst.SUB_REGION, subRegion, isFirst);
                isFirst = false;
            }
            if (!MyHelper.isEmpty(stateAbbr))
            {
                where += MyHelper.CreateEqualStatement(StateConst.STATE_ABBR, stateAbbr, isFirst);
                isFirst = false;
            }

            return where;
        }
        
        private StateDetails GetStateDetails(IFeature state, IFeatureClass statesClass)
        {
            int areaIdx = statesClass.FindField(StateConst.AREA);
            int stateNameIdx = statesClass.FindField(StateConst.STATE_NAME);
            int subRegionIdx = statesClass.FindField(StateConst.SUB_REGION);
            int stateAbbrIdx = statesClass.FindField(StateConst.STATE_ABBR);
            int pop2000Idx = statesClass.FindField(StateConst.POP2000);
            int pop00_sqmiIdx = statesClass.FindField(StateConst.POP00_SQMI);

            return new StateDetails
            {
                Area = (double)state.get_Value(areaIdx),
                StateName = state.get_Value(stateNameIdx) as string,
                SubRegion = state.get_Value(subRegionIdx) as string,
                StateAbbr = state.get_Value(stateAbbrIdx) as string,
                Pop2000 = (int)state.get_Value(pop2000Idx),
                Pop00_SQMI = (int)state.get_Value(pop00_sqmiIdx)
            };
        }

        #endregion
    }
}