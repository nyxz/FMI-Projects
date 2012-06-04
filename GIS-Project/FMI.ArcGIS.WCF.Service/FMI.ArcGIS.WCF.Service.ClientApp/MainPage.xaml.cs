using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;
using FMI.ArcGIS.WCF.Service.ClientApp.USAWCFService;

namespace FMI.ArcGIS.WCF.Service.ClientApp
{
    public partial class MainPage : UserControl
    {
        public MainPage()
        {
            InitializeComponent();
        }

        /* search by coordinates with buffer */

        private void searchButton_Click(object sender, RoutedEventArgs e)
		{
			double x = 0;
			double y = 0;
			double distance = 0;

			if (Double.TryParse(xTextBox.Text, out x) &&
				Double.TryParse(yTextBox.Text, out y) &&
				Double.TryParse(dTextBox.Text, out distance))
			{
                USAServiceClient wcfClient = new USAServiceClient();
                wcfClient.SearchCitiesCompleted += new EventHandler<SearchCitiesCompletedEventArgs>(wcfClient_SearchCitiesCompleted);
                wcfClient.SearchCitiesAsync("sde", "sde", x, y, distance);
            }
            else
            {
                MessageBox.Show("Invalid parameters.", "Search Cities", MessageBoxButton.OK);
            }
        }

        private void wcfClient_SearchCitiesCompleted(object sender, SearchCitiesCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                citiesGrid.ItemsSource = e.Result;
            }
            else
            {
                citiesGrid.ItemsSource = new List<City>();

                MessageBox.Show("Error calling WCF service. Failed to find cities.", "Search Cities", MessageBoxButton.OK);
            }
        }


        /* search by attributes */

        /* search cities */
        private void searchCities_Click(object sender, RoutedEventArgs e)
        {
            if (ClientInputValidator.validateSearchCityByAttrInput(areaNameTextBox.Text, stateTextBox.Text, classTextBox.Text, capitalTextBox.Text, pop2000TextBox.Text))
            {
                USAServiceClient wcfClient = new USAServiceClient();
                wcfClient.FindCitiesByAttributesCompleted += new EventHandler<FindCitiesByAttributesCompletedEventArgs>(wcfClient_FindCitiesByAttributesCompleted);
                wcfClient.FindCitiesByAttributesAsync(areaNameTextBox.Text, stateTextBox.Text, classTextBox.Text, capitalTextBox.Text, pop2000TextBox.Text);
            }
            else
            {
                MessageBox.Show("Invalid parameters.", "Search Cities", MessageBoxButton.OK);
            }
        }

        private void wcfClient_FindCitiesByAttributesCompleted(object sender, FindCitiesByAttributesCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                foundCitiesGrid.ItemsSource = e.Result;
            }
            else
            {
                foundCitiesGrid.ItemsSource = new List<CityDetails>();

                MessageBox.Show("Error calling WCF service. Failed to find cities.", "Search Cities", MessageBoxButton.OK);
            }
        }

        /* search highways */
        private void searchHighways_Click(object sender, RoutedEventArgs e)
        {
            if (ClientInputValidator.validateSearchHighwaysByAttrInput(lengthBottomTextBox.Text, lengthTopTextBox.Text, admnClassTextBox.Text, rtNumTextBox.Text, routeTextBox.Text))
            {
                USAServiceClient wcfClient = new USAServiceClient();
                wcfClient.FindHighwaysByAttributesCompleted += new EventHandler<FindHighwaysByAttributesCompletedEventArgs>(wcfClient_FindHighwaysByAttributesCompleted);
                wcfClient.FindHighwaysByAttributesAsync(lengthBottomTextBox.Text, lengthTopTextBox.Text, admnClassTextBox.Text, rtNumTextBox.Text, routeTextBox.Text);
            }
            else
            {
                MessageBox.Show("Invalid parameters.", "Search Highways", MessageBoxButton.OK);
            }
        }

        private void wcfClient_FindHighwaysByAttributesCompleted(object sender, FindHighwaysByAttributesCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                foundHighwaysGrid.ItemsSource = e.Result;
            }
            else
            {
                foundHighwaysGrid.ItemsSource = new List<HighwayDetails>();

                MessageBox.Show("Error calling WCF service. Failed to find highways.", "Search Highways", MessageBoxButton.OK);
            }
        }

        /* search states */
        private void searchStates_Click(object sender, RoutedEventArgs e)
        {
            if (ClientInputValidator.validateSearchStateByAttrInput(stateNameTextBox.Text, subRegionTextBox.Text, stateAbbrTextBox.Text))
            {
                USAServiceClient wcfClient = new USAServiceClient();
                wcfClient.FindStatesByAttributesCompleted += new EventHandler<FindStatesByAttributesCompletedEventArgs>(wcfClient_FindStatesByAttributesCompleted);
                wcfClient.FindStatesByAttributesAsync(stateNameTextBox.Text, subRegionTextBox.Text, stateAbbrTextBox.Text);
            }
            else
            {
                MessageBox.Show("Invalid parameters.", "Search States", MessageBoxButton.OK);
            }
        }

        public void wcfClient_FindStatesByAttributesCompleted(object sender, FindStatesByAttributesCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                foundStatesGrid.ItemsSource = e.Result;
            }
            else
            {
                foundStatesGrid.ItemsSource = new List<StateDetails>();

                MessageBox.Show("Error calling WCF service. Failed to find states.", "Search States", MessageBoxButton.OK);
            }
        }


        /* search counties */
        private void searchCounties_Click(object sender, RoutedEventArgs e)
        {
            if (ClientInputValidator.validateSearchCountyByAttrInput(countyNameTextBox.Text, countyStateNameTextBox.Text, countyAreaGTTextBox.Text, countyAreaLTTextBox.Text))
            {
                USAServiceClient serviceClient = new USAServiceClient();
                serviceClient.FindCountiesByAttributesCompleted += new EventHandler<FindCountiesByAttributesCompletedEventArgs>(wcfClient_FindCountiesByAttributesCompleted);
                serviceClient.FindCountiesByAttributesAsync(countyNameTextBox.Text, countyStateNameTextBox.Text, countyAreaGTTextBox.Text, countyAreaLTTextBox.Text);
            }
            else
            {
                MessageBox.Show("Invalid parameters.", "Search County", MessageBoxButton.OK);
            }
        }

        private void wcfClient_FindCountiesByAttributesCompleted(object sender, FindCountiesByAttributesCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                foundCountiesGrid.ItemsSource = e.Result;
            }
            else
            {
                foundCountiesGrid.ItemsSource = new List<CountyDetails>();

                MessageBox.Show("Error calling WCF service. Failed to find counties.", "Search County", MessageBoxButton.OK);
            }
        }


        /* search city by state (geospatial) */

        private void searchCityByState_Click(object sender, RoutedEventArgs e)
        {
            if (ClientInputValidator.validateSearchCityByStateInput(stateAbbr.Text))
            {
                USAServiceClient serviceClient = new USAServiceClient();
                serviceClient.SearchCitiesInStateCompleted += new EventHandler<SearchCitiesInStateCompletedEventArgs>(wcfClient_SearchCityByStateCompleted);
                serviceClient.SearchCitiesInStateAsync(stateAbbr.Text);
            }
            else
            {
                MessageBox.Show("Invalid input parameters.", "Search Cities by State Abbr.", MessageBoxButton.OK);
            }
        }

        private void wcfClient_SearchCityByStateCompleted(object sender, SearchCitiesInStateCompletedEventArgs e)
        {
            if (!e.Cancelled && e.Error == null)
            {
                cityByStateGrid.ItemsSource = e.Result;
            }
            else
            {
                cityByStateGrid.ItemsSource = new List<City>();

                MessageBox.Show("Error calling WCF service. Failed to find cities.", "Search Cities by state", MessageBoxButton.OK);
            }
        }
    }
}
