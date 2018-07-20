import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class BlurImageNsfwScore {
	// Target Image: Change to any link (Possibly adult) you want or switch to POST if you want to upload your image directly, refer to the sample set for more info.
	private static String img = "https://i.redd.it/oetdn9wc13by.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		// Blur an image based on its NSFW score
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("nsfw")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key).build();
		
		Request requesthttp = new Request.Builder()
                .addHeader("accept", "application/json")
                .url(httpUrl)
                .build();

        Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
			System.exit(1);
		}else if(jResponse.getFloat("score")<0.5) {
			System.out.println("No adult content were detected on this picture");
		} else {
			// Highly NSFW picture
			System.out.println("Censuring NSFW picture...");
			// Call blur with the highest possible radius and sigma
			HttpUrl httpUrl2 = new HttpUrl.Builder()
	                .scheme("https")
	                .host("api.pixlab.io")
	                .addPathSegment("blur")
	                .addQueryParameter("img", img)
	                .addQueryParameter("key", "Pix_Key")
		    		.addQueryParameter("rad", "50")
		    		.addQueryParameter("sig", "30").build();

			Request requesthttp2 = new Request.Builder()
	                .addHeader("Content-Type","application/json")
	                .url(httpUrl2)
	                .build();
			Response response2 = client.newCall(requesthttp2).execute();
	
			JSONObject jResponse2 = new JSONObject(response2.body().string());
			if (jResponse2.getInt("status") != 200) { 
				System.out.println("Error :: " + jResponse2.getString("error"));
			}else {
				System.out.println("Censured image: "+ jResponse2.getString("link"));
			}
			
		}
	}
}
