package com.svb.coffee.ui.theme;

import android.app.Activity;
import android.location.Location;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.Nullable;

import com.svb.coffee.R;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;


public class MainActivity extends Activity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);
        run();
    }

    public void run() {
        OkHttpClient client = new OkHttpClient();
        Thread thread = new Thread(() -> {
            try {
                Request request = new Request.Builder()
                        .url("http://192.168.0.38:8090/coffee")
                        .build();
                Response response = client.newCall(request).execute();
                String res = response.body().string();
                runOnUiThread(() -> Toast.makeText(getApplicationContext(), res, Toast.LENGTH_SHORT).show());
            } catch (Exception e) {
                runOnUiThread(() -> {
                    Log.e(MainActivity.class.toString(), "" + e.getMessage());
                    Toast.makeText(getApplicationContext(), "ERR: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                });
            }
            finish();
        });

        thread.start();
        finish();
    }
}