import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class DynamicImageMeme {
	// Dynamically create a 300x300 PNG image with a yellow background and draw some text on the center of it later.
	// Refer to https://pixlab.io/#/cmd?id=newimage && https://pixlab.io/#/cmd?id=drawtext for additional information.
	
	// Target image
	private static String img = "https://pixlab.io/images/jdr.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("newimage")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("width", "300")
                .addQueryParameter("height", "300")
                .addQueryParameter("color", "yellow")
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
			String newImg = jResponse.getString("link");
			
			HttpUrl httpUrl2 = new HttpUrl.Builder()
	                .scheme("https")
	                .host("api.pixlab.io")
	                .addPathSegment("drawtext")
	                .addQueryParameter("img", newImg)
	                .addQueryParameter("key", key)
	                .addQueryParameter("center", "bonjour")
	                .addQueryParameter("font", "wolf")
	                .addQueryParameter("cap", "True")
	                .addQueryParameter("color", "black")
	                .build();
			
			Request requesthttp2 = new Request.Builder()
	                .addHeader("accept", "application/json")
	                .url(httpUrl2)
	                .build();

	        Response response2 = client.newCall(requesthttp2).execute();

			JSONObject jResponse2 = new JSONObject(response2.body().string());
			if (jResponse2.getInt("status") != 200) { 
				System.out.println("Error :: " + jResponse2.getString("error"));
				System.exit(1);
			}else {
				System.out.println("Link to the picture: "+ jResponse2.getString("link"));
			}
		}
	}

}
