import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ImgDiff {
	
	// Compute the difference between two images and output the reconstructed image and the diff output.
	// Keep in mind that the two images must be of the same size or call 'resize' or 'crop' before to
	// fit the images to the same dimension.
	// Read more on imgdiff here: https://pixlab.io/#/cmd?id=imgdiff

	// Source image which is the famous Michael Jordan's crying face.
	private static String src = "https://pixlab.io/images/jdr.jpg";
	
	// Target image which is the same Jordan's face but a MEME is drawn on top of it.
	private static String target = "https://pixlab.io/images/jdr_draw.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("imgdiff")
                .addQueryParameter("src", src)
                .addQueryParameter("target", target)
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
			System.out.println("Diff Output: "+ jResponse.getString("diff"));
			System.out.println("Reconstructed image link: "+ jResponse.getString("link"));
			
		}
	}
}
