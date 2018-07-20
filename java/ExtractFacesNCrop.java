import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ExtractFacesNCrop {
	// Detect all human faces present in a given image via 'facedetect' and extract each one of them via 'crop'.
	
	// Target image: Feel free to change to whatever image holding as many human faces you want
	private static String img = "http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";

    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("facedetect")
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
			JSONArray faces = jResponse.getJSONArray("faces");
			int nfaces = faces.length();
			System.out.println(nfaces+" faces were detected");
			
			// Extract each face via crop now 
			for(int i=0;i<nfaces;i++) {
				JSONObject face = faces.getJSONObject(i);
				HttpUrl httpUrl2 = new HttpUrl.Builder()
		                .scheme("https")
		                .host("api.pixlab.io")
		                .addPathSegment("crop")
		                .addQueryParameter("img", img)
		                .addQueryParameter("key", key)
		                .addQueryParameter("width", face.getString("width"))
		                .addQueryParameter("height", face.getString("height"))
		                .addQueryParameter("x", face.getString("left"))
		                .addQueryParameter("y", face.getString("top"))
		                .build();
				
				Request requesthttp2 = new Request.Builder()
		                .addHeader("accept", "application/json")
		                .url(httpUrl2)
		                .build();
				
				Response response2 = client.newCall(requesthttp2).execute();

				JSONObject jResponse2 = new JSONObject(response2.body().string());
				if (jResponse2.getInt("status") != 200) { 
					System.out.println("Error :: " + jResponse2.getString("error"));
				}else {
					System.out.println("Face #" +jResponse2.getInt("face_id")+ " location: " + jResponse2.getInt("link"));
				}
			}
		}
	}

}
