import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MediaDelete {
	// Draw some funny text on top & button of the famous Michael Jordan crying face. 
	// https://pixlab.io/#/cmd?id=drawtext is the target command
	
	// Target image
	private static String img = "http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg";
	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("oilpaint")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("radius", "3")
                .build();
		
		Request requesthttp = new Request.Builder()
                .addHeader("accept", "application/json")
                .url(httpUrl)
                .build();

        Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
		}else {
			System.out.println("Deleting: "+ jResponse.getString("link")+"...");
			
			HttpUrl httpUrl2 = new HttpUrl.Builder()
	                .scheme("https")
	                .host("api.pixlab.io")
	                .addPathSegment("delete")
	                .addQueryParameter("link", jResponse.getString("link"))
	                .addQueryParameter("key", key)
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
				System.out.println("Deletion succeed");
			}
		}
	}

}
