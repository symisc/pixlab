import java.io.IOException;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class EncryptImg {
	// Converts plain pixels of a given image to enciphered pixels. The image is not readable until it has been deciphered using decrypt.
	// https://pixlab.io/#/cmd?id=encrypt && https://pixlab.io/#/cmd?id=decrypt
	
	// Target image
	private static String img = "https://pixlab.io/images/bencrypt.png";
	// Your PixLab key
	private static String key = "Pix_Key";
	// Password used for decryption
	private static String pwd = "pass_code";

    static OkHttpClient client = new OkHttpClient();

	public static void main(String[] args) throws IOException, JSONException {
		
		HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("https")
                .host("api.pixlab.io")
                .addPathSegment("encrypt")
                .addQueryParameter("img", img)
                .addQueryParameter("key", key)
                .addQueryParameter("pwd", pwd)
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
			System.out.println("Link to the decrypted picture: "+ jResponse.getString("link"));
			// use https://api.pixlab.io/decrypt with your passphrase to make it readable again
		}
	}

}
