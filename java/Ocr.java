import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Ocr {
	// Given an image with human readable characters. Detect input language & extract text content from there.
	// https://pixlab.io/#/cmd?id=ocr for additional information.
	
	// Target Image: 
	private static String img = "http://quotesten.com/wp-content/uploads/2016/06/Confucius-Quote.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("ocr")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("nl", "True")
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
			System.out.println("Input Language: "+ jResponse.getString("lang"));
			System.out.println("Text Output: "+ jResponse.getString("output"));
			JSONArray boxes = jResponse.getJSONArray("bbox");
			int nBoxes = boxes.length();
			for (int i=0;i<nBoxes;i++) {
				JSONObject box = boxes.getJSONObject(i);
				System.out.println("Word: "+ box.getString("word"));
				System.out.println("Bounding box - X: "+ box.getString("x")+
						"Y: "+box.getString("y")+" Width: "+box.getString("w")+" Height: "+box.getString("h"));
			}
		}
	}

}
