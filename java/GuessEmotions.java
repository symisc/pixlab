import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class GuessEmotions {
	// Detect all human faces present in a given image and try to guess their emotions.
	// https://pixlab.io/#/cmd?id=facemotion for additional information

	private static String img = "http://www.scienceforums.com/uploads/1282315190/gallery_1625_35_9165.jpg";
	
    static OkHttpClient client = new OkHttpClient();
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("facemotion")
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
			JSONArray faces = jResponse.getJSONArray("faces");
			int nfaces = faces.length();
			for(int i=0;i<nfaces;i++) {
				JSONObject face = faces.getJSONObject(i);
				JSONObject cord = face.getJSONObject("rectangle");
				System.out.println("Face coordinate: width: "+cord.getString("width")+" height: "+cord.getString("height")+" x: "+cord.getString("left")+" y: "+cord.getString("top"));
				System.out.println("Emotion guess");
				JSONArray emotions = face.getJSONArray("emotion");
				for(int j=0;j<emotions.length();j++) {
					System.out.println(emotions.getJSONObject(i).getString("state")+" : "+emotions.getJSONObject(i).getString("score"));
				}
			}
			
		}

	}

}
