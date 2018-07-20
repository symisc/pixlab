import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class DrawTextAt {
	// Draw some funny text at the specified offset on the famous Michael Jordan crying face.
	// https://pixlab.io/#/cmd?id=drawtextat && https://pixlab.io/#/cmd?id=drawtext for more info.
	
	// Target image
	private static String img = "https://pixlab.io/images/jdr.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("drawtextat")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("text", "monday morning mood")
                .addQueryParameter("x", "75")
                .addQueryParameter("y", "150")
                .addQueryParameter("ycap", "True")
                .addQueryParameter("strokecolor", "black")
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
