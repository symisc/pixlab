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

public class DrawRectanglesOnFaces {
	// Mark Jeremy's face by drawing a rectangle on it. The rectangle coordinates was obtained from the facedetect command and passed untouched to this command. 
	// Refer to the command page https://pixlab.io/#/cmd?id=drawrectangles for more info.
	
	// Target image
	private static String img = "http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg";
	
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

	// Your PixLab key
	private static String key = "Pix_Key";
	
    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("drawrectangles").build();

		JSONObject Obj1 = new JSONObject();
		Obj1.append("x", "164");
		Obj1.append("y", "95");
		Obj1.append("width", "145");
		Obj1.append("height", "145");
		
		JSONObject jObj = new JSONObject();
		jObj.append("img", img);
		jObj.append("cord", new JSONArray().put(Obj1));
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
