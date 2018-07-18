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

public class makeGif {
	// Generate GIF from a set of static image
	// https://pixlab.io/#/cmd?id=makegif for additional information.
	
    static OkHttpClient client = new OkHttpClient();
    
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("makegif").build();
		
		JSONArray Obj = new JSONArray();
		Obj.put(new JSONObject().append("img", "https://cdn1.iconfinder.com/data/icons/human-6/48/266-512.png"));
		Obj.put(new JSONObject().append("img", "https://cdn1.iconfinder.com/data/icons/human-6/48/267-512.png"));
		Obj.put(new JSONObject().append("img", "https://cdn1.iconfinder.com/data/icons/human-6/48/278-512.png"));
		Obj.put(new JSONObject().append("img", "https://cdn1.iconfinder.com/data/icons/human-6/48/279-512.png"));
		
		JSONObject jObj = new JSONObject();
		jObj.append("key", "Pix_Key");
		//jObj.append("frames", Obj.toString());
		
		RequestBody body = RequestBody.create(JSON, jObj.toString());

		Request requesthttp = new Request.Builder()
                .url(httpUrl)
                .post(body)
                .addHeader("content-type", "application/json; charset=utf-8")

                .build();
		Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
			System.exit(1);
		}else {
			System.out.println("GIF location: "+ jResponse.getString("link"));
		}

	}

}
