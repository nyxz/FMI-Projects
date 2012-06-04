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
    public class CityBufferedSearchManager
    {

        public List<City> SearchCities(string userName, string password, double centerX, double centerY, double distance)
		{
            IFeatureCursor citiesCursor = null;
            List<City> resultCities = new List<City>();

            try
            {
                IFeatureClass citiesClass = MyHelper.GetLayer(Layers.CITIES);
                citiesCursor = getCityCursor(centerX, centerY, distance, citiesClass);
                IFeature capital = citiesCursor.NextFeature();

                while (capital != null)
                {
                    resultCities.Add(GetCity(capital, citiesClass));
                    capital = citiesCursor.NextFeature();
                }

            }
            catch (Exception)
            {
                Console.WriteLine("Error searching cities with buffer.");
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

        private static IFeatureCursor getCityCursor(double centerX, double centerY, double distance, IFeatureClass citiesClass)
        {
            ISpatialFilter spatialFilter = getSpatialFilter(centerX, centerY, distance);

            return citiesClass.Search((QueryFilter)spatialFilter, true);
        }

        private City GetCity(IFeature capital, IFeatureClass citiesClass)
        {
            IPoint capitalShape = capital.Shape as IPoint;
            
            int areaNameIndex = citiesClass.FindField(CityConst.AREA_NAME);

            return new City()
            {
                AreaName = capital.get_Value(areaNameIndex) as string,
                X = capitalShape.X,
                Y = capitalShape.Y
            };
        }

        private static ISpatialFilter getSpatialFilter(double centerX, double centerY, double distance)
        {
            IPoint center = getCenter(centerX, centerY);
            IGeometry buffer = getBuffer(distance, center);

            ISpatialFilter spatialFilter = new SpatialFilterClass();
            spatialFilter.Geometry = buffer;
            spatialFilter.SpatialRel = esriSpatialRelEnum.esriSpatialRelIntersects;

            return spatialFilter;
        }

        private static IGeometry getBuffer(double distance, IPoint center)
        {
            return (center as ITopologicalOperator).Buffer(distance);
        }

        private static IPoint getCenter(double centerX, double centerY)
        {
            IPoint center = new Point();
            center.PutCoords(centerX, centerY);
            return center;
        }

        #endregion
    }
}