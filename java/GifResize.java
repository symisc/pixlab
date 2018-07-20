import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class GifResize {
	// Scales a GIF file to the desired dimensions: https://pixlab.io/#/cmd?id=resizegif

	private static String gif = "http://cloud.addictivetips.com/wp-content/uploads/2009/testing.gif";
	
    static OkHttpClient client = new OkHttpClient();
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("resizegif")
                .addQueryParameter("img", gif)
                .addQueryParameter("width", "256")
                .addQueryParameter("height", "256")
                .addQueryParameter("key", "Pix_Key")
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
		} else {// success
			
			System.out.println("Gif location: "+ jResponse.getString("link"));
			
		}

	}

}
