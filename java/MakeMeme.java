import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MakeMeme {
	// Draw some funny text on top & button of the famous Michael Jordan crying face. 
	// https://pixlab.io/#/cmd?id=drawtext is the target command
	
	// Target image
	private static String img = "https://pixlab.io/images/jdr.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("drawtext")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("top", "someone bumps the table")
                .addQueryParameter("bottom", "right before you win")
                .addQueryParameter("cap", "True")
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
			System.out.println("Meme: "+ jResponse.getString("link"));
		}
	}

}
