import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class OilPaint {
	// Simulates an oil painting. Each pixel is replaced by the most frequent color occurring in a circular region defined by radius. 
	// https://pixlab.io/#/cmd?id=oilpaint
	
	// Target image
	private static String img = "http://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("oilpaint")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("radius", "3")
                .build();
		
		Request requesthttp = new Request.Builder()
                .addHeader("accept", "application/json")
                .url(httpUrl)
                .build();

        Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
		}else {
			System.out.println("Link to the pic: "+ jResponse.getString("link")+"...");
		}
	}

}
