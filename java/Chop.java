import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Chop {
	// Removes a region of an image and collapses the image to occupy the removed portion.
	// https://pixlab.io/#/cmd?id=chop for more info.
	
	// Target image
	private static String img = "https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("chop")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("height", "20")
                .addQueryParameter("x", "45")
                .addQueryParameter("y", "75")
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
