import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Colorize {
	// Colorize this 1933 picture of this little girl via: https://pixlab.io/cmd?id=colorize
	
	// Target image
	private static String img = "https://i.redd.it/7z1q27vaa9tz.png";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("colorize")
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
