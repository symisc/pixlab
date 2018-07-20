import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Crop {
	// Extract Jeremy's face. The rectangle coordinates were obtained from the facedetect command and passed untouched to this command. 
	// https://pixlab.io/#/cmd?id=crop for more info.
	
	// Target image
	private static String img = "http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("crop")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("width", "145")
                .addQueryParameter("height", "145")
                .addQueryParameter("x", "164")
                .addQueryParameter("y", "95")
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
			System.out.println("Face location: "+ jResponse.getString("link"));
		}
	}

}
