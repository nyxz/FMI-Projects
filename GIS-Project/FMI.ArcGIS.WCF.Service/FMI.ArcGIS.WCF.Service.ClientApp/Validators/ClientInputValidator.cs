using System;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;

namespace FMI.ArcGIS.WCF.Service.ClientApp
{
    public class ClientInputValidator
    {
        public static bool validateSearchCityByAttrInput(string areaName, string state, string cityClass, string isCapital, string pop2000)
        {
            return validateString(areaName) && validateString(state) && validateString(cityClass)
                && validateString(isCapital) && validateNumber(pop2000);
        }

        public static bool validateSearchHighwaysByAttrInput(string lenBottomBound, string lenUpperBound, string admClass, string rtNum, string route)
        {
            return validateNumber(lenBottomBound) && validateNumber(lenUpperBound) && validateString(admClass)
                && validateString(rtNum) && validateString(route);
        }

        public static bool validateSearchStateByAttrInput(string stateName, string subRegion, string stateAbbr) 
        {
            return validateString(stateName) && validateString(subRegion) && validateString(stateAbbr);
        }

        public static bool validateSearchCountyByAttrInput(string name, string stateName, string areaBottom, string areaTop)
        {
            return validateString(name) && validateString(stateName) && validateNumber(areaBottom)
                && validateNumber(areaTop);
        }

        public static bool validateSearchCityByStateInput(string stateAbbr)
        {
            return validateString(stateAbbr);
        }

        private static bool validateString(string value)
        { 
            return !value.Contains("\'") && !value.Contains("\"");
        }

        private static bool validateNumber(string value)
        {
            if (isEmpty(value))
            {
                return true;
            }
            double temp = 0;
            return Double.TryParse(value, out temp);
        }

        private static bool isEmpty(string value)
        {
            return (null == value) || (value.Trim().Length == 0);
        }
    }
}
