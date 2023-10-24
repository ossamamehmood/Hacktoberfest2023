
# Blazor SharePoint Web Application

This Readme provides an overview of a Blazor SharePoint Web Application, explaining what it is and how to set it up.

## What is a Blazor SharePoint Web Application?

A Blazor SharePoint Web Application is a web application built using Blazor, a framework for building interactive web applications with C# instead of JavaScript. In this case, the web application is designed to be hosted within SharePoint, a popular platform for collaboration and content management.

Blazor applications run in the browser and allow you to build web applications using C# and .NET technologies. When hosted within SharePoint, they can take advantage of SharePoint's integration capabilities and provide custom user interfaces and functionality to interact with SharePoint lists, libraries, and other SharePoint resources.

## Getting Started

To create and set up a Blazor SharePoint Web Application, follow these steps:

### Dependencies

Visual Studio 2022
SharePoint Online
AAD App

## Register and configure an AAD app

In order for the user to authenticate on the App, A new app registration should be created on Azure Portal

- Go to [Azure Active Directory Portal](https://aad.portal.azure.com)

- In App registrations, click __New registration__

- Enter a name for your new app, make sure *Accounts in this organizational directory only* is selected. As the Redirect URI, in Web platform enter __https://localhost:44349/authentication/login-callback__ (The port may vary according to your Visual Studio)

- Make sure you have added the Redirect URI as Single-Page Application
-
- Under __Implicit grant__ section, check __Access tokens__ and __ID tokens__

- Go to __API permissions__ section , click __Add a permission__
-- Select __SharePoint__ > __Delegated permissions__ > select __AllSites.FullControl__
-- Select __Microsoft Graph__ > __Delegated permissions__ > select __email__, __openid__ and __Sites.FullControl.All__

- Click __Grant admin consent for {tenant}__

- From __Overview__,
-- copy the value of __Directory (tenant) ID__
-- copy the value of __Application (client) ID__

## Configure your application

- Configure the URL of your SharePoint site as the value of `SharePoint:SiteUrl` app setting
- in the file `wwwroot/appsettings.json`, replace the `{clientid}` and the `{tenantid}` accordingly with the values from above

## Execute

  Hit F5 in Visual studio to execute the Blazor app.
  When trying to access one of the sections, the applications prompts you for signing in


