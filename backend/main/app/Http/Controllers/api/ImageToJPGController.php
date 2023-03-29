<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Aws\S3\S3Client;

class ImageToJPGController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return;
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $image_data = $request->input('image'); // get the blob image data from the request    
        // create an image resource from the blob data
        $image = imagecreatefromstring($image_data);
        
        // create a JPEG image from the original image
        $jpeg_data = imagejpeg($image);
        
        //upload the JPEG image to S3
        $s3 = new S3Client([
            'region' => env('AWS_S3_REGION', ''),
            'version' => 'latest',
            'credentials' => [
                'key' => env('AWS_S3_ACCESS_KEY', ''),
                'secret' => env('AWS_S3_SECRET_KEY', ''),
            ],
        ]);
        
        $result = $s3->putObject([
            'Bucket' => 'your_s3_bucket',
            'Key' => 'path/to/image.jpg',
            'Body' => $jpeg_data,
            'ContentType' => 'image/jpg',
        ]);

        return $result['ObjectURL'];
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        return;
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        return;
    }
}