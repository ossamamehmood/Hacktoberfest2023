using Microsoft.Identity.Web;
using Microsoft.SharePoint.Client;

namespace BlazorApp2.Services
{
    public static class SharePointClientContextFactoryServiceConfiguration
    {
        public static IServiceCollection AddSharePointContextFactory(this IServiceCollection serviceCollection)
        {
            serviceCollection.AddScoped<ISharePointClientContextFactory, SharePointClientContextFactory>();
            return serviceCollection;
        }

        public static IServiceCollection AddCurrentUserSharePointClientContext(this IServiceCollection serviceCollection)
        {
            serviceCollection.AddSharePointContextFactory();

            serviceCollection.AddScoped<ClientContext>((services) =>
            {
                var clientContextFactory = services.GetService<ISharePointClientContextFactory>();
                return clientContextFactory.GetClientContext();
            });

            return serviceCollection;
        }
    }

    public interface ISharePointClientContextFactory
    {
        ClientContext GetClientContext(string siteUrl = null);
    }

    class SharePointClientContextFactory : ISharePointClientContextFactory
    {
        private readonly ITokenAcquisition _tokenAcquisition;
        private readonly IConfiguration _configuration;

        public SharePointClientContextFactory(IConfiguration configuration, ITokenAcquisition tokenAcquisition)
        {
            _configuration = configuration;
            _tokenAcquisition = tokenAcquisition;
        }

        private string GetResourceUri(string siteUrl)
        {
            var uri = new Uri(siteUrl);
            return $"{uri.Scheme}://{uri.DnsSafeHost}";
        }

        private string[] GetSharePointResourceScope(string siteUrl, string[] scopes = null)
        {
            string resourceUri = GetResourceUri(siteUrl);
            return scopes == null
                ? new[] { $"{resourceUri}/.default" }
                : scopes.Select(scope => $"{resourceUri}/{scope}").ToArray();
        }


        private ClientContext GetClientContextInternal(string siteUrl, string[]? scopes = null)
        {
            siteUrl ??= _configuration.GetValue<string>("SharePoint:Url");
            if (string.IsNullOrEmpty(siteUrl))
                throw new Exception("The SharePoint site URL is not specified or configured");

            // Acquire the access token.
            string[] effectiveScopes = GetSharePointResourceScope(siteUrl, new string[] { "User.Read" });
            var clientContext = new ClientContext(siteUrl);
            clientContext.ExecutingWebRequest += (object sender, WebRequestEventArgs e) =>
            {
                string accessToken = _tokenAcquisition.GetAccessTokenForUserAsync(effectiveScopes).GetAwaiter().GetResult();
                e.WebRequestExecutor.RequestHeaders.Add("Authorization", $"Bearer {accessToken}");
            };
            return clientContext;
        }

        public ClientContext GetClientContext(string? siteUrl = null)
        {
            return GetClientContextInternal(siteUrl);
        }
    }
}
