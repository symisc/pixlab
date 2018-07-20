import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class CropGif {
	// Extracts a region from each frame of a given GIF file
	// https://pixlab.io/#/cmd?id=cropgif for more info.
	
	// Target image
	private static String img = "http://cloud.addictivetips.com/wp-content/uploads/2009/testing.gif";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("cropgif")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("width", "256")
                .addQueryParameter("x", "150")
                .addQueryParameter("y", "70")
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
			System.out.println("Link to the picture: "+ jResponse.getString("link"));
		}
	}

}
