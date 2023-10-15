import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;

public class AdvancedWebScraper {

    public static void main(String[] args) {
        // URL of the website to scrape - just this line inorder to scrap and extract the data from any url
        String url = "https://example.com";

        try {
            // Connect to the website and get the HTML document
            Document document = Jsoup.connect(url).get();

            // Extract and print the title of the website
            String title = document.title();
            System.out.println("Title: " + title);

            // Extract and print all the links on the website
            Elements links = document.select("a[href]");
            System.out.println("Links:");
            for (Element link : links) {
                System.out.println(link.attr("href"));
            }

            // Extract and print the text content of paragraphs
            Elements paragraphs = document.select("p");
            System.out.println("\nParagraphs:");
            for (Element paragraph : paragraphs) {
                System.out.println(paragraph.text());
            }

            // Extract and print the source URLs of images
            Elements images = document.select("img[src]");
            System.out.println("\nImages:");
            for (Element image : images) {
                System.out.println(image.attr("src"));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
