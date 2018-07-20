import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class TagImg {
	// Tag an image based on detected visual content which mean running a CNN on top of it.
	// https://pixlab.io/#/cmd?id=tagimg for more info.
	
	// Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the sample set for more info.
	private static String img = "https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("tagimg")
                .addQueryParameter("img", img)
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
			System.out.println("Link to the picture: "+ jResponse.getString("link"));
		}
	}

}
