import { DefaultSeoProps } from "next-seo";

export const baseUrl = "https://slack-clone-martstech.vercel.app";

export const defaultSEO: DefaultSeoProps = {
  title: "Slack Clone",
  description:
    "Slack is a new way to communicate with your team. It’s faster, better organized, and more secure than email.",
  openGraph: {
    type: "website",
    locale: "en_US",
    url: baseUrl,
    site_name: "Slack Clone",
    images: [
      {
        url: `${baseUrl}/meta/og-image.png`,
        alt: "Slack Clone",
      },
    ],
  },
};
