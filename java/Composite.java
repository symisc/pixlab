import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONArray;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Composite {
	// Composite two smiley on top of the famous Michael jordan crying face.
	// A more sophisticated approach would be to extract the face landmarks using facelandmarks and composite something on the different regions.
	// https://pixlab.io/#/cmd?id=merge for more info.
	
	// Target image
	private static String src = "https://pbs.twimg.com/media/CcEfpp0W4AEQVPf.jpg";
	private static String img1 = "http://www.wowpng.com/wp-content/uploads/2016/10/lol-troll-face-png-image-october-2016-370x297.png";
	private static String img2 = "http://orig08.deviantart.net/67d1/f/2010/216/6/7/lol_face_by_bloodyhalfdemon.png";
	
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("merge").build();
		
		JSONObject Obj1 = new JSONObject();
		Obj1.append("img", img1);
		Obj1.append("x", "30");
		Obj1.append("y", "320");
		
		JSONObject Obj2 = new JSONObject();
		Obj2.append("img", img2);
		Obj1.append("x", "630");
		Obj1.append("y", "95");

		
		JSONObject jObj = new JSONObject();
		jObj.append("src", src);
		jObj.append("cord", new JSONArray().put(Obj1).put(Obj2));
		jObj.append("key", key);
		
		RequestBody body = RequestBody.create(JSON, jObj.toString());

		Request requesthttp = new Request.Builder()
                .addHeader("Content-Type","application/json")
                .url(httpUrl)
                .post(body)
                .build();
		Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
			System.exit(1);
		}else {
			System.out.println("Picture Link: "+ jResponse.getString("link"));
		}
	}

}
