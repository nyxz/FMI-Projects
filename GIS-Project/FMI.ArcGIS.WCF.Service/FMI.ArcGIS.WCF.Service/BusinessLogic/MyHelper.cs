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
    public class MyHelper
    {

        /*===============================================================================*/
        /* Manage connection, workspace and layer */
        /*===============================================================================*/

        public static IFeatureClass GetLayer(string layer)
        {
            IWorkspace workspace = GetWorkspace();
            return (workspace as IFeatureWorkspace).OpenFeatureClass(layer);
        }

        public static IWorkspace GetWorkspace()
        {
            return Connect();
        }

        private static IWorkspace Connect()
        {
            IPropertySet propertySet = null;
            IWorkspaceFactory workspaceFactory = null;

            try
            {
                propertySet = new PropertySet();
                propertySet.SetProperty(Connection.DATABASE, Connection.DATABASE_PATH);

                workspaceFactory = new FileGDBWorkspaceFactoryClass();

                return workspaceFactory.Open(propertySet, IntPtr.Zero.ToInt32());
            }
            catch(Exception e)
            {
                Console.WriteLine("Error establishing connection to DB. Error: " + e.Message);
            }
            finally
            {
                if (workspaceFactory != null)
                    Marshal.ReleaseComObject(workspaceFactory);
                if (propertySet != null)
                    Marshal.ReleaseComObject(propertySet);
            }

            return null;
        }



        /*===============================================================================*/
        /* Manage query building */
        /*===============================================================================*/

        public static string CreateEqualStatement(string key, string value, bool isFirst)
        {
            string result = " " + key.ToUpper() + " = '" + value + "' ";
            if (!isFirst)
            {
                return " AND " + result;
            }
            return result;
        }


        public static string CreateEqualStatementForNum(string key, Int32 value, bool isFirst)
        {
            return CreateStatementForInt(key, value, isFirst, "=");
        }


        public static string CreateStatementForInt(string key, Int32 value, bool isFirst, string sign)
        {
            string result = " " + key.ToUpper() + " " + sign + " " + value + " ";
            if (!isFirst)
            {
                return " AND " + result;
            }
            return result;
        }

        public static string CreateGreaterThanStmntForDouble(string key, double value, bool isFirst)
        {
            return CreateStatementForDouble(key, value, isFirst, ">");
        }

        public static string CreateLessThanStmntForDouble(string key, double value, bool isFirst)
        {
            return CreateStatementForDouble(key, value, isFirst, "<");
        }

        private static string CreateStatementForDouble(string key, double value, bool isFirst, string sign)
        {
            string result = " " + key.ToUpper() + " " + sign + " " + value + " ";
            if (!isFirst)
            {
                return " AND " + result;
            }
            return result;
        }

        /*===============================================================================*/
        /* small help */
        /*===============================================================================*/

        public static bool isEmpty(string value)
        {
            if (null == value || value.Trim().Length == 0)
            {
                return true;
            }
            return false;
        }

        public static Int32 getInt32FromString(string strValue)
        {
            Int32 numValue = -1;
            try
            {
                numValue = Convert.ToInt32(strValue.Trim());
            }
            catch (FormatException)
            {
                Console.WriteLine("Input string is not a sequence of digits.");
            }
            catch (OverflowException)
            {
                Console.WriteLine("The number cannot fit in an Int32.");
            }

            return numValue;
        }

        public static double getDoubleFromString(string strValue)
        {
            double numValue = -1;
            try
            {
                numValue = Convert.ToDouble(strValue.Trim());
            }
            catch (FormatException)
            {
                Console.WriteLine("Input string is not a sequence of digits.");
            }
            catch (OverflowException)
            {
                Console.WriteLine("The number cannot fit in a double.");
            }

            return numValue;
        }

        public static string GetData(int value)
        {
            return string.Format("You entered: {0}", value);
        }
    }
}