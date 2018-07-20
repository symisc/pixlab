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

public class UploadMedia {
	// Upload a local image to the remote https://pixlab.xyz storage server or your own S3 bucket depending on the configuration from your dashboard.
	// Use the output link for other purposes such as processing via mogrify, drawrectangles, etc. or simply serving content.
	// https://pixlab.io/#/cmd?id=store for more info.
	
	// Your PixLab key
	private static String key = "Pix_Key";

	public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

    
	public static void main(String[] args) throws IOException, JSONException {
		OkHttpClient client = new OkHttpClient();
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("http") // Switch to http:// for fast upload
                .host("api.pixlab.io")
                .addPathSegment("store")
                .build();
		
		File file = new File("local_image.png");
		RequestBody body = new MultipartBody.Builder()
		        .setType(MultipartBody.FORM)
		        .addFormDataPart("file", file.getName(),
		            RequestBody.create(MediaType.parse("png"), file))
		        .addFormDataPart("key", key)
		        .addFormDataPart("comment", "Super Secret Stuff")
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
			System.out.println("Upload Pic Link: "+ jResponse.getString("score"));
		}
	}

}
