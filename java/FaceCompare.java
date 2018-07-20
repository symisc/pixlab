import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class FaceCompare {
	// Check whether the given faces belong to the same person or not.
	// https://pixlab.io/#/cmd?id=facecompare for additional information.
	
	// Target image
	private static String src = "https://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg";
	private static String target = "https://static01.nyt.com/images/2011/07/31/sunday-review/FACES/FACES-jumbo.jpg";

	// Unrelated face
	//private static String target2 = "https://static01.nyt.com/images/2011/07/31/sunday-review/FACES/FACES-jumbo.jpg";
	
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("facecompare")
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
			System.out.println("Same Face: "+ jResponse.getString("same_face"));
			System.out.println("Confidence: "+ jResponse.getString("confidence"));
		}
	}

}
