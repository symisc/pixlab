import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class GrayScale {
	// Convert a given image to gray color model. A grayscale (or graylevel) image is simply one in which the only colors are shades of gray.
	// https://pixlab.io/#/cmd?id=grayscale for additional information.

	private static String img = "https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg";
	
    static OkHttpClient client = new OkHttpClient();
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("grayscale")
                .addQueryParameter("img", img)
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
			System.out.println("Link to the grayscaled picture: "+ jResponse.getString("link"));
		}

	}

}
