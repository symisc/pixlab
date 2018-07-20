import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class GifComposite {
	// Composite a static image on top of a GIF.
	// If you want to composite multiple images, then use the `merge` command instead.
	
	private static String gif = "http://i.stack.imgur.com/h8Hjm.gif";
	
	// Static images to be displayed starting from frame 5
	private static String img = "http://i.stack.imgur.com/WFr1K.png";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("gifcomposite")
                .addQueryParameter("img", gif)
                .addQueryParameter("composite", img)
                .addQueryParameter("x", "10")
                .addQueryParameter("y", "30")
                .addQueryParameter("frame", "5") // Display the result starting from frame number 5
                .addQueryParameter("key", key)
                .build();
		
		Request requesthttp = new Request.Builder()
                .addHeader("accept", "application/json")
                .url(httpUrl)
                .build();

        Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
			System.exit(1);
		}else {
			// Highly NSFW picture
			System.out.println("Gif Location: "+ jResponse.getString("link"));
			
		}
	}
}
