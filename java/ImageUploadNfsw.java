import java.io.File;
import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class ImageUploadNfsw {
	// Upload an image first & detect whether it is Not Suitable for Work (NSFW)
	// https://pixlab.io/#/cmd?id=nsfw
	
	// Your PixLab key
	private static String key = "Pix_Key";

	public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

    
	public static void main(String[] args) throws IOException, JSONException {
		OkHttpClient client = new OkHttpClient();
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("nsfw")
                .build();
		
		File file = new File("local_image.png");
		RequestBody body = new MultipartBody.Builder()
		        .setType(MultipartBody.FORM)
		        .addFormDataPart("file", file.getName(),
		            RequestBody.create(MediaType.parse("png"), file))
		        .addFormDataPart("key", key)
		        .build();
		
		Request requesthttp = new Request.Builder()
                .addHeader("accept", "application/json")
                .url(httpUrl)
                .post(body)
                .build();

        Response response = client.newCall(requesthttp).execute();

		JSONObject jResponse = new JSONObject(response.body().string());
		if (jResponse.getInt("status") != 200) { 
			System.out.println("Error :: " + jResponse.getString("error"));
			System.exit(1);
		}else {
			System.out.println("NSFW Score: "+ jResponse.getString("score"));
		}
	}

}
