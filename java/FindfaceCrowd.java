import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class FindfaceCrowd {
	// Find a person's face in a crowd or group of people. https://pixlab.io/cmd?id=facelookup for additional information.
	
	// This is the target face we are looking for.
	private static String face = "http://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg";
	// The people crowd to look on
	private static String crowd = "http://www.acclaimimages.com/_gallery/_free_images/0519-0908-1001-0556_president_barack_obama_walking_with_a_crowd_of_people_o.jpg";

	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("facelookup")
                .addQueryParameter("face", face)
                .addQueryParameter("crowd", crowd)
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
			boolean found = jResponse.getBoolean("found");
			if (found) {
				System.out.println("Face found with confidence value = "+ jResponse.getString("confidence"));
				JSONObject rectangle = jResponse.getJSONObject("rectangle"); // Rectangle coordinates of the target face
				System.out.println("Face Coordinates: top: "+rectangle.getInt("top")+" left: "+rectangle.getInt("left")+" width: "+rectangle.getInt("width")+" height:"+rectangle.getInt("height"));
			}else{
				System.out.println("Face NOT found in the target crowd..picking up the best candidate:");
				JSONObject best = jResponse.getJSONObject("best");
				JSONObject rectangle = best.getJSONObject("rectangle"); // Rectangle coordinates of the best candidate
				System.out.println("Confidence: "+ best.getString("confidence"));
				System.out.println("Best Candidate Coordinates: top: "+rectangle.getInt("top")+" left: "+rectangle.getInt("left")+" width: "+rectangle.getInt("width")+" height:"+rectangle.getInt("height"));
			}
		}
	}

}
