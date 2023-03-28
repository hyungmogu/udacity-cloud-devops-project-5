<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class ImageConvertController extends Controller
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
        // convert image to target format
        // upload image to amazon s3
        // set time for it to be deleted after 15 minutes or 1 day (if this is only thing allowed)
        // return uploaded amazon s3 url back to user
        
        $post = $request->all();
        $file = @$post['file'];
        $code = 200;
        $extension = $file->getClientOriginalExtension();
        $imageName = $file->getClientOriginalName();
        $path = 'your_path';

        // from https://stackoverflow.com/questions/62790089/how-to-encode-jpeg-jpg-to-webp-in-laravel
        if(in_array($extension,["jpeg","jpg","png"])){
            //old image
            $webp = public_path().'/'.$path.'/'.$imageName;
            $im = imagecreatefromstring(file_get_contents($webp));
            imagepalettetotruecolor($im);
            // have exact value with WEBP extension
            $new_webp = preg_replace('"\.(jpg|jpeg|png|webp)$"', '.webp', $webp);
            //del old image
            unlink($webp);
            // set qualityy according to requirement
            return imagewebp($im, $new_webp, 50); 
        }
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
