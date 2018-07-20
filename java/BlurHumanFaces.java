import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class BlurHumanFaces {
	// Detect all human faces in a given image via facedetect and blur all of them via mogrify.
	// https://pixlab.io/#/cmd?id=facedetect & https://pixlab.io/#/cmd?id=mogrify for additional information.

	private static String img = "http://anewscafe.com/wp-content/uploads/2012/05/Brave-Faces-Group-shot.jpg";
	
    static OkHttpClient client = new OkHttpClient();
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("facedetect")
                .addQueryParameter("img", img)
                .addQueryParameter("key", "Pix_Key").build();
		
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
			JSONArray coordinates = jResponse.getJSONArray("faces");
			int nFaces = coordinates.length();
			System.out.println(nFaces+" faces were detected");
			if(nFaces<1) {
				// No faces were detected, exit immediately
				System.exit(1);
			}
			// Pass the detected faces coordinates untouched to mogrify 
			HttpUrl httpUrl2 = new HttpUrl.Builder()
	                .scheme("https")
	                .host("api.pixlab.io")
	                .addPathSegment("mogrify").build();
			
			JSONObject jObj = new JSONObject();
			jObj.append("img", img);
			jObj.append("cord", coordinates);
			jObj.append("key", "Pix_Key");
			
			RequestBody body = RequestBody.create(JSON, jObj.toString());

			Request requesthttp2 = new Request.Builder()
	                .addHeader("Content-Type","application/json")
	                .url(httpUrl2)
	                .post(body)
	                .build();
			Response response2 = client.newCall(requesthttp2).execute();

			JSONObject jResponse2 = new JSONObject(response2.body().string());
			if (jResponse2.getInt("status") != 200) { 
				System.out.println("Error :: " + jResponse2.getString("error"));
				System.exit(1);
			}else {
				System.out.println("Censured pic location: "+ jResponse2.getString("link"));
			}
		}

	}

}
