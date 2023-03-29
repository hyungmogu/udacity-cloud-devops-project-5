<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Aws\S3\S3Client;

class ImageToWEBPController extends Controller
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
        $imageData = $request->input('image'); // get the blob image data from the request    
        // create an image resource from the blob data
        $image = imagecreatefromstring($imageData);
        
        // create a JPEG image from the original image
        $jpegData = imagejpeg($image);
        
        // upload the JPEG image to S3
        $s3 = new S3Client([
            'region' => env('AWS_S3_REGION', ''),
            'version' => 'latest',
            'credentials' => [
                'key' => env('AWS_S3_ACCESS_KEY', ''),
                'secret' => env('AWS_S3_SECRET_KEY', ''),
            ],
        ]);
        
        $s3->putObject([
            'Bucket' => env('AWS_S3_BUCKET', ''),
            'Key' => 'path/to/image.jpg',
            'Body' => $jpegData,
            'ContentType' => 'image/jpeg',
        ]);
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
