<?php

namespace App\Http\Controllers\Api;

use GdImage;
use App\Http\Controllers\Controller;
use Illuminate\Http\UploadedFile;
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
        $request->validate([
            'image' => 'required|image|mimes:jpeg,png,jpg,svg,webp|max:5120',
        ]);
        
        // get the blob image data from the request
        $image_data = $request->file('image');    
        
        // create an image resource from the image data
        $image = $this->createImageResource($image_data);
        
        // create a JPEG image from the image resource
        ob_start();
        imagejpeg($image);
        $jpeg_data = ob_get_clean();

        // Cleanup
        imagedestroy($image);

        return response($jpeg_data, 200, [
            'Content-Type' => 'image/jpeg',
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

    private function createImageResource(UploadedFile $uploaded_image): ?GdImage
    {
        $image_mime_type = $uploaded_image->getMimeType();
        $image_path = $uploaded_image->getPathname();

        switch ($image_mime_type) {
            case 'image/jpeg':
            case 'image/jpg':
                return imagecreatefromjpeg($image_path);
            case 'image/png':
                return @imagecreatefrompng($image_path);
            case 'image/webp':
                return imagecreatefromwebp($image_path);
            default:
                return null;
        }
    }
}
